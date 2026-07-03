#!/usr/bin/env python3
"""
Phase 1.1 — HTTP Status Code Sweep
Crawls all URLs from bharatneurotech.com/sitemap.xml and reports:
- HTTP status code
- Response time
- Redirect chain (if any)
- Content-Type header
"""

import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
import time
import ssl
import json
import sys

SITEMAP_URL = "https://bharatneurotech.com/sitemap.xml"
TIMEOUT = 15  # seconds per request

# Also test these non-sitemap URLs
EXTRA_URLS = [
    "https://bharatneurotech.com/robots.txt",
    "https://bharatneurotech.com/manifest.webmanifest",
    "https://bharatneurotech.com/favicon.png",
    "https://bharatneurotech.com/favicon-32.png",
    "https://bharatneurotech.com/apple-touch-icon.png",
    "https://bharatneurotech.com/og/home.jpg",
    # Test HTTP -> HTTPS redirect
    "http://bharatneurotech.com/",
    # Test www redirect
    "https://www.bharatneurotech.com/",
    # Test 404 handling
    "https://bharatneurotech.com/this-page-should-not-exist-qa-test",
]

def fetch_sitemap(url):
    """Parse sitemap.xml and extract all URLs."""
    ctx = ssl.create_default_context()
    req = urllib.request.Request(url, headers={"User-Agent": "BNT-QA-Bot/1.0"})
    with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
        xml_data = resp.read()

    root = ET.fromstring(xml_data)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = []
    for url_elem in root.findall("sm:url", ns):
        loc = url_elem.find("sm:loc", ns)
        lastmod = url_elem.find("sm:lastmod", ns)
        priority = url_elem.find("sm:priority", ns)
        if loc is not None:
            urls.append({
                "url": loc.text.strip(),
                "lastmod": lastmod.text.strip() if lastmod is not None else "N/A",
                "priority": priority.text.strip() if priority is not None else "N/A",
            })
    return urls


def check_url(url, follow_redirects=True):
    """Check a URL and return status info."""
    ctx = ssl.create_default_context()
    result = {
        "url": url,
        "status": None,
        "response_time_ms": None,
        "content_type": None,
        "redirect_chain": [],
        "error": None,
        "final_url": url,
    }

    start = time.time()
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "BNT-QA-Bot/1.0"})

        if not follow_redirects:
            class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
                def redirect_request(self, req, fp, code, msg, headers, newurl):
                    result["redirect_chain"].append({"from": req.full_url, "to": newurl, "code": code})
                    result["status"] = code
                    result["final_url"] = newurl
                    return None

            opener = urllib.request.build_opener(NoRedirectHandler, urllib.request.HTTPSHandler(context=ctx))
            try:
                resp = opener.open(req, timeout=TIMEOUT)
                result["status"] = resp.getcode()
                result["content_type"] = resp.headers.get("Content-Type", "N/A")
                result["final_url"] = resp.url
            except urllib.error.HTTPError as e:
                if result["status"] is None:
                    result["status"] = e.code
        else:
            resp = urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx)
            result["status"] = resp.getcode()
            result["content_type"] = resp.headers.get("Content-Type", "N/A")
            result["final_url"] = resp.url

    except urllib.error.HTTPError as e:
        result["status"] = e.code
        result["error"] = str(e.reason)
    except urllib.error.URLError as e:
        result["status"] = "ERR"
        result["error"] = str(e.reason)
    except Exception as e:
        result["status"] = "ERR"
        result["error"] = str(e)

    result["response_time_ms"] = round((time.time() - start) * 1000)
    return result


