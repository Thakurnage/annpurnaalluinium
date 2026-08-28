#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Janakpur-area local SEO engine for Annapurna Aluminium & UPVC Udhyog.

Generates crawlable service + city landing pages, a full XML sitemap,
robots.txt, llms.txt, a web app manifest, and homepage injections so
Google can rank the workshop for Janakpur Dham / Dhanusha queries —
not only the single-page homepage.
"""

from __future__ import annotations

import json
from datetime import date
from html import escape
from pathlib import Path
from typing import Any

SITE = "https://annapurna-upvc-janakpur.com"
TODAY = date(2026, 8, 28).isoformat()
PHONE_DISPLAY = "+977 9817658719"
PHONE_E164 = "+9779817658719"
PHONE2_DISPLAY = "+977 9817667115"
WA = "9779817658719"
PAN = "616619779"
GEO_LAT = 26.7288
GEO_LNG = 85.9254
MAPS = "https://maps.google.com/?q=Murli+Chowk+Airport+Road+Janakpur+Dham+Nepal"
OG_DEFAULT = f"{SITE}/catalog_assets/real_projects/facade_commercial_plaza.jpg"
LOGO = f"{SITE}/catalog_assets/board_final.png"
FAV192 = f"{SITE}/catalog_assets/favicon-192.png"

NAP_EN = "Murli Chowk (Airport Road), Janakpur Dham-8, Dhanusha, Madhesh Province, Nepal"
NAP_NE = "मुरली चोक (एयरपोर्ट रोड), जनकपुरधाम-८, धनुषा, मधेश प्रदेश, नेपाल"

JANAKPUR_NEIGHBOURHOODS = [
    ("Murli Chowk / Airport Road", "Workshop & showroom — free walk-in measurement"),
    ("Janaki Mandir / Janak Chowk", "Heritage homes, hotels and temple-adjacent work"),
    ("Ramanand Chowk", "Residential UPVC windows and balcony railings"),
    ("Bhanu Chowk", "Shopfront glazing, ACP cladding and rolling shutters"),
    ("Pidari Chowk", "Aluminium partitions, office cabins and glass doors"),
    ("Zero Mile", "New-build villas — full window, door and kitchen packages"),
    ("Mills Area", "Commercial facades and steel compound gates"),
    ("Railway Station Road", "Hotel, lodge and rental-property upgrades"),
    ("Dehati / Nagarain side", "Farmhouse gates, grills and mosquito-mesh windows"),
    ("Mithila Bihari / Kamala", "Ward-level site visits across the municipality"),
]

NEARBY_TOWNS = [
    ("Dhalkebar", "Dhanusha", "East-West Highway junction — fast delivery"),
    ("Dhanushadham", "Dhanusha", "Temple gates, SS railings, residential UPVC"),
    ("Mahendranagar (Dhanusha)", "Dhanusha", "New housing colonies and shopfronts"),
    ("Shahidnagar", "Dhanusha", "Home windows, kitchen racks, balcony glass"),
    ("Chhireshwarnath", "Dhanusha", "Municipal buildings and private residences"),
    ("Jaleshwor", "Mahottari", "Free measurement for district HQ projects"),
    ("Gaushala", "Mahottari", "Highway commercial glazing and ACP"),
    ("Bardibas", "Mahottari / Sindhuli", "Hill-road villas and hotel facades"),
    ("Lahan", "Siraha", "UPVC, aluminium and steel packages"),
    ("Malangwa", "Sarlahi", "Shopfront, railing and kitchen fabrication"),
    ("Rajbiraj", "Saptari", "Scheduled installation crews"),
    ("Matihani", "Mahottari", "Village and bazaar steel + window work"),
]


def wa_url(msg: str) -> str:
    from urllib.parse import quote
    return f"https://wa.me/{WA}?text={quote(msg)}"


PAGES: list[dict[str, Any]] = [
    {
        "slug": "upvc-window-janakpur",
        "nav": "UPVC Windows",
        "title": "UPVC Window Janakpur Dham | Soundproof German Profile Windows & Doors",
        "h1": "UPVC Windows & Doors in Janakpur Dham",
        "description": (
            "Factory-direct UPVC windows in Janakpur Dham-8. German multi-chamber soundproof "
            "sliding, casement and tilt-turn windows with free site measurement at Murli Chowk "
            "(Airport Road). WhatsApp +977 9817658719."
        ),
        "keywords": (
            "UPVC window Janakpur, UPVC window Janakpur Dham, UPVC jhyal Janakpur, "
            "soundproof window Dhanusha, German UPVC Nepal, UPVC door Janakpur, "
            "यूपीभीसी झ्याल जनकपुरधाम, झ्याल ढोका जनकपुर"
        ),
        "og_image": f"{SITE}/catalog_assets/real_projects/villa_upvc_doors_windows.jpg",
        "hero_kicker": "German multi-chamber · monsoon sealed · Murli Chowk workshop",
        "service_name": "German-profile UPVC windows and doors",
        "related": ["aluminium-janakpur", "glass-railing-janakpur", "modular-kitchen-janakpur", "janakpur-dham"],
        "faq": [
            {
                "q": "What is the price of UPVC windows in Janakpur?",
                "a": "Factory-direct UPVC window rates in Janakpur typically start around NRs 450–850 per sq.ft depending on 2-track vs 3-track with mesh, German multi-chamber grade, and glass (float, reflective, or 5+9A+5 double glazing). We quote after a free laser measurement at your site in Janakpur Dham or nearby Dhanusha wards.",
            },
            {
                "q": "Do you install UPVC windows in every ward of Janakpur Dham?",
                "a": "Yes. Annapurna Aluminium & UPVC visits Murli Chowk, Airport Road, Ramanand Chowk, Bhanu Chowk, Pidari Chowk, Zero Mile, Mills Area, Janaki Mandir side and all 25 wards of Janakpur Sub-Metropolitan City for free measurement.",
            },
            {
                "q": "Is UPVC better than aluminium for Janakpur bedrooms?",
                "a": "For bedrooms facing the highway, bazaar or temple traffic, UPVC with double glazing is the better choice in Janakpur’s hot Terai climate — it cuts noise, blocks heat, and needs no yearly painting. Aluminium is better for slim shopfronts and large commercial spans.",
            },
        ],
        "body": """
<p>If you are searching for a <strong>UPVC window in Janakpur</strong>, you want a workshop that actually fabricates in Dhanusha — not a Kathmandu trader who ships frames and disappears. <strong>Annapurna Aluminium &amp; UPVC Udhyog</strong> manufactures German-profile multi-chamber uPVC windows and patio doors at <strong>Murli Chowk (Airport Road), Janakpur Dham-8</strong>, then fits them with monsoon-grade EPDM seals.</p>
<p>Janakpur summers regularly push past 38°C. Highway dust from the Airport Road, temple-procession noise around Janaki Mandir, and three months of Terai monsoon are hard on ordinary timber and slim aluminium sliders. A multi-chamber UPVC frame with galvanized steel inserts stays square, stays white, and keeps the room cooler without a second AC unit.</p>
<h2>UPVC window types we fabricate in Janakpur</h2>
<ul>
  <li><strong>2-track and 3-track sliding windows</strong> — the everyday choice for new houses from Zero Mile to Ramanand Chowk, with an optional SS mosquito-mesh track.</li>
  <li><strong>Casement and tilt-and-turn windows</strong> — airtight bedrooms and hotel rooms near Bhanu Chowk and the railway station.</li>
  <li><strong>French patio doors and woodgrain UPVC entry doors</strong> — villa courtyards that want a teak look without termites.</li>
  <li><strong>Arch, bay and corner UPVC units</strong> — custom geometry for heritage-style facades around Janak Chowk.</li>
</ul>
<h2>Why Janakpur homeowners choose factory-direct UPVC</h2>
<p>Every sash is miter-cut and steel-reinforced in our Murli Chowk workshop. You see the profile sample, the glass (5 mm float, royal-blue reflective, or 5+9A+5 insulated), and the multi-point lock before we cut. Typical residential orders across Janakpur Dham finish in <strong>3–5 working days</strong>, with on-site fitting and a written weather-seal check.</p>
<p>We also replace failed sliding windows in older houses in Mills Area and Pidari Chowk — same opening, better profile, no civil breaking if the rebate is sound.</p>
<h2>Free site visit in Dhanusha</h2>
<p>Message <a href="{wa}">WhatsApp {phone}</a> with your ward and a rough window count. Our engineer brings laser meters and physical UPVC corners to your plot in Janakpur, Dhalkebar, Dhanushadham or Jaleshwor. There is no measurement fee inside Madhesh Province for genuine building work.</p>
""".format(wa=wa_url("Namaste Annapurna, I want UPVC window measurement in Janakpur."), phone=PHONE_DISPLAY),
        "ne": """
