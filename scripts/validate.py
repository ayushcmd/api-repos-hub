"""
API Repos Hub — Link Validator
Checks all links in markdown files for broken URLs
"""

import re
import requests
import os
from pathlib import Path

def get_all_links(directory):
    """Extract all markdown links from .md files"""
    links = []
    md_files = Path(directory).rglob("*.md")
    
    for file in md_files:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            found = re.findall(r'\[.*?\]\((https?://[^\)]+)\)', content)
            for link in found:
                links.append({"url": link, "file": str(file)})
    
    return links

def check_link(url, timeout=10):
    """Check if a URL is accessible"""
    try:
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        return response.status_code < 400
    except Exception:
        return False

def validate_all_links(directory="."):
    """Main validator function"""
    print("🔍 API Repos Hub — Link Validator\n")
    
    links = get_all_links(directory)
    print(f"Found {len(links)} links to check...\n")
    
    broken = []
    ok = []
    
    for item in links:
        url = item["url"]
        file = item["file"]
        
        is_valid = check_link(url)
        
        if is_valid:
            print(f"  ✅ {url}")
            ok.append(item)
        else:
            print(f"  ❌ {url} — in {file}")
            broken.append(item)
    
    print(f"\n📊 Results:")
    print(f"  ✅ Working: {len(ok)}")
    print(f"  ❌ Broken: {len(broken)}")
    
    if broken:
        print(f"\n🔧 Broken links to fix:")
        for item in broken:
            print(f"  - {item['url']} ({item['file']})")
    else:
        print("\n🎉 All links are working!")

if __name__ == "__main__":
    validate_all_links()