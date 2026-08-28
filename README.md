# 🏢 Annapurna Aluminium & UPVC Udhyog — Official Showcase & Catalog Website

> **Ultra-Luxury Architectural Fabrication Platform & 102+ Design Catalog**  
> **Location:** Murli Chowk (Airport Road), Janakpur Dham-8, Dhanusha, Madhesh Province, Nepal  
> **Helpline / WhatsApp:** `+977 9817658719` / `+977 9817667115`  
> **Founder:** Prof. Nageshwar Thakur  

---

## 🌟 Overview

This repository contains the complete source code, curated photographic assets, technical SVG architectural drawings, and build automation for the official business platform of **Annapurna Aluminium & UPVC Udhyog**.

### Key Highlights
- **🌐 Seamless Dual-Language Support**: Instant 1-click reactive toggle between **English** and **नेपाली (Nepali)**.
- **📸 40+ Authentic Real Workshop Project Gallery**: Curated high-res installations including commercial curtain walls, Sri Nav Durga Mandir Duhaba gates, luxury villa UPVC sliding windows, black marble staircase railings, and modular kitchen racks.
- **📦 102+ Master Design Catalog**: Instant debounce search across 11 product categories, with a live view mode switch between **📸 Real Photo View** and **📐 Architectural Blueprint Vector Mode**.
- **📝 Free Site Visit & Measurement Booking**: Interactive form with automatic direct WhatsApp booking dispatch.
- **🔬 Material & Factory Standards Matrix**: Deep-dive into German multi-chamber UPVC, 6063-T5 virgin aluminium alloy, and SS 304 mirror-grade stainless steel.
- **📱 Floating Speed Dials**: Pulse-animated direct WhatsApp and phone call buttons for high conversion.

---

## 📁 Repository Structure

```
├── index.html                   # Main production website entry (Root)
├── catalog/
│   ├── build_all.py             # Master website and catalog compilation engine
│   ├── catalog.html             # Standalone catalog entry
│   ├── products_data.py         # 102 master product definitions & technical specs
│   ├── products_list.json       # JSON database of 102 products
│   ├── real_projects.json       # JSON database of 40+ real workshop projects
│   ├── render_svg.js            # Node.js SVG vector blueprint rendering script
│   ├── svg_art_map.json         # Pre-rendered vector line drawings (102 SVGs)
│   ├── templates.js             # Client-side parametric vector drawing engine
│   └── google_business_profile.md # Local SEO NAP & service area records
├── catalog_assets/
│   ├── real_projects/           # 44 full-resolution optimized project photos + thumbnails
│   └── products/                # Product asset storage
├── image/                       # Raw original archive photos (91 images)
├── uploads/                     # Workshop signboards, branding & identity assets
├── .gitignore                   # Clean git tracking ignore rules
└── README.md                    # Project documentation
```

---

## 🚀 How to Run & Build Locally

### 1. View Website in Browser
Simply open `index.html` in any modern web browser or serve via Python:

```bash
# Start local development server
python -m http.server 8080
```
Open `http://localhost:8080` in your browser.

### 2. Re-compile or Update Website Data
If you modify `catalog/products_data.py` or add new project photos to `catalog_assets/real_projects/`:

```bash
# Rebuild the master HTML website and catalog
python catalog/build_all.py
```

---

## 🌐 Free Instant 1-Click Hosting Options

### Option A: GitHub Pages (Recommended)
1. In your GitHub repository, go to **Settings** → **Pages**.
2. Under **Build and deployment** → **Source**, select **Deploy from a branch**.
3. Choose branch `main` (or `master`) and folder `/ (root)`.
4. Click **Save**. Your website will be live at `https://<username>.github.io/<repo-name>/` in under 60 seconds!

### Option B: Vercel / Netlify / Cloudflare Pages
- Connect your GitHub repository to **Vercel** or **Netlify**.
- Set the publish directory to `./` (root).
- Deploy with 0 configuration needed.

---

## 🗺️ Janakpur local SEO

The build writes crawlable service pages (not hash-only SPA routes) so Google can rank the workshop for neighbourhood and product searches:

| Page | Intent |
|---|---|
| `/upvc-window-janakpur/` | UPVC window Janakpur / यूपीभीसी झ्याल |
| `/aluminium-janakpur/` | Aluminium door & partition |
| `/glass-railing-janakpur/` | Toughened balcony / stair glass |
| `/steel-gate-janakpur/` | SS 304 railing & temple gate |
| `/modular-kitchen-janakpur/` | Waterproof kitchen rack |
| `/acp-cladding-janakpur/` | Shopfront & ACP facade |
| `/janakpur-dham/` | Workshop NAP — Murli Chowk, Ward 8 |
| `/service-areas/` | Dhalkebar, Jaleshwor, Lahan, Bardibas, Madhesh |
| `/faq-janakpur/` | Price, free visit, UPVC vs aluminium |

Also generated: `sitemap.xml` (real URLs + hreflang), `robots.txt`, `llms.txt`, `manifest.webmanifest`, `humans.txt`, `404.html`. Re-run `python catalog/build_all.py` after copy changes. Live site: [annapurna-upvc-janakpur.com](https://annapurna-upvc-janakpur.com/).

---

## 📞 Business Contact & Inquiries

- **Workshop Address:** Murli Chowk (Airport Road), Janakpur Dham-8, Dhanusha, Nepal
- **WhatsApp:** [+977 9817658719](https://wa.me/9779817658719)
- **Call:** `+977 9817658719` / `+977 9817667115`
- **Hours:** 9:00 AM – 7:00 PM (Open All 7 Days)