<p lang="ne">जनकपुरधाममा <strong>यूपीभीसी झ्याल</strong> खोज्दै हुनुहुन्छ भने अन्नपूर्णा आल्मुनियम तथा यूपीभीसी उद्योग, मुरली चोक (एयरपोर्ट रोड), जनकपुरधाम-८ मा जर्मन मल्टि-च्याम्बर साउन्डप्रुफ झ्याल र ढोका कारखाना मूल्यमा बनाउँछ। गर्मी, धुलो र मनसुनमा काठको झ्याल बिग्रन्छ — यूपीभीसीमा रंग लगाउन पर्दैन, धमिरा लाग्दैन, र कोठा चिसो रहन्छ। निःशुल्क नाप जाँचका लागि ह्वाट्सएप <strong>+९७७ ९८१७६५८७१९</strong> मा म्यासेज गर्नुहोस्।</p>
""",
    },
    {
        "slug": "aluminium-janakpur",
        "nav": "Aluminium",
        "title": "Aluminium Door & Window Janakpur | Sliding, Partition & Powder-Coated Frames",
        "h1": "Aluminium Windows, Doors & Partitions in Janakpur",
        "description": (
            "Aluminium sliding windows, powder-coated doors and office partitions in Janakpur Dham. "
            "6063-T5 alloy, fabricated at Murli Chowk Airport Road. Free measurement. WhatsApp +977 9817658719."
        ),
        "keywords": (
            "aluminium door Janakpur, aluminium window Janakpur, aluminium partition Janakpur, "
            "sliding window Dhanusha, आल्मुनियम ढोका जनकपुर, aluminium shopfront Nepal"
        ),
        "og_image": f"{SITE}/catalog_assets/real_projects/window_aluminium_blue_slider.jpg",
        "hero_kicker": "6063-T5 alloy · powder coated · slim commercial frames",
        "service_name": "Aluminium windows, doors and office partitions",
        "related": ["upvc-window-janakpur", "acp-cladding-janakpur", "glass-railing-janakpur", "service-areas"],
        "faq": [
            {
                "q": "Where can I buy aluminium doors in Janakpur Dham?",
                "a": "Annapurna Aluminium & UPVC fabricates powder-coated 6063-T5 aluminium doors and sliding windows at Murli Chowk (Airport Road), Janakpur Dham-8. Walk in or WhatsApp +977 9817658719 for a same-week measurement.",
            },
            {
                "q": "Do you make aluminium office partitions in Janakpur?",
                "a": "Yes — grid glass partitions, half-wall cabins, blinds-in-glass and sliding stack panels for banks, clinics and chambers around Bhanu Chowk, Pidari Chowk and the commercial plazas of Janakpur.",
            },
        ],
        "body": """
<p><strong>Aluminium doors and windows in Janakpur</strong> are the backbone of shopfronts, hospitals, schools and slim modern houses. At Murli Chowk we extrude nothing ourselves — we fabricate <strong>virgin 6063-T5 architectural alloy</strong> with 60–80 micron powder coating that does not chalk in the Terai sun.</p>
<h2>What we build</h2>
<ul>
  <li>2-track and 3-track <strong>aluminium sliding windows</strong> with royal-blue or reflective glass for commercial complexes on Airport Road.</li>
  <li><strong>Casement, awning, louver and projected windows</strong> for kitchens and washrooms that need rain-safe ventilation.</li>
  <li><strong>Aluminium main doors, bi-folds and slim office doors</strong> — Eurobond ACP panels or 3D-etched glass, hydraulic floor springs, SS pull handles.</li>
  <li><strong>Office partitions</strong> — acoustic glass cabins for advocates, cooperatives and nursing homes in Janakpur Dham.</li>
</ul>
<h2>Aluminium vs UPVC in Dhanusha</h2>
<p>Choose aluminium when the opening is wide, the look must be slim, or the building is a shop, hotel lobby or hospital corridor. Choose UPVC when the room is a bedroom that needs silence and cooler indoor temperatures. Many Janakpur villas mix both: UPVC on the sleeping side, aluminium on the shop or verandah side. We design that split on one site visit.</p>
<p>Powder-coated white, bronze, woodgrain and custom RAL colours are finished before delivery so your facade on Bhanu Chowk or Mills Area matches the elevation drawing.</p>
""".format(),
        "ne": """
<p lang="ne">जनकपुरधाममा <strong>आल्मुनियम झ्याल, ढोका र पार्टिसन</strong> मुरली चोक वर्कसपमा ६०६३-टी५ अलॉय र पाउडर कोटिङमा बनाइन्छ। पसल, अस्पताल, स्कूल र स्लिम आधुनिक घरका लागि आल्मुनियम उत्तम हो। निःशुल्क नाप — ह्वाट्सएप +९७७ ९८१७६५८७१९।</p>
""",
    },
    {
        "slug": "glass-railing-janakpur",
        "nav": "Glass Railing",
        "title": "Glass Railing Janakpur | Toughened Balcony, Stair & Frameless Balustrade",
        "h1": "Toughened Glass Railings in Janakpur Dham",
        "description": (
            "Toughened glass balcony and staircase railings in Janakpur. 10–12 mm frameless spigot "
            "and SS-clamp balustrades, fitted by Annapurna Aluminium, Murli Chowk. WhatsApp +977 9817658719."
        ),
        "keywords": (
            "glass railing Janakpur, balcony glass railing Dhanusha, frameless glass railing Nepal, "
            "toughened glass Janakpur, ग्लास रेलिङ जनकपुर, stair glass railing Janakpur Dham"
        ),
        "og_image": f"{SITE}/catalog_assets/real_projects/facade_glass_tower.jpg",
        "hero_kicker": "10–12 mm toughened · frameless spigot · SS 304 clamps",
        "service_name": "Toughened glass railings and balustrades",
        "related": ["steel-gate-janakpur", "acp-cladding-janakpur", "aluminium-janakpur", "janakpur-dham"],
        "faq": [
            {
                "q": "How much does balcony glass railing cost in Janakpur?",
                "a": "Price depends on 10 mm vs 12 mm toughened glass, frameless spigot vs SS clamp, and handrail type. We quote per running foot after measuring your balcony or stair in Janakpur Dham. WhatsApp +977 9817658719 for a free site visit.",
            },
            {
                "q": "Is frameless glass railing safe for houses near Janaki Mandir?",
                "a": "Yes when we use certified 10–12 mm toughened glass, SS 304 spigots or clamps, and child-safe gaps. We install on duplex stairs, cantilever balconies and hotel corridors across Janakpur.",
            },
        ],
        "body": """
<p>A <strong>glass railing in Janakpur</strong> changes how a duplex or hotel feels — light through the stairwell, an open view from the Airport Road balcony, and no rust streaks on white marble. Annapurna fabricates <strong>10 mm and 12 mm toughened</strong> stair, balcony and terrace balustrades with SS 304 clamps, spigots or a slim top rail.</p>
<h2>Where we install in the city</h2>
<p>Recent work includes commercial glass towers on Airport Road, black-marble duplex stairs in private villas, and frameless balcony guards on new colonies toward Zero Mile and Dhalkebar road. We also do shower cubicles, shopfront glass and acid-etched partition walls for living rooms that want a Mithila-art or palm motif.</p>
<ul>
  <li>Staircase glass with SS handrail</li>
  <li>Frameless balcony spigot systems</li>
  <li>Shower enclosures and bathroom glass doors</li>
  <li>Mirror walls for gyms, salons and hotel lobbies</li>
  <li>Structural shopfront and canopy glass</li>
</ul>
<p>Every panel is toughened; edges are polished; fittings are marine-grade SS 304 so Janakpur’s monsoon and groundwater salts do not stain the clamp. Ask for a sample clamp and a glass offcut on the site visit.</p>
""",
        "ne": """
<p lang="ne">जनकपुरधाममा <strong>टफन्ड ग्लास रेलिङ</strong> — भर्याङ, बालकनी र टेरेसका लागि १०–१२ मिमी सेफ्टी ग्लास, एसएस ३०४ क्लाम्प वा स्पिगट। मनसुनमा खिया नलाग्ने फिटिङ। निःशुल्क नाप जाँच: +९७७ ९८१७६५८७१९।</p>
""",
    },
    {
        "slug": "steel-gate-janakpur",
        "nav": "SS & Steel",
        "title": "SS 304 Railing & Temple Gate Janakpur | Steel Main Gate Dhanusha",
        "h1": "SS 304 Railings, Temple Gates & Steel Work in Janakpur",
        "description": (
            "SS 304 temple gates, staircase railings and MS compound gates in Janakpur Dham. "
            "Mirror-polish TIG welding at Murli Chowk workshop. Free visit. WhatsApp +977 9817658719."
        ),
        "keywords": (
            "SS 304 railing Janakpur, temple gate Janakpur, steel gate Dhanusha, "
            "stainless steel railing Nepal, मन्दिर गेट जनकपुर, स्टील रेलिङ जनकपुरधाम"
        ),
        "og_image": f"{SITE}/catalog_assets/real_projects/gate_navdurga_mandir.jpg",
        "hero_kicker": "SS 304 marine grade · TIG welded · lifetime mirror polish",
        "service_name": "SS 304 railings, temple gates and MS steel fabrication",
        "related": ["glass-railing-janakpur", "acp-cladding-janakpur", "janakpur-dham", "service-areas"],
        "faq": [
            {
                "q": "Do you fabricate temple gates in Dhanusha?",
                "a": "Yes. We built the ceremonial SS 304 double gate for Sri Nav Durga Mandir Duhaba and take similar temple, math and dharamshala work across Dhanusha and Mahottari — sunburst motifs, Devanagari nameplates and heavy ball-bearing hinges.",
            },
            {
                "q": "What steel grade do you use for outdoor railings in Janakpur?",
                "a": "Genuine SS 304 with nickel content, argon TIG welding and diamond-compound mirror polish. We do not pass SS 202 as 304. Outdoor balcony and stair railings stay bright through the monsoon.",
            },
        ],
        "body": """
