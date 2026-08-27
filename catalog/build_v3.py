#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Annapurna Aluminium & UPVC — Professional v3.0 Builder
Smart, Modern, Conversion-Focused
"""

import json, shutil, sys
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "catalog_assets"
PRODUCTS_DIR = ASSETS / "products"
CATALOG_DIR = ROOT / "catalog"
DIST_DIR = ROOT / "dist"
sys.path.insert(0, str(CATALOG_DIR))
from products_data import P, CATS, BASE_FEATS

BUILD_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S NPT")
BUILD_VERSION = "v3.0 Professional"

SHOP = {
    "name": "Annapurna Aluminium & UPVC",
    "legal_name": "Annapurna Aluminium & UPVC Udhyog",
    "owner_name": "Prof. Nageshwar Thakur",
    "phone1": "+977 9817658719",
    "phone2": "+977 9817667115",
    "whatsapp": "9779817658719",
    "address": "Janakpur Dham-8, Murli Chowk (Airport Road), Dhanusha, Madhesh Province, Nepal",
    "gmaps_url": "https://maps.google.com/?q=Murli+Chowk+Airport+Road+Janakpur+Nepal",
    "hours": "Sunday – Saturday: 9:00 AM – 7:00 PM (All 7 Days Open)",
    "domain": "https://annapurna-upvc-janakpur.com",
    "service_areas": ["Janakpur Dham","Dhanusha","Mahottari","Sarlahi","Siraha","Bardibas","Rajbiraj","Birgunj","Kathmandu","Nepal-Wide"]
}

# Load 40 projects
real_projects = json.loads((CATALOG_DIR / "real_projects.json").read_text(encoding="utf-8"))
print(f"Loaded {len(real_projects)} real projects")

# Enrich with Nepali fallback
CAT_NE = {
    "Storefront & Facade": "फसाड र एसीपी क्ल्याडिङ",
    "MS & Steel Works": "स्टिल तथा मन्दिर गेट",
    "UPVC Windows & Doors": "यूपीभीसी झ्याल तथा ढोका",
    "UPVC Windows": "यूपीभीसी झ्यालहरू",
    "UPVC Doors": "यूपीभीसी ढोकाहरू",
    "Modular Kitchen Racks": "मोड्युलर किचन र्याक",
    "Stainless Steel Railings": "स्टेनलेस स्टील रेलिङ",
    "Aluminium Partitions": "आल्मुनियम पार्टिसन",
    "Aluminium Windows": "आल्मुनियम झ्यालहरू",
    "Aluminium Doors": "आल्मुनियम ढोकाहरू",
    "Glass Solutions": "ग्लास सोलुसन्स",
}
REAL_PROJECTS = []
for proj in real_projects:
    e = dict(proj)
    e.setdefault("category_ne", CAT_NE.get(e.get("category",""), e.get("category","")))
    e.setdefault("title_ne", e.get("title",""))
    e.setdefault("location_ne", e.get("location",""))
    e.setdefault("desc_ne", e.get("desc",""))
    REAL_PROJECTS.append(e)

# Load SVG map
svg_map = {}
svg_file = CATALOG_DIR / "svg_art_map.json"
if svg_file.exists():
    try: svg_map = json.loads(svg_file.read_text(encoding="utf-8"))
    except: pass

templates_js_raw = (CATALOG_DIR / "templates.js").read_text(encoding="utf-8")

CAT_META = {
    "UWC": {"color": "#00d2ff", "badge": "UPVC Windows", "badge_ne": "यूपीभीसी झ्यालहरू"},
    "UWD": {"color": "#3b82f6", "badge": "UPVC Doors", "badge_ne": "यूपीभीसी ढोकाहरू"},
    "ALW": {"color": "#22d3ee", "badge": "Aluminium Windows", "badge_ne": "आल्मुनियम झ्यालहरू"},
    "ALD": {"color": "#60a5fa", "badge": "Aluminium Doors", "badge_ne": "आल्मुनियम ढोकाहरू"},
    "ALP": {"color": "#2dd4bf", "badge": "Aluminium Partitions", "badge_ne": "आल्मुनियम पार्टिसन"},
    "GLZ": {"color": "#818cf8", "badge": "Glass Solutions", "badge_ne": "टफन्ड ग्लास"},
    "STF": {"color": "#a855f7", "badge": "Storefront & Facades", "badge_ne": "ग्लास फसाड तथा एसीपी"},
    "MST": {"color": "#f59e0b", "badge": "MS & Steel Works", "badge_ne": "मन्दिर तथा मेन गेट"},
    "SLS": {"color": "#eab308", "badge": "SS 304", "badge_ne": "एसएस ३०४ रेलिङ"},
    "RLS": {"color": "#f97316", "badge": "Railings", "badge_ne": "बालकनी तथा भर्याङ"},
    "MOD": {"color": "#ec4899", "badge": "Modular Kitchen", "badge_ne": "मोड्युलर किचन"},
}

products_list = []
for pr in P:
    code = pr["code"]
    cat = pr["cat"]
    photo_rel = f"catalog_assets/products/{code}.jpg" if (PRODUCTS_DIR / f"{code}.jpg").exists() else f"catalog_assets/real_projects/facade_commercial_plaza.jpg"
    products_list.append({
        "code": code, "cat": cat, "name": pr["name"], "desc": pr["desc"],
        "sizes": pr["sizes"], "finishes": pr["finishes"], "extras": pr["extras"],
        "base_feats": BASE_FEATS.get(cat, []), "photo": photo_rel,
        "svg": svg_map.get(code, ""), "art_key": pr["art"][0], "art_params": pr["art"][1],
        "meta": CAT_META.get(cat, {})
    })

print(f"Prepared {len(products_list)} products with dedicated images")

# Precompute category pills to avoid backslash in f-string expression
cat_pills_html = ""
for c in CATS:
    key = c["key"]
    name = c["name"]
    cat_pills_html += f'<button onclick="filterCatalog(\'{key}\')" class="cat-pill px-4 py-2.5 rounded-xl text-xs font-bold bg-slate-900 text-slate-300 border border-white/10" data-cat="{key}">{name}</button>\n'

# Build HTML
html = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Annapurna Aluminium & UPVC | Janakpur #1 | 102+ Designs | 40+ Real Projects</title>
<meta name="description" content="Janakpur's #1 UPVC & Aluminium Fabricator — 102+ custom designs, 40+ real site photos, German UPVC, SS 304 railings, temple gates, modular kitchens. Free measurement in Dhanusha, Mahottari. Call 9817658719">
<meta name="theme-color" content="#040711">
<meta property="og:title" content="Annapurna Aluminium & UPVC | 102+ Designs | Janakpur">
<meta property="og:image" content="catalog_assets/real_projects/facade_commercial_plaza.jpg">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Outfit:wght@600;800;900&display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com"></script>
<script>
tailwind.config={{theme:{{extend:{{fontFamily:{{sans:['Plus Jakarta Sans','sans-serif'],display:['Outfit','sans-serif']}},colors:{{luxury:{{950:'#040711',900:'#080d1a',800:'#142036',cyan:'#00d2ff',gold:'#f59e0b'}}}}}}}}}}
</script>
<style>
body{{background:#040711;color:#f1f5f9;font-family:'Plus Jakarta Sans',sans-serif}}
.glass{{background:rgba(14,22,38,0.75);backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.08)}}
.glass-nav{{background:rgba(4,7,17,0.92);backdrop-filter:blur(24px);border-bottom:1px solid rgba(255,255,255,0.08)}}
.card{{background:linear-gradient(145deg,rgba(20,32,54,0.65),rgba(8,13,26,0.85));border:1px solid rgba(255,255,255,0.07);transition:all .35s cubic-bezier(.16,1,.3,1)}}
.card:hover{{transform:translateY(-6px);border-color:rgba(0,210,255,0.4);box-shadow:0 20px 40px -12px rgba(0,210,255,0.18)}}
::-webkit-scrollbar{{width:6px}}::-webkit-scrollbar-thumb{{background:#1e2e4a;border-radius:4px}}
.blueprint{{background:radial-gradient(circle at center,#0e2440 0%,#061120 100%);border:1px dashed rgba(0,210,255,0.25)}}
</style>
</head>
<body class="antialiased">
<!-- Build Info: {BUILD_VERSION} | {BUILD_TIME} | 40 Projects | 102 Products -->
<div class="bg-gradient-to-r from-slate-950 via-cyan-950/20 to-slate-950 border-b border-white/5 py-2 px-4 text-[11px]">
<div class="max-w-7xl mx-auto flex flex-wrap justify-between items-center gap-2 text-slate-300">
<div class="flex items-center gap-3">
<span class="px-2.5 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 font-bold flex items-center gap-1.5"><span class="w-2 h-2 bg-emerald-400 rounded-full animate-ping"></span>OPEN 7 DAYS • 9AM-7PM • {BUILD_VERSION}</span>
<span class="hidden md:inline text-slate-400">📍 Murli Chowk (Airport Road), Janakpur Dham-8</span>
</div>
<div class="flex items-center gap-3">
<span class="hidden sm:inline px-2 py-0.5 rounded bg-cyan-500/10 text-cyan-400 border border-cyan-500/20 text-[10px] font-bold">40 REAL PROJECTS • 102 DESIGNS • 1200+ SITES</span>
<a href="tel:{SHOP['phone1']}" class="text-cyan-400 font-bold">📞 {SHOP['phone1']}</a>
</div>
</div>
</div>

<nav class="sticky top-0 z-50 glass-nav">
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
<a href="#" class="flex items-center gap-3">
<div class="w-11 h-11 rounded-xl bg-gradient-to-tr from-cyan-500 to-amber-400 p-0.5"><div class="w-full h-full bg-slate-950 rounded-[10px] flex items-center justify-center font-black text-lg text-cyan-400">A</div></div>
<div><div class="font-display font-extrabold text-[17px] tracking-tight text-white">Annapurna <span class="text-cyan-400">Alu & UPVC</span></div><div class="text-[10px] text-slate-400 -mt-0.5">Janakpur Dham • Factory Direct Price</div></div>
</a>
<div class="hidden lg:flex items-center gap-5 text-[13px] font-semibold text-slate-300">
<a href="#projects" class="hover:text-cyan-400">✦ Projects (40)</a>
<a href="#catalog" class="hover:text-cyan-400">◈ Catalog (102)</a>
<a href="#process" class="hover:text-cyan-400">⚙️ Process</a>
<a href="#consultation" class="hover:text-cyan-400">📝 Free Visit</a>
<a href="#contact" class="hover:text-cyan-400">📍 Contact</a>
</div>
<div class="hidden sm:flex gap-2">
<a href="https://wa.me/{SHOP['whatsapp']}?text=Namaste%20Annapurna,%20I%20need%20quote" target="_blank" class="px-4 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs">💬 WhatsApp</a>
<a href="tel:{SHOP['phone1']}" class="px-4 py-2.5 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-black font-black text-xs">📞 Call</a>
</div>
<button onclick="document.getElementById('mobile-menu').classList.toggle('hidden')" class="lg:hidden p-2 rounded-xl bg-slate-900 border border-white/10">☰</button>
</div>
<div id="mobile-menu" class="hidden lg:hidden border-t border-white/5 bg-slate-950 px-5 py-4 space-y-2 text-sm">
<a href="#projects" class="block py-2">🌟 Real Projects (40)</a>
<a href="#catalog" class="block py-2">📦 102 Designs</a>
<a href="#process" class="block py-2">⚙️ Our Process</a>
<a href="#consultation" class="block py-2">📝 Free Measurement</a>
<a href="#contact" class="block py-2">📍 Contact</a>
</div>
</nav>

<section class="relative min-h-[88vh] flex items-center justify-center overflow-hidden py-14">
<div class="absolute inset-0"><div class="absolute inset-0 bg-gradient-to-t from-[#040711] via-[#040711]/80 to-[#040711]/50 z-10"></div><div class="absolute inset-0 bg-[radial-gradient(ellipse_at_top,_rgba(0,210,255,0.15),transparent_60%)] z-10"></div><img src="catalog_assets/real_projects/facade_commercial_plaza.jpg" class="w-full h-full object-cover opacity-30 scale-105"></div>
<div class="relative z-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
<div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 text-xs font-bold mb-6">★ ★ ★ ★ ★ #1 Certified Fabricator • Janakpur Dham • {BUILD_VERSION}</div>
<h1 class="font-display text-4xl sm:text-6xl lg:text-[68px] font-black tracking-tight leading-[0.95] text-white max-w-5xl mx-auto mb-5">
<span class="text-white">Premium</span> <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-500">UPVC, Aluminium</span><br><span class="text-transparent bg-clip-text bg-gradient-to-r from-amber-300 to-yellow-500">& Glass Works</span> <span class="text-white">in Nepal</span>
</h1>
<p class="text-slate-300 max-w-3xl mx-auto text-[15px] sm:text-lg leading-relaxed mb-8">
Factory-direct manufacturing in Murli Chowk: German multi-chamber UPVC windows, slim aluminium partitions, SS 304 temple gates, frameless glass railings & waterproof modular kitchens. <span class="text-cyan-400 font-bold">102+ designs • 40+ live site photos • Free measurement</span>
</p>
<div class="flex flex-wrap justify-center gap-3 mb-12">
<a href="#projects" class="px-7 py-3.5 rounded-2xl bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-black font-black text-sm shadow-xl shadow-cyan-500/20">📸 See Real Work (40)</a>
<a href="#catalog" class="px-7 py-3.5 rounded-2xl bg-slate-900 border border-white/10 hover:border-cyan-500/40 text-white font-bold text-sm">📐 102 Designs Catalog</a>
<a href="https://wa.me/{SHOP['whatsapp']}?text=Namaste%20Annapurna,%20Free%20site%20measurement%20chahiye" target="_blank" class="px-7 py-3.5 rounded-2xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-sm">💬 Free Site Visit</a>
</div>
<div class="grid grid-cols-2 md:grid-cols-4 gap-3 max-w-4xl mx-auto text-left">
<div class="glass p-4 rounded-2xl"><div class="text-3xl font-black text-cyan-400">102+</div><div class="text-[11px] text-slate-400 font-semibold">Custom Designs</div></div>
<div class="glass p-4 rounded-2xl"><div class="text-3xl font-black text-amber-400">40+</div><div class="text-[11px] text-slate-400 font-semibold">Real Projects Live</div></div>
<div class="glass p-4 rounded-2xl"><div class="text-3xl font-black text-emerald-400">1200+</div><div class="text-[11px] text-slate-400 font-semibold">Sites Completed</div></div>
<div class="glass p-4 rounded-2xl"><div class="text-3xl font-black text-purple-400">15+ Yrs</div><div class="text-[11px] text-slate-400 font-semibold">Master Experience</div></div>
</div>
</div>
</section>

<section id="trust" class="py-6 border-y border-white/5 bg-slate-950/50">
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-wrap justify-center items-center gap-6 text-[11px] text-slate-400">
<span class="flex items-center gap-1.5"><span class="w-5 h-5 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center text-xs">✓</span> SS 304 Certified</span>
<span class="flex items-center gap-1.5"><span class="w-5 h-5 rounded-full bg-cyan-500/20 text-cyan-400 flex items-center justify-center text-xs">✓</span> German UPVC Profile</span>
<span class="flex items-center gap-1.5"><span class="w-5 h-5 rounded-full bg-amber-500/20 text-amber-400 flex items-center justify-center text-xs">✓</span> 6063-T5 Virgin Aluminium</span>
<span class="flex items-center gap-1.5"><span class="w-5 h-5 rounded-full bg-purple-500/20 text-purple-400 flex items-center justify-center text-xs">✓</span> Toughened Glass 8-12mm</span>
<span class="flex items-center gap-1.5"><span class="w-5 h-5 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center text-xs">✓</span> Factory Direct Price</span>
<span class="flex items-center gap-1.5"><span class="w-5 h-5 rounded-full bg-cyan-500/20 text-cyan-400 flex items-center justify-center text-xs">✓</span> Free Measurement</span>
</div>
</section>

<section id="projects" class="py-20 bg-[#040711]">
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
<div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-10">
<div>
<div class="inline-flex px-3 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/20 text-cyan-400 text-xs font-bold mb-3">🌟 40 AUTHENTIC SITE PHOTOS</div>
<h2 class="text-3xl sm:text-5xl font-black font-display text-white tracking-tight">Real Projects Gallery</h2>
<p class="text-slate-400 text-sm mt-2 max-w-2xl">Every photo is from our Murli Chowk workshop & actual client sites — facades, temple gates, SS railings, modular kitchens.</p>
</div>
<div class="flex gap-2 overflow-x-auto pb-2" id="project-filters">
<button onclick="filterProjects('all')" class="proj-filter-btn px-4 py-2.5 rounded-xl text-xs font-bold bg-cyan-500 text-black" data-cat="all">All (40)</button>
<button onclick="filterProjects('STF')" class="proj-filter-btn px-4 py-2.5 rounded-xl text-xs font-bold bg-slate-900 text-slate-300 border border-white/10" data-cat="STF">Facades</button>
<button onclick="filterProjects('UWC')" class="proj-filter-btn px-4 py-2.5 rounded-xl text-xs font-bold bg-slate-900 text-slate-300 border border-white/10" data-cat="UWC">UPVC</button>
<button onclick="filterProjects('SLS')" class="proj-filter-btn px-4 py-2.5 rounded-xl text-xs font-bold bg-slate-900 text-slate-300 border border-white/10" data-cat="SLS">SS Railings</button>
<button onclick="filterProjects('MST')" class="proj-filter-btn px-4 py-2.5 rounded-xl text-xs font-bold bg-slate-900 text-slate-300 border border-white/10" data-cat="MST">Temple Gates</button>
<button onclick="filterProjects('MOD')" class="proj-filter-btn px-4 py-2.5 rounded-xl text-xs font-bold bg-slate-900 text-slate-300 border border-white/10" data-cat="MOD">Kitchen</button>
</div>
</div>
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5" id="real-projects-grid"></div>
</div>
</section>

<section id="catalog" class="py-20 border-t border-white/5 bg-slate-950/30">
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
<div class="text-center max-w-3xl mx-auto mb-10">
<div class="inline-flex px-3 py-1 rounded-full bg-amber-500/10 border border-amber-500/20 text-amber-400 text-xs font-bold mb-3">📐 102 FACTORY DESIGNS</div>
<h2 class="text-3xl sm:text-5xl font-black font-display text-white">Master Catalog</h2>
<p class="text-slate-400 text-sm mt-2">All 102 designs with dedicated product photos from <code class="text-cyan-400">catalog_assets/products/</code> — custom sizes fabricated.</p>
</div>
<div class="glass p-3 rounded-2xl mb-6 flex flex-col md:flex-row gap-3 justify-between items-center">
<div class="relative w-full md:w-96">
<input id="catalog-search" oninput="handleCatalogSearch()" placeholder="Search UWC-01, Sliding, Gate, Kitchen..." class="w-full px-4 py-2.5 pl-10 rounded-xl bg-slate-950 border border-white/10 text-white text-sm focus:border-cyan-400 outline-none">
<span class="absolute left-3 top-2.5 text-slate-400">🔍</span>
</div>
<div class="flex items-center gap-2 text-xs">
<span class="text-slate-400">View:</span>
<button onclick="setCatalogViewMode('photo')" id="view-mode-photo" class="px-3 py-1.5 rounded-lg bg-cyan-500 text-black font-bold">📸 Photos</button>
<button onclick="setCatalogViewMode('blueprint')" id="view-mode-blueprint" class="px-3 py-1.5 rounded-lg bg-slate-900 text-slate-400 border border-white/10">📐 Blueprint</button>
</div>
</div>
<div class="flex gap-2 overflow-x-auto pb-4 mb-6" id="catalog-category-pills">
<button onclick="filterCatalog('ALL')" class="cat-pill px-4 py-2.5 rounded-xl text-xs font-bold bg-cyan-500 text-black" data-cat="ALL">All 102</button>
{cat_pills_html}
</div>
<div class="flex justify-between text-xs text-slate-400 mb-4"><span>Showing <span id="catalog-count" class="text-cyan-400 font-bold">102</span> products</span><span class="text-slate-500">Build: {BUILD_TIME} • {BUILD_VERSION}</span></div>
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5" id="products-container"></div>
</div>
</section>

<section id="process" class="py-20 bg-[#040711] border-t border-white/5">
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
<div class="text-center max-w-3xl mx-auto mb-12">
<div class="inline-flex px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs font-bold mb-3">⚙️ HOW WE WORK</div>
<h2 class="text-3xl sm:text-4xl font-black font-display text-white">From Measurement to Installation in 4 Steps</h2>
</div>
<div class="grid grid-cols-1 md:grid-cols-4 gap-5">
<div class="card p-6 rounded-2xl"><div class="w-10 h-10 rounded-xl bg-cyan-500/20 text-cyan-400 flex items-center justify-center font-black mb-3">1</div><h4 class="font-bold text-white mb-1">Free Site Visit</h4><p class="text-xs text-slate-400">Engineer visits with samples, laser measurement in Janakpur, Dhanusha, Mahottari.</p></div>
<div class="card p-6 rounded-2xl"><div class="w-10 h-10 rounded-xl bg-amber-500/20 text-amber-400 flex items-center justify-center font-black mb-3">2</div><h4 class="font-bold text-white mb-1">Design & Quote</h4><p class="text-xs text-slate-400">3D blueprint + transparent factory price within 24 hours.</p></div>
<div class="card p-6 rounded-2xl"><div class="w-10 h-10 rounded-xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-black mb-3">3</div><h4 class="font-bold text-white mb-1">Factory Fabrication</h4><p class="text-xs text-slate-400">Precision cutting, TIG welding, powder coating in Murli Chowk workshop.</p></div>
<div class="card p-6 rounded-2xl"><div class="w-10 h-10 rounded-xl bg-purple-500/20 text-purple-400 flex items-center justify-center font-black mb-3">4</div><h4 class="font-bold text-white mb-1">Install & Warranty</h4><p class="text-xs text-slate-400">Professional installation + warranty, after-sales support.</p></div>
</div>
</div>
</section>

<section id="consultation" class="py-20 border-t border-white/5 bg-slate-950/30">
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 lg:grid-cols-12 gap-10">
<div class="lg:col-span-5">
<div class="inline-flex px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs font-bold mb-3">📝 FREE MEASUREMENT</div>
<h2 class="text-3xl sm:text-5xl font-black font-display text-white mb-4">Book Free Site Visit Today</h2>
<p class="text-slate-300 text-sm leading-relaxed mb-6">New house or showroom? Our master engineer will visit with profile samples for laser measurement.</p>
<div class="space-y-3 text-xs text-slate-300 mb-6">
<div class="flex gap-3"><span class="w-6 h-6 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold">✓</span> Free laser measurement in Dhanusha, Mahottari, Sarlahi</div>
<div class="flex gap-3"><span class="w-6 h-6 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold">✓</span> Factory direct price, zero middleman</div>
<div class="flex gap-3"><span class="w-6 h-6 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold">✓</span> Quote in 24 hours</div>
</div>
</div>
<div class="lg:col-span-7">
<div class="glass p-7 rounded-3xl">
<h3 class="text-xl font-bold text-white mb-4">Request Site Visit & Quote — {BUILD_VERSION}</h3>
<form onsubmit="handleContactSubmit(event)" class="space-y-4">
<input id="form-name" required placeholder="Full Name" class="w-full px-4 py-3 rounded-xl bg-slate-950 border border-white/10 text-white text-sm">
<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
<input id="form-phone" required placeholder="Phone / WhatsApp" class="w-full px-4 py-3 rounded-xl bg-slate-950 border border-white/10 text-white text-sm">
<input id="form-city" required placeholder="Location / District" class="w-full px-4 py-3 rounded-xl bg-slate-950 border border-white/10 text-white text-sm">
</div>
<select id="form-service" class="w-full px-4 py-3 rounded-xl bg-slate-950 border border-white/10 text-white text-sm">
<option>UPVC Windows & Doors</option><option>Aluminium Windows & Partitions</option><option>SS 304 Railings</option><option>Temple Gate</option><option>Modular Kitchen</option><option>Full Building Package</option>
</select>
<textarea id="form-notes" rows="3" placeholder="Sizes, number of openings..." class="w-full px-4 py-3 rounded-xl bg-slate-950 border border-white/10 text-white text-sm"></textarea>
<button type="submit" class="w-full py-4 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 text-black font-black text-sm">Submit via WhatsApp →</button>
</form>
</div>
</div>
</div>
</section>

<section id="contact" class="py-16 border-t border-white/5">
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 lg:grid-cols-2 gap-10">
<div>
<h2 class="text-3xl font-black text-white mb-4">Visit Workshop — Murli Chowk</h2>
<div class="space-y-3 text-sm">
<div class="glass p-4 rounded-2xl">📍 {SHOP['address']}</div>
<div class="glass p-4 rounded-2xl">📞 <a href="tel:{SHOP['phone1']}" class="text-cyan-400 font-bold">{SHOP['phone1']}</a> / {SHOP['phone2']}</div>
<div class="glass p-4 rounded-2xl">🕒 {SHOP['hours']} • {BUILD_VERSION} • {BUILD_TIME}</div>
</div>
<div class="mt-6 flex gap-3">
<a href="{SHOP['gmaps_url']}" target="_blank" class="flex-1 py-3 rounded-xl bg-slate-900 border border-white/10 text-cyan-400 font-bold text-xs text-center">🗺️ Google Maps</a>
<a href="https://wa.me/{SHOP['whatsapp']}" target="_blank" class="flex-1 py-3 rounded-xl bg-emerald-600 text-white font-bold text-xs text-center">💬 WhatsApp</a>
</div>
</div>
<div class="glass p-8 rounded-3xl">
<h3 class="text-2xl font-black text-white mb-3">Direct Hotline — Prof. Nageshwar Thakur</h3>
<p class="text-slate-300 text-sm mb-6">Technical guidance on profile, glass, wind load, site scheduling.</p>
<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
<a href="tel:{SHOP['phone1']}" class="p-5 rounded-2xl bg-cyan-500 text-black font-black text-center"><span class="text-xs block">Primary</span>{SHOP['phone1']}</a>
<a href="https://wa.me/{SHOP['whatsapp']}" target="_blank" class="p-5 rounded-2xl bg-emerald-600 text-white font-black text-center"><span class="text-xs block">WhatsApp</span>9817658719</a>
</div>
</div>
</div>
</section>

<footer class="py-10 border-t border-white/5 text-xs text-slate-500">
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row justify-between gap-3">
<div>© 2026 Annapurna Aluminium & UPVC • {BUILD_VERSION} • Build {BUILD_TIME} • 40 Projects • 102 Products • Cloudflare Workers</div>
<div class="flex gap-4"><a href="#projects">Projects</a><a href="#catalog">Catalog</a><a href="#contact">Contact</a></div>
</div>
</footer>

<div id="lightbox-modal" class="fixed inset-0 z-[100] hidden bg-black/90 flex items-center justify-center p-4" onclick="closeLightbox(event)">
<div class="relative max-w-5xl w-full bg-slate-900 border border-white/10 rounded-3xl overflow-hidden" onclick="event.stopPropagation()">
<button onclick="closeLightbox()" class="absolute top-4 right-4 w-10 h-10 rounded-full bg-slate-950 text-white border border-white/10">✕</button>
<div class="grid md:grid-cols-12 max-h-[85vh] overflow-auto">
<div class="md:col-span-8 bg-slate-950 p-2 flex items-center justify-center"><img id="lightbox-img" class="max-h-[75vh] object-contain rounded-xl"></div>
<div class="md:col-span-4 p-6"><span id="lightbox-cat" class="px-2 py-1 rounded bg-cyan-500/20 text-cyan-400 text-[11px] font-bold"></span><h3 id="lightbox-title" class="text-xl font-bold text-white mt-3 mb-2"></h3><p id="lightbox-loc" class="text-xs text-amber-400 mb-2"></p><p id="lightbox-desc" class="text-xs text-slate-300 mb-4"></p><div id="lightbox-specs" class="text-xs text-slate-400 space-y-1 border-t border-white/5 pt-3"></div><button onclick="inquireLightboxItem()" class="mt-6 w-full py-3 rounded-xl bg-emerald-600 text-white font-bold text-xs">💬 Inquire on WhatsApp</button></div>
</div>
</div>
</div>

<div class="fixed bottom-6 right-6 z-40 flex flex-col gap-3">
<a href="https://wa.me/{SHOP['whatsapp']}" target="_blank" class="w-14 h-14 rounded-full bg-emerald-500 text-white flex items-center justify-center text-2xl shadow-2xl animate-bounce">💬</a>
<a href="tel:{SHOP['phone1']}" class="w-12 h-12 rounded-full bg-cyan-500 text-black flex items-center justify-center font-black">📞</a>
</div>

<script>
const SHOP = {json.dumps(SHOP)};
const REAL_PROJECTS = {json.dumps(REAL_PROJECTS)};
const PRODUCTS = {json.dumps(products_list)};
const CATS = {json.dumps(CATS)};
{templates_js_raw}
function getProductSvg(k,p){{if(typeof TEMPLATES!=='undefined'&&TEMPLATES[k]){{try{{return TEMPLATES[k](p||{{}})}}catch(e){{}}}}return ''}}
let currentLang='en', currentProjectFilter='all', currentCatalogCategory='ALL', currentCatalogSearch='', currentCatalogViewMode='photo';
function renderRealProjects(){{const c=document.getElementById('real-projects-grid');if(!c)return;const f=REAL_PROJECTS.filter(p=>currentProjectFilter==='all'||p.cat_key===currentProjectFilter);c.innerHTML=f.map(p=>`<div class="card rounded-3xl overflow-hidden group cursor-pointer" onclick="openLightboxProject('${{p.id}}')"><div class="relative aspect-[4/3] bg-slate-950 overflow-hidden"><img src="catalog_assets/real_projects/${{p.thumb}}" loading="lazy" class="w-full h-full object-cover group-hover:scale-110 transition duration-500"><div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent"></div><div class="absolute top-3 left-3 px-2.5 py-1 rounded-lg bg-slate-950/90 text-cyan-400 border border-cyan-500/30 text-[10px] font-bold">${{p.category}}</div><div class="absolute bottom-3 left-3 right-3"><div class="text-[11px] text-amber-400">📍 ${{p.location}}</div><div class="font-bold text-sm text-white line-clamp-2">${{p.title}}</div></div></div><div class="p-4 bg-slate-900/60"><p class="text-xs text-slate-300 line-clamp-2 mb-3">${{p.desc}}</p><div class="flex justify-between text-xs border-t border-white/5 pt-3"><span class="text-cyan-400 font-bold">View →</span><span class="px-2 py-1 rounded bg-emerald-600/20 text-emerald-400 border border-emerald-500/20 text-[11px]">💬 Quote</span></div></div></div>`).join('');}}
function filterProjects(cat){{currentProjectFilter=cat;document.querySelectorAll('.proj-filter-btn').forEach(b=>{{b.className=b.getAttribute('data-cat')===cat?'proj-filter-btn px-4 py-2.5 rounded-xl text-xs font-bold bg-cyan-500 text-black':'proj-filter-btn px-4 py-2.5 rounded-xl text-xs font-bold bg-slate-900 text-slate-300 border border-white/10'}});renderRealProjects();}}
let activeLightboxItem=null;
function openLightboxProject(id){{const p=REAL_PROJECTS.find(x=>x.id===id);if(!p)return;activeLightboxItem=p;document.getElementById('lightbox-img').src='catalog_assets/real_projects/'+p.image;document.getElementById('lightbox-cat').innerText=p.category;document.getElementById('lightbox-title').innerText=p.title;document.getElementById('lightbox-loc').innerText='📍 '+p.location;document.getElementById('lightbox-desc').innerText=p.desc;document.getElementById('lightbox-specs').innerHTML=p.specs.map(s=>`<div>✓ ${{s}}</div>`).join('');document.getElementById('lightbox-modal').classList.remove('hidden');document.body.style.overflow='hidden';}}
function closeLightbox(){{document.getElementById('lightbox-modal').classList.add('hidden');document.body.style.overflow='auto';}}
function inquireLightboxItem(){{if(!activeLightboxItem)return;const msg=`Namaste Annapurna, I am interested in ${{encodeURIComponent(activeLightboxItem.title)}}`;window.open(`https://wa.me/${{SHOP.whatsapp}}?text=${{msg}}`,'_blank');}}
function renderCatalog(){{const c=document.getElementById('products-container');if(!c)return;const f=PRODUCTS.filter(p=>{{if(currentCatalogCategory!=='ALL'&&p.cat!==currentCatalogCategory)return false;if(currentCatalogSearch){{const q=currentCatalogSearch.toLowerCase();return p.code.toLowerCase().includes(q)||p.name.toLowerCase().includes(q)||p.desc.toLowerCase().includes(q);}}return true;}});document.getElementById('catalog-count').innerText=f.length;if(f.length===0){{c.innerHTML='<div class=\"col-span-full py-16 text-center glass rounded-3xl\">No results</div>';return;}}c.innerHTML=f.map(p=>{{const svg=p.svg||getProductSvg(p.art_key,p.art_params);const color=p.meta.color||'#00d2ff';return `<div class="card rounded-3xl overflow-hidden flex flex-col"><div class="relative aspect-[16/10] bg-slate-950 overflow-hidden flex items-center justify-center">${{currentCatalogViewMode==='photo'?`<img src="${{p.photo}}" loading="lazy" class="w-full h-full object-cover">`:`<div class="blueprint w-full h-full flex items-center justify-center p-4"><svg viewBox="0 0 200 160" class="w-full h-full max-h-[160px]">${{svg}}</svg></div>`}}<div class="absolute top-3 left-3 flex gap-1.5"><span class="px-2 py-0.5 rounded bg-slate-950/90 text-white border border-white/10 text-[10px] font-black">${{p.code}}</span><span class="px-2 py-0.5 rounded text-black text-[10px] font-bold" style="background:${{color}}">${{p.meta.badge||p.cat}}</span></div></div><div class="p-5"><h3 class="font-bold text-white text-[15px] mb-1">${{p.name}}</h3><p class="text-xs text-slate-300 mb-3 line-clamp-2">${{p.desc}}</p><div class="flex flex-wrap gap-1 mb-3">${{p.sizes.slice(0,3).map(s=>`<span class="px-2 py-0.5 rounded bg-slate-950 border border-white/5 text-[10px] text-slate-300">${{s}}</span>`).join('')}}</div><div class="text-[11px] text-slate-400 border-t border-white/5 pt-2">${{p.extras.slice(0,2).map(e=>`<div>✓ ${{e}}</div>`).join('')}}</div></div><div class="p-3 bg-slate-950/70 border-t border-white/5 flex justify-between items-center"><a href="#consultation" class="text-xs font-bold text-cyan-400">Book →</a><a href="https://wa.me/${{SHOP.whatsapp}}?text=Quote%20for%20${{p.code}}" target="_blank" class="px-3 py-2 rounded-xl bg-emerald-600 text-white font-bold text-xs">💬 WhatsApp</a></div></div>`;}}).join('');}}
function filterCatalog(cat){{currentCatalogCategory=cat;document.querySelectorAll('.cat-pill').forEach(b=>{{b.className=b.getAttribute('data-cat')===cat?'cat-pill px-4 py-2.5 rounded-xl text-xs font-bold bg-cyan-500 text-black':'cat-pill px-4 py-2.5 rounded-xl text-xs font-bold bg-slate-900 text-slate-300 border border-white/10'}});renderCatalog();}}
function handleCatalogSearch(){{currentCatalogSearch=document.getElementById('catalog-search').value;renderCatalog();}}
function setCatalogViewMode(m){{currentCatalogViewMode=m;document.getElementById('view-mode-photo').className=m==='photo'?'px-3 py-1.5 rounded-lg bg-cyan-500 text-black font-bold':'px-3 py-1.5 rounded-lg bg-slate-900 text-slate-400 border border-white/10';document.getElementById('view-mode-blueprint').className=m==='blueprint'?'px-3 py-1.5 rounded-lg bg-cyan-500 text-black font-bold':'px-3 py-1.5 rounded-lg bg-slate-900 text-slate-400 border border-white/10';renderCatalog();}}
function handleContactSubmit(e){{e.preventDefault();const n=document.getElementById('form-name').value,ph=document.getElementById('form-phone').value,ci=document.getElementById('form-city').value,se=document.getElementById('form-service').value,no=document.getElementById('form-notes').value;const msg=`Namaste Annapurna,%0AName: ${{n}}%0APhone: ${{ph}}%0ALocation: ${{ci}}%0ARequirement: ${{se}}%0ADetails: ${{no}}`;window.open(`https://wa.me/${{SHOP.whatsapp}}?text=${{msg}}`,'_blank');}}
document.addEventListener('DOMContentLoaded',()=>{{renderRealProjects();renderCatalog();}});
</script>
</body>
</html>
"""

