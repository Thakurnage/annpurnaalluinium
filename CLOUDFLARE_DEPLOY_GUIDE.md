# ✅ Cloudflare Deploy Fix + Landing Page Upgrade — Completed

## 🐛 Original Error (from logs)
```
✘ [ERROR] Asset too large. Cloudflare Workers supports assets up to 25 MiB.
Found file /opt/buildhome/repo/.git/objects/pack/pack-baffb59bbe0c6df9187f33585fe23d976dad3e66.pack 62.2 MiB
Assets directory "/opt/buildhome/repo" (".")
```

**Root Cause:** `wrangler.jsonc` had `assets.directory = "."` which scans ENTIRE repo including `.git` folder (62 MiB pack file > 25 MiB limit).

## ✅ Fix Applied

### 1. New `wrangler.jsonc` (Cloudflare Ready)
```json
{
  "$schema": "node_modules/wrangler/config-schema.json",
  "name": "annpurnaalluinium",
  "compatibility_date": "2026-08-26",
  "compatibility_flags": ["assets_navigation_prefers_asset_serving"],
  "observability": {"enabled": True},
  "assets": {
    "directory": "./dist",
    "not_found_handling": "single-page-application"
  }
}
```
- `directory: "./dist"` — clean folder with only `index.html` + `catalog_assets/` (NO .git)
- `not_found_handling: "single-page-application"` — SPA routing for landing page

### 2. Clean `dist/` Folder Generation
`catalog/build_all.py` now auto-creates `dist/`:
- Copies `index.html`
- Copies `catalog_assets/` (products + real_projects + grids + owner etc)
- Copies `robots.txt`, `sitemap.xml`, `_headers`, `_redirects`, `_routes.json`
- **Result:** `npx wrangler deploy --dry-run` now reads **238 files from dist** (was 401 from root with .git) — ✅ No error

### 3. Landing Page Upgrades
- **Real Projects:** Now loads **40** from `catalog/real_projects.json` (was hardcoded 26)
  - `All Projects (40)` badge updated
  - Lightbox gallery shows all 40
- **Product Photos:** Now uses **102 dedicated images** from `catalog_assets/products/CODE.jpg`
  - Previously: `PRODUCT_REAL_PHOTO_MAP` reused `real_projects/` images, leaving `products/` folder unused
  - Now: Each product (UWC-01, UWD-03, etc) shows its own product photo
  - Count verified: 102 product JPG references in index.html
- **SEO & Cloudflare Files Added:**
  - `robots.txt` — sitemap reference
  - `sitemap.xml` — 4 URLs with priority
  - `_headers` — caching + security headers (immutable for assets)
  - `_redirects` — SPA fallback `/* /index.html 200`
  - `_routes.json` — routing config
  - `.assetsignore` — prevents .git inclusion even if misconfigured

### 4. `.gitignore` Updated
Ignores `.wrangler/`, `.dev.vars`, `node_modules/`, `dist/` (dist is built locally, not committed to keep repo small)

## 🚀 Deployment Instructions

### Option A: Cloudflare Workers (Wrangler) — Recommended for you
```bash
# Build clean dist
python catalog/build_all.py

# Deploy (reads from ./dist, no .git error)
npx wrangler deploy

# Dry-run test (already verified - 238 files OK)
npx wrangler deploy --dry-run
```

### Option A2: Automatic GitHub Actions (Auto Apply)
`.github/workflows/auto-apply.yml` automatically runs on every push/merge to `main`:
1. Runs `python catalog/build_all.py` → regenerates `index.html`, `catalog.html`, and `dist/`.
2. Uploads the built `dist/` as an artifact (`annapurna-dist`).
3. If repo secrets are configured, deploys directly to Cloudflare automatically.
   - Add repo secrets (Settings → Secrets and variables → Actions):
     - `CLOUDFLARE_API_TOKEN`
     - `CLOUDFLARE_ACCOUNT_ID`
   - If secrets are missing, the workflow still builds and uploads `dist/`, then prints a notice.

### Option B: Cloudflare Pages (GitHub Connected)
1. Go to Cloudflare Dashboard → Pages → Create Project → Connect to GitHub `Thakurnage/annpurnaalluinium`
2. Build Settings:
   - **Framework preset:** None
   - **Build command:** `python catalog/build_all.py`
   - **Build output directory:** `dist`
   - **Root directory:** `/`
3. Environment Variables: None needed
4. Deploy — Pages will run build and publish `dist`

### Option C: GitHub Pages (still works)
- `index.html` at repo root is the full site (384KB)
- Already updated with 40 projects + 102 product images

## 📊 Verification
```bash
# Dry-run now succeeds
✨ Read 238 files from the assets directory /home/user/annpurnaalluinium/dist
Total Upload: 0.33 KiB / gzip: 0.24 KiB
--dry-run: exiting now.

# Content checks
All Projects (40) — found
Product images from products/: 102
Real projects count: 40
No .git in dist: verified
```

## 📁 Files Changed / Created
- **Modified:** `catalog/build_all.py` (now loads JSON, uses products/ images, generates dist)
- **Modified:** `index.html` (40 projects, 102 product photos)
- **Modified:** `catalog/catalog.html`
- **Modified:** `catalog/products_list.json` (photo paths fixed)
- **Modified:** `catalog/real_projects.json` (enriched with 40 entries)
- **Modified:** `.gitignore`
- **Created:** `wrangler.jsonc` (fixed)
- **Created:** `_headers`, `_redirects`, `_routes.json`, `robots.txt`, `sitemap.xml`, `.assetsignore`
- **Generated (gitignored):** `dist/` folder (49M with assets, 238 files, largest file 2.3M < 25M limit)

## 🎯 Next Step for You
Push already done to branch `arena/01a04441-annpurnaalluinium`. Merge to `main` on GitHub, then:
- If using Workers: run `npx wrangler deploy` locally once, or set Cloudflare Build to run build_all.py
- If using Pages: Connect repo, set build command as above, it will auto-deploy

Your site is now **Cloudflare-ready** and **GitHub-upgraded** with all 40 real projects visible!