<p>Janakpur is a temple city. Gates and railings here are not only security — they are the first thing pilgrims and wedding guests see. <strong>Annapurna Aluminium &amp; UPVC</strong> fabricates <strong>SS 304 temple gates, staircase pillars, balcony guards and MS compound gates</strong> at Murli Chowk, then installs them from Duhaba to Dhanushadham.</p>
<h2>Steel work we are known for</h2>
<ul>
  <li><strong>Temple and math gates</strong> — arched SS double leaves, laser-cut jaali, religious sunburst, nameboard in Devanagari.</li>
  <li><strong>SS 304 stair and balcony railings</strong> — mirror pipe, crystal acrylic posts, wave and sunburst balusters.</li>
  <li><strong>MS sliding and swing compound gates</strong> for private houses on Airport Road and farm plots toward Nagarain.</li>
  <li>Window grills, security doors, pergolas, parking sheds and rooftop guard rails.</li>
</ul>
<p>Cheap SS 202 rusts at the weld within one Janakpur monsoon. We specify 304, show you a magnet test on request, and polish after TIG so the bead itself is a mirror. Hybrid gates (MS box frame + SS tubes) keep cost honest on long compound openings without looking rural.</p>
""",
        "ne": """
<p lang="ne">जनकपुरधाम र धनुषाका मन्दिर, घर र कम्पाउण्डका लागि <strong>एसएस ३०४ रेलिङ र मन्दिर गेट</strong> मुरली चोकमा टिग वेल्ड र मिरर पालिसमा बन्छ। श्री नव दुर्गा मन्दिर दुहबाको गेट हाम्रै काम हो। खिया नलाग्ने ग्यारेन्टी — ह्वाट्सएप +९७७ ९८१७६५८७१९।</p>
""",
    },
    {
        "slug": "modular-kitchen-janakpur",
        "nav": "Kitchen Racks",
        "title": "Modular Kitchen Janakpur | Waterproof Aluminium Kitchen Rack Dhanusha",
        "h1": "Waterproof Modular Kitchen Racks in Janakpur",
        "description": (
            "Termite-proof aluminium modular kitchen racks in Janakpur Dham. 100% waterproof ACP "
            "cabinets, made to measure at Murli Chowk. Free kitchen visit. WhatsApp +977 9817658719."
        ),
        "keywords": (
            "modular kitchen Janakpur, kitchen rack Janakpur, aluminium kitchen Nepal, "
            "waterproof kitchen Dhanusha, किचन र्याक जनकपुर, मोड्युलर किचन जनकपुरधाम"
        ),
        "og_image": f"{SITE}/catalog_assets/real_projects/kitchen_modular_lshape.jpg",
        "hero_kicker": "100% waterproof · termite proof · ACP + aluminium",
        "service_name": "Waterproof aluminium modular kitchen racks",
        "related": ["aluminium-janakpur", "upvc-window-janakpur", "janakpur-dham", "faq-janakpur"],
        "faq": [
            {
                "q": "Are aluminium kitchen racks good for Janakpur humidity?",
                "a": "Yes. Terai kitchens stay humid through monsoon and Chhath cooking. Plywood swells and termites eat the carcass. Our racks use anodized aluminium frames and waterproof ACP panels that you can wash with a pipe.",
            },
            {
                "q": "Do you make L-shaped modular kitchens in Janakpur?",
                "a": "Yes — L-shape, straight and pantry racks, glass crockery units and under-counter drawers, all made to the actual wall after a free kitchen measurement in Janakpur Dham.",
            },
        ],
        "body": """
<p>A <strong>modular kitchen in Janakpur</strong> fails for one reason: wood. Groundwater moisture, monsoon steam and festival cooking destroy MDF in two seasons. We build <strong>aluminium-frame, ACP-panel kitchen racks</strong> that are waterproof, termite-proof and fire-retardant — then fit telescopic drawers and toughened-glass crockery shutters.</p>
<h2>What a typical Janakpur kitchen order includes</h2>
<ul>
  <li>L-shaped or straight lower cabinets with SS handles</li>
  <li>Wall racks and glass-front crockery showcases</li>
  <li>Under-sink waterproof carcass (the first place plywood dies)</li>
  <li>Optional SS countertop support and chimney cut-outs</li>
</ul>
<p>We measure the actual plinth, column offsets and gas-pipe run in your kitchen — Ramanand Chowk flats, Zero Mile villas, hotel pantries near the station. Colour is your choice: high-gloss red, woodgrain, white or dual-tone. Lead time is usually under a week for a standard 8–12 foot run.</p>
""",
        "ne": """
<p lang="ne">जनकपुरधामको गर्मी र मनसुनमा काठको किचन र्याक बिग्रन्छ। हाम्रो <strong>आल्मुनियम मोड्युलर किचन र्याक</strong> १००% वाटरप्रुफ र धमिरा-मुक्त छ। एल-आकार, सिधा र क्रोकरी युनिट — घरको नापमा। ह्वाट्सएप +९७७ ९८१७६५८७१९।</p>
""",
    },
    {
        "slug": "acp-cladding-janakpur",
        "nav": "ACP & Shopfront",
        "title": "ACP Cladding & Shopfront Glazing Janakpur | Commercial Facade Dhanusha",
        "h1": "ACP Cladding & Shopfront Glazing in Janakpur",
        "description": (
            "ACP facade cladding, curtain-wall glazing and shopfront glass in Janakpur Dham. "
            "Commercial plazas, hotels and showrooms. Murli Chowk workshop. WhatsApp +977 9817658719."
        ),
        "keywords": (
            "ACP cladding Janakpur, shopfront glazing Janakpur, curtain wall Dhanusha, "
            "glass facade Nepal, एसीपी क्ल्याडिङ जनकपुर, शोरुम ग्लास जनकपुरधाम"
        ),
        "og_image": f"{SITE}/catalog_assets/real_projects/facade_commercial_plaza.jpg",
        "hero_kicker": "ACP · curtain wall · structural silicone glazing",
        "service_name": "ACP cladding, curtain walls and shopfront glazing",
        "related": ["aluminium-janakpur", "glass-railing-janakpur", "steel-gate-janakpur", "service-areas"],
        "faq": [
            {
                "q": "Who does ACP cladding in Janakpur Dham?",
                "a": "Annapurna Aluminium & UPVC fabricates ACP (aluminium composite panel) facades and structural glass shopfronts at Murli Chowk, including 4-storey commercial plazas with solar-control glass and fire-retardant ACP.",
            },
            {
                "q": "Can you glaze a shop on Bhanu Chowk without closing for a week?",
                "a": "Yes. We prefabricate frames at the workshop and schedule night or early-morning fitting so bazaar shops lose minimum trading hours.",
            },
        ],
        "body": """
<p>Janakpur’s new commercial streets — Airport Road, Bhanu Chowk, Mills Area — are replacing painted brick with <strong>ACP cladding and glass shopfronts</strong>. We design, fabricate and hang fire-retardant ACP, curtain-wall grids and 12 mm toughened storefront glass from our Murli Chowk factory.</p>
<h2>Commercial packages</h2>
<ul>
  <li>4-storey plaza facades with solar-control glass and colour ACP bands</li>
  <li>Triple-arch and bronze-profile showrooms</li>
  <li>Hotel entrance glazing with glass canopy</li>
  <li>Column cladding, louvers and sunshades for west-facing walls (critical in Terai sun)</li>
  <li>Rolling shutters coordinated with the same shopfront</li>
</ul>
<p>Structural silicone, EPDM and a drainage plane behind ACP are what stop monsoon leaks. We do not glue panels onto damp plaster and hope. Ask to see a completed plaza elevation before you sign — we will walk you to a live site in Janakpur.</p>
""",
        "ne": """
<p lang="ne">जनकपुरधामका प्लाजा, होटेल र पसलका लागि <strong>एसीपी क्ल्याडिङ, पर्दा पर्खाल र शोरुम ग्लास</strong> मुरली चोकमा तयार हुन्छ। मनसुनमा नचुहिने सिल र फायर-रिटारडेन्ट एसीपी। सम्पर्क +९७७ ९८१७६५८७१९।</p>
""",
    },
    {
        "slug": "janakpur-dham",
        "nav": "Janakpur Dham",
        "title": "Annapurna Aluminium Janakpur Dham | UPVC, Glass & Steel Workshop Murli Chowk",
        "h1": "Annapurna Aluminium & UPVC — Janakpur Dham Workshop",
        "description": (
            "Official Janakpur Dham workshop of Annapurna Aluminium & UPVC at Murli Chowk, Airport Road, "
            "Ward 8. UPVC windows, aluminium doors, glass railing, SS gates, kitchen racks. Open 7 days. "
            "WhatsApp +977 9817658719."
        ),
        "keywords": (
            "Annapurna Aluminium Janakpur, UPVC Janakpur Dham, Murli Chowk aluminium, "
            "झ्याल ढोका जनकपुरधाम, Airport Road workshop Dhanusha, glass shop Janakpur"
        ),
        "og_image": f"{SITE}/catalog_assets/board_final.png",
        "hero_kicker": "Murli Chowk · Airport Road · Ward 8 · open 9 AM – 7 PM",
        "service_name": "Architectural fabrication workshop in Janakpur Dham",
        "related": ["upvc-window-janakpur", "aluminium-janakpur", "steel-gate-janakpur", "service-areas"],
        "faq": [
            {
                "q": "Where is Annapurna Aluminium workshop in Janakpur?",
                "a": "Murli Chowk (Airport Road), Janakpur Dham-8, Dhanusha, Madhesh Province, Nepal. Open all 7 days, 9:00 AM to 7:00 PM. WhatsApp +977 9817658719. Look for the red-and-blue Annapurna Aluminium & UPVC board.",
            },
            {
                "q": "Which areas of Janakpur Dham do you cover the same day?",
                "a": "Same-day or next-morning measurement for Murli Chowk, Airport Road, Janaki Mandir / Janak Chowk, Ramanand Chowk, Bhanu Chowk, Pidari Chowk, Zero Mile, Mills Area, railway station road and adjoining wards of the sub-metropolitan city.",
            },
        ],
        "body": """