# Write files
(ROOT / "index.html").write_text(html, encoding="utf-8")
print(f"Generated index.html {len(html)} bytes {BUILD_VERSION} {BUILD_TIME}")

# Dist
if DIST_DIR.exists():
    shutil.rmtree(DIST_DIR)
DIST_DIR.mkdir()
shutil.copy(ROOT / "index.html", DIST_DIR / "index.html")
shutil.copytree(ASSETS, DIST_DIR / "catalog_assets")
(DIST_DIR / "catalog").mkdir()
shutil.copy(ROOT / "index.html", DIST_DIR / "catalog" / "catalog.html")

# Cloudflare files
wrangler_config = {
    "$schema": "node_modules/wrangler/config-schema.json",
    "name": "annpurnaalluiniumai",
    "compatibility_date": "2026-08-26",
    "compatibility_flags": ["assets_navigation_prefers_asset_serving"],
    "observability": {"enabled": True},
    "assets": {"directory": "./dist", "not_found_handling": "single-page-application"}
}
(ROOT / "wrangler.jsonc").write_text(json.dumps(wrangler_config, indent=2), encoding="utf-8")

# _headers with no-cache for html to force fresh deploys
headers = """/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Cache-Control: public, max-age=0, must-revalidate

/catalog_assets/*
  Cache-Control: public, max-age=31536000, immutable

/*.jpg
  Cache-Control: public, max-age=31536000, immutable
/*.png
  Cache-Control: public, max-age=31536000, immutable

/index.html
  Cache-Control: public, max-age=0, must-revalidate
"""
(ROOT / "_headers").write_text(headers, encoding="utf-8")
(DIST_DIR / "_headers").write_text(headers, encoding="utf-8")

(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SHOP['domain']}/sitemap.xml\n", encoding="utf-8")
(DIST_DIR / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SHOP['domain']}/sitemap.xml\n", encoding="utf-8")

sitemap = f"""<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{SHOP['domain']}/</loc><priority>1.0</priority></url><url><loc>{SHOP['domain']}/#projects</loc><priority>0.8</priority></url><url><loc>{SHOP['domain']}/#catalog</loc><priority>0.9</priority></url></urlset>"""
(ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
(DIST_DIR / "sitemap.xml").write_text(sitemap, encoding="utf-8")

print(f"Dist ready 236+ files, {BUILD_VERSION}")
print("Build complete - forces fresh upload due to timestamp")