def main():
    print("=" * 80)
    print("PHASE 1.1 — HTTP STATUS CODE SWEEP")
    print("Target: https://bharatneurotech.com")
    print("=" * 80)
    print()

    # Step 1: Fetch sitemap
    print("[1/4] Fetching sitemap.xml...")
    try:
        sitemap_urls = fetch_sitemap(SITEMAP_URL)
        print(f"      Found {len(sitemap_urls)} URLs in sitemap")
    except Exception as e:
        print(f"      Failed to fetch sitemap: {e}")
        sys.exit(1)

    # Step 2: Check lastmod dates
    print()
    print("[2/4] Checking sitemap lastmod dates...")
    bad_lastmod = [u for u in sitemap_urls if u["lastmod"] == "1970-01-01"]
    good_lastmod = [u for u in sitemap_urls if u["lastmod"] != "1970-01-01" and u["lastmod"] != "N/A"]
    print(f"      WARNING: {len(bad_lastmod)} URLs have lastmod = 1970-01-01 (needs fix)")
    print(f"      OK: {len(good_lastmod)} URLs have valid lastmod dates")

    # Step 3: Crawl all sitemap URLs
    print()
    print(f"[3/4] Crawling {len(sitemap_urls)} sitemap URLs...")
    print("-" * 80)

    results = {"pass": [], "fail": [], "slow": []}
    total = len(sitemap_urls)

    for i, entry in enumerate(sitemap_urls, 1):
        url = entry["url"]
        short_path = url.replace("https://bharatneurotech.com", "")
        if not short_path:
            short_path = "/"

        r = check_url(url)
        status = r["status"]
        ms = r["response_time_ms"]

        if status == 200:
            icon = "PASS"
            results["pass"].append(r)
        elif status in (301, 302, 307, 308):
            icon = "RDIR"
            results["pass"].append(r)
        else:
            icon = "FAIL"
            results["fail"].append(r)

        if ms and ms > 3000:
            results["slow"].append(r)

        err_info = f" [{r['error']}]" if r.get("error") else ""
        print(f"  [{i:3d}/{total}] {icon}  {status:>4}  {ms:>5}ms  {short_path}{err_info}")

    # Step 4: Check extra URLs
    print()
    print(f"[4/4] Checking {len(EXTRA_URLS)} extra URLs (redirects, 404, assets)...")
    print("-" * 80)

    extra_results = []
    for url in EXTRA_URLS:
        follow = not (url.startswith("http://") or "www." in url)
        r = check_url(url, follow_redirects=follow)
        status = r["status"]
        ms = r["response_time_ms"]

        if url == "https://bharatneurotech.com/this-page-should-not-exist-qa-test":
            expected = 404
            icon = "PASS" if status == 404 else "FAIL"
            note = f" (expected 404, got {status})" if status != 404 else " (404 as expected)"
        elif url.startswith("http://") or "www." in url:
            expected = "3xx"
            icon = "PASS" if str(status).startswith("3") or status == 200 else "FAIL"
            note = f" -> {r.get('final_url', 'N/A')}" if r.get("redirect_chain") else f" (status: {status})"
        else:
            expected = 200
            icon = "PASS" if status == 200 else "FAIL"
            note = ""

        err_info = f" [{r['error']}]" if r.get("error") else ""
        print(f"  {icon}  {status:>4}  {ms:>5}ms  {url}{note}{err_info}")
        extra_results.append(r)

    # ===== SUMMARY =====
    print()
    print("=" * 80)
    print("PHASE 1.1 — SUMMARY")
    print("=" * 80)

    total_pass = len(results["pass"])
    total_fail = len(results["fail"])
    total_slow = len(results["slow"])

    print(f"""
  Sitemap URLs tested:     {total}
  Passed (200/3xx):        {total_pass}
  Failed (4xx/5xx/ERR):    {total_fail}
  Slow (>3000ms):          {total_slow}
  Bad lastmod dates:       {len(bad_lastmod)}
""")

    if results["fail"]:
        print("  FAILED URLs:")
        for r in results["fail"]:
            print(f"     {r['status']}  {r['url']}  [{r.get('error', '')}]")
        print()

    if results["slow"]:
        print("  SLOW URLs (>3000ms):")
        for r in results["slow"]:
            print(f"     {r['response_time_ms']}ms  {r['url']}")
        print()

    if total_fail == 0:
        print("  VERDICT: PHASE 1.1 PASSED — All sitemap URLs are healthy!")
    else:
        print(f"  VERDICT: PHASE 1.1 FAILED — {total_fail} URLs need attention!")

    print()

    # Save detailed results to JSON
    output = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "sitemap_url_count": total,
        "passed": total_pass,
        "failed": total_fail,
        "slow": total_slow,
        "bad_lastmod_count": len(bad_lastmod),
        "failed_urls": [{"url": r["url"], "status": r["status"], "error": r.get("error")} for r in results["fail"]],
        "slow_urls": [{"url": r["url"], "ms": r["response_time_ms"]} for r in results["slow"]],
    }

    json_path = sys.argv[1] if len(sys.argv) > 1 else "qa_phase1_results.json"
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"  Detailed results saved to: {json_path}")


if __name__ == "__main__":
    main()