<p><strong>Annapurna Aluminium &amp; UPVC Udhyog</strong> is a Janakpur Dham workshop — not a Facebook page that outsources to Birgunj. Founder <strong>Prof. Nageshwar Thakur</strong> runs fabrication at <strong>Murli Chowk on the Airport Road, Ward No. 8</strong>. If you live in the city, you can stand in the workshop, touch the UPVC corner sample, see an SS 304 weld, and book fitting for this week.</p>
<h2>How to reach the workshop</h2>
<p>From Janaki Mandir, follow the Airport Road toward Murli Chowk. The shop board reads aluminium and UPVC windows, doors, partitions, kitchen racks and steel railings — in Nepali, the line every local already knows: <em>यहाँ आल्मुनियम र UPVC को झ्याल, ढोका, पार्टिसन, किचन रैक तथा स्टील रेलिङको काम गरिन्छ।</em></p>
<p>Open <strong>Sunday to Saturday, 9:00 AM – 7:00 PM</strong>. Parking is on the Airport Road. WhatsApp before you come if you want the engineer on site instead of at the shop.</p>
<h2>Neighbourhoods we measure every week</h2>
<p>Janakpur is not one market. A hotel glass door near the mandir, a soundproof bedroom on Ramanand Chowk, a plaza facade on Mills Area and a farmhouse gate toward Nagarain are four different jobs. We keep crews for all four.</p>
""",
        "ne": """
<p lang="ne"><strong>अन्नपूर्णा आल्मुनियम तथा यूपीभीसी उद्योग</strong> जनकपुरधाम-८, मुरली चोक (एयरपोर्ट रोड) मा छ। हप्ताको सातै दिन बिहान ९ बजेदेखि साँझ ७ बजेसम्म खुला। संस्थापक प्रो. नागेश्वर ठाकुर। झ्याल, ढोका, ग्लास रेलिङ, मन्दिर गेट र किचन र्याक — एउटै वर्कसप। ह्वाट्सएप +९७७ ९८१७६५८७१९।</p>
""",
    },
    {
        "slug": "service-areas",
        "nav": "Service Areas",
        "title": "UPVC & Aluminium Service Areas | Dhanusha, Jaleshwor, Lahan, Bardibas",
        "h1": "Service Areas — Dhanusha, Mahottari, Siraha & Madhesh",
        "description": (
            "Free site visit for UPVC windows, aluminium doors, glass railing and steel gates across "
            "Janakpur, Dhalkebar, Jaleshwor, Lahan, Bardibas, Malangwa and Madhesh Province. "
            "WhatsApp +977 9817658719."
        ),
        "keywords": (
            "UPVC window Dhanusha, aluminium Jaleshwor, glass railing Lahan, steel gate Bardibas, "
            "UPVC Malangwa, fabrication Madhesh Province, झ्याल ढोका धनुषा"
        ),
        "og_image": f"{SITE}/catalog_assets/hero_facade.jpg",
        "hero_kicker": "Free measurement across Madhesh · Nepal-wide installation",
        "service_name": "Site measurement and installation across Madhesh Province",
        "related": ["janakpur-dham", "upvc-window-janakpur", "aluminium-janakpur", "faq-janakpur"],
        "faq": [
            {
                "q": "Do you visit Jaleshwor, Lahan and Bardibas for free?",
                "a": "Yes. Free laser measurement for genuine building work in Mahottari (Jaleshwor, Gaushala, Bardibas), Siraha (Lahan), Sarlahi (Malangwa), Dhanusha (Dhalkebar, Dhanushadham) and adjoining districts. Installation crews are scheduled after the quote.",
            },
            {
                "q": "Can you deliver to Kathmandu or Birgunj?",
                "a": "Yes. Frames are factory-finished in Janakpur and dispatched Nepal-wide. Large curtain walls and temple gates travel with our own fitting team.",
            },
        ],
        "body": """
<p>The workshop is in Janakpur Dham, but the work is <strong>Madhesh-wide</strong>. If you are building on the East-West Highway — Dhalkebar, Bardibas, Lahan — you do not need to hire a Kathmandu fabricator. We measure, fabricate in Murli Chowk, and install with the same crew that works inside the city.</p>
<h2>District coverage</h2>
<ul>
  <li><strong>Dhanusha</strong> — Janakpur Dham, Dhalkebar, Dhanushadham, Mahendranagar, Shahidnagar, Chhireshwarnath, Kamala, Mithila, Nagarain, Bateshwar, Hansapur.</li>
  <li><strong>Mahottari</strong> — Jaleshwor, Gaushala, Bardibas, Matihani, Aurahi.</li>
  <li><strong>Siraha</strong> — Lahan and adjoining bazaars.</li>
  <li><strong>Sarlahi</strong> — Malangwa.</li>
  <li><strong>Saptari / further</strong> — Rajbiraj on scheduled runs; Birgunj, Hetauda and Kathmandu by dispatch.</li>
</ul>
<p>Highway projects get a morning measurement slot so the engineer is back at the workshop to cut the same afternoon. WhatsApp your landmark (for example “Dhalkebar chowk, 200 m south”) and a photo of the opening.</p>
""",
        "ne": """
<p lang="ne">धनुषा, महोत्तरी (जलेश्वर, बर्दीबास), सिरहा (लहान), सर्लाही (मलङ्गवा) र मधेशभर <strong>निःशुल्क साइट नाप</strong>। बनाउने काम जनकपुरधाम मुरली चोकमै, फिटिङ तपाईंको साइटमा। ह्वाट्सएप +९७७ ९८१७६५८७१९।</p>
""",
    },
    {
        "slug": "faq-janakpur",
        "nav": "FAQ",
        "title": "FAQ | UPVC Window Price Janakpur, Free Site Visit, Aluminium vs UPVC",
        "h1": "Janakpur Fabrication FAQ — Prices, Visits & Materials",
        "description": (
            "Answers for Janakpur Dham: UPVC window price, aluminium vs UPVC, free site visit in "
            "Dhanusha, SS 304 vs 202, kitchen rack termites, and installation time. WhatsApp +977 9817658719."
        ),
        "keywords": (
            "UPVC window price Janakpur, aluminium vs UPVC Nepal, free site visit Dhanusha, "
            "SS 304 vs 202, kitchen rack termite, झ्यालको भाउ जनकपुर"
        ),
        "og_image": f"{SITE}/uploads/owner_professional.jpg",
        "hero_kicker": "Straight answers from the Murli Chowk workshop",
        "service_name": "Architectural fabrication consultation in Janakpur",
        "related": ["upvc-window-janakpur", "aluminium-janakpur", "janakpur-dham", "service-areas"],
        "faq": [
            {
                "q": "How do I get an exact quote in Janakpur Dham?",
                "a": "WhatsApp +977 9817658719 with your ward, a photo of the opening, and a rough count. Inside Dhanusha we visit free with a laser meter and profile samples. You receive a line-item quote (profile, glass, mesh, fitting) before we cut.",
            },
            {
                "q": "How long does manufacturing take?",
                "a": "Standard residential windows and doors: 3–5 business days after measurement. Temple gates, curtain walls and full kitchens follow the site programme.",
            },
            {
                "q": "Which is cheaper in Janakpur — UPVC or aluminium?",
                "a": "Entry aluminium sliders can be cheaper per sq.ft; German multi-chamber UPVC with double glazing costs more and returns the difference in heat and noise. We show both samples on the same visit so you decide by room, not by rumour.",
            },
            {
                "q": "Do you work during Chhath and wedding season?",
                "a": "The workshop stays open 7 days. We book extra fitting slots before Chhath and the winter wedding months because Janakpur hotels and homes renovate then. Message early.",
            },
        ],
        "body": """
<p>These are the questions we hear every week at Murli Chowk. If your question is not here, WhatsApp the founder — you will not get a bot.</p>
<h2>Materials we will not fake</h2>
<p>UPVC wall thickness, aluminium alloy grade (6063-T5), glass toughening stamp, and SS 304 nickel content are written on the quote. If another shop in Janakpur is dramatically cheaper, ask them to write the same four lines. That is usually where the gap is.</p>
<p>PAN of the firm is <strong>{pan}</strong>. Hours: 9:00 AM – 7:00 PM, all seven days. Second line: {phone2}.</p>
""".format(pan=PAN, phone2=PHONE2_DISPLAY),
        "ne": """
