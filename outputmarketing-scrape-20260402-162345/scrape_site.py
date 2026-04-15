#!/usr/bin/env python3
"""Careful website scraper for outputmarketing.lovable.app.

- Crawls internal HTML pages
- Downloads linked assets (JS/CSS/images/fonts/media)
- Parses CSS url() and @import references
- Parses JS for likely static/dynamic chunk URLs
- Rewrites local links for same-origin references
"""
from __future__ import annotations

import hashlib
import json
import os
import queue
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional, Set, Tuple
from urllib.parse import parse_qsl, quote, unquote, urljoin, urlparse

import requests
from bs4 import BeautifulSoup

START_URL = "https://outputmarketing.lovable.app/"
USER_AGENT = "Mozilla/5.0 (compatible; OutputMarketingScraper/1.0; +https://outputmarketing.lovable.app)"
TIMEOUT = 30
MAX_URLS = 5000

HTML_CT = ("text/html", "application/xhtml+xml")
CSS_CT = ("text/css",)
JS_CT = (
    "application/javascript",
    "text/javascript",
    "application/x-javascript",
    "application/ecmascript",
    "text/ecmascript",
    "application/json",  # sometimes used for JS modules/content types are odd
)

URL_IN_CSS_RE = re.compile(r"url\(([^)]+)\)", re.IGNORECASE)
CSS_IMPORT_RE = re.compile(r"@import\s+(?:url\()?['\"]?([^'\")\s]+)", re.IGNORECASE)
# Conservative JS URL finder: absolute/root-relative and common static extensions.
URL_IN_JS_RE = re.compile(
    r"(?P<q>['\"])"
    r"(?P<url>(?:https?:)?//[^'\"]+|/[^'\"]+|\./[^'\"]+|\.\./[^'\"]+)"
    r"(?P=q)",
    re.IGNORECASE,
)
ASSET_EXT_RE = re.compile(
    r"\.(?:js|mjs|css|map|png|jpe?g|gif|webp|svg|ico|woff2?|ttf|otf|eot|mp4|webm|mp3|wav|json|txt)(?:$|[?#])",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Job:
    url: str
    kind: str  # html | asset
    referrer: Optional[str] = None


def normalize_url(url: str, base: str) -> Optional[str]:
    if not url:
        return None
    url = url.strip()
    if not url or url.startswith("#"):
        return None
    if url.startswith(("mailto:", "tel:", "javascript:", "data:")):
        return None

    absolute = urljoin(base, url)
    p = urlparse(absolute)
    if p.scheme not in ("http", "https"):
        return None

    # Drop fragment for canonical fetch.
    clean = p._replace(fragment="")

    # Stable ordering for query params.
    qsl = parse_qsl(clean.query, keep_blank_values=True)
    query = "&".join(f"{quote(k, safe='')}={quote(v, safe='')}" for k, v in qsl)
    clean = clean._replace(query=query)
    return clean.geturl()


def safe_seg(seg: str) -> str:
    seg = unquote(seg)
    seg = seg.replace(os.sep, "_")
    seg = seg.replace("\x00", "")
    if seg in ("", ".", ".."):
        return "_"
    return seg


def local_path_for_url(root: Path, url: str, content_type: str) -> Path:
    p = urlparse(url)
    host = p.netloc.replace(":", "_")

    parts = [safe_seg(x) for x in p.path.split("/") if x]
    if not parts:
        parts = ["index.html"]

    path = Path(*parts)

    # If path ends with slash-like or no extension and HTML, save as .../index.html
    suffix = path.suffix.lower()
    if p.path.endswith("/"):
        path = path / "index.html"
    elif not suffix:
        if any(ct in content_type for ct in HTML_CT):
            path = path / "index.html"
        else:
            # best effort asset fallback
            path = Path(str(path) + ".bin")

    # Encode query in filename when present.
    if p.query:
        h = hashlib.sha1(p.query.encode("utf-8")).hexdigest()[:10]
        path = path.with_name(f"{path.stem}__q_{h}{path.suffix}")

    return root / host / path


def is_same_origin(url: str, origin: str) -> bool:
    return urlparse(url).netloc == urlparse(origin).netloc


def guess_kind(url: str) -> str:
    path = urlparse(url).path.lower()
    if path.endswith((".html", ".htm")):
        return "html"
    if ASSET_EXT_RE.search(path):
        return "asset"
    return "html"


def extract_html_links(html: str, base_url: str) -> Iterable[Tuple[str, str]]:
    soup = BeautifulSoup(html, "html.parser")

    def add(tag: str, attr: str, kind: str):
        for t in soup.find_all(tag):
            v = t.get(attr)
            if not v:
                continue
            u = normalize_url(v, base_url)
            if u:
                yield (u, kind)

    # Internal/external navigation + assets
    yield from add("a", "href", "html")
    yield from add("link", "href", "asset")
    yield from add("script", "src", "asset")
    yield from add("img", "src", "asset")
    yield from add("source", "src", "asset")
    yield from add("video", "src", "asset")
    yield from add("audio", "src", "asset")
    yield from add("iframe", "src", "html")

    # srcset attributes
    for tag in soup.find_all(["img", "source"]):
        srcset = tag.get("srcset")
        if not srcset:
            continue
        for item in srcset.split(","):
            candidate = item.strip().split(" ")[0]
            u = normalize_url(candidate, base_url)
            if u:
                yield (u, "asset")

    # inline style urls
    for tag in soup.find_all(style=True):
        style = tag.get("style", "")
        for m in URL_IN_CSS_RE.finditer(style):
            raw = m.group(1).strip().strip('"\'')
            u = normalize_url(raw, base_url)
            if u:
                yield (u, "asset")


def extract_css_urls(css: str, base_url: str) -> Iterable[str]:
    for m in URL_IN_CSS_RE.finditer(css):
        raw = m.group(1).strip().strip('"\'')
        u = normalize_url(raw, base_url)
        if u:
            yield u
    for m in CSS_IMPORT_RE.finditer(css):
        raw = m.group(1).strip().strip('"\'')
        u = normalize_url(raw, base_url)
        if u:
            yield u


def extract_js_urls(js: str, base_url: str) -> Iterable[str]:
    for m in URL_IN_JS_RE.finditer(js):
        raw = m.group("url")
        # Skip obvious non-URL syntactic strings quickly
        if raw.startswith("//"):
            raw = f"https:{raw}"
        if raw.startswith(("http://", "https://", "/", "./", "../")):
            u = normalize_url(raw, base_url)
            if u and ASSET_EXT_RE.search(urlparse(u).path.lower()):
                yield u


def rewrite_same_origin_links(local_file: Path, origin: str, root: Path):
    """Rewrite same-origin absolute links in saved html/css/js to local relative paths.

    Best effort only; keeps original if target wasn't downloaded.
    """
    try:
        content = local_file.read_text(encoding="utf-8")
    except Exception:
        return

    origin_host = urlparse(origin).netloc

    # Very safe replacement around quoted URLs only.
    pattern = re.compile(r"(['\"])(https?://[^'\"]+|/[^'\"]+)(['\"])")

    def repl2(m: re.Match) -> str:
        q1, maybe_url, q2 = m.group(1), m.group(2), m.group(3)
        if q1 != q2:
            return m.group(0)
        u = normalize_url(maybe_url, origin)
        if not u:
            return m.group(0)
        if urlparse(u).netloc != origin_host:
            return m.group(0)
        # Determine target in filesystem using likely type by extension.
        ct_guess = "text/html"
        if ASSET_EXT_RE.search(urlparse(u).path.lower()):
            ct_guess = "application/octet-stream"
        target = local_path_for_url(root, u, ct_guess)
        if not target.exists() and ct_guess == "text/html":
            target = local_path_for_url(root, u, "application/octet-stream")
        if not target.exists():
            return m.group(0)
        rel = os.path.relpath(target, local_file.parent).replace(os.sep, "/")
        return f"{q1}{rel}{q2}"

    final = pattern.sub(repl2, content)
    if final != content:
        local_file.write_text(final, encoding="utf-8")


def main() -> int:
    out_root = Path(sys.argv[1]).resolve()
    out_root.mkdir(parents=True, exist_ok=True)

    origin = START_URL
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    q: "queue.Queue[Job]" = queue.Queue()
    q.put(Job(url=START_URL, kind="html", referrer=None))

    queued: Set[str] = {START_URL}
    fetched: Set[str] = set()
    saved_files: Set[Path] = set()
    errors = []
    html_files: Set[Path] = set()
    fetch_count = 0

    while not q.empty() and fetch_count < MAX_URLS:
        job = q.get()
        url = job.url
        if url in fetched:
            continue

        try:
            resp = session.get(url, timeout=TIMEOUT, allow_redirects=True)
            final_url = normalize_url(resp.url, resp.url) or url
            ct = (resp.headers.get("content-type") or "").split(";")[0].strip().lower()
            if resp.status_code >= 400:
                raise RuntimeError(f"HTTP {resp.status_code}")

            local_path = local_path_for_url(out_root, final_url, ct)
            local_path.parent.mkdir(parents=True, exist_ok=True)
            local_path.write_bytes(resp.content)
            saved_files.add(local_path)
            fetched.add(url)
            fetched.add(final_url)
            fetch_count += 1

            print(f"[{fetch_count:04d}] {resp.status_code} {final_url} -> {local_path.relative_to(out_root)}")

            body_bytes = resp.content
            if any(x in ct for x in HTML_CT) or local_path.suffix.lower() in (".html", ".htm"):
                html_files.add(local_path)
                text = body_bytes.decode(resp.encoding or "utf-8", errors="replace")
                for u, k in extract_html_links(text, final_url):
                    # Crawl only same-origin HTML pages.
                    if k == "html" and not is_same_origin(u, origin):
                        continue
                    kind = k if k in ("html", "asset") else guess_kind(u)
                    if kind == "html" and not is_same_origin(u, origin):
                        continue
                    if u not in queued and u not in fetched:
                        q.put(Job(url=u, kind=kind, referrer=final_url))
                        queued.add(u)

            elif any(x in ct for x in CSS_CT) or local_path.suffix.lower() == ".css":
                text = body_bytes.decode(resp.encoding or "utf-8", errors="replace")
                for u in extract_css_urls(text, final_url):
                    if u not in queued and u not in fetched:
                        q.put(Job(url=u, kind="asset", referrer=final_url))
                        queued.add(u)

            elif any(x in ct for x in JS_CT) or local_path.suffix.lower() in (".js", ".mjs"):
                # Parse likely static chunk URLs from JS for completeness.
                text = body_bytes.decode(resp.encoding or "utf-8", errors="replace")
                for u in extract_js_urls(text, final_url):
                    if u not in queued and u not in fetched:
                        q.put(Job(url=u, kind="asset", referrer=final_url))
                        queued.add(u)

        except Exception as exc:
            fetched.add(url)
            errors.append({"url": url, "referrer": job.referrer, "kind": job.kind, "error": str(exc)})
            print(f"[ERR ] {url} <- {job.referrer or '-'} :: {exc}")

    # Rewrite same-origin links in HTML files for easier offline browsing.
    for f in sorted(html_files):
        rewrite_same_origin_links(f, origin, out_root)

    manifest = {
        "target": START_URL,
        "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "output_root": str(out_root),
        "fetched_url_count": len(fetched),
        "saved_file_count": len(saved_files),
        "error_count": len(errors),
        "max_urls": MAX_URLS,
        "errors": errors,
    }

    (out_root / "scrape_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print("\n=== SUMMARY ===")
    print(json.dumps({k: manifest[k] for k in ("target", "saved_file_count", "fetched_url_count", "error_count")}, indent=2))
    if errors:
        print(f"First error: {errors[0]}")

    return 0 if manifest["saved_file_count"] > 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
