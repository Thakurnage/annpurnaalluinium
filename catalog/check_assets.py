#!/usr/bin/env python3
"""
Smart Asset Checker — Ensures Cloudflare 25 MiB limit never breaks deployment
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
LIMIT_MB = 25
LIMIT_BYTES = LIMIT_MB * 1024 * 1024

def check_assets():
    print(f"🔍 Checking assets in {DIST} for Cloudflare {LIMIT_MB} MiB limit...")
    if not DIST.exists():
        print(f"❌ dist/ not found, run python catalog/build_all.py first")
        return False
    
    large_files = []
    total_files = 0
    total_size = 0
    
    for f in DIST.rglob("*"):
        if f.is_file():
            total_files += 1
            size = f.stat().st_size
            total_size += size
            if size > LIMIT_BYTES:
                large_files.append((f, size))
    
    print(f"📦 Total: {total_files} files, {total_size / (1024*1024):.2f} MiB")
    
    if large_files:
        print(f"\n❌ Found {len(large_files)} files > {LIMIT_MB} MiB (will break deploy):")
        for path, size in large_files:
            rel = path.relative_to(ROOT)
            print(f"   - {rel}: {size / (1024*1024):.2f} MiB")
        print(f"\n💡 Smart Fix Options:")
        print(f"   1. Move to Cloudflare R2 (for videos, large PDFs)")
        print(f"   2. Compress images: Use TinyPNG or python -m Pillow")
        print(f"   3. Add to .assetsignore if not needed")
        print(f"   4. Split large files")
        return False
    else:
        print(f"✅ All files < {LIMIT_MB} MiB — Deployment will succeed for any size repo!")
        print(f"   Largest file: {max((f.stat().st_size for f in DIST.rglob('*') if f.is_file()), default=0) / (1024*1024):.2f} MiB")
        return True

if __name__ == "__main__":
    ok = check_assets()
    sys.exit(0 if ok else 1)