<p lang="ne">जनकपुरधाममा झ्यालको भाउ, निःशुल्क नाप, यूपीभीसी कि आल्मुनियम, र एसएस ३०४ को सत्य जवाफ यस पेजमा छ। थप प्रश्न भए ह्वाट्सएप +९७७ ९८१७६५८७१९।</p>
""",
    },
]


def _page_by_slug(slug: str) -> dict[str, Any]:
    for p in PAGES:
        if p["slug"] == slug:
            return p
    raise KeyError(slug)


def _ld(obj: dict) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=2)


def _schema_business() -> dict:
    return {
        "@context": "https://schema.org",
        "@type": ["HomeAndConstructionBusiness", "LocalBusiness"],
        "@id": f"{SITE}/#business",
        "name": "Annapurna Aluminium & UPVC Udhyog",
        "alternateName": [
            "Annapurna Aluminium Janakpur",
            "Annapurna UPVC Janakpur",
            "अन्नपूर्णा आल्मुनियम जनकपुरधाम",
        ],
        "url": f"{SITE}/",
        "logo": LOGO,
        "image": [
            OG_DEFAULT,
            f"{SITE}/catalog_assets/real_projects/gate_navdurga_mandir.jpg",
            f"{SITE}/catalog_assets/board_final.png",
        ],
        "telephone": [PHONE_E164, "+9779817667115"],
        "priceRange": "$$",
        "currenciesAccepted": "NPR",
        "paymentAccepted": "Cash, eSewa, Khalti, Bank Transfer",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Murli Chowk (Airport Road), Janakpur Dham-8",
            "addressLocality": "Janakpur Dham",
            "addressRegion": "Dhanusha",
            "postalCode": "45600",
            "addressCountry": "NP",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": GEO_LAT, "longitude": GEO_LNG},
        "hasMap": MAPS,
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": [
                "Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday",
            ],
            "opens": "09:00",
            "closes": "19:00",
        },
        "founder": {
            "@type": "Person",
            "name": "Prof. Nageshwar Thakur",
            "jobTitle": "Founder & Master Architectural Fabricator",
        },
        "identifier": {"@type": "PropertyValue", "name": "PAN", "value": PAN},
        "knowsLanguage": ["ne", "en", "mai"],
        "areaServed": [
            {"@type": "City", "name": "Janakpur Dham"},
            {"@type": "AdministrativeArea", "name": "Dhanusha"},
            {"@type": "AdministrativeArea", "name": "Madhesh Province"},
            {"@type": "Country", "name": "Nepal"},
        ],
        "contactPoint": {
            "@type": "ContactPoint",
            "telephone": PHONE_E164,
            "contactType": "sales",
            "availableLanguage": ["Nepali", "English", "Maithili"],
            "areaServed": "NP",
        },
    }


def render_page(page: dict[str, Any]) -> str:
    url = f"{SITE}/{page['slug']}/"
    crumbs = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": page["h1"], "item": url},
        ],
    }
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": f["q"],
                "acceptedAnswer": {"@type": "Answer", "text": f["a"]},
            }
            for f in page["faq"]
        ],
    }
    service_schema = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": page["service_name"],
        "provider": {"@id": f"{SITE}/#business"},
        "areaServed": [
            {"@type": "City", "name": "Janakpur Dham"},
            {"@type": "AdministrativeArea", "name": "Dhanusha"},
        ],
        "url": url,
        "image": page["og_image"],
    }

    nav_links = "".join(
        f'<a href="/{p["slug"]}/" class="{"text-emerald-300" if p["slug"]==page["slug"] else "text-slate-300 hover:text-white"}">{escape(p["nav"])}</a>'
        for p in PAGES
    )
    related = "".join(
        f'<a class="block rounded-xl border border-white/10 bg-slate-900/70 px-4 py-3 text-sm font-semibold text-emerald-300 hover:border-emerald-400/50" href="/{_page_by_slug(s)["slug"]}/">{escape(_page_by_slug(s)["h1"])}</a>'
        for s in page["related"]
    )
    faq_html = "".join(
        f"""<details class="rounded-2xl border border-white/10 bg-slate-900/60 p-4">
          <summary class="cursor-pointer font-bold text-white">{escape(f["q"])}</summary>
          <p class="mt-3 text-sm leading-relaxed text-slate-300">{escape(f["a"])}</p>
        </details>"""
        for f in page["faq"]
    )
    if page["slug"] == "janakpur-dham":
        extra = "<h2>Janakpur neighbourhoods we serve</h2><ul>" + "".join(
            f"<li><strong>{escape(n)}</strong> — {escape(d)}</li>" for n, d in JANAKPUR_NEIGHBOURHOODS
        ) + "</ul>"
    elif page["slug"] == "service-areas":
        extra = "<h2>Town-by-town</h2><ul>" + "".join(
            f"<li><strong>{escape(t)}</strong> ({escape(d)}) — {escape(n)}</li>" for t, d, n in NEARBY_TOWNS
        ) + "</ul>"
    else:
        extra = ""

    wa = wa_url(f"Namaste Annapurna, I am enquiring from the {page['nav']} Janakpur page.")
    title = escape(page["title"])
    desc = escape(page["description"])
    h1 = escape(page["h1"])
    kicker = escape(page["hero_kicker"])
    keywords = escape(page["keywords"])
    og = escape(page["og_image"])

    return f"""<!DOCTYPE html>
<html lang="en-NP">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
<meta name="author" content="Annapurna Aluminium &amp; UPVC Udhyog — Janakpur Dham">
<meta name="geo.region" content="NP-P2">
<meta name="geo.placename" content="Janakpur Dham, Dhanusha, Nepal">
<meta name="geo.position" content="{GEO_LAT};{GEO_LNG}">
<meta name="ICBM" content="{GEO_LAT}, {GEO_LNG}">
<meta name="theme-color" content="#030712">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{url}">
<link rel="alternate" hreflang="ne" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="192x192" href="/catalog_assets/favicon-192.png">
<link rel="apple-touch-icon" href="/catalog_assets/apple-touch-icon.png">
<link rel="manifest" href="/manifest.webmanifest">
<link rel="sitemap" type="application/xml" href="/sitemap.xml">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Annapurna Aluminium &amp; UPVC Udhyog">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:image:alt" content="{h1}">
<meta property="og:locale" content="en_NP">
<meta property="og:locale:alternate" content="ne_NP">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{og}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Noto+Sans+Devanagari:wght@400;600;700&display=swap" rel="stylesheet">
<script src="https://cdn.tailwindcss.com"></script>
<style>
  body {{ background:#030712; color:#e2e8f0; font-family:"Plus Jakarta Sans","Noto Sans Devanagari",system-ui,sans-serif; }}
  h1,h2,h3 {{ font-family:Outfit,"Noto Sans Devanagari",sans-serif; }}
  article h2 {{ font-size:1.35rem; font-weight:800; color:#fff; margin:1.6rem 0 .7rem; }}
  article p, article li {{ font-size:.95rem; line-height:1.75; color:#cbd5e1; }}
  article ul {{ margin:.4rem 0 1rem 1.1rem; list-style:disc; }}
  article a {{ color:#34d399; text-decoration:underline; }}
</style>
<script type="application/ld+json">{_ld(_schema_business())}</script>
<script type="application/ld+json">{_ld(crumbs)}</script>
<script type="application/ld+json">{_ld(faq_schema)}</script>
<script type="application/ld+json">{_ld(service_schema)}</script>
</head>
<body>
  <div class="h-1 bg-gradient-to-r from-emerald-500 via-cyan-400 to-amber-400"></div>
  <header class="border-b border-white/10 bg-slate-950/90">
    <div class="mx-auto flex max-w-5xl flex-wrap items-center justify-between gap-3 px-4 py-3">
      <a href="/" class="font-extrabold tracking-tight text-amber-300">ANNAPURNA <span class="text-emerald-400">Aluminium &amp; UPVC</span></a>
      <a href="{wa}" class="rounded-xl bg-emerald-600 px-3 py-2 text-xs font-bold text-white">WhatsApp {PHONE_DISPLAY}</a>
    </div>
    <nav class="mx-auto flex max-w-5xl gap-4 overflow-x-auto px-4 pb-3 text-[11px] font-bold uppercase tracking-wide" aria-label="Service pages">
      <a href="/" class="text-slate-400 hover:text-white">Home</a>
      {nav_links}
    </nav>
  </header>
  <main class="mx-auto max-w-5xl px-4 py-10">
    <nav class="mb-6 text-xs text-slate-500" aria-label="Breadcrumb">
      <a href="/" class="hover:text-emerald-400">Home</a>
      <span class="mx-2">/</span>
      <span class="text-slate-300">{h1}</span>
    </nav>
    <p class="mb-3 text-[11px] font-extrabold uppercase tracking-[0.18em] text-emerald-400">{kicker}</p>
    <h1 class="mb-4 text-3xl font-black text-white sm:text-5xl">{h1}</h1>
    <p class="mb-8 text-sm text-slate-400">{escape(NAP_EN)} · Open 7 days · <a class="text-emerald-400" href="{MAPS}" rel="noopener" target="_blank">Google Maps</a></p>
    <div class="overflow-hidden rounded-3xl border border-white/10">
      <img src="{og.replace(SITE, "")}" alt="{h1} — Annapurna Aluminium Janakpur Dham" class="h-64 w-full object-cover sm:h-80" width="1200" height="630">
    </div>
    <article class="mt-10 max-w-3xl">
      {page["body"]}
      {extra}
      <div lang="ne" class="mt-8 rounded-2xl border border-amber-400/20 bg-amber-500/5 p-5">
        <h2 class="!mt-0">नेपालीमा</h2>
        {page["ne"]}
      </div>
    </article>
    <section class="mt-12">
      <h2 class="mb-4 text-2xl font-extrabold text-white">Questions from Janakpur clients</h2>
      <div class="space-y-3">{faq_html}</div>
    </section>
    <section class="mt-12">
      <h2 class="mb-4 text-2xl font-extrabold text-white">Related in Janakpur Dham</h2>
      <div class="grid gap-3 sm:grid-cols-2">{related}</div>
    </section>
    <section class="mt-12 rounded-3xl border border-emerald-400/30 bg-emerald-500/10 p-6 sm:p-8">
      <h2 class="text-2xl font-black text-white">Book a free measurement in Janakpur</h2>
      <p class="mt-2 max-w-2xl text-sm text-slate-300">Laser visit with real UPVC, aluminium and glass samples. Reply on WhatsApp within 15 minutes during workshop hours.</p>
      <div class="mt-5 flex flex-wrap gap-3">
        <a class="rounded-2xl bg-emerald-600 px-5 py-3 text-sm font-extrabold text-white" href="{wa}">WhatsApp {PHONE_DISPLAY}</a>
        <a class="rounded-2xl border border-white/15 px-5 py-3 text-sm font-bold text-white" href="tel:{PHONE_E164}">Call now</a>
        <a class="rounded-2xl border border-white/15 px-5 py-3 text-sm font-bold text-white" href="/#booking">Booking form</a>
      </div>
    </section>
  </main>
  <footer class="border-t border-white/10 px-4 py-10 text-xs text-slate-500">
    <div class="mx-auto max-w-5xl space-y-2">
      <p class="font-bold text-slate-300">Annapurna Aluminium &amp; UPVC Udhyog</p>
      <p>{escape(NAP_EN)}</p>
      <p lang="ne">{escape(NAP_NE)}</p>
      <p>WhatsApp / Call {PHONE_DISPLAY} · {PHONE2_DISPLAY} · PAN {PAN}</p>
      <p class="pt-3"><a class="text-emerald-400" href="/">Home</a> · <a class="text-emerald-400" href="/sitemap.xml">Sitemap</a></p>
    </div>
  </footer>
</body>
</html>
"""


HOMEPAGE_TITLE = (
    "UPVC Window Janakpur | Aluminium Door, Glass Railing &amp; Kitchen Rack | Annapurna"
)
HOMEPAGE_DESC = (
    "Annapurna Aluminium &amp; UPVC — Murli Chowk (Airport Road), Janakpur Dham-8, Dhanusha. "
    "Factory-direct UPVC windows, aluminium doors, glass railing, SS 304 temple gates and modular "
    "kitchen racks. Free site visit across Janakpur, Dhalkebar, Jaleshwor and Madhesh. WhatsApp +977 9817658719."
)
HOMEPAGE_KEYWORDS = (
    "UPVC window Janakpur, UPVC window Janakpur Dham, aluminium door Janakpur, "
    "glass railing Janakpur, SS 304 railing Janakpur, modular kitchen Janakpur, "
    "ACP cladding Janakpur, temple gate Dhanusha, Murli Chowk Airport Road, "
    "झ्याल ढोका जनकपुरधाम, यूपीभीसी झ्याल जनकपुर, आल्मुनियम ढोका धनुषा, "
    "किचन र्याक जनकपुर, Annapurna Aluminium, 9817658719"
)

LOCAL_SECTION = r'''
<!-- SECTION: JANAKPUR LOCAL SEO HUB (crawlable, not JS) -->
<section id="janakpur-areas" class="py-16 px-4 relative z-10 border-t border-white/5 bg-slate-950/70">
  <div class="max-w-7xl mx-auto">
    <div class="text-center mb-10">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-400 text-xs font-bold uppercase tracking-wider mb-3">📍 Janakpur Dham · Dhanusha · Madhesh</div>
      <h2 class="text-2xl sm:text-4xl font-extrabold font-display text-white mb-3">UPVC, Aluminium &amp; Steel Fabrication for Janakpur Area</h2>
      <p class="text-xs sm:text-sm text-slate-300 max-w-3xl mx-auto leading-relaxed">Annapurna Aluminium &amp; UPVC Udhyog manufactures at Murli Chowk (Airport Road), Janakpur Dham-8 — not a trading desk. Free laser measurement across the sub-metropolitan city and neighbouring Madhesh towns, then factory-finished fitting by the same crew.</p>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mb-10">
      <a href="/upvc-window-janakpur/" class="glass-card rounded-2xl p-5 block hover:border-emerald-400/50">
        <h3 class="font-bold text-white text-base mb-1">UPVC Windows Janakpur</h3>
        <p class="text-xs text-slate-400 leading-relaxed">German multi-chamber soundproof sliding, casement and tilt-turn windows for Terai heat, dust and monsoon. Factory-direct from Murli Chowk.</p>
      </a>
      <a href="/aluminium-janakpur/" class="glass-card rounded-2xl p-5 block hover:border-emerald-400/50">
        <h3 class="font-bold text-white text-base mb-1">Aluminium Doors &amp; Partitions</h3>
        <p class="text-xs text-slate-400 leading-relaxed">6063-T5 powder-coated sliders, shop doors and office glass cabins for Bhanu Chowk, Pidari Chowk and Airport Road plazas.</p>
      </a>
      <a href="/glass-railing-janakpur/" class="glass-card rounded-2xl p-5 block hover:border-emerald-400/50">
        <h3 class="font-bold text-white text-base mb-1">Glass Railing Janakpur</h3>
        <p class="text-xs text-slate-400 leading-relaxed">10–12 mm toughened balcony, stair and frameless spigot balustrades with SS 304 clamps.</p>
      </a>
      <a href="/steel-gate-janakpur/" class="glass-card rounded-2xl p-5 block hover:border-emerald-400/50">
        <h3 class="font-bold text-white text-base mb-1">SS 304 Gates &amp; Railings</h3>
        <p class="text-xs text-slate-400 leading-relaxed">Temple gates, compound gates and mirror-polish stair railings — including Sri Nav Durga Mandir Duhaba.</p>
      </a>
      <a href="/modular-kitchen-janakpur/" class="glass-card rounded-2xl p-5 block hover:border-emerald-400/50">
        <h3 class="font-bold text-white text-base mb-1">Modular Kitchen Racks</h3>
        <p class="text-xs text-slate-400 leading-relaxed">Termite-proof, 100% waterproof aluminium + ACP kitchens sized to Janakpur homes and hotel pantries.</p>
      </a>
      <a href="/acp-cladding-janakpur/" class="glass-card rounded-2xl p-5 block hover:border-emerald-400/50">
        <h3 class="font-bold text-white text-base mb-1">ACP &amp; Shopfront Glazing</h3>
        <p class="text-xs text-slate-400 leading-relaxed">Commercial plaza facades, curtain walls and bazaar shopfronts prefabricated for fast fitting.</p>
      </a>
    </div>
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <div class="glass-card rounded-2xl p-6">
        <h3 class="font-bold text-white text-lg mb-3">Janakpur Dham neighbourhoods</h3>
        <ul class="text-xs text-slate-300 space-y-1.5 leading-relaxed">
          <li><a class="text-emerald-400 hover:underline" href="/janakpur-dham/">Murli Chowk / Airport Road</a> — workshop, walk-in samples</li>
          <li>Janaki Mandir / Janak Chowk — hotels, heritage homes, temple-side steel</li>
          <li>Ramanand Chowk · Bhanu Chowk · Pidari Chowk — windows, railings, shopfronts</li>
          <li>Zero Mile · Mills Area · Railway Station Road — villas, plazas, lodges</li>
          <li>Dehati / Nagarain side — farmhouse gates and mesh windows</li>
        </ul>
        <a href="/janakpur-dham/" class="inline-block mt-4 text-xs font-bold text-amber-300 hover:underline">Full Janakpur Dham page →</a>
      </div>
      <div class="glass-card rounded-2xl p-6">
        <h3 class="font-bold text-white text-lg mb-3">Nearby towns (free measurement)</h3>
        <p class="text-xs text-slate-300 leading-relaxed mb-3">Dhalkebar, Dhanushadham, Mahendranagar, Jaleshwor, Gaushala, Bardibas, Lahan, Malangwa, Rajbiraj and Matihani — WhatsApp your landmark and a photo of the opening.</p>
        <p lang="ne" class="text-xs text-slate-400 leading-relaxed">धनुषा, महोत्तरी, सिरहा र मधेशभर निःशुल्क नाप जाँच। बनाउने काम जनकपुरधाममै।</p>
        <a href="/service-areas/" class="inline-block mt-4 text-xs font-bold text-amber-300 hover:underline">All Madhesh service areas →</a>
      </div>
    </div>
  </div>
</section>
'''

EXTRA_FAQS = r'''
      <!-- FAQ 6 · Janakpur local -->
      <div class="glass-card rounded-2xl overflow-hidden">
        <button onclick="toggleFaq(6)" class="w-full p-5 text-left font-bold text-sm sm:text-base text-white flex items-center justify-between gap-4">
          <span>Do you give free site visit in every ward of Janakpur Dham?</span>
          <span id="faq-icon-6" class="text-emerald-400 font-mono text-xl">+</span>
        </button>
        <div id="faq-content-6" class="hidden p-5 pt-0 text-xs sm:text-sm text-slate-300 leading-relaxed border-t border-white/5">
          Yes. Murli Chowk, Airport Road, Janaki Mandir / Janak Chowk, Ramanand Chowk, Bhanu Chowk, Pidari Chowk, Zero Mile, Mills Area, railway station road and all wards of Janakpur Sub-Metropolitan City. WhatsApp <strong>+977 9817658719</strong> with your ward number.
        </div>
      </div>
      <!-- FAQ 7 -->
      <div class="glass-card rounded-2xl overflow-hidden">
        <button onclick="toggleFaq(7)" class="w-full p-5 text-left font-bold text-sm sm:text-base text-white flex items-center justify-between gap-4">
          <span>जनकपुरधाममा झ्याल ढोका कहाँ बनाउने?</span>
          <span id="faq-icon-7" class="text-emerald-400 font-mono text-xl">+</span>
        </button>
        <div id="faq-content-7" class="hidden p-5 pt-0 text-xs sm:text-sm text-slate-300 leading-relaxed border-t border-white/5" lang="ne">
          अन्नपूर्णा आल्मुनियम तथा यूपीभीसी उद्योग, मुरली चोक (एयरपोर्ट रोड), जनकपुरधाम-८। यूपीभीसी झ्याल, आल्मुनियम ढोका, ग्लास रेलिङ, एसएस ३०४ मन्दिर गेट र किचन र्याक कारखानामा बन्छ। ह्वाट्सएप <strong>+९७७ ९८१७६५८७१९</strong>।
        </div>
      </div>
      <!-- FAQ 8 -->
      <div class="glass-card rounded-2xl overflow-hidden">
        <button onclick="toggleFaq(8)" class="w-full p-5 text-left font-bold text-sm sm:text-base text-white flex items-center justify-between gap-4">
          <span>Do you cover Dhalkebar, Jaleshwor, Lahan and Bardibas?</span>
          <span id="faq-icon-8" class="text-emerald-400 font-mono text-xl">+</span>
        </button>
        <div id="faq-content-8" class="hidden p-5 pt-0 text-xs sm:text-sm text-slate-300 leading-relaxed border-t border-white/5">
          Yes — free measurement for genuine building work across Dhanusha (Dhalkebar, Dhanushadham), Mahottari (Jaleshwor, Gaushala, Bardibas), Siraha (Lahan) and Sarlahi (Malangwa). Fabrication stays in Janakpur; fitting is on your site. See <a href="/service-areas/" class="text-emerald-400 underline">service areas</a>.
        </div>
      </div>
'''

NOSCRIPT = """
<noscript>
  <div style="max-width:720px;margin:24px auto;padding:16px;color:#e2e8f0;font-family:sans-serif">
    <h2>Annapurna Aluminium &amp; UPVC — Janakpur Dham</h2>
    <p>Murli Chowk (Airport Road), Janakpur Dham-8, Dhanusha, Nepal. WhatsApp +977 9817658719.</p>
    <ul>
      <li><a href="/upvc-window-janakpur/">UPVC windows Janakpur</a></li>
      <li><a href="/aluminium-janakpur/">Aluminium doors &amp; windows Janakpur</a></li>
      <li><a href="/glass-railing-janakpur/">Glass railing Janakpur</a></li>
      <li><a href="/steel-gate-janakpur/">SS 304 railing &amp; temple gate</a></li>
      <li><a href="/modular-kitchen-janakpur/">Modular kitchen rack Janakpur</a></li>
      <li><a href="/acp-cladding-janakpur/">ACP cladding &amp; shopfront</a></li>
      <li><a href="/janakpur-dham/">Workshop in Janakpur Dham</a></li>
      <li><a href="/service-areas/">Dhanusha &amp; Madhesh service areas</a></li>
    </ul>
  </div>
</noscript>
"""


def _extra_head() -> str:
    website = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": f"{SITE}/#website",
        "name": "Annapurna Aluminium & UPVC Janakpur",
        "url": f"{SITE}/",
        "inLanguage": ["en", "ne"],
        "publisher": {"@id": f"{SITE}/#business"},
    }
    return f"""
<link rel="alternate" hreflang="en" href="{SITE}/">
<link rel="alternate" hreflang="ne" href="{SITE}/">
<link rel="alternate" hreflang="x-default" href="{SITE}/">
<link rel="manifest" href="/manifest.webmanifest">
<link rel="sitemap" type="application/xml" href="/sitemap.xml">
<meta property="og:image:alt" content="Annapurna Aluminium &amp; UPVC workshop projects in Janakpur Dham">
<meta name="twitter:image:alt" content="UPVC windows, aluminium doors and steel gates fabricated in Janakpur">
<script type="application/ld+json">{_ld(_schema_business())}</script>
<script type="application/ld+json">{_ld(website)}</script>
"""


def enhance_homepage(html: str, shop: dict | None = None) -> str:
    """Inject Janakpur-first title, schemas, local hub section, extra FAQs, footer links."""
    html = html.replace(
        "<title>Annapurna Aluminium &amp; UPVC Udhyog | Janakpur Dham, Nepal | Premier Architectural Glass, Doors, Windows &amp; Steel Works</title>",
        f"<title>{HOMEPAGE_TITLE}</title>",
        1,
    )
    html = html.replace(
        'content="Official platform of Annapurna Aluminium &amp; UPVC Udhyog, Murli Chowk (Airport Road), Janakpur Dham. Direct WhatsApp Contact: +977 9817658719. 102+ custom architectural designs: German-profile UPVC soundproof windows, aluminium partitions, toughened glass railings, SS 304 temple gates, modular kitchen racks, ACP facade glazing. Free site visit &amp; fast Nepal-wide delivery."',
        f'content="{HOMEPAGE_DESC}"',
        1,
    )
    html = html.replace(
        'content="UPVC window Janakpur, UPVC window Nepal, aluminium door Janakpur, glass railing Nepal, SS 304 railing Janakpur, modular kitchen Nepal, ACP cladding Janakpur, temple gate fabrication Nepal, Murli Chowk Airport Road, Dhanusha glass works, Prof Nageshwar Thakur, Annapurna Aluminium, WhatsApp 9817658719"',
        f'content="{HOMEPAGE_KEYWORDS}"',
        1,
    )
    html = html.replace(
        '<html lang="en" class="scroll-smooth">',
        '<html lang="en-NP" class="scroll-smooth">',
        1,
    )
    html = html.replace(
        '<meta property="og:title" content="Annapurna Aluminium &amp; UPVC Udhyog | Direct WhatsApp +977 9817658719">',
        f'<meta property="og:title" content="{HOMEPAGE_TITLE}">',
        1,
    )
    html = html.replace(
        '<meta property="og:description" content="Explore 40+ authentic workshop projects and 102+ master custom designs. Direct WhatsApp contact for free site visit &amp; fast quotes: +977 9817658719.">',
        f'<meta property="og:description" content="{HOMEPAGE_DESC}">',
        1,
    )
    html = html.replace(
        '<meta name="twitter:title" content="Annapurna Aluminium &amp; UPVC Udhyog | Janakpur Dham, Nepal">',
        f'<meta name="twitter:title" content="{HOMEPAGE_TITLE}">',
        1,
    )
    html = html.replace("</head>", _extra_head() + "\n</head>", 1)
    html = html.replace(
        '<a href="#faq" class="hover:text-emerald-400 transition-colors py-1 border-b-2 border-transparent hover:border-emerald-400">FAQs</a>',
        '<a href="#janakpur-areas" class="hover:text-emerald-400 transition-colors py-1 border-b-2 border-transparent hover:border-emerald-400">Janakpur</a>\n      <a href="#faq" class="hover:text-emerald-400 transition-colors py-1 border-b-2 border-transparent hover:border-emerald-400">FAQs</a>',
        1,
    )
    html = html.replace(
        "<!-- SECTION: FREE SITE VISIT & CONSULTATION BOOKING",
        LOCAL_SECTION + "\n<!-- SECTION: FREE SITE VISIT & CONSULTATION BOOKING",
        1,
    )
    faq5 = (
        'data-i18n="faq_a5">\n'
        "          Standard residential window and door orders are completed in "
        "<strong>3 to 5 business days</strong>. Commercial facade glazing, large temple gates, "
        "and custom modular kitchens are scheduled as per site milestones with prompt delivery.\n"
        "        </div>\n      </div>"
    )
    if faq5 in html:
        html = html.replace(faq5, faq5 + "\n" + EXTRA_FAQS, 1)
    html = html.replace("</main>", NOSCRIPT + "\n</main>", 1)

    old_quick = """        <li><a href="#projects" class="hover:text-white transition-colors">40+ Real Projects Gallery</a></li>
        <li><a href="#catalog" class="hover:text-white transition-colors">102+ Product Catalog</a></li>
        <li><a href="#workflow" class="hover:text-white transition-colors">Precision Workflow</a></li>
        <li><a href="#booking" class="hover:text-white transition-colors">Book Free Site Visit</a></li>
        <li><a href="#about" class="hover:text-white transition-colors">Founder &amp; Workshop</a></li>"""
    new_quick = old_quick + """
        <li><a href="/upvc-window-janakpur/" class="hover:text-white transition-colors">UPVC Window Janakpur</a></li>
        <li><a href="/aluminium-janakpur/" class="hover:text-white transition-colors">Aluminium Door Janakpur</a></li>
        <li><a href="/glass-railing-janakpur/" class="hover:text-white transition-colors">Glass Railing Janakpur</a></li>
        <li><a href="/janakpur-dham/" class="hover:text-white transition-colors">Janakpur Dham Workshop</a></li>
        <li><a href="/service-areas/" class="hover:text-white transition-colors">Dhanusha &amp; Madhesh Areas</a></li>
        <li><a href="/faq-janakpur/" class="hover:text-white transition-colors">Local FAQ</a></li>"""
    html = html.replace(old_quick, new_quick, 1)

    chip = (
        '<span class="px-2 py-0.5 rounded-md bg-slate-900/80 border border-white/10 '
        'text-[10px] font-semibold text-slate-300 hover:border-emerald-400/45 '
        'hover:text-emerald-300 transition-colors">{label}</span>'
    )
    linked = {
        "Janakpur Dham": "/janakpur-dham/",
        "Dhanusha": "/service-areas/",
        "Jaleshwor": "/service-areas/",
        "Malangwa": "/service-areas/",
        "Lahan": "/service-areas/",
        "Bardibas": "/service-areas/",
        "Rajbiraj": "/service-areas/",
        "Birgunj": "/service-areas/",
        "Hetauda": "/service-areas/",
        "Kathmandu": "/service-areas/",
        "All Nepal": "/service-areas/",
    }
    for label, href in linked.items():
        html = html.replace(
            chip.format(label=label),
            f'<a href="{href}" class="px-2 py-0.5 rounded-md bg-slate-900/80 border border-white/10 text-[10px] font-semibold text-slate-300 hover:border-emerald-400/45 hover:text-emerald-300 transition-colors">{label}</a>',
            1,
        )

    html = html.replace("https://maps.google.com/?q=26.7118,85.9189", MAPS)
    html = html.replace("https://maps.google.com/?q=26.7288,85.9248", MAPS)
    html = html.replace(
        "https://maps.google.com/?q=Murli+Chowk+Airport+Road+Janakpur+Nepal",
        MAPS,
    )
    return html


def _sitemap_xml() -> str:
    urls = [
        (f"{SITE}/", "1.0", "daily"),
    ]
    for p in PAGES:
        urls.append((f"{SITE}/{p['slug']}/", "0.9", "weekly"))
    chunks = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    ]
    for loc, pri, freq in urls:
        chunks.append("  <url>")
        chunks.append(f"    <loc>{escape(loc)}</loc>")
        chunks.append(f"    <lastmod>{TODAY}</lastmod>")
        chunks.append(f"    <changefreq>{freq}</changefreq>")
        chunks.append(f"    <priority>{pri}</priority>")
        chunks.append(f'    <xhtml:link rel="alternate" hreflang="en" href="{escape(loc)}"/>')
        chunks.append(f'    <xhtml:link rel="alternate" hreflang="ne" href="{escape(loc)}"/>')
        if loc.rstrip("/").endswith("annapurna-upvc-janakpur.com"):
            chunks.append(
                "    <image:image>"
                f"<image:loc>{escape(OG_DEFAULT)}</image:loc>"
                "<image:title>Annapurna Aluminium commercial facade Janakpur Dham</image:title>"
                "<image:geo_location>Janakpur Dham, Nepal</image:geo_location>"
                "</image:image>"
            )
        chunks.append("  </url>")
    chunks.append("</urlset>")
    return "\n".join(chunks) + "\n"


def _robots() -> str:
    return f"""User-agent: *
Allow: /
Disallow: /catalog/build_all.py
Disallow: /catalog/build_v3.py
Disallow: /catalog/build_catalog.py

Sitemap: {SITE}/sitemap.xml

User-agent: Googlebot
Allow: /

User-agent: Googlebot-Image
Allow: /

User-agent: Bingbot
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /
"""


def _llms() -> str:
    lines = [
        "# Annapurna Aluminium & UPVC Udhyog",
        "",
        f"> Architectural fabrication workshop in Janakpur Dham, Nepal. {NAP_EN}. WhatsApp {PHONE_DISPLAY}.",
        "",
        "## Business",
        "",
        f"- Name: Annapurna Aluminium & UPVC Udhyog",
        f"- Founder: Prof. Nageshwar Thakur",
        f"- Address: {NAP_EN}",
        f"- Hours: 09:00–19:00, all 7 days",
        f"- PAN: {PAN}",
        f"- Phone: {PHONE_DISPLAY} / {PHONE2_DISPLAY}",
        f"- Website: {SITE}/",
        "",
        "## Services (Janakpur & Madhesh)",
        "",
    ]
    for p in PAGES:
        lines.append(f"- [{p['h1']}]({SITE}/{p['slug']}/): {p['service_name']}")
    lines += [
        "",
        "## Neighbourhoods",
        "",
        "- Murli Chowk / Airport Road (workshop)",
        "- Janaki Mandir / Janak Chowk, Ramanand Chowk, Bhanu Chowk, Pidari Chowk, Zero Mile, Mills Area",
        "- Dhalkebar, Dhanushadham, Jaleshwor, Lahan, Bardibas, Malangwa",
        "",
    ]
    return "\n".join(lines)


def _manifest() -> str:
    return json.dumps(
        {
            "name": "Annapurna Aluminium & UPVC — Janakpur Dham",
            "short_name": "Annapurna Janakpur",
            "description": "UPVC windows, aluminium doors, glass railing and steel gates in Janakpur Dham.",
            "start_url": "/",
            "scope": "/",
            "display": "standalone",
            "background_color": "#030712",
            "theme_color": "#030712",
            "lang": "en-NP",
            "icons": [
                {"src": "/catalog_assets/favicon-192.png", "sizes": "192x192", "type": "image/png"},
                {"src": "/catalog_assets/favicon-512.png", "sizes": "512x512", "type": "image/png"},
                {"src": "/catalog_assets/apple-touch-icon.png", "sizes": "180x180", "type": "image/png"},
            ],
        },
        ensure_ascii=False,
        indent=2,
    )


def _humans() -> str:
    return f"""/* TEAM */
Founder: Prof. Nageshwar Thakur
Workshop: Annapurna Aluminium & UPVC Udhyog
Location: {NAP_EN}
Contact: {PHONE_DISPLAY}

/* SITE */
Standards: HTML5, Schema.org LocalBusiness, XML Sitemap
Local SEO: Janakpur Dham, Dhanusha, Madhesh Province
Last update: {TODAY}
"""


def _not_found() -> str:
    links = "".join(
        f'<li><a class="text-emerald-400 underline" href="/{p["slug"]}/">{escape(p["nav"])}</a></li>'
        for p in PAGES
    )
    return f"""<!DOCTYPE html>
<html lang="en-NP">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found | Annapurna Aluminium Janakpur</title>
<meta name="robots" content="noindex, follow">
<link rel="canonical" href="{SITE}/404.html">
<style>body{{background:#030712;color:#e2e8f0;font-family:system-ui,sans-serif;padding:48px 20px;max-width:640px;margin:auto}}</style>
</head>
<body>
<h1>This page is not on the Janakpur workshop site.</h1>
<p>Return to <a href="/" style="color:#34d399">Annapurna Aluminium &amp; UPVC</a> or open a service page:</p>
<ul>{links}</ul>
<p>WhatsApp {PHONE_DISPLAY}</p>
</body>
</html>
"""


def _redirects() -> str:
    return """/upvc-windows-janakpur /upvc-window-janakpur/ 301
/upvc-window-nepal /upvc-window-janakpur/ 301
/aluminium-door-janakpur /aluminium-janakpur/ 301
/aluminium-window-janakpur /aluminium-janakpur/ 301
/glass-railing-nepal /glass-railing-janakpur/ 301
/ss-railing-janakpur /steel-gate-janakpur/ 301
/temple-gate-janakpur /steel-gate-janakpur/ 301
/kitchen-rack-janakpur /modular-kitchen-janakpur/ 301
/modular-kitchen-nepal /modular-kitchen-janakpur/ 301
/acp-janakpur /acp-cladding-janakpur/ 301
"""


SEO_SLUGS = [p["slug"] for p in PAGES]


def generate_local_seo(root: Path, dist: Path | None = None, shop: dict | None = None) -> None:
    """Write landing pages + technical SEO files into repo root and dist/."""
    targets = [root]
    if dist is not None:
        targets.append(dist)

    files = {
        "sitemap.xml": _sitemap_xml(),
        "robots.txt": _robots(),
        "llms.txt": _llms(),
        "manifest.webmanifest": _manifest(),
        "humans.txt": _humans(),
        "404.html": _not_found(),
        "_redirects": _redirects(),
        ".nojekyll": "",
    }

    for dest in targets:
        dest.mkdir(parents=True, exist_ok=True)
        for slug in SEO_SLUGS:
            page = _page_by_slug(slug)
            folder = dest / slug
            folder.mkdir(parents=True, exist_ok=True)
            (folder / "index.html").write_text(render_page(page), encoding="utf-8")
        for name, content in files.items():
            (dest / name).write_text(content, encoding="utf-8")
        print(f"Local SEO pages written under {dest} ({len(SEO_SLUGS)} hubs)")


if __name__ == "__main__":
    repo = Path(__file__).resolve().parent.parent
    generate_local_seo(repo, repo / "dist" if (repo / "dist").exists() else None)
