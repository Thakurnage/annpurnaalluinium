#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Annapurna Aluminium & UPVC — Master Builder & Website Compiler
Generates ultra-professional, premium architectural landing page (index.html and catalog/catalog.html)
with:
1. Ultra-Premium Smart AI Architectural Chatbot Widget featuring custom AI icon, preset general FAQs, typing indicator, instant expert answers, and 1-click Direct WhatsApp Call/Chat to Founder Prof. Nageshwar Thakur (+977 9817658719)
2. Automatic Infinite Sliding Background/Hero Product Banner Carousel
3. Ultra-Luxury High-Tech CAD Blueprint Cards with glowing grid & technical CAD markings
4. Direct WhatsApp Contact (+977 9817658719) across all touchpoints
5. Deep SEO optimization (JSON-LD structured data, Open Graph, Geo tags, semantic HTML5)
6. 40+ real workshop project lightbox gallery and 102+ design catalog switcher
7. Seamless dual-language support (English & Nepali).
"""

import json
import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "catalog_assets"
REAL_PROJ_DIR = ASSETS / "real_projects"
PRODUCTS_DIR = ASSETS / "products"
CATALOG_DIR = ROOT / "catalog"
DIST_DIR = ROOT / "dist"
sys.path.insert(0, str(CATALOG_DIR))

from products_data import P, CATS, BASE_FEATS  # noqa: E402

# Business details - Single WhatsApp contact number +977 9817658719
SHOP = {
    "name": "Annapurna Aluminium & UPVC",
    "legal_name": "Annapurna Aluminium & UPVC Udhyog",
    "tagline": "UPVC Windows & Doors · Aluminium Partitions · Toughened Glass · SS Steel Works",
    "owner_name": "Prof. Nageshwar Thakur",
    "phone1": "+977 9817658719",
    "phone1_raw": "9817658719",
    "whatsapp": "9779817658719",
    "address": "Janakpur Dham-8, Murli Chowk (Airport Road), Dhanusha, Madhesh Province, Nepal",
    "address_short": "Murli Chowk (Airport Road), Janakpur Dham-8, Dhanusha",
    "gmaps_url": "https://maps.google.com/?q=Murli+Chowk+Airport+Road+Janakpur+Dham+Nepal",
    "hours": "Sunday – Saturday: 9:00 AM – 7:00 PM (All 7 Days Open)",
    "province": "Madhesh Province",
    "country": "Nepal",
    "phone2": "+977 9817667115",
    "pan": "616619779",
    "geo_lat": 26.7288,
    "geo_lng": 85.9254,
    "service_areas": [
        "Janakpur Dham", "Dhanusha", "Mahottari (Jaleshwor)", "Sarlahi (Malangwa)",
        "Siraha (Lahan)", "Sindhuli (Bardibas)", "Udayapur (Gaighat)", "Rajbiraj",
        "Birgunj", "Hetauda", "Kathmandu", "Nepal-Wide Supply & Installation",
        "Murli Chowk", "Airport Road Janakpur", "Ramanand Chowk", "Bhanu Chowk",
        "Pidari Chowk", "Zero Mile Janakpur", "Dhalkebar", "Dhanushadham",
    ]
}

# Real projects catalog data (44 items)
REAL_PROJECTS = [
    {
        "id": "rp-1",
        "image": "facade_commercial_plaza.jpg",
        "thumb": "thumb_facade_commercial_plaza.jpg",
        "title": "4-Story Commercial Plaza Glass Facade & Red ACP Cladding",
        "title_ne": "४ तले व्यावसायिक प्लाजा ग्लास फसाड र रातो एसीपी क्ल्याडिङ",
        "category": "Storefront & Facade",
        "category_ne": "फसाड र एसीपी क्ल्याडिङ",
        "cat_key": "STF",
        "location": "Janakpur Commercial Hub",
        "location_ne": "जनकपुरधाम व्यापारिक केन्द्र",
        "desc": "Full structural silicone glazed curtain wall with premium thermal solar-control glass and fire-retardant Red ACP composite panel accents.",
        "desc_ne": "१२ मिमी टफन्ड ग्लास, स्ट्रक्चरल सिलिकन ग्लाजिङ र फायर-रिटारडेन्ट रातो एसीपी प्यानल जडित ४ तले आधुनिक व्यापारिक कम्प्लेक्स।",
        "specs": ["12mm Toughened Solar Glass", "Heavy 6063-T5 Subframe", "Eurobond ACP Cladding", "Zero-Leak EPDM Seals"]
    },
    {
        "id": "rp-2",
        "image": "facade_glass_tower.jpg",
        "thumb": "thumb_facade_glass_tower.jpg",
        "title": "Modern Commercial Glass Tower & Balcony Glass Railings",
        "title_ne": "आधुनिक ग्लास टावर र बालकनी ग्लास रेलिङ",
        "category": "Storefront & Facade",
        "category_ne": "फसाड र एसीपी क्ल्याडिङ",
        "cat_key": "STF",
        "location": "Airport Road, Janakpur",
        "location_ne": "एयरपोर्ट रोड, जनकपुरधाम",
        "desc": "Contemporary multi-story facade featuring dark tinted reflective glass panels and frameless glass balustrades on all cantilevered balconies.",
        "desc_ne": "गाढा रिफ्लेक्टिभ ग्लास प्यानल र क्यान्टिलिभर बालकनीहरूमा फ्रेमलेस टफन्ड ग्लास रेलिङ जडान गरिएको आधुनिक टावर।",
        "specs": ["Frameless Toughened Glass", "Reflective Curtain Wall", "Integrated UPVC Windows", "Weatherproof Seal"]
    },
    {
        "id": "rp-3",
        "image": "gate_navdurga_mandir.jpg",
        "thumb": "thumb_gate_navdurga_mandir.jpg",
        "title": "Sri Nav Durga Mandir Duhaba Grand SS Double Gate",
        "title_ne": "श्री नव दुर्गा मन्दिर दुहबा भव्य एसएस डबल मेन गेट",
        "category": "MS & Steel Works",
        "category_ne": "स्टिल तथा मन्दिर गेट",
        "cat_key": "MST",
        "location": "Duhaba Temple, Dhanusha",
        "location_ne": "दुहबा मन्दिर, धनुषा",
        "desc": "Massive ceremonial temple entrance double gate handcrafted from mirror-polished heavy SS 304 stainless steel pipes with religious sunburst motifs.",
        "desc_ne": "१००% खिया नलाग्ने एसएस ३०४ स्टेनलेस स्टीलबाट निर्मित, धार्मिक सूर्य किरण बुट्टा र देवनागरी नामपट्टी सहितको भव्य मन्दिर गेट।",
        "specs": ["100% Rust-Proof SS 304", "Laser-Cut Grillework", "Heavy Ball Bearing Hinges", "Lifetime Mirror Polish"]
    },
    {
        "id": "rp-4",
        "image": "gate_mandir_closeup.jpg",
        "thumb": "thumb_gate_mandir_closeup.jpg",
        "title": "Ornamental Stainless Steel Temple Arch Security Gate",
        "title_ne": "सजावटी स्टेनलेस स्टील मन्दिर सुरक्षा गेट",
        "category": "MS & Steel Works",
        "category_ne": "स्टिल तथा मन्दिर गेट",
        "cat_key": "MST",
        "location": "Janakpur Pilgrimage Route",
        "location_ne": "जनकपुरधाम परिक्रमा मार्ग",
        "desc": "Architectural arched temple gate engineered for maximum security and enduring aesthetic brilliance under high pedestrian footfall.",
        "desc_ne": "उच्च सुरक्षा र आकर्षक सजावटको लागि निर्माण गरिएको आर्क आकारको एसएस ३०४ स्टेनलेस स्टील गेट।",
        "specs": ["Precision TIG Welded", "Heavy Gauge SS Sections", "Anti-Sag Framework", "Dual Security Locks"]
    },
    {
        "id": "rp-5",
        "image": "villa_upvc_doors_windows.jpg",
        "thumb": "thumb_villa_upvc_doors_windows.jpg",
        "title": "Luxury Villa Courtyard UPVC French Doors & Sliding Windows",
        "title_ne": "लक्जरी भिल्ला यूपीभीसी फ्रेन्च ढोका र स्लाइडिङ झ्यालहरू",
        "category": "UPVC Windows & Doors",
        "category_ne": "यूपीभीसी झ्याल तथा ढोका",
        "cat_key": "UWC",
        "location": "Janakpur Private Villa",
        "location_ne": "जनकपुरधाम लक्जरी भिल्ला",
        "desc": "Full courtyard glazing with German multi-chamber white uPVC sliding windows, double-glazed French patio doors, and natural lighting transoms.",
        "desc_ne": "जर्मन प्रोफाइल साउन्डप्रुफ यूपीभीसी स्लाइडिङ झ्याल र ५+९+५ डबल ग्लाज्ड फ्रेन्च ढोकाहरू।",
        "specs": ["Multi-Chamber Soundproof", "5+9A+5 Double Glazing", "Multi-Point Security Locks", "Monsoon Rainproof Seals"]
    },
    {
        "id": "rp-6",
        "image": "kitchen_modular_lshape.jpg",
        "thumb": "thumb_kitchen_modular_lshape.jpg",
        "title": "Custom L-Shaped Aluminium Modular Kitchen Counter & Storage Racks",
        "title_ne": "एल-आकारको आल्मुनियम मोड्युलर किचन र्याक र क्याबिनेट",
        "category": "Modular Kitchen Racks",
        "category_ne": "मोड्युलर किचन र्याक",
        "cat_key": "MOD",
        "location": "Janakpur Modern Residence",
        "location_ne": "जनकपुरधाम आधुनिक आवास",
        "desc": "Termite-proof, 100% waterproof modular kitchen counter and drawer organization system finished in high-gloss pink ACP panels.",
        "desc_ne": "धमिरा नलाग्ने, पानीले नबिग्रिने १००% वाटरप्रुफ आल्मुनियम मोड्युलर किचन र्याक र क्याबिनेट प्रणाली।",
        "specs": ["100% Waterproof & Termite Proof", "Heavy Aluminium Framing", "Smooth Telescopic Drawers", "Easy-Clean Hygiene Panels"]
    },
    {
        "id": "rp-7",
        "image": "kitchen_aluminium_racks.jpg",
        "thumb": "thumb_kitchen_aluminium_racks.jpg",
        "title": "Red & Silver Aluminium Crockery & Storage Rack Showcase",
        "title_ne": "रातो र सिल्भर आल्मुनियम क्रोकरी तथा भण्डारण र्याक",
        "category": "Modular Kitchen Racks",
        "category_ne": "मोड्युलर किचन र्याक",
        "cat_key": "MOD",
        "location": "Showroom Display Unit",
        "location_ne": "शोरुम डिस्प्ले युनिट",
        "desc": "Multipurpose kitchen storage rack with toughened glass shelves, sliding glass front panels, and heavy-duty corner-braced aluminium structure.",
        "desc_ne": "भाँडाकुँडा सुरक्षित राख्न टफन्ड ग्लास सेल्फ र स्लाइडिङ ग्लास सहितको बहुउपयोगी आल्मुनियम र्याक।",
        "specs": ["Adjustable Shelving", "High Impact ACP Backing", "Smooth Slide Glass", "Lifetime Rust-Free"]
    },
    {
        "id": "rp-8",
        "image": "kitchen_installed_counter.jpg",
        "thumb": "thumb_kitchen_installed_counter.jpg",
        "title": "Installed Red Composite Kitchen Lower Cabinets & SS Countertop",
        "title_ne": "फिटिङ गरिएको मोड्युलर किचन क्याबिनेट र काउन्टरटप",
        "category": "Modular Kitchen Racks",
        "category_ne": "मोड्युलर किचन र्याक",
        "cat_key": "MOD",
        "location": "Residential Kitchen, Janakpur",
        "location_ne": "जनकपुरधाम घरायसी किचन",
        "desc": "Custom made-to-measure under-counter storage cabinets with stainless steel pulls and integrated ventilation louvers.",
        "desc_ne": "किचनको वास्तविक साइज अनुसार निर्माण गरिएको कम्पोजिट प्यानल र स्टेनलेस स्टील ह्यान्डल क्याबिनेट।",
        "specs": ["Custom Made-to-Measure", "SS Handles & Latches", "Fire-Safe Composite Panels", "Heavy Load Capacity"]
    },
    {
        "id": "rp-9",
        "image": "stair_black_marble_ss.jpg",
        "thumb": "thumb_stair_black_marble_ss.jpg",
        "title": "Luxury Black Marble Staircase with SS & Black Acrylic Posts",
        "title_ne": "कालो मार्बल भर्याङमा एसएस र एक्रिलिक रेलिङ",
        "category": "Stainless Steel Railings",
        "category_ne": "स्टेनलेस स्टील रेलिङ",
        "cat_key": "SLS",
        "location": "Luxury Duplex, Janakpur",
        "location_ne": "जनकपुरधाम लक्जरी डुप्लेक्स",
        "desc": "Stunning internal staircase balustrade featuring solid black acrylic inserts, mirror-finish SS 304 top handrail, and heavy marble-anchor base plates.",
        "desc_ne": "कालो ग्रेनाइट भर्याङमा जडान गरिएको लक्जरी एसएस ३०४ र ब्ल्याक एक्रिलिक रेलिङ।",
        "specs": ["Solid Acrylic Master Posts", "Mirror Polish SS 304 Pipe", "Hidden Heavy Expansion Anchors", "Zero-Wobble Rigidity"]
    },
    {
        "id": "rp-10",
        "image": "crystal_acrylic_ss_pillars.jpg",
        "thumb": "thumb_crystal_acrylic_ss_pillars.jpg",
        "title": "Royal Stair Balustrade with Faceted Crystal Acrylic Pillars",
        "title_ne": "रोयल क्रिस्टल एक्रिलिक पिलर भर्याङ रेलिङ",
        "category": "Stainless Steel Railings",
        "category_ne": "स्टेनलेस स्टील रेलिङ",
        "cat_key": "SLS",
        "location": "Private Mansion, Dhanusha",
        "location_ne": "धनुषा लक्जरी निवास",
        "desc": "Premium interior staircase railing highlighting clear diamond-cut acrylic crystal newel posts with gold-accented stainless steel rings.",
        "desc_ne": "लाइटिङ पर्दा टल्किने डाइमण्ड कट क्रिस्टल एक्रिलिक पिलर र गोल्ड-रिम एसएस ३०४ रेलिङ।",
        "specs": ["Diamond-Cut Acrylic Pillars", "Gold & Chrome Accents", "SS 304 Multi-Tier Balusters", "Custom Corner Elbows"]
    },
    {
        "id": "rp-11",
        "image": "balcony_ss_sunburst.jpg",
        "thumb": "thumb_balcony_ss_sunburst.jpg",
        "title": "Sunburst Motif SS 304 Balcony Guard Railing",
        "title_ne": "सूर्य किरण बुट्टा एसएस ३०४ बालकनी रेलिङ",
        "category": "Stainless Steel Railings",
        "category_ne": "स्टेनलेस स्टील रेलिङ",
        "cat_key": "SLS",
        "location": "Residential Villa, Janakpur",
        "location_ne": "जनकपुरधाम आवासीय भिल्ला",
        "desc": "Heavy-duty exterior balcony protection railing featuring center sunburst medallion grills and 2-inch continuous top safety pipe.",
        "desc_ne": "घरको मुख्य बालकनीको सुरक्षा र सुन्दरताको लागि निर्मित सूर्य किरण बुट्टा एसएस रेलिङ।",
        "specs": ["Central Decorative Medallions", "Heavy Wall Thickness SS Pipes", "Weather-Resistant Weld Joints", "Child-Safe Vertical Spacing"]
    },
    {
        "id": "rp-12",
        "image": "balcony_ss_wave_railing.jpg",
        "thumb": "thumb_balcony_ss_wave_railing.jpg",
        "title": "Curved Wave Pattern SS 304 Balcony Protection Railing",
        "title_ne": "वेभ ढाँचा एसएस ३०४ बालकनी रेलिङ",
        "category": "Stainless Steel Railings",
        "category_ne": "स्टेनलेस स्टील रेलिङ",
        "cat_key": "SLS",
        "location": "Commercial Residence, Jaleshwor",
        "location_ne": "जलेश्वर व्यावसायिक निवास",
        "desc": "Custom hydro-bent wave baluster railing installed along a long cantilevered building balcony for modern aesthetic impact.",
        "desc_ne": "आकर्षक वेभ ढाँचामा पाइप ब्यान्डिङ गरी जडान गरिएको दिगो एसएस ३०४ बालकनी रेलिङ।",
        "specs": ["Hydro-Bent Wave Profiles", "Continuous Corner Jointing", "Corrosion Free Outdoors", "Heavy Floor Anchor Flanges"]
    },
    {
        "id": "rp-13",
        "image": "door_3d_floral_glass.jpg",
        "thumb": "thumb_door_3d_floral_glass.jpg",
        "title": "3D Sculpted Floral Etched Glass Aluminium Main Door",
        "title_ne": "३डी फ्लोरल इच्ड ग्लास आल्मुनियम मुख्य ढोका",
        "category": "Aluminium Doors",
        "category_ne": "आल्मुनियम ढोका",
        "cat_key": "ALD",
        "location": "Executive Office, Janakpur",
        "location_ne": "जनकपुरधाम कार्यकारी कार्यालय",
        "desc": "Heavy aluminium frame entrance door featuring double-layered 3D sandblasted floral artwork glass panel with frosted privacy background.",
        "desc_ne": "३डी इचिङ गरिएको कलात्मक ग्लास र पाउडर कोटेड आल्मुनियम फ्रेम ढोका।",
        "specs": ["3D Deep Etched Artwork", "10mm Toughened Glass", "Heavy Hydraulic Floor Spring", "SS Vertical Bar Pull Handle"]
    },
    {
        "id": "rp-14",
        "image": "door_eurobond_panel.jpg",
        "thumb": "thumb_door_eurobond_panel.jpg",
        "title": "Red Eurobond Composite Panel Aluminium Office Flush Door",
        "title_ne": "रातो यूरोबन्ड कम्पोजिट प्यानल आल्मुनियम ढोका",
        "category": "Aluminium Doors",
        "category_ne": "आल्मुनियम ढोका",
        "cat_key": "ALD",
        "location": "Commercial Plaza, Janakpur",
        "location_ne": "जनकपुरधाम प्लाजा",
        "desc": "Ultra-durable, waterproof composite panel interior flush door engineered for high-traffic office corridors and washrooms.",
        "desc_ne": "पानी र धमिराले कहिल्यै नबिग्रिने उच्च गुणस्तरको रातो कम्पोजिट प्यानल ढोका।",
        "specs": ["Waterproof & Termite Proof", "Heavy Duty Aluminium Frame", "Mortise Cylinder Lockset", "Zero Distortion Under Moisture"]
    },
    {
        "id": "rp-15",
        "image": "door_islamic_arch_entry.jpg",
        "thumb": "thumb_door_islamic_arch_entry.jpg",
        "title": "Traditional Arch Motif Aluminium Composite Entrance Door",
        "title_ne": "ट्रेडिसनल आर्क बुट्टा आल्मुनियम ढोका",
        "category": "Aluminium Doors",
        "category_ne": "आल्मुनियम ढोका",
        "cat_key": "ALD",
        "location": "Residence, Dhanusha",
        "location_ne": "धनुषा निजी निवास",
        "desc": "Ornate arched top composite panel entrance door combining golden highlights with frosted glass vision panels.",
        "desc_ne": "आकर्षक आर्क ढाँचा र गोल्डेन स्ट्रिप सहितको आल्मुनियम मुख्य ढोका।",
        "specs": ["Precision Arch Geometry", "Integrated Vision Panel", "Gold Anodized Trims", "Multi-Point Latch"]
    },
    {
        "id": "rp-16",
        "image": "door_ss_arched_security_grill.jpg",
        "thumb": "thumb_door_ss_arched_security_grill.jpg",
        "title": "Arched Stainless Steel Security Safety Door Grill",
        "title_ne": "आर्क आकारको एसएस ३०४ सेफ्टी ढोका गेट",
        "category": "MS & Steel Works",
        "category_ne": "स्टिल तथा मन्दिर गेट",
        "cat_key": "MST",
        "location": "Villa Entrance, Janakpur",
        "location_ne": "जनकपुरधाम भिल्ला",
        "desc": "Heavy main entrance safety door featuring intricate arched SS 304 grille bars and dual deadbolt lock mechanisms.",
        "desc_ne": "घरको मुख्य ढोका बाहिर जडान गरिने उच्च सुरक्षा एसएस ३०४ आर्क सेफ्टी ढोका।",
        "specs": ["Heavy Gauge SS 304 Rods", "Dual Deadbolt Security", "Tamper-Proof Hinges", "Lifetime Polish"]
    },
    {
        "id": "rp-17",
        "image": "door_upvc_frosted_texture.jpg",
        "thumb": "thumb_door_upvc_frosted_texture.jpg",
        "title": "Frosted Textured Glass UPVC Bathroom & Balcony Door",
        "title_ne": "फ्रस्टेड ग्लास यूपीभीसी बाथरुम तथा ढोका",
        "category": "UPVC Windows & Doors",
        "category_ne": "यूपीभीसी झ्याल तथा ढोका",
        "cat_key": "UWD",
        "location": "Hotel Suite, Janakpur",
        "location_ne": "जनकपुरधाम होटेल सुइट",
        "desc": "White uPVC single sash casement door with pinhead frosted obscure privacy glass for wet areas and balconies.",
        "desc_ne": "बाथरुम र बालकनीको लागि उपयुक्त १००% वाटरप्रुफ साउन्डप्रुफ यूपीभीसी ढोका।",
        "specs": ["Obscure Privacy Glass", "Multi-Chamber uPVC Frame", "Rust-Proof SS Friction Stays", "Monsoon Rain Seal"]
    },
    {
        "id": "rp-18",
        "image": "door_upvc_mosaic_glass.jpg",
        "thumb": "thumb_door_upvc_mosaic_glass.jpg",
        "title": "Mosaic Pattern Decorative Glass UPVC Patio Door",
        "title_ne": "मोजाइक ग्लास यूपीभीसी प्याटियो ढोका",
        "category": "UPVC Windows & Doors",
        "category_ne": "यूपीभीसी झ्याल तथा ढोका",
        "cat_key": "UWD",
        "location": "Residence, Lahan",
        "location_ne": "लहान निजी निवास",
        "desc": "Decorative interior UPVC door with multi-colored bevel mosaic glass inserts and heavy steel reinforcement.",
        "desc_ne": "रंगीन मोजाइक आर्ट ग्लास र स्टिल रिइन्फोर्समेन्ट सहितको आकर्षक यूपीभीसी ढोका।",
        "specs": ["Bevel Cut Mosaic Glass", "Steel Core Reinforcement", "Smooth Lever Handle", "Noise Insulation"]
    },
    {
        "id": "rp-19",
        "image": "door_woodgrain_teak_finish.jpg",
        "thumb": "thumb_door_woodgrain_teak_finish.jpg",
        "title": "Golden Teak Woodgrain Finish UPVC French Main Door",
        "title_ne": "गोल्डेन टिक काठ फिनिसिङ यूपीभीसी मुख्य ढोका",
        "category": "UPVC Windows & Doors",
        "category_ne": "यूपीभीसी झ्याल तथा ढोका",
        "cat_key": "UWD",
        "location": "Private Villa, Janakpur",
        "location_ne": "जनकपुरधाम लक्जरी घर",
        "desc": "UV-resistant golden teak wood texture laminated UPVC French double door with clear double glazing.",
        "desc_ne": "हुबहु काठ जस्तै देखिने, घाम र पानीले नखुइलिने गोल्डेन टिक यूपीभीसी ढोका।",
        "specs": ["German Foil Wood Laminate", "Double Glazed 5+9A+5", "Multi-Point Locking System", "Zero Painting Required"]
    },
    {
        "id": "rp-20",
        "image": "window_aluminium_blue_slider.jpg",
        "thumb": "thumb_window_aluminium_blue_slider.jpg",
        "title": "Royal Blue Tint Reflective Glass Aluminium 3-Track Slider",
        "title_ne": "रोयल ब्लु रिफ्लेक्टिभ ग्लास आल्मुनियम झ्याल",
        "category": "Aluminium Windows",
        "category_ne": "आल्मुनियम झ्याल",
        "cat_key": "ALW",
        "location": "Commercial Complex, Janakpur",
        "location_ne": "जनकपुरधाम व्यापारिक भवन",
        "desc": "Powder-coated white aluminium 3-track sliding window fitted with solar heat reducing blue reflective glass panels.",
        "desc_ne": "घामको तापक्रम घटाउने रोयल ब्लु रिफ्लेक्टिभ ग्लास सहितको आल्मुनियम ३-ट्र्याक झ्याल।",
        "specs": ["Solar Heat Control Glass", "Interlocking Sash Locks", "SS Mesh Track Included", "Powder Coated Frame"]
    },
    {
        "id": "rp-21",
        "image": "window_upvc_colonial_grid.jpg",
        "thumb": "thumb_window_upvc_colonial_grid.jpg",
        "title": "Colonial Georgian Grid UPVC Architectural Casement Window",
        "title_ne": "जर्जियन ग्रिड यूपीभीसी आर्किटेक्चरल झ्याल",
        "category": "UPVC Windows & Doors",
        "category_ne": "यूपीभीसी झ्याल तथा ढोका",
        "cat_key": "UWC",
        "location": "Heritage Residence, Janakpur",
        "location_ne": "जनकपुरधाम हेरिटेज घर",
        "desc": "Classic European colonial style white uPVC casement window with internal decorative Georgian bar lattice.",
        "desc_ne": "क्लासिक युरोपियन शैलीको ग्रिड बुट्टा र साउन्डप्रुफ यूपीभीसी क्यासमेन्ट झ्याल।",
        "specs": ["Internal Georgian Lattice", "Acoustic Double Glazing", "Multi-Point Security Stays", "100% Dust Sealed"]
    },
    {
        "id": "rp-22",
        "image": "facade_islamic_triple_arches.jpg",
        "thumb": "thumb_facade_islamic_triple_arches.jpg",
        "title": "Triple Arch Architectural Storefront Facade & Commercial Glazing",
        "title_ne": "ट्रिपल आर्क आर्किटेक्चरल स्टोरफ्रन्ट फसाड",
        "category": "Storefront & Facade",
        "category_ne": "फसाड र एसीपी क्ल्याडिङ",
        "cat_key": "STF",
        "location": "Grand Showroom, Janakpur",
        "location_ne": "जनकपुरधाम मुख्य शोरुम",
        "desc": "Monumental triple-arched commercial glass storefront with dark bronze structural aluminium profiles and frameless glass entry.",
        "desc_ne": "भव्य ट्रिपल आर्क आकारमा निर्मित डार्क ब्रोन्ज आल्मुनियम र टफन्ड ग्लास शोरुम फसाड।",
        "specs": ["Custom Precision Bending", "12mm Toughened Glass", "Heavy Bronze Subframe", "Structural Silicone Glazing"]
    },
    {
        "id": "rp-23",
        "image": "gate_house_compound_ms_ss.jpg",
        "thumb": "thumb_gate_house_compound_ms_ss.jpg",
        "title": "Modern Hybrid Compound Gate with SS Pipes & MS Frame",
        "title_ne": "आधुनिक हाइब्रिड एसएस र एमएस कम्पाउण्ड गेट",
        "category": "MS & Steel Works",
        "category_ne": "स्टिल तथा मन्दिर गेट",
        "cat_key": "MST",
        "location": "Private Compound, Janakpur",
        "location_ne": "जनकपुरधाम कम्पाउण्ड",
        "desc": "Heavy dual-sliding compound main gate engineered with heavy gauge MS perimeter box sections and mirror SS horizontal tubes.",
        "desc_ne": "मजबुत एमएस फ्रेम र ऐना जस्तै टल्किने एसएस ३०४ पाइपबाट निर्मित आधुनिक कम्पाउण्ड गेट।",
        "specs": ["Dual Track Roller Assemblies", "Heavy Box Frame", "Mirror SS Highlights", "Anti-Sag Hinge Assembly"]
    },
    {
        "id": "rp-24",
        "image": "glass_etched_palm_tree.jpg",
        "thumb": "thumb_glass_etched_palm_tree.jpg",
        "title": "Custom Acid-Etched Tropical Palm Tree Glass Partition Wall",
        "title_ne": "कस्टम एसिड-इच्ड पाम ट्री ग्लास पार्टिसन",
        "category": "Glass Solutions",
        "category_ne": "टफन्ड ग्लास",
        "cat_key": "GLZ",
        "location": "Luxury Residence, Janakpur",
        "location_ne": "जनकपुरधाम लक्जरी निवास",
        "desc": "Custom artistic room divider featuring precision acid-etched tropical palm tree scenery on 10mm toughened glass.",
        "desc_ne": "१० मिमी टफन्ड ग्लासमा आकर्षक पाम ट्री बुट्टा इचिङ गरिएको लिभिङ रुम पार्टिसन।",
        "specs": ["10mm Safety Toughened Glass", "Deep Acid Etch Artwork", "SS Corner Clamps", "Fingerprint-Resistant Finish"]
    },
    {
        "id": "rp-25",
        "image": "hardware_american_handle.jpg",
        "thumb": "thumb_hardware_american_handle.jpg",
        "title": "Heavy-Duty American Architectural Lever Lockset & Hardware",
        "title_ne": "हेभी-ड्युटी अमेरिकन आर्किटेक्चरल लक तथा ह्यान्डल",
        "category": "UPVC Windows & Doors",
        "category_ne": "यूपीभीसी झ्याल तथा ढोका",
        "cat_key": "UWD",
        "location": "Hardware Specimen Display",
        "location_ne": "हार्डवेयर स्पेसिमेन डिस्प्ले",
        "desc": "Solid brass & SS 304 architectural door hardware utilized on all Annapurna premium UPVC and aluminium doors.",
        "desc_ne": "हाम्रा ढोकाहरूमा प्रयोग गरिने ओरिजिनल एसएस ३०४ र ब्रास मल्टि-पोइन्ट लकसेट।",
        "specs": ["Solid Brass Cylinder Keys", "SS 304 Escutcheon Plates", "100,000 Cycle Tested", "Anti-Pick Keyway"]
    },
    {
        "id": "rp-26",
        "image": "hardware_ss_glass_clamps.jpg",
        "thumb": "thumb_hardware_ss_glass_clamps.jpg",
        "title": "Solid SS 304 Heavy-Duty Glass Holding Clamps & Fittings",
        "title_ne": "एसएस ३०४ हेभी-ड्युटी ग्लास क्लाम्प र फिटिङ्स",
        "category": "Glass Solutions",
        "category_ne": "टफन्ड ग्लास",
        "cat_key": "GLZ",
        "location": "Fitting Specification Workshop",
        "location_ne": "फेब्रिकेसन वर्कसप जनकपुर",
        "desc": "Precision cast SS 304 heavy glass clamps designed to hold 10-12mm toughened structural glass securely without drilling.",
        "desc_ne": "रेलिङ र फसाड ग्लासमा प्रयोग गरिने उच्च भार बहन क्षमताको एसएस ३०४ क्लाम्प।",
        "specs": ["Cast SS 304 Alloy", "EPDM Cushion Gaskets", "Mirror Buffed Finish", "High Load Capacity"]
    }
]

# Map product codes to real project photos for photo view
PROD_PHOTO_MAP = {
    "UWC-01": "villa_upvc_doors_windows.jpg",
    "UWC-02": "window_upvc_colonial_grid.jpg",
    "UWC-03": "villa_upvc_doors_windows.jpg",
    "UWC-04": "window_upvc_colonial_grid.jpg",
    "UWC-05": "villa_upvc_doors_windows.jpg",
    "UWC-06": "window_upvc_colonial_grid.jpg",
    "UWC-07": "villa_upvc_doors_windows.jpg",
    "UWC-08": "window_upvc_colonial_grid.jpg",
    "UWC-09": "villa_upvc_doors_windows.jpg",
    "UWC-10": "window_upvc_colonial_grid.jpg",
    "UWC-11": "villa_upvc_doors_windows.jpg",
    "UWC-12": "window_upvc_colonial_grid.jpg",
    
    "UWD-01": "door_upvc_frosted_texture.jpg",
    "UWD-02": "door_woodgrain_teak_finish.jpg",
    "UWD-03": "door_upvc_mosaic_glass.jpg",
    "UWD-04": "villa_upvc_doors_windows.jpg",
    "UWD-05": "door_woodgrain_teak_finish.jpg",
    "UWD-06": "door_upvc_frosted_texture.jpg",
    "UWD-07": "door_upvc_mosaic_glass.jpg",
    "UWD-08": "villa_upvc_doors_windows.jpg",
    "UWD-09": "door_woodgrain_teak_finish.jpg",
    "UWD-10": "door_upvc_frosted_texture.jpg",
    
    "ALW-01": "window_aluminium_blue_slider.jpg",
    "ALW-02": "window_aluminium_blue_slider.jpg",
    "ALW-03": "window_aluminium_blue_slider.jpg",
    "ALW-04": "window_aluminium_blue_slider.jpg",
    "ALW-05": "window_aluminium_blue_slider.jpg",
    "ALW-06": "window_aluminium_blue_slider.jpg",
    "ALW-07": "window_aluminium_blue_slider.jpg",
    "ALW-08": "window_aluminium_blue_slider.jpg",
    "ALW-09": "window_aluminium_blue_slider.jpg",
    "ALW-10": "window_aluminium_blue_slider.jpg",
    
    "ALD-01": "door_3d_floral_glass.jpg",
    "ALD-02": "door_eurobond_panel.jpg",
    "ALD-03": "door_islamic_arch_entry.jpg",
    "ALD-04": "door_3d_floral_glass.jpg",
    "ALD-05": "door_eurobond_panel.jpg",
    "ALD-06": "door_islamic_arch_entry.jpg",
    "ALD-07": "door_3d_floral_glass.jpg",
    "ALD-08": "door_eurobond_panel.jpg",
    
    "ALP-01": "glass_etched_palm_tree.jpg",
    "ALP-02": "glass_etched_palm_tree.jpg",
    "ALP-03": "glass_etched_palm_tree.jpg",
    "ALP-04": "glass_etched_palm_tree.jpg",
    "ALP-05": "glass_etched_palm_tree.jpg",
    "ALP-06": "glass_etched_palm_tree.jpg",
    "ALP-07": "glass_etched_palm_tree.jpg",
    "ALP-08": "glass_etched_palm_tree.jpg",

    "GLZ-01": "glass_etched_palm_tree.jpg",
    "GLZ-02": "hardware_ss_glass_clamps.jpg",
    "GLZ-03": "glass_etched_palm_tree.jpg",
    "GLZ-04": "hardware_ss_glass_clamps.jpg",
    "GLZ-05": "glass_etched_palm_tree.jpg",
    "GLZ-06": "hardware_ss_glass_clamps.jpg",
    "GLZ-07": "glass_etched_palm_tree.jpg",
    "GLZ-08": "hardware_ss_glass_clamps.jpg",
    "GLZ-09": "glass_etched_palm_tree.jpg",
    "GLZ-10": "hardware_ss_glass_clamps.jpg",

    "STF-01": "facade_commercial_plaza.jpg",
    "STF-02": "facade_glass_tower.jpg",
    "STF-03": "facade_islamic_triple_arches.jpg",
    "STF-04": "facade_commercial_plaza.jpg",
    "STF-05": "facade_glass_tower.jpg",
    "STF-06": "facade_islamic_triple_arches.jpg",
    "STF-07": "facade_commercial_plaza.jpg",
    "STF-08": "facade_glass_tower.jpg",

    "MST-01": "gate_navdurga_mandir.jpg",
    "MST-02": "gate_mandir_closeup.jpg",
    "MST-03": "door_ss_arched_security_grill.jpg",
    "MST-04": "gate_house_compound_ms_ss.jpg",
    "MST-05": "gate_navdurga_mandir.jpg",
    "MST-06": "gate_mandir_closeup.jpg",
    "MST-07": "door_ss_arched_security_grill.jpg",
    "MST-08": "gate_house_compound_ms_ss.jpg",
    "MST-09": "gate_navdurga_mandir.jpg",
    "MST-10": "gate_mandir_closeup.jpg",

    "SLS-01": "stair_black_marble_ss.jpg",
    "SLS-02": "crystal_acrylic_ss_pillars.jpg",
    "SLS-03": "balcony_ss_sunburst.jpg",
    "SLS-04": "balcony_ss_wave_railing.jpg",
    "SLS-05": "stair_black_marble_ss.jpg",
    "SLS-06": "crystal_acrylic_ss_pillars.jpg",
    "SLS-07": "balcony_ss_sunburst.jpg",
    "SLS-08": "balcony_ss_wave_railing.jpg",

    "RLS-01": "stair_black_marble_ss.jpg",
    "RLS-02": "crystal_acrylic_ss_pillars.jpg",
    "RLS-03": "balcony_ss_sunburst.jpg",
    "RLS-04": "balcony_ss_wave_railing.jpg",
    "RLS-05": "stair_black_marble_ss.jpg",
    "RLS-06": "crystal_acrylic_ss_pillars.jpg",
    "RLS-07": "balcony_ss_sunburst.jpg",
    "RLS-08": "balcony_ss_wave_railing.jpg",

    "MOD-01": "kitchen_modular_lshape.jpg",
    "MOD-02": "kitchen_aluminium_racks.jpg",
    "MOD-03": "kitchen_installed_counter.jpg",
    "MOD-04": "kitchen_modular_lshape.jpg",
    "MOD-05": "kitchen_aluminium_racks.jpg",
    "MOD-06": "kitchen_installed_counter.jpg",
    "MOD-07": "kitchen_modular_lshape.jpg",
    "MOD-08": "kitchen_aluminium_racks.jpg",
    "MOD-09": "kitchen_installed_counter.jpg",
    "MOD-10": "kitchen_modular_lshape.jpg",
}

# Category metadata with Nepali badges
CAT_META = {
    "UWC": {"color": "#00d2ff", "icon": "⬚", "badge": "UPVC Windows", "badge_ne": "यूपीभीसी झ्यालहरू", "tag": "German Multi-Chamber · Soundproof · Heatproof"},
    "UWD": {"color": "#3b82f6", "icon": "▤", "badge": "UPVC Doors", "badge_ne": "यूपीभीसी ढोकाहरू", "tag": "Steel Reinforced · Weatherproof · High Security"},
    "ALW": {"color": "#22d3ee", "icon": "◫", "badge": "Aluminium Windows", "badge_ne": "आल्मुनियम झ्यालहरू", "tag": "6063-T5 Alloy · Slim Profiles · Powder Coated"},
    "ALD": {"color": "#60a5fa", "icon": "▣", "badge": "Aluminium Doors", "badge_ne": "आल्मुनियम ढोकाहरू", "tag": "Eurobond ACP · Frosted Glass · Zero Warping"},
    "ALP": {"color": "#2dd4bf", "icon": "▥", "badge": "Aluminium Partitions", "badge_ne": "आल्मुनियम पार्टिसन", "tag": "Acoustic Glass · Office Cabins · Modern Privacy"},
    "GLZ": {"color": "#818cf8", "icon": "◈", "badge": "Glass Solutions", "badge_ne": "टफन्ड ग्लास", "tag": "8-12mm Toughened · Frameless Spigots · Safety"},
    "STF": {"color": "#a855f7", "icon": "▦", "badge": "Storefront & Facades", "badge_ne": "ग्लास फसाड तथा एसीपी", "tag": "Curtain Wall Glazing · ACP Cladding · Showrooms"},
    "MST": {"color": "#f59e0b", "icon": "⛓", "badge": "MS & Steel Works", "badge_ne": "मन्दिर तथा मेन गेट", "tag": "Temple Gates · Grills · Security Doors · Sheds"},
    "SLS": {"color": "#eab308", "icon": "✦", "badge": "Stainless Steel (SS 304)", "badge_ne": "एसएस ३०४ रेलिङ", "tag": "Mirror Polish · Crystal Pillars · Lifetime Rust-Free"},
    "RLS": {"color": "#f97316", "icon": "⤢", "badge": "Railings & Balustrades", "badge_ne": "बालकनी तथा भर्याङ", "tag": "Staircases · Balconies · Glass & SS Hybrid"},
    "MOD": {"color": "#ec4899", "icon": "▧", "badge": "Modular Kitchen & Racks", "badge_ne": "मोड्युलर किचन र्याक", "tag": "Termite-Proof · 100% Waterproof · ACP Racks"},
}

def load_svg_map():
    svg_map_file = CATALOG_DIR / "svg_art_map.json"
    if svg_map_file.exists():
        try:
            return json.loads(svg_map_file.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}

print("Building Ultra-Luxury Master Portal with Smart AI Chatbot Assistant...")
svg_map = load_svg_map()
print(f"Loaded {len(svg_map)} technical SVG blueprints.")

products_list = []
for pr in P:
    code = pr["code"]
    cat = pr["cat"]
    real_photo = PROD_PHOTO_MAP.get(code, "facade_commercial_plaza.jpg")
    photo_rel = f"catalog_assets/real_projects/{real_photo}"
    svg_art = svg_map.get(code, "")
    
    prod_obj = {
        "code": code,
        "cat": cat,
        "name": pr["name"],
        "desc": pr["desc"],
        "sizes": pr["sizes"],
        "finishes": pr["finishes"],
        "extras": pr["extras"],
        "base_feats": BASE_FEATS.get(cat, []),
        "photo": photo_rel,
        "real_photo_name": real_photo,
        "svg": svg_art,
        "art_key": pr["art"][0],
        "art_params": pr["art"][1],
        "meta": CAT_META.get(cat, {})
    }
    products_list.append(prod_obj)

print(f"Prepared {len(products_list)} rich product definitions.")

templates_js_raw = (CATALOG_DIR / "templates.js").read_text(encoding="utf-8")

# JSON-LD Structured Data for Deep SEO
schema_local_business = {
    "@context": "https://schema.org",
    "@type": "HomeAndConstructionBusiness",
    "name": SHOP["legal_name"],
    "alternateName": [
        "Annapurna Aluminium Janakpur",
        "Annapurna UPVC Janakpur",
        "अन्नपूर्णा आल्मुनियम जनकपुरधाम",
    ],
    "image": [
        "https://annapurna-upvc-janakpur.com/catalog_assets/real_projects/facade_commercial_plaza.jpg",
        "https://annapurna-upvc-janakpur.com/catalog_assets/real_projects/gate_navdurga_mandir.jpg",
        "https://annapurna-upvc-janakpur.com/catalog_assets/board_final.png",
    ],
    "logo": "https://annapurna-upvc-janakpur.com/catalog_assets/board_final.png",
    "@id": "https://annapurna-upvc-janakpur.com/#business",
    "url": "https://annapurna-upvc-janakpur.com/",
    "telephone": [SHOP["phone1"], SHOP["phone2"]],
    "priceRange": "$$",
    "currenciesAccepted": "NPR",
    "paymentAccepted": "Cash, eSewa, Khalti, Bank Transfer",
    "hasMap": SHOP["gmaps_url"],
    "knowsLanguage": ["ne", "en", "mai"],
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Murli Chowk (Airport Road), Janakpur Dham-8",
        "addressLocality": "Janakpur Dham",
        "addressRegion": "Dhanusha, Madhesh Province",
        "postalCode": "45600",
        "addressCountry": "NP"
    },
    "geo": {
        "@type": "GeoCoordinates",
        "latitude": 26.7288,
        "longitude": 85.9254
    },
    "openingHoursSpecification": {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "opens": "09:00",
        "closes": "19:00"
    },
    "founder": {
        "@type": "Person",
        "name": SHOP["owner_name"],
        "jobTitle": "Founder & Master Architectural Fabricator"
    },
    "identifier": {"@type": "PropertyValue", "name": "PAN", "value": SHOP["pan"]},
    "contactPoint": {
        "@type": "ContactPoint",
        "telephone": SHOP["phone1"],
        "contactType": "sales",
        "availableLanguage": ["Nepali", "English", "Maithili"],
        "areaServed": "NP"
    },
    "areaServed": SHOP["service_areas"],
    "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "Architectural UPVC, Glass, Aluminium & Steel Fabrication Services",
        "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "German UPVC Soundproof Windows & Doors"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Aluminium Partitions & Powder Coated Doors"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Toughened Frameless Glass Railings & Balustrades"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "SS 304 Temple Gates & Staircase Pillars"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "100% Waterproof Modular Kitchen Racks"}},
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "ACP Cladding & Commercial Curtain Wall Glazing"}}
        ]
    }
}

schema_item_list = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "102+ Master Architectural Fabrication Designs",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": idx + 1,
            "name": p["name"],
            "description": p["desc"],
            "sku": p["code"]
        } for idx, p in enumerate(products_list)
    ]
}

schema_faq = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "Where is Annapurna Aluminium & UPVC workshop located in Nepal?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Our primary manufacturing workshop and showroom is located at Murli Chowk (Airport Road), Janakpur Dham-8, Dhanusha, Madhesh Province, Nepal. We serve all districts of Madhesh Province with free site measurement and provide delivery + installation Nepal-wide."
            }
        },
        {
            "@type": "Question",
            "name": "How can I contact Annapurna Aluminium on WhatsApp?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "You can directly text or message our master engineer on WhatsApp at +977 9817658719 for free site measurements, quotations, and 3D architectural consultations."
            }
        },
        {
            "@type": "Question",
            "name": "What is the difference between UPVC and Aluminium windows?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "UPVC windows feature multi-chamber insulated profiles with superior acoustic soundproofing, zero heat transfer (thermal efficiency), and 100% weather sealing without maintenance. Aluminium windows offer ultra-slim aesthetic frames, immense structural rigidity, and custom powder-coated finishes suitable for large architectural spans and commercial storefronts."
            }
        },
        {
            "@type": "Question",
            "name": "Are your modular kitchen racks 100% waterproof and termite proof?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes, our modular kitchen racks are fabricated exclusively from heavy architectural aluminium sections and high-pressure composite panels (ACP), making them 100% waterproof, termite-proof, rust-free, and fire-retardant unlike traditional wood or MDF."
            }
        },
        {
            "@type": "Question",
            "name": "What grade of stainless steel do you use for railings and temple gates?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "We use genuine SS 304 marine grade stainless steel with high chromium-nickel content, mirror buffed finish, and argon TIG welding to guarantee lifetime shine without rusting or tarnishing under monsoon rains."
            }
        },
        {
            "@type": "Question",
            "name": "Do you give free site visit in every ward of Janakpur Dham?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes. Our engineer visits Murli Chowk, Airport Road, Janaki Mandir / Janak Chowk, Ramanand Chowk, Bhanu Chowk, Pidari Chowk, Zero Mile, Mills Area, railway station road and all wards of Janakpur Sub-Metropolitan City for free laser measurement. WhatsApp +977 9817658719."
            }
        },
        {
            "@type": "Question",
            "name": "जनकपुरधाममा झ्याल ढोका कहाँ बनाउने?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "अन्नपूर्णा आल्मुनियम तथा यूपीभीसी उद्योग, मुरली चोक (एयरपोर्ट रोड), जनकपुरधाम-८, धनुषा। यूपीभीसी झ्याल, आल्मुनियम ढोका, ग्लास रेलिङ, एसएस ३०४ मन्दिर गेट र मोड्युलर किचन र्याक कारखाना मूल्यमा। ह्वाट्सएप +977 9817658719।"
            }
        },
        {
            "@type": "Question",
            "name": "Do you cover Dhalkebar, Jaleshwor, Lahan and Bardibas from Janakpur?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes. Free site measurement for genuine building work across Dhanusha (Dhalkebar, Dhanushadham), Mahottari (Jaleshwor, Gaushala, Bardibas), Siraha (Lahan) and Sarlahi (Malangwa). Frames are fabricated in Janakpur Dham and installed on your site."
            }
        }
    ]
}

schema_breadcrumbs = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://annapurna-upvc-janakpur.com/"
        },
        {
            "@type": "ListItem",
            "position": 2,
            "name": "Real Projects Gallery",
            "item": "https://annapurna-upvc-janakpur.com/#projects"
        },
        {
            "@type": "ListItem",
            "position": 3,
            "name": "102+ Design Catalog",
            "item": "https://annapurna-upvc-janakpur.com/#catalog"
        }
    ]
}

# Construct Ultra-Professional Landing Page HTML String
PREMIUM_BOOKING_CSS = r'''/* ==================== PREMIUM BOOKING v3.7 — LUXURY GLASSMORPHISM SHELL ==================== */
.bk-shell {
  position: relative;
  border-radius: 1.75rem;
  padding: 2px;
  overflow: hidden;
  isolation: isolate;
}
.bk-shell::before {
  content: "";
  position: absolute;
  inset: -120%;
  z-index: -2;
  background: linear-gradient(115deg, #10b981, #22d3ee, #fbbf24, #34d399, #0ea5e9, #f59e0b, #10b981);
  background-size: 400% 400%;
  animation: bkBorderFlow 9s ease-in-out infinite;
}
@keyframes bkBorderFlow {
  0%   { background-position: 0% 50%; }
  50%  { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
.bk-shell::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  border-radius: calc(1.75rem - 2px);
  background:
    radial-gradient(60% 45% at 12% 0%, rgba(16, 185, 129, 0.16), transparent 60%),
    radial-gradient(50% 42% at 88% 8%, rgba(251, 191, 36, 0.12), transparent 60%),
    radial-gradient(55% 45% at 50% 100%, rgba(34, 211, 238, 0.10), transparent 65%),
    rgba(4, 10, 24, 0.94);
}

/* Benefit cards */
.bk-benefit-card {
  display: flex;
  align-items: flex-start;
  gap: 0.8rem;
  padding: 1rem 1.1rem;
  border-radius: 1.1rem;
  background: linear-gradient(150deg, rgba(17, 29, 66, 0.5), rgba(7, 12, 28, 0.72));
  border: 1px solid rgba(255, 255, 255, 0.09);
  backdrop-filter: blur(14px) saturate(1.4);
  -webkit-backdrop-filter: blur(14px) saturate(1.4);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.07);
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}
.bk-benefit-card:hover {
  transform: translateY(-3px);
  border-color: rgba(16, 185, 129, 0.5);
  box-shadow: 0 14px 30px -14px rgba(16, 185, 129, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.1);
}
.bk-benefit-ic {
  flex: 0 0 auto;
  width: 2.6rem;
  height: 2.6rem;
  border-radius: 0.85rem;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.15rem;
  background: linear-gradient(145deg, rgba(16, 185, 129, 0.24), rgba(34, 211, 238, 0.14));
  border: 1px solid rgba(16, 185, 129, 0.35);
  box-shadow: 0 0 18px -6px rgba(16, 185, 129, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.18);
}

/* How-It-Works mini timeline */
.bk-timeline {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0.5rem;
}
.bk-tl-step { position: relative; text-align: center; }
.bk-tl-step::after {
  content: "";
  position: absolute;
  top: 1.12rem;
  left: calc(50% + 1.35rem);
  width: calc(100% - 2.7rem);
  height: 2px;
  background: linear-gradient(90deg, rgba(16, 185, 129, 0.55), rgba(34, 211, 238, 0.3));
  border-radius: 2px;
}
.bk-tl-step:last-child::after { display: none; }
.bk-tl-num {
  position: relative;
  z-index: 1;
  width: 2.3rem;
  height: 2.3rem;
  margin: 0 auto 0.45rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 900;
  font-size: 0.8rem;
  color: #ffffff;
  background: linear-gradient(145deg, #059669, #0d9488);
  border: 2px solid rgba(255, 255, 255, 0.28);
  box-shadow: 0 0 0 4px rgba(16, 185, 129, 0.14), 0 8px 18px -8px rgba(16, 185, 129, 0.7);
}
.bk-tl-cap {
  font-size: 0.62rem;
  font-weight: 800;
  letter-spacing: 0.02em;
  text-transform: uppercase;
  color: #cbd5e1;
  line-height: 1.25;
}

/* Premium inputs */
.bk-input-wrap { position: relative; }
.bk-input-ic {
  position: absolute;
  left: 0.9rem;
  top: 50%;
  transform: translateY(-50%);
  font-size: 0.95rem;
  opacity: 0.85;
  pointer-events: none;
  z-index: 1;
}
.bk-input-wrap input,
.bk-input-wrap select,
.bk-input-wrap textarea {
  width: 100%;
  padding: 0.8rem 1rem 0.8rem 2.6rem;
  border-radius: 0.9rem;
  background: rgba(7, 12, 28, 0.85);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: #f8fafc;
  font-size: 0.78rem;
  transition: border-color 0.25s, box-shadow 0.25s, background 0.25s;
}
.bk-input-wrap textarea { padding-left: 1rem; }
.bk-input-wrap input::placeholder,
.bk-input-wrap textarea::placeholder { color: #64748b; }
.bk-input-wrap input:focus,
.bk-input-wrap select:focus,
.bk-input-wrap textarea:focus {
  outline: none;
  border-color: rgba(16, 185, 129, 0.75);
  box-shadow: 0 0 0 4px rgba(16, 185, 129, 0.16), 0 0 22px -6px rgba(16, 185, 129, 0.5);
  background: rgba(7, 14, 32, 0.96);
}
.bk-input-wrap select {
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding-right: 2.5rem;
  cursor: pointer;
}
.bk-input-wrap optgroup { background: #0b132b; color: #fbbf24; font-weight: 800; font-size: 0.72rem; }
.bk-input-wrap option { background: #0b132b; color: #e2e8f0; font-size: 0.78rem; font-weight: 500; }
.bk-select-chev {
  position: absolute;
  right: 1rem;
  top: 50%;
  transform: translateY(-50%);
  pointer-events: none;
  color: #34d399;
  font-size: 0.8rem;
  filter: drop-shadow(0 0 6px rgba(52, 211, 153, 0.6));
  z-index: 1;
}

/* Premium submit — WhatsApp SVG + shine sweep */
.bk-submit {
  position: relative;
  overflow: hidden;
  width: 100%;
  padding: 0.95rem 1rem;
  border-radius: 1rem;
  background: linear-gradient(135deg, #047857, #10b981 45%, #0d9488);
  color: #ffffff;
  font-weight: 800;
  font-size: 0.8rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.6rem;
  border: 1px solid rgba(255, 255, 255, 0.18);
  box-shadow: 0 14px 34px -12px rgba(16, 185, 129, 0.65), inset 0 1px 0 rgba(255, 255, 255, 0.35);
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s;
}
.bk-submit:hover {
  transform: translateY(-2px);
  box-shadow: 0 20px 44px -12px rgba(16, 185, 129, 0.85), inset 0 1px 0 rgba(255, 255, 255, 0.4);
}
.bk-submit::after {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  left: -75%;
  width: 42%;
  background: linear-gradient(105deg, transparent, rgba(255, 255, 255, 0.45), transparent);
  transform: skewX(-20deg);
  animation: bkShine 3.2s ease-in-out infinite;
  pointer-events: none;
}
@keyframes bkShine {
  0%, 55% { left: -75%; }
  90%, 100% { left: 135%; }
}
.bk-sub-ic { width: 18px; height: 18px; flex: 0 0 auto; }

/* Badge + divider */
.bk-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.35rem 0.85rem;
  border-radius: 999px;
  background: linear-gradient(90deg, rgba(16, 185, 129, 0.16), rgba(34, 211, 238, 0.12));
  border: 1px solid rgba(52, 211, 153, 0.4);
  color: #6ee7b7;
  font-size: 0.62rem;
  font-weight: 800;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
}

@media (max-width: 640px) {
  .bk-timeline { grid-template-columns: repeat(2, 1fr); row-gap: 1rem; }
  .bk-tl-step:nth-child(2)::after { display: none; }
}
@media (prefers-reduced-motion: reduce) {
  .bk-shell::before, .bk-submit::after { animation: none; }
}'''

PREMIUM_BOOKING_HTML = '''<!-- SECTION: FREE SITE VISIT & CONSULTATION BOOKING (v3.7 PREMIUM · WHATSAPP DISPATCH) -->
<section id="booking" class="py-16 px-4 relative z-10 bg-slate-950/60 border-t border-white/5">
  <div class="max-w-6xl mx-auto">

    <div class="bk-shell">
      <div class="relative p-6 sm:p-10 lg:p-12">

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-10 items-start">

          <!-- LEFT: Benefit Cards + How-It-Works Timeline -->
          <div>
            <div class="bk-badge mb-4">💬 WhatsApp Direct Appointment</div>
            <h2 class="text-2xl sm:text-4xl font-black font-display text-white mb-4" data-i18n="booking_title">Book Free On-Site Measurement</h2>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed mb-6" data-i18n="booking_desc">Building a new house, commercial showroom, or renovating your hotel in Janakpur Dham or nearby districts? Our master engineer will visit your site with actual profile and glass samples for laser-guided measurement.</p>

            <div class="space-y-3 mb-7">
              <div class="bk-benefit-card">
                <div class="bk-benefit-ic">💬</div>
                <div>
                  <div class="text-[13px] font-extrabold text-white" data-i18n="bk_benefit_1_t">Direct WhatsApp Dispatch</div>
                  <div class="text-[11px] text-slate-400 leading-snug mt-0.5" data-i18n="bk_benefit_1_d">Booking lands instantly with our master engineer (+977 9817658719)</div>
                </div>
              </div>
              <div class="bk-benefit-card">
                <div class="bk-benefit-ic">🧪</div>
                <div>
                  <div class="text-[13px] font-extrabold text-white" data-i18n="bk_benefit_2_t">Real Sample Demo On-Site</div>
                  <div class="text-[11px] text-slate-400 leading-snug mt-0.5" data-i18n="bk_benefit_2_d">Physical UPVC, aluminium &amp; glass samples with laser-guided measurement</div>
                </div>
              </div>
              <div class="bk-benefit-card">
                <div class="bk-benefit-ic">📐</div>
                <div>
                  <div class="text-[13px] font-extrabold text-white" data-i18n="bk_benefit_3_t">Instant Quote + 3D Advice</div>
                  <div class="text-[11px] text-slate-400 leading-snug mt-0.5" data-i18n="bk_benefit_3_d">Structural quotation &amp; 3D drawing advice on the spot</div>
                </div>
              </div>
            </div>

            <!-- How It Works mini timeline -->
            <div class="rounded-2xl border border-white/10 bg-slate-950/55 p-5">
              <div class="flex items-center gap-2 text-[10px] font-extrabold uppercase tracking-[0.18em] text-emerald-300 mb-4">
                <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/></svg>
                <span data-i18n="bk_how_title">How It Works</span>
              </div>
              <div class="bk-timeline">
                <div class="bk-tl-step"><div class="bk-tl-num">1</div><div class="bk-tl-cap" data-i18n="bk_step_1">Request</div></div>
                <div class="bk-tl-step"><div class="bk-tl-num">2</div><div class="bk-tl-cap" data-i18n="bk_step_2">Confirm Slot</div></div>
                <div class="bk-tl-step"><div class="bk-tl-num">3</div><div class="bk-tl-cap" data-i18n="bk_step_3">Site Visit</div></div>
                <div class="bk-tl-step"><div class="bk-tl-num">4</div><div class="bk-tl-cap" data-i18n="bk_step_4">Quote &amp; Blueprint</div></div>
              </div>
            </div>
          </div>

          <!-- RIGHT: Premium Booking Form (Direct WhatsApp Dispatch) -->
          <form onsubmit="handleContactSubmit(event)" class="space-y-4 rounded-2xl border border-white/10 bg-slate-950/70 p-6 sm:p-7 backdrop-blur-xl shadow-2xl relative">
            <div class="flex items-center gap-3 mb-1">
              <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-500/25 to-cyan-500/20 border border-emerald-400/40 flex items-center justify-center text-base shadow-[0_0_16px_-4px_rgba(16,185,129,0.6)]">📋</div>
              <div>
                <h3 class="font-extrabold text-white text-[15px] leading-tight" data-i18n="form_title">Request Site Visit &amp; Custom Quote</h3>
                <div class="text-[10px] text-slate-400 font-semibold tracking-wide" data-i18n="bk_form_sub">100% free · Reply within 15 minutes</div>
              </div>
            </div>
            <div class="h-px bg-gradient-to-r from-transparent via-emerald-500/50 to-transparent"></div>

            <div>
              <label class="block text-[11px] font-bold text-slate-300 mb-1.5" data-i18n="form_label_name">Your Full Name *</label>
              <div class="bk-input-wrap">
                <span class="bk-input-ic">👤</span>
                <input type="text" id="form-name" required placeholder="e.g. Er. Ram Shrestha" autocomplete="name">
              </div>
            </div>

            <div>
              <label class="block text-[11px] font-bold text-slate-300 mb-1.5" data-i18n="form_label_phone">Your WhatsApp Number *</label>
              <div class="bk-input-wrap">
                <span class="bk-input-ic">📱</span>
                <input type="tel" id="form-phone" required placeholder="e.g. 9817658719" autocomplete="tel">
              </div>
            </div>

            <div>
              <label class="block text-[11px] font-bold text-slate-300 mb-1.5" data-i18n="form_label_city">Project Location / District *</label>
              <div class="bk-input-wrap">
                <span class="bk-input-ic">📍</span>
                <input type="text" id="form-city" required placeholder="e.g. Janakpur-8, Dhanusha" autocomplete="address-level2">
              </div>
            </div>

            <div>
              <label class="block text-[11px] font-bold text-slate-300 mb-1.5" data-i18n="form_label_service">Primary Architectural Requirement</label>
              <div class="bk-input-wrap">
                <span class="bk-input-ic">🪟</span>
                <select id="form-service" class="bk-select">
                  <optgroup label="🪟 Windows &amp; Doors">
                    <option>UPVC Windows &amp; Patio Doors</option>
                    <option>Soundproof German UPVC Casement Windows</option>
                    <option>Aluminium Sliding Windows &amp; Frames</option>
                    <option>UPVC French / Patio Doors</option>
                    <option>Aluminium Main Entry Doors</option>
                  </optgroup>
                  <optgroup label="🏢 Office, Glass &amp; Steel">
                    <option>Aluminium Office Partitions &amp; Doors</option>
                    <option>Toughened Glass Railings &amp; Balustrades</option>
                    <option>SS 304 Temple Gate &amp; Main Gate</option>
                    <option>Structural Curtain Wall Glazing</option>
                    <option>SS 304 Railings &amp; Spiral Stairs</option>
                  </optgroup>
                  <optgroup label="🏠 Interior &amp; Facade">
                    <option>Modular Waterproof Kitchen Racks</option>
                    <option>ACP Facade Cladding</option>
                    <option>Aluminium Louvers &amp; Sunshades</option>
                    <option>Glass Wardrobes &amp; Shower Enclosures</option>
                  </optgroup>
                </select>
                <span class="bk-select-chev">▾</span>
              </div>
            </div>

            <div>
              <label class="block text-[11px] font-bold text-slate-300 mb-1.5" data-i18n="form_label_notes">Approximate Openings / Notes</label>
              <div class="bk-input-wrap">
                <textarea id="form-notes" rows="2" placeholder="e.g. 10 windows, 2 main doors, 30 ft balcony railing..."></textarea>
              </div>
            </div>

            <button type="submit" class="bk-submit">
              <svg class="bk-sub-ic" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.64.07-.3-.15-1.26-.46-2.4-1.47-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.44-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.5 0 1.47 1.07 2.9 1.22 3.1.15.2 2.11 3.22 5.1 4.51.71.31 1.27.49 1.7.63.72.23 1.37.2 1.88.12.57-.09 1.76-.72 2.01-1.41.25-.7.25-1.29.17-1.41-.07-.13-.27-.2-.57-.35Z"/><path d="M12.05 2a9.97 9.97 0 0 0-8.61 14.98L2 22l5.13-1.4A10 10 0 1 0 12.05 2Zm0 18.2a8.2 8.2 0 0 1-4.19-1.15l-.3-.18-3.05.83.84-2.97-.2-.31a8.2 8.2 0 1 1 6.9 3.78Z"/></svg>
              <span data-i18n="bk_submit">Send Booking to WhatsApp</span>
            </button>
            <p class="text-[10px] text-slate-500 text-center">🔒 No spam · Direct to master engineer · Reply within 15 minutes</p>
          </form>

        </div>

      </div>
    </div>

  </div>
</section>'''

html_content = f"""<!DOCTYPE html>
<!-- BUILD v3.6-premium-hero | 2026-08-28 | Premium hero redesign · cinematic crossfade background showcase · managed visibility scrim · synced auto-slide progress · gold shimmer headline · entrance reveal · count-up stats | Annapurna Aluminium & UPVC Udhyog -->
<html lang="en" class="scroll-smooth">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Annapurna Aluminium &amp; UPVC Udhyog | Janakpur Dham, Nepal | Premier Architectural Glass, Doors, Windows &amp; Steel Works</title>

<!-- DEEP SEO META TAGS -->
<meta name="description" content="Official platform of Annapurna Aluminium &amp; UPVC Udhyog, Murli Chowk (Airport Road), Janakpur Dham. Direct WhatsApp Contact: +977 9817658719. 102+ custom architectural designs: German-profile UPVC soundproof windows, aluminium partitions, toughened glass railings, SS 304 temple gates, modular kitchen racks, ACP facade glazing. Free site visit &amp; fast Nepal-wide delivery.">
<meta name="keywords" content="UPVC window Janakpur, UPVC window Nepal, aluminium door Janakpur, glass railing Nepal, SS 304 railing Janakpur, modular kitchen Nepal, ACP cladding Janakpur, temple gate fabrication Nepal, Murli Chowk Airport Road, Dhanusha glass works, Prof Nageshwar Thakur, Annapurna Aluminium, WhatsApp 9817658719">
<meta name="author" content="Annapurna Aluminium &amp; UPVC Udhyog — Janakpur Dham, Nepal">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
<meta name="googlebot" content="index, follow">
<meta name="theme-color" content="#030712">

<!-- FAVICON · Founder's professional portrait with brand gradient ring (v3.4) -->
<link rel="icon" type="image/x-icon" sizes="16x16 32x32 48x48" href="favicon.ico">
<link rel="icon" type="image/png" sizes="192x192" href="catalog_assets/favicon-192.png">
<link rel="icon" type="image/png" sizes="512x512" href="catalog_assets/favicon-512.png">
<link rel="apple-touch-icon" sizes="180x180" href="catalog_assets/apple-touch-icon.png">

<!-- GEO LOCAL SEO -->
<meta name="geo.region" content="NP-P2">
<meta name="geo.placename" content="Janakpur Dham, Dhanusha, Madhesh Province, Nepal">
<meta name="geo.position" content="26.7288;85.9254">
<meta name="ICBM" content="26.7288, 85.9254">

<!-- CANONICAL URL -->
<link rel="canonical" href="https://annapurna-upvc-janakpur.com/">

<!-- OPEN GRAPH META TAGS -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="Annapurna Aluminium &amp; UPVC Udhyog">
<meta property="og:title" content="Annapurna Aluminium &amp; UPVC Udhyog | Direct WhatsApp +977 9817658719">
<meta property="og:description" content="Explore 40+ authentic workshop projects and 102+ master custom designs. Direct WhatsApp contact for free site visit &amp; fast quotes: +977 9817658719.">
<meta property="og:image" content="https://annapurna-upvc-janakpur.com/catalog_assets/real_projects/facade_commercial_plaza.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:url" content="https://annapurna-upvc-janakpur.com/">
<meta property="og:locale" content="en_US">
<meta property="og:locale:alternate" content="ne_NP">

<!-- TWITTER CARDS -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Annapurna Aluminium &amp; UPVC Udhyog | Janakpur Dham, Nepal">
<meta name="twitter:description" content="102+ Custom Designs &amp; 40+ Workshop Real Projects. WhatsApp Direct: +977 9817658719.">
<meta name="twitter:image" content="https://annapurna-upvc-janakpur.com/catalog_assets/real_projects/facade_commercial_plaza.jpg">

<!-- GOOGLE FONTS -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800;900&family=Noto+Sans+Devanagari:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;800&display=swap" rel="stylesheet">

<!-- TAILWIND CSS CDN -->
<script src="https://cdn.tailwindcss.com"></script>
<script>
tailwind.config = {{
  darkMode: 'class',
  theme: {{
    extend: {{
      fontFamily: {{
        sans: ['Plus Jakarta Sans', 'Noto Sans Devanagari', 'system-ui', 'sans-serif'],
        display: ['Outfit', 'Noto Sans Devanagari', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      }},
      colors: {{
        obsidian: {{
          950: '#030712',
          900: '#0b132b',
          850: '#111d42',
          800: '#1c2b5e',
        }},
        gold: {{
          400: '#fbbf24',
          500: '#f59e0b',
          600: '#d97706',
        }}
      }}
    }}
  }}
}}
</script>

<style>
:root {{
  --bg-obsidian: #030712;
  --glass-bg: rgba(11, 19, 43, 0.78);
  --glass-border: rgba(255, 255, 255, 0.08);
  --cyan-glow: rgba(56, 189, 248, 0.25);
  --emerald-glow: rgba(16, 185, 129, 0.25);
}}

body {{
  background-color: #030712;
  color: #f3f4f6;
  font-family: 'Plus Jakarta Sans', 'Noto Sans Devanagari', sans-serif;
  overflow-x: hidden;
}}

/* Ultra-Luxury Glassmorphism */
.glass-panel {{
  background: rgba(11, 19, 43, 0.52);
  backdrop-filter: blur(20px) saturate(1.5);
  -webkit-backdrop-filter: blur(20px) saturate(1.5);
  border: 1px solid rgba(255, 255, 255, 0.12);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.07);
}}

.glass-nav {{
  background: rgba(3, 7, 18, 0.88);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}}

.glass-card {{
  background: linear-gradient(145deg, rgba(17, 29, 66, 0.44) 0%, rgba(7, 12, 28, 0.66) 100%);
  backdrop-filter: blur(16px) saturate(1.5);
  -webkit-backdrop-filter: blur(16px) saturate(1.5);
  border: 1px solid rgba(255, 255, 255, 0.12);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.07);
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}}

.glass-card:hover {{
  transform: translateY(-6px);
  border-color: rgba(16, 185, 129, 0.45);
  box-shadow: 0 20px 40px -12px rgba(16, 185, 129, 0.2);
}}

/* ===== v3.3 · RIGHT-EDGE PER-ROW EXPANDING SOCIAL RAIL ===== */
.social-dock{{position:fixed;top:50%;right:0;transform:translateY(-50%);z-index:45;display:flex;flex-direction:column;align-items:flex-end;gap:9px;padding:10px 0}}
.social-dock-row{{display:flex;align-items:center;text-decoration:none;background:linear-gradient(155deg,rgba(13,22,48,.94),rgba(3,7,18,.97));backdrop-filter:blur(20px) saturate(1.5);-webkit-backdrop-filter:blur(20px) saturate(1.5);border:1px solid rgba(255,255,255,.14);border-radius:15px;padding:6px;box-shadow:0 12px 30px -12px rgba(0,0,0,.85),inset 0 1px 0 rgba(255,255,255,.07);transform:translateX(21px);transition:transform .45s cubic-bezier(.16,1,.3,1),box-shadow .4s,border-color .3s;will-change:transform;position:relative}}
.social-dock-row:hover,.social-dock-row:focus-visible{{transform:translateX(0);border-color:rgba(255,255,255,.3);box-shadow:-14px 14px 34px -12px rgba(0,0,0,.85),inset 0 1px 0 rgba(255,255,255,.12)}}
.social-dock-label{{font-size:12px;font-weight:700;white-space:nowrap;color:#e2e8f0;max-width:0;opacity:0;overflow:hidden;transition:max-width .45s cubic-bezier(.16,1,.3,1),opacity .28s ease .07s,padding .45s cubic-bezier(.16,1,.3,1)}}
.social-dock-row:hover .social-dock-label,.social-dock-row:focus-visible .social-dock-label{{max-width:230px;opacity:1;padding-left:13px;padding-right:3px}}
.social-dock-icon{{flex:0 0 auto;width:42px;height:42px;border-radius:11px;display:flex;align-items:center;justify-content:center;border:1px solid rgba(255,255,255,.12);transition:transform .32s cubic-bezier(.16,1,.3,1),background .3s,box-shadow .3s}}
.social-dock-row:hover .social-dock-icon{{transform:scale(1.07)}}
.social-dock-row::after{{content:"";position:absolute;left:2px;top:50%;transform:translateY(-50%);width:3px;height:26px;border-radius:3px;background:linear-gradient(to bottom,#10b981,#38bdf8);opacity:.7;box-shadow:0 0 10px rgba(16,185,129,.55)}}
.social-dock-row:hover::after{{opacity:0}}
.social-dock-call{{margin-top:5px}}
@media(max-width:640px){{.social-dock{{gap:7px}}.social-dock-row{{transform:translateX(25px);padding:5px}}.social-dock-icon{{width:38px;height:38px;border-radius:10px}}}}

/* ==================== PREMIUM HERO BACKGROUND SHOWCASE ENGINE (v3.6) ==================== */
/* Smooth cinematic crossfade — product photos stay visible while the text zone keeps full contrast */
.hero-slide-layer {{
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity 1.8s cubic-bezier(0.4, 0, 0.2, 1);
  will-change: opacity;
}}
.hero-slide-layer.is-active {{
  opacity: 1;
}}

/* Slow Ken Burns breathing on the photo layer only (the content layer stays perfectly still) */
.hero-slide-img {{
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  transform: scale(1.04);
  will-change: transform;
}}
.hero-slide-img.play {{
  animation: heroKenBurns 5.5s linear forwards;
}}
@keyframes heroKenBurns {{
  from {{ transform: scale(1.04); }}
  to   {{ transform: scale(1.12); }}
}}

/* Auto-slide progress bar (kept in sync with the 4.5s slide interval in JS) */
.hero-progress-fill {{
  animation: heroProgressFill 4.5s linear forwards;
}}
@keyframes heroProgressFill {{
  from {{ width: 0%; }}
  to   {{ width: 100%; }}
}}

/* Premium CTA shine sweep */
.btn-shine {{
  position: relative;
  overflow: hidden;
}}
.btn-shine::after {{
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  left: -70%;
  width: 45%;
  background: linear-gradient(105deg, transparent, rgba(255, 255, 255, 0.38), transparent);
  transform: skewX(-20deg);
  transition: left 0.7s ease;
  pointer-events: none;
}}
.btn-shine:hover::after {{
  left: 130%;
}}

/* ==================== PREMIUM HERO v3.6 ENHANCEMENTS ==================== */
/* Cinematic golden shimmer on the headline brand line */
.gold-shimmer-text {{
  background: linear-gradient(100deg, #f7e8b6 0%, #f5c76d 18%, #fff6db 36%, #d99a2b 52%, #f7c86b 68%, #fff0c4 82%, #e6aa3a 100%);
  background-size: 220% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: goldShimmerSweep 5.2s linear infinite;
}}
@keyframes goldShimmerSweep {{
  0%   {{ background-position: 0% 0; }}
  100% {{ background-position: -220% 0; }}
}}

/* Cinematic entrance reveal used on hero content blocks */
.hero-entrance {{
  opacity: 0;
  transform: translateY(22px);
  animation: heroEntranceIn 0.9s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}}
.hero-entrance-delay-1 {{ animation-delay: 0.12s; }}
.hero-entrance-delay-2 {{ animation-delay: 0.24s; }}
.hero-entrance-delay-3 {{ animation-delay: 0.36s; }}
.hero-entrance-delay-4 {{ animation-delay: 0.48s; }}
.hero-entrance-delay-5 {{ animation-delay: 0.60s; }}
.hero-entrance-delay-6 {{ animation-delay: 0.72s; }}
@keyframes heroEntranceIn {{
  from {{ opacity: 0; transform: translateY(22px) scale(0.985); }}
  to   {{ opacity: 1; transform: translateY(0) scale(1); }}
}}

/* Animated count-up stats band shine sweep */
.hero-stats-band {{
  position: relative;
}}
.hero-stats-band::before {{
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  pointer-events: none;
  background: linear-gradient(120deg, transparent 0%, rgba(255,255,255,0.07) 42%, rgba(255,222,128,0.16) 50%, transparent 58%);
  background-size: 260% 100%;
  animation: heroStatsSheen 7s ease-in-out infinite;
}}
@keyframes heroStatsSheen {{
  0%   {{ background-position: 120% 0; }}
  55%  {{ background-position: -120% 0; }}
  100% {{ background-position: -120% 0; }}
}}

@media (prefers-reduced-motion: reduce) {{
  .hero-slide-img.play {{ animation: none; }}
  .hero-progress-fill {{ animation: none; width: 100%; }}
  .gold-shimmer-text {{ animation: none; background-position: 0% 0; }}
  .hero-entrance {{ opacity: 1; transform: none; animation: none; }}
  .hero-stats-band::before {{ animation: none; }}
}}

.glow-orb {{
  position: absolute;
  border-radius: 9999px;
  filter: blur(120px);
  pointer-events: none;
  opacity: 0.35;
}}

/* INFINITE AUTO-SLIDING MARQUEE CAROUSEL */
.marquee-container {{
  overflow: hidden;
  position: relative;
  width: 100%;
  padding: 1.5rem 0;
}}

.marquee-track {{
  display: flex;
  gap: 1.5rem;
  width: max-content;
  animation: marqueeSlide 40s linear infinite;
}}

.marquee-container:hover .marquee-track {{
  animation-play-state: paused;
}}

@keyframes marqueeSlide {{
  0% {{ transform: translateX(0); }}
  100% {{ transform: translateX(-50%); }}
}}

/* ULTRA-HIGH-TECH REALISTIC ARCHITECTURAL CAD BLUEPRINT STYLING */
.cad-blueprint-box {{
  background: radial-gradient(circle at 50% 35%, #0a2d48 0%, #031424 65%, #010812 100%);
  border: 1px solid rgba(56, 189, 248, 0.55);
  position: relative;
  overflow: hidden;
  box-shadow: inset 0 0 35px rgba(0, 0, 0, 0.9), 0 10px 25px rgba(2, 132, 199, 0.2);
  transition: all 0.4s ease;
}}

/* Precision Major & Minor Architectural Grid Mesh */
.cad-blueprint-box::before {{
  content: "";
  position: absolute;
  inset: 0;
  background-size: 10px 10px, 40px 40px;
  background-image: 
    linear-gradient(to right, rgba(56, 189, 248, 0.08) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(56, 189, 248, 0.08) 1px, transparent 1px),
    linear-gradient(to right, rgba(56, 189, 248, 0.22) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(56, 189, 248, 0.22) 1px, transparent 1px);
  pointer-events: none;
}}

/* Hover Laser Scanline Sweep Effect */
.cad-blueprint-box::after {{
  content: "";
  position: absolute;
  top: -100%;
  left: 0;
  right: 0;
  height: 100%;
  background: linear-gradient(to bottom, transparent, rgba(56, 189, 248, 0.25), transparent);
  pointer-events: none;
}}

.cad-blueprint-box:hover::after {{
  animation: laserScan 2.5s linear infinite;
}}

@keyframes laserScan {{
  0% {{ top: -100%; }}
  100% {{ top: 100%; }}
}}

/* SVG Line Override for High-Tech CAD Luminescence */
.cad-blueprint-box svg line,
.cad-blueprint-box svg rect,
.cad-blueprint-box svg path,
.cad-blueprint-box svg circle {{
  stroke: #38bdf8 !important;
  stroke-width: 1.8px !important;
  filter: drop-shadow(0 0 3px rgba(56, 189, 248, 0.85));
}}

.cad-blueprint-box svg path[stroke="#b98a2f"],
.cad-blueprint-box svg circle[fill="#b98a2f"],
.cad-blueprint-box svg line[stroke="#b98a2f"] {{
  stroke: #fde047 !important;
  fill: #fde047 !important;
  filter: drop-shadow(0 0 4px rgba(253, 224, 71, 0.95));
}}

.cad-blueprint-box svg rect[fill^="rgba"] {{
  fill: rgba(14, 165, 233, 0.15) !important;
  stroke: #38bdf8 !important;
}}

/* Official Architectural CAD Title Stamp Box */
.cad-title-stamp {{
  position: absolute;
  bottom: 5px;
  right: 5px;
  background: rgba(2, 12, 27, 0.94);
  border: 1px solid rgba(56, 189, 248, 0.6);
  padding: 3px 6px;
  border-radius: 4px;
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
  font-size: 7.5px;
  color: #38bdf8;
  backdrop-filter: blur(8px);
  pointer-events: none;
  z-index: 10;
  box-shadow: 0 4px 12px rgba(0,0,0,0.6);
}}

.cad-art {{
  width: 100%;
  height: 100%;
  max-height: 175px;
  filter: drop-shadow(0 0 10px rgba(56, 189, 248, 0.85)) drop-shadow(0 0 2px rgba(253, 224, 71, 0.5));
}}

/* Corner Bracket Crosshairs */
.corner-bracket {{
  position: absolute;
  width: 14px;
  height: 14px;
  border-color: #38bdf8;
  pointer-events: none;
  z-index: 10;
}}
.cb-tl {{ top: 5px; left: 5px; border-top: 2px solid; border-left: 2px solid; }}
.cb-tr {{ top: 5px; right: 5px; border-top: 2px solid; border-right: 2px solid; }}
.cb-bl {{ bottom: 5px; left: 5px; border-bottom: 2px solid; border-left: 2px solid; }}
.cb-br {{ bottom: 5px; right: 5px; border-bottom: 2px solid; border-right: 2px solid; }}

/* Custom Scrollbar */
::-webkit-scrollbar {{
  width: 8px;
  height: 8px;
}}
::-webkit-scrollbar-track {{
  background: #030712;
}}
::-webkit-scrollbar-thumb {{
  background: #1c2b5e;
  border-radius: 4px;
}}
::-webkit-scrollbar-thumb:hover {{
  background: #10b981;
}}
{PREMIUM_BOOKING_CSS}
</style>

<!-- JSON-LD STRUCTURED DATA SCHEMAS -->
<script type="application/ld+json">
{json.dumps(schema_local_business, ensure_ascii=False, indent=2)}
</script>

<script type="application/ld+json">
{json.dumps(schema_item_list, ensure_ascii=False, indent=2)}
</script>

<script type="application/ld+json">
{json.dumps(schema_faq, ensure_ascii=False, indent=2)}
</script>

<script type="application/ld+json">
{json.dumps(schema_breadcrumbs, ensure_ascii=False, indent=2)}
</script>

</head>

<body class="selection:bg-emerald-500 selection:text-white">

<!-- TOP METALLIC GRADIENT LINE -->
<div class="h-1 bg-gradient-to-r from-emerald-500 via-cyan-400 via-amber-400 to-emerald-500 w-full sticky top-0 z-50"></div>

<!-- TOP NOTIFICATION & WHATSAPP DIRECT BAR -->
<div class="bg-slate-950/95 border-b border-white/10 text-xs text-slate-300 py-2.5 px-3 sm:px-4">
  <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-2 sm:gap-3">
    
    <div class="flex items-center gap-2 sm:gap-4 text-slate-300">
      <span class="flex items-center gap-1.5 font-medium" data-i18n="top_open">
        <span class="inline-block w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
        Workshop Open 7 Days · 9 AM – 7 PM
      </span>
      <span class="hidden md:inline text-slate-700">|</span>
      <a href="https://maps.google.com/?q=26.7118,85.9189" target="_blank" rel="noopener" class="hidden md:flex items-center gap-1.5 text-slate-300 hover:text-emerald-400 transition-colors font-medium group cursor-pointer" title="Click to open Google Maps live directions">
        <span>📍</span> <span data-i18n="top_loc">Murli Chowk (Airport Road), Janakpur Dham-8, Dhanusha</span>
        <span class="text-[9px] bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 px-1.5 py-0.5 rounded font-bold group-hover:bg-emerald-500 group-hover:text-white transition-all">Live GPS 🗺️</span>
      </a>
    </div>

    <div class="flex items-center gap-3 ml-auto sm:ml-0">
      <a href="https://wa.me/{SHOP['whatsapp']}?text=Namaste%20Annapurna%20Aluminium,%20I%20am%20contacting%20you%20from%20your%20website." target="_blank" rel="noopener" class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-emerald-500/10 hover:bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 font-bold transition-all text-xs shadow-sm">
        <span>💬</span> <span>WhatsApp Direct:</span> <span class="font-mono text-white text-xs">+977 9817658719</span>
      </a>
      
      <!-- Dual Language Toggle (EN / नेपाली) -->
      <div class="inline-flex items-center bg-slate-900 rounded-lg p-0.5 border border-white/10 text-xs">
        <button onclick="setLanguage('en')" id="lang-btn-en" class="px-2.5 py-1 rounded-md font-bold bg-emerald-500 text-white transition-all shadow-sm">EN</button>
        <button onclick="setLanguage('ne')" id="lang-btn-ne" class="px-2.5 py-1 rounded-md font-bold text-slate-300 hover:text-white transition-all">नेपाली</button>
      </div>
    </div>

  </div>
</div>

<!-- MAIN STICKY NAVIGATION -->
<header class="glass-nav sticky top-0 z-40 px-3 sm:px-4 py-2.5 sm:py-3 border-b border-white/10 shadow-2xl backdrop-blur-2xl bg-slate-950/90">
  <div class="max-w-7xl mx-auto flex items-center justify-between gap-3">
    
    <!-- Brand Logo -->
    <a href="#" class="flex items-center gap-2.5 sm:gap-3 group" aria-label="Annapurna Aluminium Homepage">
      <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-emerald-500 via-cyan-500 to-amber-500 p-0.5 shadow-lg group-hover:scale-105 transition-transform flex-shrink-0">
        <div class="w-full h-full bg-slate-950 rounded-[10px] flex items-center justify-center">
          <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" aria-hidden="true">
            <rect x="2.4" y="3" width="19.2" height="18" rx="2.8" fill="#fff"/>
            <path d="M2.4 5.8c0-1.55 1.25-2.8 2.8-2.8h13.6c1.55 0 2.8 1.25 2.8 2.8v2.6H2.4V5.8Z" fill="#E52427"/>
            <path d="M2.4 15.6h19.2v2.6c0 1.55-1.25 2.8-2.8 2.8H5.2c-1.55 0-2.8-1.25-2.8-2.8v-2.6Z" fill="#3A519A"/>
            <rect x="6.3" y="9.3" width="11.4" height="4.6" rx="0.8" stroke="#DC2829" stroke-width="1.5"/>
            <path d="M12 9.3v4.6" stroke="#3A519A" stroke-width="1.2"/>
            <path d="M6.3 11.6h11.4" stroke="#3A519A" stroke-width="0.9"/>
          </svg>
        </div>
      </div>
      <div>
        <div class="font-extrabold font-display text-base sm:text-xl tracking-tight flex items-center gap-1.5">
          <span style="background:linear-gradient(90deg,#fde68a,#fbbf24,#34d399);-webkit-background-clip:text;background-clip:text;color:transparent;-webkit-text-fill-color:transparent">ANNAPURNA</span>
          <span class="text-[10px] sm:text-xs px-2 py-0.5 rounded-md bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 font-semibold">ALUMINIUM &amp; UPVC</span>
        </div>
        <p class="text-[10px] sm:text-[11px] text-amber-400/90 font-medium tracking-wide truncate max-w-[200px] sm:max-w-none flex items-center gap-1" data-i18n="nav_subtitle">
          <svg class="w-3 h-3 flex-shrink-0 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>
          <span>Janakpur Dham · Windows, Doors, Glass &amp; Steel Works</span>
        </p>
      </div>
    </a>

    <!-- Desktop Nav Links -->
    <nav class="hidden lg:flex items-center gap-5 xl:gap-6 text-xs font-semibold text-slate-300" aria-label="Main Navigation">
      <a href="#projects" class="hover:text-emerald-400 transition-colors py-1 border-b-2 border-transparent hover:border-emerald-400" data-i18n="nav_projects">Real Projects (40+)</a>
      <a href="#catalog" class="hover:text-emerald-400 transition-colors py-1 border-b-2 border-transparent hover:border-emerald-400" data-i18n="nav_catalog">102+ Design Catalog</a>
      <a href="#workflow" class="hover:text-emerald-400 transition-colors py-1 border-b-2 border-transparent hover:border-emerald-400" data-i18n="nav_workflow">Workflow &amp; Quality</a>
      <a href="#standards" class="hover:text-emerald-400 transition-colors py-1 border-b-2 border-transparent hover:border-emerald-400" data-i18n="nav_standards">Material Specs</a>
      <a href="#booking" class="hover:text-emerald-400 transition-colors py-1 border-b-2 border-transparent hover:border-emerald-400" data-i18n="nav_consult">Book Site Visit</a>
      <a href="#about" class="hover:text-emerald-400 transition-colors py-1 border-b-2 border-transparent hover:border-emerald-400" data-i18n="nav_about">About &amp; Team</a>
      <a href="#faq" class="hover:text-emerald-400 transition-colors py-1 border-b-2 border-transparent hover:border-emerald-400">FAQs</a>
    </nav>

    <!-- Desktop Action Buttons -->
    <div class="hidden sm:flex items-center gap-2">
      <button onclick="toggleChatbot()" class="px-3 py-2 rounded-xl bg-cyan-500/10 hover:bg-cyan-500/20 text-cyan-400 border border-cyan-500/30 text-xs font-bold transition-all flex items-center gap-1.5 shadow-sm">
        <span>🤖</span> <span>AI Assistant</span>
      </button>

      <a href="https://wa.me/{SHOP['whatsapp']}?text=Namaste%20Annapurna%20Aluminium,%20I%20would%20like%20a%20free%20site%20visit%20and%20quotation." target="_blank" rel="noopener" class="px-3.5 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition-all shadow-lg shadow-emerald-600/30 flex items-center gap-1.5">
        <span class="text-sm">💬</span> <span data-i18n="btn_whatsapp">WhatsApp Direct (+977 9817658719)</span>
      </a>
    </div>

    <!-- Mobile Navigation Toggle Button -->
    <button onclick="toggleMobileMenu()" class="lg:hidden px-3 py-2 rounded-xl bg-slate-900/90 text-slate-200 border border-emerald-500/30 hover:bg-slate-800 hover:text-white flex items-center gap-2 shadow-lg transition-all" aria-label="Toggle Mobile Menu">
      <span class="text-xs font-bold uppercase tracking-wider text-emerald-400">Menu</span>
      <svg class="w-5 h-5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M4 6h16M4 12h16M4 18h16"></path></svg>
    </button>

  </div>

  <!-- Mobile Dropdown Navigation Drawer -->
  <div id="mobile-menu" class="hidden lg:hidden mt-3 pt-3 border-t border-white/10 space-y-2.5 text-sm text-slate-300 animate-fadeIn">
    
    <div class="grid grid-cols-2 gap-2">
      <a href="#projects" onclick="toggleMobileMenu()" class="flex items-center gap-2 p-2.5 rounded-xl bg-slate-900/80 hover:bg-emerald-500/20 hover:text-emerald-400 border border-white/5 transition-all text-xs font-bold" data-i18n="nav_projects">
        <span>🖼️</span> <span>Real Projects (40+)</span>
      </a>
      <a href="#catalog" onclick="toggleMobileMenu()" class="flex items-center gap-2 p-2.5 rounded-xl bg-slate-900/80 hover:bg-emerald-500/20 hover:text-emerald-400 border border-white/5 transition-all text-xs font-bold" data-i18n="nav_catalog">
        <span>📐</span> <span>102+ Catalog</span>
      </a>
      <a href="#workflow" onclick="toggleMobileMenu()" class="flex items-center gap-2 p-2.5 rounded-xl bg-slate-900/80 hover:bg-emerald-500/20 hover:text-emerald-400 border border-white/5 transition-all text-xs font-bold" data-i18n="nav_workflow">
        <span>⚡</span> <span>Workflow &amp; Quality</span>
      </a>
      <a href="#standards" onclick="toggleMobileMenu()" class="flex items-center gap-2 p-2.5 rounded-xl bg-slate-900/80 hover:bg-emerald-500/20 hover:text-emerald-400 border border-white/5 transition-all text-xs font-bold" data-i18n="nav_standards">
        <span>🔬</span> <span>Material Specs</span>
      </a>
      <a href="#booking" onclick="toggleMobileMenu()" class="flex items-center gap-2 p-2.5 rounded-xl bg-slate-900/80 hover:bg-emerald-500/20 hover:text-emerald-400 border border-white/5 transition-all text-xs font-bold" data-i18n="nav_consult">
        <span>📅</span> <span>Book Site Visit</span>
      </a>
      <a href="#about" onclick="toggleMobileMenu()" class="flex items-center gap-2 p-2.5 rounded-xl bg-slate-900/80 hover:bg-emerald-500/20 hover:text-emerald-400 border border-white/5 transition-all text-xs font-bold" data-i18n="nav_about">
        <span>🏛️</span> <span>About &amp; Team</span>
      </a>
    </div>

    <a href="#faq" onclick="toggleMobileMenu()" class="flex items-center gap-2 p-2.5 rounded-xl bg-slate-900/80 hover:bg-emerald-500/20 hover:text-emerald-400 border border-white/5 transition-all text-xs font-bold">
      <span>❓</span> <span>Frequently Asked Questions (FAQs)</span>
    </a>
    
    <!-- Direct Action Touch Buttons -->
    <div class="pt-2 grid grid-cols-1 gap-2">
      <button onclick="toggleChatbot(); toggleMobileMenu();" class="w-full py-3 rounded-xl bg-gradient-to-r from-slate-900 to-cyan-950 text-cyan-400 border border-cyan-500/40 font-bold text-xs flex items-center justify-center gap-2 shadow-lg">
        <span>🤖</span> <span>Open Smart AI Architectural Assistant</span>
      </button>

      <a href="https://wa.me/{SHOP['whatsapp']}?text=Namaste%20Annapurna,%20I%20want%20a%20free%20site%20visit%20quotation." target="_blank" class="w-full text-center py-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-extrabold text-xs flex items-center justify-center gap-2 shadow-xl shadow-emerald-600/30">
        <span class="text-base">💬</span> <span>Direct WhatsApp Consultation (+977 9817658719)</span>
      </a>
    </div>

    <!-- Mobile Language & Blueprint Quick Toggles -->
    <div class="pt-2 flex items-center justify-between border-t border-white/10 text-xs">
      <div class="text-slate-400 font-medium">Language:</div>
      <div class="inline-flex items-center bg-slate-900 rounded-lg p-1 border border-white/10">
        <button onclick="setLanguage('en'); toggleMobileMenu();" class="px-3 py-1 rounded-md font-bold bg-emerald-500 text-white">English</button>
        <button onclick="setLanguage('ne'); toggleMobileMenu();" class="px-3 py-1 rounded-md font-bold text-slate-300">नेपाली</button>
      </div>
    </div>

  </div>
</header>

<main>

<!-- HERO SECTION · v3.6 PREMIUM SHOWCASE (Cinematic Crossfade · Gold Shimmer · Entrance Reveal · Count-Up Stats) -->
<section class="relative pt-20 pb-16 sm:pt-28 sm:pb-24 px-4 overflow-hidden min-h-[92vh] flex items-center justify-center">
  
  <!-- HERO BACKGROUND · 2-LAYER CINEMATIC CROSSFADE SHOWCASE -->
  <div id="hero-bg-carousel" class="absolute inset-0 z-0 overflow-hidden pointer-events-none" aria-hidden="true">
    <!-- Background Slide Layer A (photo + slow Ken Burns) -->
    <div id="bg-slide-a" class="hero-slide-layer is-active"><div class="hero-slide-img play"></div></div>
    <!-- Background Slide Layer B -->
    <div id="bg-slide-b" class="hero-slide-layer"><div class="hero-slide-img"></div></div>

    <!-- Managed Visibility Stack: workshop photos stay visible · text zone gets cinematic focus -->
    <div class="absolute inset-0 bg-slate-950/40"></div>
    <div class="absolute inset-0 bg-gradient-to-b from-slate-950/85 via-slate-950/20 to-slate-950"></div>
    <div class="absolute inset-0" style="background:radial-gradient(ellipse 66% 52% at 50% 40%, rgba(2,6,17,0.68) 0%, rgba(2,6,17,0.30) 52%, rgba(2,6,17,0) 78%)"></div>
    <div class="absolute inset-0 bg-[linear-gradient(to_right,#0f172a22_1px,transparent_1px),linear-gradient(to_bottom,#0f172a22_1px,transparent_1px)] bg-[size:3rem_3rem] opacity-30"></div>
  </div>

  <!-- Ambient Glow Orbs -->
  <div class="glow-orb w-[500px] h-[500px] bg-emerald-500/25 -top-24 -left-24 pointer-events-none"></div>
  <div class="glow-orb w-[450px] h-[450px] bg-amber-500/15 top-1/3 -right-24 pointer-events-none"></div>

  <div class="relative z-10 w-full max-w-5xl mx-auto text-center">

    <!-- Live Showcase Ticker · with synced auto-slide progress bar -->
    <div class="hero-entrance hero-entrance-delay-1 inline-flex flex-col max-w-full mb-8 rounded-2xl border border-cyan-400/25 bg-slate-950/70 backdrop-blur-xl overflow-hidden shadow-[0_18px_50px_-12px_rgba(0,0,0,0.8),inset_0_1px_0_rgba(255,255,255,0.06)]">
      <div class="flex items-center gap-2.5 sm:gap-3 px-3.5 sm:px-5 py-2.5">
        <span class="relative flex w-2.5 h-2.5 flex-shrink-0">
          <span class="absolute inline-flex w-full h-full rounded-full bg-emerald-400 opacity-60 animate-ping"></span>
          <span class="relative inline-flex w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
        </span>
        <span class="hidden sm:inline-block text-[10px] font-extrabold uppercase tracking-[0.22em] text-amber-300/90">Live Showcase</span>
        <span id="bg-slide-ticker" class="font-mono text-[11px] sm:text-xs text-cyan-100 truncate">📸 ALW-01 Heavy Duty Sliding Window System</span>
        <span id="bg-slide-counter" class="font-mono text-[10px] sm:text-[11px] font-bold text-amber-300/90 tabular-nums flex-shrink-0">01 / 17</span>
      </div>
      <div class="h-[3px] w-full bg-white/5">
        <div id="bg-slide-progress" class="hero-progress-fill h-full w-0 bg-gradient-to-r from-emerald-400 via-cyan-400 to-amber-300"></div>
      </div>
    </div>

    <!-- Top Verified Pill -->
    <div class="hero-entrance hero-entrance-delay-2 inline-flex items-center gap-2 px-4 py-1.5 rounded-full border border-amber-300/30 bg-slate-950/65 backdrop-blur-md text-amber-200 text-xs sm:text-sm font-semibold mb-7 shadow-lg">
      <svg class="w-4 h-4 text-amber-300 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 8l4.5 3.5L12 4l5.5 7.5L22 8l-2 10a2 2 0 0 1-2 1.6H6a2 2 0 0 1-2-1.6Z"/></svg>
      <span data-i18n="hero_badge">#1 Certified UPVC, Aluminium &amp; SS Fabrication Center · Janakpur Dham, Nepal</span>
    </div>

    <!-- Main Title -->
    <h1 class="hero-entrance hero-entrance-delay-3 text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-black font-display tracking-tight text-white mb-6 leading-[1.06] drop-shadow-[0_4px_28px_rgba(0,0,0,0.65)]">
      <span data-i18n="hero_h1_1">World-Class</span> <br class="hidden sm:inline">
      <span class="gold-shimmer-text" data-i18n="hero_h1_2">UPVC, Aluminium &amp; Glass</span> <br class="hidden sm:inline">
      <span data-i18n="hero_h1_3">Precision Craftsmanship</span>
    </h1>

    <!-- Subtitle -->
    <p class="hero-entrance hero-entrance-delay-4 max-w-2xl mx-auto text-sm sm:text-base md:text-lg text-slate-200/90 leading-relaxed mb-10 [text-shadow:0_1px_14px_rgba(0,0,0,0.85)]" data-i18n="hero_desc">
      102+ Custom Designs manufactured at our Janakpur workshop: German-profile UPVC windows, modern aluminium doors &amp; partitions, SS 304 temple gates, balustrades, modular kitchen racks, and commercial ACP glass facades.
    </p>

    <!-- Action Buttons · Premium -->
    <div class="hero-entrance hero-entrance-delay-5 flex flex-wrap items-center justify-center gap-3.5 sm:gap-4 mb-12">
      <a href="https://wa.me/{SHOP['whatsapp']}?text=Namaste%20Annapurna%20Aluminium,%20I%20want%20to%20consult%20on%20WhatsApp%20for%20a%20project." target="_blank" rel="noopener" class="btn-shine inline-flex items-center gap-2.5 px-7 sm:px-8 py-4 rounded-2xl bg-gradient-to-r from-emerald-500 via-emerald-400 to-teal-500 text-white font-extrabold text-sm sm:text-base shadow-[0_16px_40px_-10px_rgba(16,185,129,0.55),inset_0_1px_0_rgba(255,255,255,0.35)] transition-all duration-300 hover:-translate-y-0.5 hover:shadow-[0_22px_50px_-10px_rgba(16,185,129,0.7)]">
        <span class="w-6 h-6 rounded-full bg-white/20 flex items-center justify-center flex-shrink-0">
          <svg class="w-3.5 h-3.5 fill-white" viewBox="0 0 24 24" aria-hidden="true"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.387.709.282 1.263.45 1.694.59.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
        </span>
        <span data-i18n="hero_btn_whatsapp">WhatsApp Consultation (+977 9817658719)</span>
      </a>

      <button onclick="toggleChatbot()" class="group inline-flex items-center gap-2.5 px-6 sm:px-7 py-4 rounded-2xl border border-cyan-400/30 bg-cyan-500/10 backdrop-blur-xl text-cyan-200 font-bold text-sm sm:text-base shadow-lg transition-all duration-300 hover:-translate-y-0.5 hover:border-cyan-300/60 hover:bg-cyan-500/20 hover:shadow-[0_18px_44px_-12px_rgba(34,211,238,0.45)]">
        <span class="text-lg transition-transform duration-300 group-hover:scale-110">🤖</span>
        <span>Ask AI Assistant</span>
      </button>

      <a href="#catalog" class="group inline-flex items-center gap-2.5 px-6 sm:px-7 py-4 rounded-2xl border border-amber-300/30 bg-amber-400/10 backdrop-blur-xl text-amber-200 font-bold text-sm sm:text-base shadow-lg transition-all duration-300 hover:-translate-y-0.5 hover:border-amber-300/60 hover:bg-amber-400/20 hover:shadow-[0_18px_44px_-12px_rgba(251,191,36,0.4)]">
        <span class="text-lg transition-transform duration-300 group-hover:scale-110">🔥</span>
        <span data-i18n="hero_btn_catalog">Browse 102+ Catalog</span>
      </a>
    </div>

    <!-- Quick Stats · Premium Band -->
    <div class="hero-entrance hero-entrance-delay-6 hero-stats-band max-w-4xl mx-auto rounded-3xl border border-white/10 bg-white/10 shadow-[0_30px_80px_-24px_rgba(0,0,0,0.9)] overflow-hidden grid grid-cols-2 md:grid-cols-4 gap-px backdrop-blur-2xl">
      <div class="bg-slate-950/70 px-4 py-6 sm:py-7 text-center">
        <div class="mx-auto mb-3 w-9 h-9 rounded-xl bg-gradient-to-br from-emerald-500/25 to-emerald-500/5 border border-emerald-400/30 flex items-center justify-center">
          <svg class="w-4 h-4 text-emerald-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg>
        </div>
        <div class="text-3xl md:text-4xl font-black font-display bg-gradient-to-r from-emerald-300 to-teal-300 bg-clip-text text-transparent"><span data-count-target="102" data-count-suffix="+">102+</span></div>
        <div class="mt-1.5 text-[10px] sm:text-[11px] font-bold uppercase tracking-[0.14em] text-slate-400" data-i18n="stat_designs">Unique Custom Designs</div>
      </div>
      <div class="bg-slate-950/70 px-4 py-6 sm:py-7 text-center">
        <div class="mx-auto mb-3 w-9 h-9 rounded-xl bg-gradient-to-br from-amber-500/25 to-amber-500/5 border border-amber-400/30 flex items-center justify-center">
          <svg class="w-4 h-4 text-amber-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 21h18"/><path d="M5 21V7l7-4 7 4v14"/><path d="M9 21v-4h6v4"/><path d="M9 10h.01M15 10h.01M9 13h.01M15 13h.01"/></svg>
        </div>
        <div class="text-3xl md:text-4xl font-black font-display bg-gradient-to-r from-amber-300 to-orange-300 bg-clip-text text-transparent"><span data-count-target="40" data-count-suffix="+">40+</span></div>
        <div class="mt-1.5 text-[10px] sm:text-[11px] font-bold uppercase tracking-[0.14em] text-slate-400" data-i18n="stat_sites">Real Workshop Projects</div>
      </div>
      <div class="bg-slate-950/70 px-4 py-6 sm:py-7 text-center">
        <div class="mx-auto mb-3 w-9 h-9 rounded-xl bg-gradient-to-br from-cyan-500/25 to-cyan-500/5 border border-cyan-400/30 flex items-center justify-center">
          <svg class="w-4 h-4 text-cyan-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/></svg>
        </div>
        <div class="text-3xl md:text-4xl font-black font-display bg-gradient-to-r from-cyan-300 to-sky-300 bg-clip-text text-transparent"><span data-count-target="100" data-count-suffix="%">100%</span></div>
        <div class="mt-1.5 text-[10px] sm:text-[11px] font-bold uppercase tracking-[0.14em] text-slate-400" data-i18n="stat_quality">SS 304 Rust-Free Guarantee</div>
      </div>
      <div class="bg-slate-950/70 px-4 py-6 sm:py-7 text-center">
        <div class="mx-auto mb-3 w-9 h-9 rounded-xl bg-gradient-to-br from-violet-500/25 to-violet-500/5 border border-violet-400/30 flex items-center justify-center">
          <svg class="w-4 h-4 text-violet-300" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="8" r="6"/><path d="M15.5 13 17 22l-5-3-5 3 1.5-9"/></svg>
        </div>
        <div class="text-3xl md:text-4xl font-black font-display bg-gradient-to-r from-violet-300 to-fuchsia-300 bg-clip-text text-transparent"><span data-count-target="15" data-count-suffix="+ Yrs">15+ Yrs</span></div>
        <div class="mt-1.5 text-[10px] sm:text-[11px] font-bold uppercase tracking-[0.14em] text-slate-400" data-i18n="stat_exp">Engineering Craftsmanship</div>
      </div>
    </div>

    <!-- Scroll Cue -->
    <a href="#projects" class="hero-entrance hero-entrance-delay-6 mt-12 inline-flex flex-col items-center gap-1.5 text-slate-400 hover:text-amber-300 transition-colors">
      <span class="text-[10px] font-bold uppercase tracking-[0.2em]">Explore Real Projects</span>
      <svg class="w-5 h-5 animate-bounce" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>
    </a>

  </div>
</section>


<!-- SECTION: AUTOMATIC INFINITE PRODUCT & PROJECT SLIDING CAROUSEL -->
<section class="py-6 border-t border-b border-white/10 bg-slate-950/80 overflow-hidden relative z-10">
  <div class="max-w-7xl mx-auto px-4 mb-3 flex items-center justify-between">
    <div class="text-xs font-bold uppercase tracking-wider text-emerald-400 flex items-center gap-2">
      <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
      <span>Live Workshop Showcase · Automatic Showcase Carousel</span>
    </div>
    <span class="text-[11px] text-slate-400 italic hidden sm:inline">(Hover mouse over cards to pause auto-slide)</span>
  </div>

  <div class="marquee-container">
    <div class="marquee-track" id="auto-marquee-track">
      <!-- Populated automatically via JS -->
    </div>
  </div>
</section>

<!-- SECTION: 4-STEP PRECISION WORKFLOW -->
<section id="workflow" class="py-16 px-4 relative z-10 bg-slate-950/60">
  <div class="max-w-7xl mx-auto">
    
    <div class="text-center mb-12">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-bold uppercase tracking-wider mb-3">
        ⚡ Precision Engineering
      </div>
      <h2 class="text-2xl sm:text-4xl font-extrabold font-display text-white mb-3" data-i18n="workflow_title">
        Our 4-Step Precision Fabrication Workflow
      </h2>
      <p class="text-xs sm:text-sm text-slate-300 max-w-2xl mx-auto" data-i18n="workflow_subtitle">
        From free site visit and 3D design to precision laser fabrication and lifetime on-site fitting.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      
      <!-- Step 1 -->
      <div class="glass-card p-6 rounded-2xl relative">
        <div class="w-10 h-10 rounded-xl bg-emerald-500/20 text-emerald-400 font-black flex items-center justify-center text-sm border border-emerald-500/40 mb-4">
          01
        </div>
        <h3 class="font-bold text-lg text-white mb-2" data-i18n="wf_s1_t">Free Site Measurement</h3>
        <p class="text-xs text-slate-300 leading-relaxed" data-i18n="wf_s1_d">
          Master engineer visits your building with laser distance meters and real metal/glass profile samples.
        </p>
      </div>

      <!-- Step 2 -->
      <div class="glass-card p-6 rounded-2xl relative">
        <div class="w-10 h-10 rounded-xl bg-amber-500/20 text-amber-400 font-black flex items-center justify-center text-sm border border-amber-500/40 mb-4">
          02
        </div>
        <h3 class="font-bold text-lg text-white mb-2" data-i18n="wf_s2_t">3D CAD &amp; Vector Blueprint</h3>
        <p class="text-xs text-slate-300 leading-relaxed" data-i18n="wf_s2_d">
          Custom technical drawing generated for your approval with exact millimeter glass and aluminum specs.
        </p>
      </div>

      <!-- Step 3 -->
      <div class="glass-card p-6 rounded-2xl relative">
        <div class="w-10 h-10 rounded-xl bg-cyan-500/20 text-cyan-400 font-black flex items-center justify-center text-sm border border-cyan-500/40 mb-4">
          03
        </div>
        <h3 class="font-bold text-lg text-white mb-2" data-i18n="wf_s3_t">Workshop CNC Fabrication</h3>
        <p class="text-xs text-slate-300 leading-relaxed" data-i18n="wf_s3_d">
          Precision miter cutting, argon TIG welding, powder coating, and EPDM weather-seal assembly at Murli Chowk.
        </p>
      </div>

      <!-- Step 4 -->
      <div class="glass-card p-6 rounded-2xl relative">
        <div class="w-10 h-10 rounded-xl bg-indigo-500/20 text-indigo-400 font-black flex items-center justify-center text-sm border border-indigo-500/40 mb-4">
          04
        </div>
        <h3 class="font-bold text-lg text-white mb-2" data-i18n="wf_s4_t">On-Site Expert Fitting</h3>
        <p class="text-xs text-slate-300 leading-relaxed" data-i18n="wf_s4_d">
          Fast, clean installation by experienced technicians with weatherproofing and 10-year quality guarantee.
        </p>
      </div>

    </div>

  </div>
</section>

<!-- SECTION: REAL WORKSHOP PROJECTS GALLERY (40+) -->
<section id="projects" class="py-16 px-4 relative z-10 border-t border-white/5">
  <div class="max-w-7xl mx-auto">
    
    <div class="flex flex-col md:flex-row md:items-end justify-between mb-10 gap-4">
      <div>
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-bold uppercase tracking-wider mb-2">
          📸 authentic workshop gallery
        </div>
        <h2 class="text-2xl sm:text-4xl font-extrabold font-display text-white" data-i18n="projects_title">
          Real Projects Fabricated in Janakpur
        </h2>
        <p class="text-xs sm:text-sm text-slate-300 mt-2 max-w-2xl" data-i18n="projects_subtitle">
          Explore actual completed commercial facades, temple gates, modern residences, staircases, and modular kitchens fabricated right here at our Murli Chowk workshop.
        </p>
      </div>

      <!-- Filter Tabs -->
      <div class="flex flex-wrap gap-1.5 bg-slate-900/90 p-1.5 rounded-2xl border border-white/10" id="project-filter-pills">
        <button onclick="filterRealProjects('all')" data-pfilter="all" class="proj-pill px-3 py-1.5 rounded-xl text-xs font-bold bg-emerald-500 text-white shadow-md">All (26)</button>
        <button onclick="filterRealProjects('STF')" data-pfilter="STF" class="proj-pill px-3 py-1.5 rounded-xl text-xs font-bold text-slate-300 hover:text-white">Facades</button>
        <button onclick="filterRealProjects('UWC')" data-pfilter="UWC" class="proj-pill px-3 py-1.5 rounded-xl text-xs font-bold text-slate-300 hover:text-white">UPVC Windows</button>
        <button onclick="filterRealProjects('SLS')" data-pfilter="SLS" class="proj-pill px-3 py-1.5 rounded-xl text-xs font-bold text-slate-300 hover:text-white">SS Railings</button>
        <button onclick="filterRealProjects('MST')" data-pfilter="MST" class="proj-pill px-3 py-1.5 rounded-xl text-xs font-bold text-slate-300 hover:text-white">Temple Gates</button>
        <button onclick="filterRealProjects('MOD')" data-pfilter="MOD" class="proj-pill px-3 py-1.5 rounded-xl text-xs font-bold text-slate-300 hover:text-white">Kitchen Racks</button>
      </div>
    </div>

    <!-- Projects Grid -->
    <div id="real-projects-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
      <!-- Dynamically rendered via JS -->
    </div>

  </div>
</section>

<!-- SECTION: 102+ PRODUCT CATALOG EXPLORER (WITH ULTRA-LUXURY CAD BLUEPRINT) -->
<section id="catalog" class="py-16 px-4 relative z-10 bg-slate-950/40 border-t border-white/5">
  <div class="max-w-7xl mx-auto">
    
    <div class="text-center mb-10">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-400 text-xs font-bold uppercase tracking-wider mb-2">
        📦 Complete Product Archive
      </div>
      <h2 class="text-2xl sm:text-4xl font-extrabold font-display text-white mb-2" data-i18n="catalog_title">
        102+ Master Product Designs
      </h2>
      <p class="text-xs sm:text-sm text-slate-300 max-w-2xl mx-auto" data-i18n="catalog_subtitle">
        Every product is precision-engineered, customizable to your exact structural measurements, and available in multiple finishes and glass configurations.
      </p>
    </div>

    <!-- Search & Controls Bar -->
    <div class="glass-panel p-4 rounded-2xl mb-8 flex flex-col md:flex-row items-center justify-between gap-4">
      
      <!-- Instant Search Input -->
      <div class="relative w-full md:w-96">
        <span class="absolute inset-y-0 left-0 flex items-center pl-3 text-slate-400">🔍</span>
        <input type="text" id="catalog-search" oninput="handleCatalogSearch()" placeholder="Search 102+ designs (e.g. sliding, gate, kitchen)..." class="w-full pl-9 pr-8 py-2.5 rounded-xl bg-slate-900 border border-white/10 text-white text-xs focus:border-emerald-400 focus:outline-none placeholder-slate-500">
        <button id="clear-search-btn" onclick="clearCatalogSearch()" class="hidden absolute inset-y-0 right-0 pr-3 flex items-center text-slate-400 hover:text-white">✕</button>
      </div>

      <!-- View Counter Badge -->
      <div class="text-xs text-emerald-400 font-mono font-bold" id="catalog-count">
        Showing 102 of 102 Designs
      </div>

      <!-- View Switcher (Real Photo vs Ultra CAD Blueprint Mode) -->
      <div class="flex items-center gap-2 bg-slate-900 p-1 rounded-xl border border-white/10 text-xs font-bold">
        <span class="text-slate-400 px-2" data-i18n="catalog_view_mode">View Mode:</span>
        <button id="view-mode-photo" onclick="setCatalogViewMode('photo')" class="px-3 py-1.5 rounded-lg bg-emerald-500 text-white transition-all flex items-center gap-1.5">
          <span>📸</span> <span data-i18n="view_photo">Photos</span>
        </button>
        <button id="view-mode-blueprint" onclick="setCatalogViewMode('blueprint')" class="px-3 py-1.5 rounded-lg text-slate-400 hover:text-white transition-all flex items-center gap-1.5">
          <span>📐</span> <span data-i18n="view_blueprint">CAD Blueprint</span>
        </button>
      </div>

    </div>

    <!-- Category Filter Tabs -->
    <div class="flex items-center gap-2 overflow-x-auto pb-4 mb-8 no-scrollbar" id="catalog-category-pills">
      <!-- Generated via JS -->
    </div>

    <!-- Catalog Grid -->
    <div id="catalog-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
      <!-- Generated via JS -->
    </div>

  </div>
</section>

<!-- SECTION: MATERIAL STANDARDS & QUALITY MATRIX -->
<section id="standards" class="py-16 px-4 relative z-10 border-t border-white/5">
  <div class="max-w-7xl mx-auto">
    
    <div class="text-center mb-12">
      <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 text-xs font-bold uppercase tracking-wider mb-2">
        🔬 Engineering Excellence
      </div>
      <h2 class="text-2xl sm:text-4xl font-extrabold font-display text-white mb-3" data-i18n="factory_title">
        Factory Machinery &amp; Raw Material Quality
      </h2>
      <p class="text-xs sm:text-sm text-slate-300 max-w-2xl mx-auto" data-i18n="factory_subtitle">
        We never compromise on metal thickness, uPVC wall gauge, or welding standards. Here is how we ensure lifetime durability.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      
      <!-- Feature 1 -->
      <div class="glass-card p-6 rounded-2xl">
        <div class="w-12 h-12 rounded-xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center text-2xl font-black mb-4">
          ❄️
        </div>
        <h3 class="text-lg font-bold text-white mb-2" data-i18n="mat_1_title">German Multi-Chamber UPVC</h3>
        <p class="text-xs text-slate-300 leading-relaxed" data-i18n="mat_1_desc">
          Multi-cavity internal chambers trap air pockets for maximum thermal &amp; sound insulation. Reinforced with galvanized steel inserts to prevent frame distortion in hot Janakpur summers.
        </p>
      </div>

      <!-- Feature 2 -->
      <div class="glass-card p-6 rounded-2xl">
        <div class="w-12 h-12 rounded-xl bg-amber-500/20 text-amber-400 flex items-center justify-center text-2xl font-black mb-4">
          🛡️
        </div>
        <h3 class="text-lg font-bold text-white mb-2" data-i18n="mat_2_title">Virgin 6063-T5 Aluminium Alloy</h3>
        <p class="text-xs text-slate-300 leading-relaxed" data-i18n="mat_2_desc">
          Manufactured using high-strength architectural aluminium alloy with 60-80 micron electro-powder coating that withstands harsh sun, monsoons, and everyday impacts.
        </p>
      </div>

      <!-- Feature 3 -->
      <div class="glass-card p-6 rounded-2xl">
        <div class="w-12 h-12 rounded-xl bg-cyan-500/20 text-cyan-400 flex items-center justify-center text-2xl font-black mb-4">
          ✨
        </div>
        <h3 class="text-lg font-bold text-white mb-2" data-i18n="mat_3_title">Authentic SS 304 Rust-Free Steel</h3>
        <p class="text-xs text-slate-300 leading-relaxed" data-i18n="mat_3_desc">
          Every stainless steel railing, temple gate, and staircase pillar is crafted from genuine SS 304 with full nickel content, assembled with inert gas TIG welding and diamond compound polishing.
        </p>
      </div>

    </div>

  </div>
</section>

{PREMIUM_BOOKING_HTML}

<!-- SECTION: FOUNDER & ABOUT US -->
<section id="about" class="py-16 px-4 relative z-10 border-t border-white/5">
  <div class="max-w-6xl mx-auto">
    
    <div class="glass-card p-8 rounded-3xl">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 items-center">
        
        <!-- Founder Photo — v3.3 professional portrait with gold gradient glow frame -->
        <div class="relative group">
          <div class="absolute -inset-1 rounded-[1.4rem] bg-gradient-to-br from-amber-300 via-emerald-400 to-cyan-400 opacity-45 blur-lg group-hover:opacity-70 transition-opacity duration-500 pointer-events-none"></div>
          <div class="relative rounded-2xl p-[2px] bg-gradient-to-br from-amber-300 via-amber-500 to-emerald-400 shadow-2xl">
            <div class="relative rounded-[14px] overflow-hidden bg-slate-950">
              <img src="uploads/owner_professional.jpg" alt="Prof. Nageshwar Thakur — Founder &amp; Master Fabricator, Annapurna Aluminium &amp; UPVC Udhyog, Janakpur Dham" class="w-full h-96 object-cover object-top group-hover:scale-105 transition-transform duration-500" loading="lazy" width="892" height="1200">
              <div class="absolute inset-0 bg-gradient-to-t from-slate-950/85 via-transparent to-transparent pointer-events-none"></div>

              <!-- Verified Badge -->
              <div class="absolute top-3 right-3 flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-slate-950/85 backdrop-blur-md border border-cyan-400/45 shadow-lg">
                <svg class="w-3.5 h-3.5 text-cyan-400" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 1.6l2.47 1.8 3.05-.03 .93 2.9 2.48 1.77-.97 2.9.97 2.9-2.48 1.77-.93 2.9-3.05-.03L12 22.4l-2.47-1.8-3.05.03-.93-2.9L3.07 15.96l.97-2.9-.97-2.9 2.48-1.77.93-2.9 3.05.03L12 1.6Zm-1.1 13.4l5.2-5.2-1.42-1.42-3.78 3.79-1.78-1.79L7.7 11.8l3.2 3.2Z"/></svg>
                <span class="text-[10px] font-extrabold uppercase tracking-wider text-cyan-300">Verified</span>
              </div>

              <!-- Name Plate -->
              <div class="absolute bottom-3 left-3 right-3 p-3 rounded-xl bg-slate-950/88 backdrop-blur-md border border-white/12 shadow-lg">
                <div class="font-bold text-white text-base leading-tight">{SHOP['owner_name']}</div>
                <div class="text-xs font-medium mt-0.5" style="background:linear-gradient(90deg,#fde68a,#fbbf24,#34d399);-webkit-background-clip:text;background-clip:text;color:transparent;-webkit-text-fill-color:transparent" data-i18n="about_tag">Founder &amp; Master Fabricator</div>
                <div class="mt-1.5 inline-flex items-center gap-1 px-2 py-0.5 rounded-md bg-emerald-500/15 border border-emerald-500/30 text-[10px] font-extrabold uppercase tracking-wider text-emerald-300">15+ Yrs</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Founder Bio -->
        <div class="md:col-span-2 space-y-4">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 text-emerald-400 text-xs font-bold uppercase tracking-wider">
            🏛️ Heritage &amp; Precision
          </div>
          
          <h2 class="text-2xl sm:text-3xl font-extrabold font-display text-white">
            Annapurna Aluminium &amp; UPVC Udhyog
          </h2>

          <p class="text-xs sm:text-sm text-slate-300 leading-relaxed italic border-l-2 border-emerald-400 pl-4 py-1" data-i18n="about_bio_1">
            "We started Annapurna Aluminium &amp; UPVC in Janakpur Dham with a singular mission: to deliver European-grade window insulation, modern aluminium elegance, and unyielding steel security at direct factory prices to every home and enterprise in Nepal."
          </p>

          <p class="text-xs sm:text-sm text-slate-300 leading-relaxed" data-i18n="about_bio_2">
            From the sacred doors of Sri Nav Durga Mandir Duhaba to commercial plazas across Madhesh Province, our team of seasoned craftsmen takes personal pride in every single weld, miter cut, and glass installation.
          </p>

          <div class="pt-2 flex flex-wrap gap-4 text-xs font-semibold text-slate-300">
            <div class="flex items-center gap-1.5 text-cyan-400">
              <span>📍 Location:</span> <span class="text-white">{SHOP['address_short']}</span>
            </div>
            <a href="https://wa.me/{SHOP['whatsapp']}?text=Namaste%20Prof.%20Nageshwar%20Thakur,%20I%20want%20to%20consult%20you%20regarding%20a%20project." target="_blank" class="flex items-center gap-1.5 text-emerald-400 hover:underline">
              <span>💬 Direct WhatsApp:</span> <span class="text-white font-mono">+977 9817658719</span>
            </a>
          </div>

        </div>

      </div>
    </div>

    <!-- Workshop Board Showcase — authentic shop signage -->
    <div class="mt-8 glass-card rounded-3xl overflow-hidden">
      <div class="p-6 sm:p-7 flex flex-wrap items-center justify-between gap-3">
        <div class="flex items-center gap-3">
          <span class="w-10 h-10 rounded-xl bg-gradient-to-br from-red-600 to-blue-900 flex items-center justify-center shadow-lg flex-shrink-0">
            <svg class="w-5 h-5 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 2 3 7v13a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V7l-3-5Z"/><path d="M3 7h18"/><path d="M16 11a4 4 0 0 1-8 0"/></svg>
          </span>
          <div>
            <h3 class="font-bold text-white text-base sm:text-lg leading-tight" data-i18n="board_title">Our Workshop — Murli Chowk, Janakpur Dham-8</h3>
            <p class="text-[11px] sm:text-xs text-slate-400 mt-0.5" data-i18n="board_sub">On the Airport Road · Open 9:00 AM – 7:00 PM, all 7 days</p>
          </div>
        </div>
        <a href="https://maps.google.com/?q=Murli+Chowk+Airport+Road+Janakpur+Nepal" target="_blank" rel="noopener" class="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-lg bg-cyan-500/15 border border-cyan-400/30 text-cyan-300 text-xs font-bold hover:bg-cyan-500/25 transition-colors">
          <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>
          <span data-i18n="board_directions">Get Directions</span>
        </a>
      </div>
      <div class="px-4 sm:px-6 pb-5 sm:pb-6">
        <div class="relative rounded-xl overflow-hidden border border-white/12 shadow-2xl ring-1 ring-white/10 bg-slate-950">
          <img src="catalog_assets/board_final.png" alt="Annapurna Aluminium &amp; UPVC shop board — Janakpur Dham-8, Murli Chowk (Airport Road)" width="1169" height="220" loading="lazy" class="w-full h-auto block">
        </div>
        <p class="text-[11px] sm:text-xs text-slate-400 mt-3.5 leading-relaxed" data-i18n="board_note"><span class="text-slate-300">“यहाँ आल्मुनियम र UPVC को झ्याल, ढोका, पार्टिसन, किचन रैक तथा स्टील रेलिङको काम गरिन्छ।”</span> — Aluminium &amp; UPVC windows, doors, partitions, kitchen racks and steel railing work, all under one roof.</p>
      </div>
    </div>

  </div>
</section>

<!-- SECTION: FAQ ACCORDION -->
<section id="faq" class="py-16 px-4 relative z-10 bg-slate-950/60 border-t border-white/5">
  <div class="max-w-4xl mx-auto">
    
    <div class="text-center mb-10">
      <h2 class="text-2xl sm:text-4xl font-extrabold font-display text-white mb-2" data-i18n="faq_title">
        Got Questions? We Have Answers.
      </h2>
    </div>

    <div class="space-y-4">
      
      <!-- FAQ 1 -->
      <div class="glass-card rounded-2xl overflow-hidden">
        <button onclick="toggleFaq(1)" class="w-full p-5 text-left font-bold text-sm sm:text-base text-white flex items-center justify-between gap-4">
          <span data-i18n="faq_q1">How can I get an exact price quote for my house or commercial building?</span>
          <span id="faq-icon-1" class="text-emerald-400 font-mono text-xl">+</span>
        </button>
        <div id="faq-content-1" class="hidden p-5 pt-0 text-xs sm:text-sm text-slate-300 leading-relaxed border-t border-white/5" data-i18n="faq_a1">
          Simply message us directly on WhatsApp at <strong>+977 9817658719</strong> with your rough room window/door dimensions or architectural floor plan. If you are in Janakpur Dham, Dhanusha, or nearby districts, our engineer will visit your site directly for free measurement.
        </div>
      </div>

      <!-- FAQ 2 -->
      <div class="glass-card rounded-2xl overflow-hidden">
        <button onclick="toggleFaq(2)" class="w-full p-5 text-left font-bold text-sm sm:text-base text-white flex items-center justify-between gap-4">
          <span data-i18n="faq_q2">What is the price of UPVC windows in Nepal?</span>
          <span id="faq-icon-2" class="text-emerald-400 font-mono text-xl">+</span>
        </button>
        <div id="faq-content-2" class="hidden p-5 pt-0 text-xs sm:text-sm text-slate-300 leading-relaxed border-t border-white/5" data-i18n="faq_a2">
          UPVC window pricing depends on track configuration (2-track vs 3-track with mesh), profile grade (multi-chamber German profile), and glass selection (single float, tinted reflective, or insulated double glazing). We offer the most competitive factory-direct rates in Nepal starting from NRs 450 - 850 per sq.ft.
        </div>
      </div>

      <!-- FAQ 3 -->
      <div class="glass-card rounded-2xl overflow-hidden">
        <button onclick="toggleFaq(3)" class="w-full p-5 text-left font-bold text-sm sm:text-base text-white flex items-center justify-between gap-4">
          <span data-i18n="faq_q3">Which is better for home bedrooms: UPVC or Aluminium?</span>
          <span id="faq-icon-3" class="text-emerald-400 font-mono text-xl">+</span>
        </button>
        <div id="faq-content-3" class="hidden p-5 pt-0 text-xs sm:text-sm text-slate-300 leading-relaxed border-t border-white/5" data-i18n="faq_a3">
          For residential bedrooms and living rooms, <strong>UPVC with double glazing</strong> is the best choice because it blocks outdoor traffic noise and maintains cooler room temperatures during summer heat. Aluminium is best for large commercial storefronts, slim partitions, and high-impact structural portals.
        </div>
      </div>

      <!-- FAQ 4 -->
      <div class="glass-card rounded-2xl overflow-hidden">
        <button onclick="toggleFaq(4)" class="w-full p-5 text-left font-bold text-sm sm:text-base text-white flex items-center justify-between gap-4">
          <span data-i18n="faq_q4">How do modular aluminium kitchen racks prevent termites and water damage?</span>
          <span id="faq-icon-4" class="text-emerald-400 font-mono text-xl">+</span>
        </button>
        <div id="faq-content-4" class="hidden p-5 pt-0 text-xs sm:text-sm text-slate-300 leading-relaxed border-t border-white/5" data-i18n="faq_a4">
          Unlike plywood or MDF boards that swell, warp, and get infested with termites in humid kitchens, our modular racks use 100% anodized architectural aluminium framing and waterproof aluminium composite panels (ACP) that can be washed directly with water without any damage.
        </div>
      </div>

      <!-- FAQ 5 -->
      <div class="glass-card rounded-2xl overflow-hidden">
        <button onclick="toggleFaq(5)" class="w-full p-5 text-left font-bold text-sm sm:text-base text-white flex items-center justify-between gap-4">
          <span data-i18n="faq_q5">How long does manufacturing and installation take?</span>
          <span id="faq-icon-5" class="text-emerald-400 font-mono text-xl">+</span>
        </button>
        <div id="faq-content-5" class="hidden p-5 pt-0 text-xs sm:text-sm text-slate-300 leading-relaxed border-t border-white/5" data-i18n="faq_a5">
          Standard residential window and door orders are completed in <strong>3 to 5 business days</strong>. Commercial facade glazing, large temple gates, and custom modular kitchens are scheduled as per site milestones with prompt delivery.
        </div>
      </div>

    </div>

  </div>
</section>

</main>

<!-- FOOTER -->
<footer class="relative bg-slate-950 border-t border-white/10 py-12 px-4 text-xs text-slate-400">
  <!-- Gradient glow line -->
  <div class="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-emerald-400/70 to-transparent"></div>
  <div class="absolute top-0 left-1/2 -translate-x-1/2 w-1/2 h-16 bg-emerald-500/10 blur-3xl pointer-events-none"></div>

  <div class="relative max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">

    <!-- Brand -->
    <div class="space-y-3">
      <div class="flex items-center gap-2.5">
        <div class="w-11 h-11 rounded-xl bg-gradient-to-br from-emerald-500 via-cyan-500 to-amber-500 p-0.5 shadow-lg flex-shrink-0">
          <div class="w-full h-full bg-slate-950 rounded-[10px] flex items-center justify-center">
            <svg class="w-7 h-7" viewBox="0 0 24 24" fill="none" aria-hidden="true">
              <rect x="2.4" y="3" width="19.2" height="18" rx="2.8" fill="#fff"/>
              <path d="M2.4 5.8c0-1.55 1.25-2.8 2.8-2.8h13.6c1.55 0 2.8 1.25 2.8 2.8v2.6H2.4V5.8Z" fill="#E52427"/>
              <path d="M2.4 15.6h19.2v2.6c0 1.55-1.25 2.8-2.8 2.8H5.2c-1.55 0-2.8-1.25-2.8-2.8v-2.6Z" fill="#3A519A"/>
              <rect x="6.3" y="9.3" width="11.4" height="4.6" rx="0.8" stroke="#DC2829" stroke-width="1.5"/>
              <path d="M12 9.3v4.6" stroke="#3A519A" stroke-width="1.2"/>
              <path d="M6.3 11.6h11.4" stroke="#3A519A" stroke-width="0.9"/>
            </svg>
          </div>
        </div>
        <div>
          <div class="font-extrabold font-display text-base tracking-tight leading-none" style="background:linear-gradient(90deg,#fde68a,#fbbf24,#34d399);-webkit-background-clip:text;background-clip:text;color:transparent;-webkit-text-fill-color:transparent">ANNAPURNA</div>
          <div class="text-[10px] font-semibold uppercase tracking-[0.16em] text-emerald-400/90 mt-1">Aluminium &amp; UPVC Udhyog</div>
        </div>
      </div>
      <p class="leading-relaxed">
        Premier architectural fabrication center in Janakpur Dham, Nepal. Specializing in soundproof UPVC windows, toughened glass balustrades, SS 304 temple gates, and modular kitchens.
      </p>
    </div>

    <!-- Quick Links -->
    <div>
      <div class="flex items-center gap-2 mb-3">
        <span class="w-6 h-6 rounded-md bg-emerald-500/12 border border-emerald-500/25 flex items-center justify-center flex-shrink-0"><svg class="w-3.5 h-3.5 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg></span>
        <span class="font-bold text-white text-xs uppercase tracking-wider">Quick Navigation</span>
      </div>
      <ul class="space-y-2">
        <li><a href="#projects" class="hover:text-white transition-colors">40+ Real Projects Gallery</a></li>
        <li><a href="#catalog" class="hover:text-white transition-colors">102+ Product Catalog</a></li>
        <li><a href="#workflow" class="hover:text-white transition-colors">Precision Workflow</a></li>
        <li><a href="#booking" class="hover:text-white transition-colors">Book Free Site Visit</a></li>
        <li><a href="#about" class="hover:text-white transition-colors">Founder &amp; Workshop</a></li>
      </ul>
    </div>

    <!-- Service Areas -->
    <div>
      <div class="flex items-center gap-2 mb-3">
        <span class="w-6 h-6 rounded-md bg-emerald-500/12 border border-emerald-500/25 flex items-center justify-center flex-shrink-0"><svg class="w-3.5 h-3.5 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg></span>
        <span class="font-bold text-white text-xs uppercase tracking-wider">Service Areas</span>
      </div>
      <div class="flex flex-wrap gap-1.5">
        <span class="px-2 py-0.5 rounded-md bg-slate-900/80 border border-white/10 text-[10px] font-semibold text-slate-300 hover:border-emerald-400/45 hover:text-emerald-300 transition-colors">Janakpur Dham</span>
        <span class="px-2 py-0.5 rounded-md bg-slate-900/80 border border-white/10 text-[10px] font-semibold text-slate-300 hover:border-emerald-400/45 hover:text-emerald-300 transition-colors">Dhanusha</span>
        <span class="px-2 py-0.5 rounded-md bg-slate-900/80 border border-white/10 text-[10px] font-semibold text-slate-300 hover:border-emerald-400/45 hover:text-emerald-300 transition-colors">Jaleshwor</span>
        <span class="px-2 py-0.5 rounded-md bg-slate-900/80 border border-white/10 text-[10px] font-semibold text-slate-300 hover:border-emerald-400/45 hover:text-emerald-300 transition-colors">Malangwa</span>
        <span class="px-2 py-0.5 rounded-md bg-slate-900/80 border border-white/10 text-[10px] font-semibold text-slate-300 hover:border-emerald-400/45 hover:text-emerald-300 transition-colors">Lahan</span>
        <span class="px-2 py-0.5 rounded-md bg-slate-900/80 border border-white/10 text-[10px] font-semibold text-slate-300 hover:border-emerald-400/45 hover:text-emerald-300 transition-colors">Bardibas</span>
        <span class="px-2 py-0.5 rounded-md bg-slate-900/80 border border-white/10 text-[10px] font-semibold text-slate-300 hover:border-emerald-400/45 hover:text-emerald-300 transition-colors">Rajbiraj</span>
        <span class="px-2 py-0.5 rounded-md bg-slate-900/80 border border-white/10 text-[10px] font-semibold text-slate-300 hover:border-emerald-400/45 hover:text-emerald-300 transition-colors">Birgunj</span>
        <span class="px-2 py-0.5 rounded-md bg-slate-900/80 border border-white/10 text-[10px] font-semibold text-slate-300 hover:border-emerald-400/45 hover:text-emerald-300 transition-colors">Hetauda</span>
        <span class="px-2 py-0.5 rounded-md bg-slate-900/80 border border-white/10 text-[10px] font-semibold text-slate-300 hover:border-emerald-400/45 hover:text-emerald-300 transition-colors">Kathmandu</span>
        <span class="px-2 py-0.5 rounded-md bg-slate-900/80 border border-white/10 text-[10px] font-semibold text-slate-300 hover:border-emerald-400/45 hover:text-emerald-300 transition-colors">All Nepal</span>
      </div>
    </div>

    <!-- Contact Summary & Live GPS Map -->
    <div>
      <div class="flex items-center gap-2 mb-3">
        <span class="w-6 h-6 rounded-md bg-emerald-500/12 border border-emerald-500/25 flex items-center justify-center flex-shrink-0"><svg class="w-3.5 h-3.5 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2Z"/></svg></span>
        <span class="font-bold text-white text-xs uppercase tracking-wider">Live Location &amp; Contact</span>
      </div>
      <a href="https://maps.google.com/?q=26.7118,85.9189" target="_blank" rel="noopener" class="block p-3 rounded-xl bg-slate-900 border border-emerald-500/30 hover:border-emerald-400 transition-all mb-3 group" title="Click to open Google Maps turn-by-turn navigation">
        <div class="flex items-center justify-between text-xs font-bold text-emerald-400 mb-1">
          <span class="flex items-center gap-1.5"><svg class="w-3.5 h-3.5 text-emerald-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg> Murli Chowk Workshop</span>
          <span class="text-[9px] bg-emerald-500/20 px-1.5 py-0.5 rounded text-emerald-300 font-mono">Open Map</span>
        </div>
        <p class="text-[11px] text-slate-300 leading-snug group-hover:text-white">
          Airport Road, Ward No. 8, Janakpur Dham, Dhanusha, Nepal
        </p>
      </a>

      <!-- WhatsApp Contact Card -->
      <a href="https://wa.me/9779817658719" target="_blank" rel="noopener" class="flex items-center gap-2.5 p-3 rounded-xl bg-slate-900 border border-emerald-500/30 hover:border-emerald-400 hover:bg-slate-900/70 transition-all mb-3 group">
        <span class="w-9 h-9 rounded-lg bg-emerald-500/18 border border-emerald-500/35 flex items-center justify-center flex-shrink-0 group-hover:bg-emerald-500 transition-colors">
          <svg class="w-4.5 h-4.5 fill-current text-emerald-400 group-hover:text-white transition-colors" style="width:1.125rem;height:1.125rem" viewBox="0 0 24 24" aria-hidden="true"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.387.709.282 1.263.45 1.694.59.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
        </span>
        <span class="min-w-0">
          <span class="block text-[10px] font-bold uppercase tracking-wider text-emerald-400">WhatsApp Direct</span>
          <span class="block font-mono font-bold text-white text-[13px] leading-tight">+977 9817658719</span>
        </span>
      </a>
      <p class="leading-relaxed text-slate-400 text-[11px]">Workshop Open 7 Days (9:00 AM – 7:00 PM)</p>
    </div>

  </div>

  <div class="relative max-w-7xl mx-auto pt-6 border-t border-white/5 flex flex-col sm:flex-row items-center justify-between gap-4 text-center sm:text-left">
    <div>
      © 2026 {SHOP['legal_name'].replace('&', '&amp;')}. All Rights Reserved. Murli Chowk, Janakpur Dham, Nepal.
    </div>
    <div class="flex items-center gap-4 text-[11px] font-semibold">
      <a href="https://wa.me/9779817658719" target="_blank" rel="noopener" class="text-slate-400 hover:text-emerald-400 transition-colors">WhatsApp</a>
      <span class="w-px h-3 bg-white/15"></span>
      <a href="https://www.facebook.com/search/top?q=Annapurna%20Aluminium%20Janakpur" target="_blank" rel="noopener" class="text-slate-400 hover:text-blue-400 transition-colors">Facebook</a>
      <span class="w-px h-3 bg-white/15"></span>
      <a href="https://www.youtube.com/results?search_query=Annapurna+Aluminium+Janakpur" target="_blank" rel="noopener" class="text-slate-400 hover:text-red-400 transition-colors">YouTube</a>
    </div>
  </div>
</footer>

<!-- LIGHTBOX MODAL WITH CAROUSEL PREV/NEXT -->
<div id="lightbox-modal" class="hidden fixed inset-0 z-50 bg-slate-950/95 backdrop-blur-2xl flex items-center justify-center p-4">
  <div class="relative max-w-4xl w-full bg-slate-900 border border-white/10 rounded-3xl overflow-hidden shadow-2xl flex flex-col max-h-[90vh]">
    
    <!-- Modal Header Bar -->
    <div class="p-4 bg-slate-950/90 border-b border-white/10 flex items-center justify-between">
      <div class="flex items-center gap-2">
        <span id="lightbox-cat" class="px-2.5 py-0.5 rounded-md text-[10px] font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">Category</span>
        <span id="lightbox-counter" class="text-xs font-mono text-slate-400">1 / 26</span>
      </div>
      
      <button onclick="closeLightbox()" class="w-8 h-8 rounded-full bg-slate-800 text-slate-300 hover:text-white flex items-center justify-center font-bold">✕</button>
    </div>

    <!-- Modal Content Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 overflow-y-auto">
      
      <!-- Image Display with Prev/Next Buttons -->
      <div class="relative bg-slate-950 flex items-center justify-center min-h-[300px]">
        <img id="lightbox-img" src="" alt="Project View" class="max-h-[70vh] w-full object-contain">

        <!-- Carousel Controls -->
        <button onclick="prevLightbox()" class="absolute left-3 top-1/2 -translate-y-1/2 w-10 h-10 rounded-full bg-slate-950/80 hover:bg-slate-900 text-emerald-400 font-black flex items-center justify-center border border-white/10 shadow-lg text-lg">←</button>
        <button onclick="nextLightbox()" class="absolute right-3 top-1/2 -translate-y-1/2 w-10 h-10 rounded-full bg-slate-950/80 hover:bg-slate-900 text-emerald-400 font-black flex items-center justify-center border border-white/10 shadow-lg text-lg">→</button>
      </div>

      <!-- Detail Sidebar -->
      <div class="p-6 flex flex-col justify-between space-y-4">
        <div>
          <h3 id="lightbox-title" class="font-bold font-display text-lg text-white mb-1">Project Title</h3>
          <p id="lightbox-loc" class="text-xs text-amber-400 font-semibold mb-3">📍 Location</p>
          <p id="lightbox-desc" class="text-xs text-slate-300 leading-relaxed mb-4">Description text</p>

          <div class="border-t border-white/10 pt-3">
            <span class="text-xs font-bold text-white block mb-2">Technical Specifications:</span>
            <div id="lightbox-specs" class="space-y-1.5 text-xs text-slate-300"></div>
          </div>
        </div>

        <button onclick="inquireLightboxItem()" class="w-full py-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs shadow-lg flex items-center justify-center gap-2">
          <span>💬</span> <span data-i18n="lightbox_btn_inquire">Direct WhatsApp Inquiry (+977 9817658719)</span>
        </button>
      </div>

    </div>

  </div>
</div>

<!-- FLOATING VERTICAL SOCIAL MEDIA DOCK (Tucked into right edge, slides out on hover) -->
<div id="social-float-dock" class="social-dock" role="complementary" aria-label="Contact and social links">

  <!-- WhatsApp Direct -->
  <a href="https://wa.me/9779817658719?text=Namaste%20Annapurna%20Aluminium,%20I%20am%20contacting%20you%20from%20your%20website." target="_blank" rel="noopener" class="social-dock-row group" aria-label="WhatsApp Direct Chat">
    <span class="social-dock-label">WhatsApp Direct · +977 9817658719</span>
    <span class="social-dock-icon bg-emerald-500/20 group-hover:border-emerald-400/60 group-hover:bg-emerald-500">
      <svg class="w-5 h-5 fill-current text-emerald-400 group-hover:text-white transition-colors" viewBox="0 0 24 24" aria-hidden="true"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.387.709.282 1.263.45 1.694.59.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
    </span>
  </a>

  <!-- Facebook -->
  <a href="https://www.facebook.com/search/top?q=Annapurna%20Aluminium%20Janakpur" target="_blank" rel="noopener" class="social-dock-row group" aria-label="Facebook Profile">
    <span class="social-dock-label">Facebook Showcase Page</span>
    <span class="social-dock-icon bg-blue-600/20 group-hover:border-blue-400/60 group-hover:bg-blue-600">
      <svg class="w-5 h-5 fill-current text-blue-400 group-hover:text-white transition-colors" viewBox="0 0 24 24" aria-hidden="true"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
    </span>
  </a>

  <!-- YouTube -->
  <a href="https://www.youtube.com/results?search_query=Annapurna+Aluminium+Janakpur" target="_blank" rel="noopener" class="social-dock-row group" aria-label="YouTube Channel">
    <span class="social-dock-label">YouTube Video Channel</span>
    <span class="social-dock-icon bg-red-600/20 group-hover:border-red-400/60 group-hover:bg-red-600">
      <svg class="w-5 h-5 fill-current text-red-500 group-hover:text-white transition-colors" viewBox="0 0 24 24" aria-hidden="true"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
    </span>
  </a>

  <!-- Instagram -->
  <a href="https://www.instagram.com/explore/tags/annapurnaaluminium/" target="_blank" rel="noopener" class="social-dock-row group" aria-label="Instagram Profile">
    <span class="social-dock-label">Instagram Feed &amp; Reels</span>
    <span class="social-dock-icon bg-pink-500/20 group-hover:border-pink-400/60 group-hover:bg-pink-500">
      <svg class="w-5 h-5 fill-current text-pink-500 group-hover:text-white transition-colors" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
    </span>
  </a>

  <!-- TikTok -->
  <a href="https://www.tiktok.com/search?q=Annapurna%20Aluminium%20Janakpur" target="_blank" rel="noopener" class="social-dock-row group" aria-label="TikTok Videos">
    <span class="social-dock-label">TikTok Video Showcase</span>
    <span class="social-dock-icon bg-pink-600/20 group-hover:border-pink-400/60 group-hover:bg-pink-600">
      <svg class="w-5 h-5 fill-current text-pink-400 group-hover:text-white transition-colors" viewBox="0 0 24 24" aria-hidden="true"><path d="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.98-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.82.57-1.32 1.53-1.34 2.53-.03.88.35 1.75 1.02 2.29.83.67 1.98.88 3.01.58.97-.27 1.8-1.02 2.15-1.97.23-.62.29-1.3.29-1.96V.02z"/></svg>
    </span>
  </a>

  <!-- Direct Call -->
  <a href="tel:+9779817658719" class="social-dock-row social-dock-call group" aria-label="Call +977 9817658719">
    <span class="social-dock-label">Call Now · +977 9817658719</span>
    <span class="social-dock-icon bg-amber-500/20 group-hover:border-amber-400/60 group-hover:bg-amber-500">
      <svg class="w-5 h-5 fill-current text-amber-400 group-hover:text-slate-950 transition-colors" viewBox="0 0 24 24" aria-hidden="true"><path d="M6.62 10.79a15.05 15.05 0 0 0 6.59 6.59l2.2-2.2a1 1 0 0 1 1.02-.24c1.12.37 2.33.57 3.57.57a1 1 0 0 1 1 1V20a1 1 0 0 1-1 1C10.4 21 3 13.6 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.24.2 2.45.57 3.57a1 1 0 0 1-.25 1.02l-2.2 2.2Z"/></svg>
    </span>
  </a>

</div>

<!-- ULTRA-PREMIUM SMART AI ARCHITECTURAL CHATBOT WIDGET -->
<div id="chatbot-widget" class="fixed bottom-6 right-6 z-50 flex flex-col items-end">
  
  <!-- Chatbot Floating Trigger Button -->
  <button id="chatbot-trigger-btn" onclick="toggleChatbot()" class="relative group flex items-center gap-3 p-1.5 rounded-full bg-slate-950/90 hover:bg-slate-900 border border-emerald-500/40 shadow-2xl backdrop-blur-xl transition-all duration-300 hover:scale-105" aria-label="Open AI Architectural Assistant">
    <div class="relative w-14 h-14 rounded-full overflow-hidden border border-emerald-400/50 p-0.5 shadow-inner bg-slate-900">
      <img src="uploads/chatbot_icon.png" alt="AI Architectural Assistant" class="w-full h-full object-cover rounded-full">
      <span class="absolute bottom-0 right-0 w-3.5 h-3.5 bg-emerald-500 border-2 border-slate-950 rounded-full"></span>
    </div>
    
    <div class="hidden sm:flex flex-col text-left pr-3">
      <span class="text-xs font-bold text-white flex items-center gap-1">
        <span>Annapurna AI</span> <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-ping"></span>
      </span>
      <span class="text-[10px] text-emerald-400 font-semibold">Architectural Support</span>
    </div>
  </button>

  <!-- Chatbot Drawer Window -->
  <div id="chatbot-window" class="hidden fixed bottom-24 right-4 sm:right-6 w-[92vw] sm:w-96 max-h-[80vh] h-[540px] glass-panel rounded-3xl border border-emerald-500/30 shadow-2xl flex flex-col overflow-hidden z-50">
    
    <!-- Chatbot Header -->
    <div class="p-4 bg-slate-950/95 border-b border-white/10 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="relative w-10 h-10 rounded-full overflow-hidden border border-emerald-400/50 p-0.5 bg-slate-900">
          <img src="uploads/chatbot_icon.png" alt="AI Assistant" class="w-full h-full object-cover rounded-full">
          <span class="absolute bottom-0 right-0 w-2.5 h-2.5 bg-emerald-500 border-2 border-slate-950 rounded-full"></span>
        </div>
        <div>
          <h3 class="font-bold text-white text-sm tracking-tight flex items-center gap-1">
            <span>Annapurna AI Assistant</span>
          </h3>
          <p class="text-[10px] text-emerald-400 font-medium">Live Workshop Support · Janakpur Dham</p>
        </div>
      </div>

      <button onclick="toggleChatbot()" class="w-7 h-7 rounded-full bg-slate-900 text-slate-400 hover:text-white flex items-center justify-center font-bold text-xs">✕</button>
    </div>

    <!-- Chat Messages Body -->
    <div id="chat-messages-container" class="flex-1 p-4 overflow-y-auto space-y-4 text-xs">
      
      <!-- Welcome Message -->
      <div class="flex items-start gap-2.5">
        <div class="w-7 h-7 rounded-full overflow-hidden bg-slate-900 border border-emerald-400/40 flex-shrink-0">
          <img src="uploads/chatbot_icon.png" alt="AI" class="w-full h-full object-cover">
        </div>
        <div class="p-3.5 rounded-2xl bg-slate-900/90 text-slate-200 border border-white/10 space-y-2 max-w-[85%]">
          <p data-i18n="chat_welcome">
            Namaste! 🙏 Welcome to Annapurna Aluminium &amp; UPVC Udhyog. How can I assist your building project today?
          </p>
        </div>
      </div>

      <!-- Quick Preset FAQ Suggestions -->
      <div class="space-y-1.5 pt-1">
        <p class="text-[10px] font-bold uppercase tracking-wider text-slate-400 block mb-1">Frequently Asked Questions:</p>
        
        <button onclick="askChatQuestion('q1')" class="w-full text-left p-2.5 rounded-xl bg-slate-900/80 hover:bg-slate-800 text-cyan-300 border border-cyan-500/20 hover:border-cyan-400/50 transition-all text-xs flex items-center justify-between">
          <span>❓ Which is better: UPVC or Aluminium?</span> <span>→</span>
        </button>

        <button onclick="askChatQuestion('q2')" class="w-full text-left p-2.5 rounded-xl bg-slate-900/80 hover:bg-slate-800 text-amber-300 border border-amber-500/20 hover:border-amber-400/50 transition-all text-xs flex items-center justify-between">
          <span>📍 Do you offer free site visit in Janakpur?</span> <span>→</span>
        </button>

        <button onclick="askChatQuestion('q3')" class="w-full text-left p-2.5 rounded-xl bg-slate-900/80 hover:bg-slate-800 text-emerald-300 border border-emerald-500/20 hover:border-emerald-400/50 transition-all text-xs flex items-center justify-between">
          <span>🍳 Are modular kitchen racks 100% waterproof?</span> <span>→</span>
        </button>

        <button onclick="askChatQuestion('q4')" class="w-full text-left p-2.5 rounded-xl bg-slate-900/80 hover:bg-slate-800 text-purple-300 border border-purple-500/20 hover:border-purple-400/50 transition-all text-xs flex items-center justify-between">
          <span>⛓️ What grade steel is used for Temple Gates?</span> <span>→</span>
        </button>

        <button onclick="askChatQuestion('owner')" class="w-full text-left p-2.5 rounded-xl bg-emerald-600/90 hover:bg-emerald-500 text-white font-bold transition-all text-xs flex items-center justify-between shadow-md">
          <span>📞 Speak / Call Founder Prof. Nageshwar Thakur on WhatsApp</span> <span>💬</span>
        </button>
      </div>

    </div>

    <!-- Chat Input Footer -->
    <form onsubmit="handleChatSubmit(event)" class="p-3 bg-slate-950/95 border-t border-white/10 flex items-center gap-2">
      <input type="text" id="chat-user-input" placeholder="Type your question or query..." class="flex-1 px-3 py-2 rounded-xl bg-slate-900 border border-white/10 text-white text-xs focus:border-emerald-400 focus:outline-none placeholder-slate-500">
      <button type="submit" class="p-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs shadow-md transition-all">
        Send
      </button>
    </form>

  </div>

</div>

<!-- EMBEDDED JAVASCRIPT APP LOGIC & DATASETS -->
<script>
const SHOP = {json.dumps(SHOP, ensure_ascii=False)};
const REAL_PROJECTS = {json.dumps(REAL_PROJECTS, ensure_ascii=False)};
const PRODUCTS = {json.dumps(products_list, ensure_ascii=False)};
const CATS = {json.dumps(CATS, ensure_ascii=False)};

/* Category metadata (colors, icons, EN/NE badges) for the 102+ catalog pills */
const CAT_META = {{
  "UWC": {{"color": "#00d2ff", "icon": "⬚", "badge": "UPVC Windows", "badge_ne": "यूपीभीसी झ्यालहरू", "tag": "German Multi-Chamber · Soundproof · Heatproof"}},
  "UWD": {{"color": "#3b82f6", "icon": "▤", "badge": "UPVC Doors", "badge_ne": "यूपीभीसी ढोकाहरू", "tag": "Steel Reinforced · Weatherproof · High Security"}},
  "ALW": {{"color": "#22d3ee", "icon": "◫", "badge": "Aluminium Windows", "badge_ne": "आल्मुनियम झ्यालहरू", "tag": "6063-T5 Alloy · Slim Profiles · Powder Coated"}},
  "ALD": {{"color": "#60a5fa", "icon": "▣", "badge": "Aluminium Doors", "badge_ne": "आल्मुनियम ढोकाहरू", "tag": "Eurobond ACP · Frosted Glass · Zero Warping"}},
  "ALP": {{"color": "#2dd4bf", "icon": "▥", "badge": "Aluminium Partitions", "badge_ne": "आल्मुनियम पार्टिसन", "tag": "Acoustic Glass · Office Cabins · Modern Privacy"}},
  "GLZ": {{"color": "#818cf8", "icon": "◈", "badge": "Glass Solutions", "badge_ne": "टफन्ड ग्लास", "tag": "8-12mm Toughened · Frameless Spigots · Safety"}},
  "STF": {{"color": "#a855f7", "icon": "▦", "badge": "Storefront & Facades", "badge_ne": "ग्लास फसाड तथा एसीपी", "tag": "Curtain Wall Glazing · ACP Cladding · Showrooms"}},
  "MST": {{"color": "#f59e0b", "icon": "⛓", "badge": "MS & Steel Works", "badge_ne": "मन्दिर तथा मेन गेट", "tag": "Temple Gates · Grills · Security Doors · Sheds"}},
  "SLS": {{"color": "#eab308", "icon": "✦", "badge": "Stainless Steel (SS 304)", "badge_ne": "एसएस ३०४ रेलिङ", "tag": "Mirror Polish · Crystal Pillars · Lifetime Rust-Free"}},
  "RLS": {{"color": "#f97316", "icon": "⤢", "badge": "Railings & Balustrades", "badge_ne": "बालकनी तथा भर्याङ", "tag": "Staircases · Balconies · Glass & SS Hybrid"}},
  "MOD": {{"color": "#ec4899", "icon": "▧", "badge": "Modular Kitchen & Racks", "badge_ne": "मोड्युलर किचन र्याक", "tag": "Termite-Proof · 100% Waterproof · ACP Racks"}}
}};



{templates_js_raw}

function getProductSvg(artKey, artParams) {{
  if (typeof TEMPLATES !== 'undefined' && TEMPLATES[artKey]) {{
    try {{
      return TEMPLATES[artKey](artParams || {{}});
    }} catch(e) {{
      return '';
    }}
  }}
  return '';
}}

const I18N = {{
  en: {{
    top_open: "Workshop Open 7 Days · 9:00 AM – 7:00 PM",
    top_loc: "Murli Chowk (Airport Road), Janakpur Dham-8, Dhanusha",
    nav_subtitle: "Janakpur Dham · Windows, Doors, Glass & Steel Works",
    nav_projects: "Real Projects (40+)",
    nav_catalog: "102+ Design Catalog",
    nav_workflow: "Workflow & Quality",
    nav_standards: "Material Specs",
    nav_consult: "Book Site Visit",
    nav_about: "About & Team",
    btn_whatsapp: "WhatsApp Direct (+977 9817658719)",
    hero_badge: "#1 Certified UPVC, Aluminium & SS Fabrication Center · Janakpur Dham, Nepal",
    hero_h1_1: "World-Class",
    hero_h1_2: "UPVC, Aluminium & Glass",
    hero_h1_3: "Precision Craftsmanship",
    hero_desc: "102+ Custom Designs manufactured at our Janakpur workshop: German-profile UPVC windows, modern aluminium doors & partitions, SS 304 temple gates, balustrades, modular kitchen racks, and commercial ACP glass facades.",
    hero_btn_whatsapp: "WhatsApp Consultation (+977 9817658719)",
    hero_btn_catalog: "Browse 102+ Catalog",
    hero_btn_projects: "Explore Real Project Photos",
    stat_designs: "Unique Custom Designs",
    stat_sites: "Real Workshop Projects",
    stat_quality: "SS 304 Rust-Free Guarantee",
    stat_exp: "Engineering Craftsmanship",
    workflow_title: "Our 4-Step Precision Fabrication Workflow",
    workflow_subtitle: "From free site visit and 3D design to precision laser fabrication and lifetime on-site fitting.",
    wf_s1_t: "Free Site Measurement",
    wf_s1_d: "Master engineer visits your building with laser distance meters and real metal/glass profile samples.",
    wf_s2_t: "3D CAD & Vector Blueprint",
    wf_s2_d: "Custom technical drawing generated for your approval with exact millimeter glass and aluminum specs.",
    wf_s3_t: "Workshop CNC Fabrication",
    wf_s3_d: "Precision miter cutting, argon TIG welding, powder coating, and EPDM weather-seal assembly at Murli Chowk.",
    wf_s4_t: "On-Site Expert Fitting",
    wf_s4_d: "Fast, clean installation by experienced technicians with weatherproofing and 10-year quality guarantee.",
    projects_title: "Real Projects Fabricated in Janakpur",
    projects_subtitle: "Explore actual completed commercial facades, temple gates, modern residences, staircases, and modular kitchens fabricated right here at our Murli Chowk workshop.",
    catalog_title: "102+ Master Product Designs",
    catalog_subtitle: "Every product is precision-engineered, customizable to your exact structural measurements, and available in multiple finishes and glass configurations.",
    catalog_view_mode: "View Mode:",
    view_photo: "Photos",
    view_blueprint: "CAD Blueprint",
    factory_title: "Factory Machinery & Raw Material Quality",
    factory_subtitle: "We never compromise on metal thickness, uPVC wall gauge, or welding standards. Here is how we ensure lifetime durability.",
    mat_1_title: "German Multi-Chamber UPVC",
    mat_1_desc: "Multi-cavity internal chambers trap air pockets for maximum thermal & sound insulation. Reinforced with galvanized steel inserts to prevent frame distortion in hot Janakpur summers.",
    mat_2_title: "Virgin 6063-T5 Aluminium Alloy",
    mat_2_desc: "Manufactured using high-strength architectural aluminium alloy with 60-80 micron electro-powder coating that withstands harsh sun, monsoons, and everyday impacts.",
    mat_3_title: "Authentic SS 304 Rust-Free Steel",
    mat_3_desc: "Every stainless steel railing, temple gate, and staircase pillar is crafted from genuine SS 304 with full nickel content, assembled with inert gas TIG welding and diamond compound polishing.",
    booking_title: "Book Free On-Site Measurement",
    booking_desc: "Building a new house, commercial showroom, or renovating your hotel in Janakpur Dham or nearby districts? Message our master engineer directly on WhatsApp for laser-guided measurement.",
    form_title: "Request Site Visit & Custom Quote",
    form_label_name: "Your Full Name *",
    form_label_phone: "Your WhatsApp Number *",
    form_label_city: "Project Location / District *",
    form_label_service: "Primary Architectural Requirement",
    form_label_notes: "Approximate Openings / Notes",
    bk_benefit_1_t: "Direct WhatsApp Dispatch",
    bk_benefit_1_d: "Booking lands instantly with our master engineer (+977 9817658719)",
    bk_benefit_2_t: "Real Sample Demo On-Site",
    bk_benefit_2_d: "Physical UPVC, aluminium & glass samples with laser-guided measurement",
    bk_benefit_3_t: "Instant Quote + 3D Advice",
    bk_benefit_3_d: "Structural quotation and 3D drawing advice on the spot",
    bk_how_title: "How It Works",
    bk_step_1: "Request",
    bk_step_2: "Confirm Slot",
    bk_step_3: "Site Visit",
    bk_step_4: "Quote & Blueprint",
    bk_form_sub: "100% free · Reply within 15 minutes",
    bk_submit: "Send Booking to WhatsApp",
    about_tag: "Founder & Master Fabricator",
    about_bio_1: '"We started Annapurna Aluminium & UPVC in Janakpur Dham with a singular mission: to deliver European-grade window insulation, modern aluminium elegance, and unyielding steel security at direct factory prices to every home and enterprise in Nepal."',
    about_bio_2: "From the sacred doors of Sri Nav Durga Mandir Duhaba to commercial plazas across Madhesh Province, our team of seasoned craftsmen takes personal pride in every single weld, miter cut, and glass installation.",
    faq_title: "Got Questions? We Have Answers.",
    faq_q1: "How can I get an exact price quote for my house or commercial building?",
    faq_a1: "Simply message us directly on WhatsApp at <strong>+977 9817658719</strong> with your rough room window/door dimensions or architectural floor plan. If you are in Janakpur Dham, Dhanusha, or nearby districts, our engineer will visit your site directly for free measurement.",
    faq_q2: "What is the price of UPVC windows in Nepal?",
    faq_a2: "UPVC window pricing depends on track configuration (2-track vs 3-track with mesh), profile grade (multi-chamber German profile), and glass selection (single float, tinted reflective, or insulated double glazing). We offer the most competitive factory-direct rates in Nepal starting from NRs 450 - 850 per sq.ft.",
    faq_q3: "Which is better for home bedrooms: UPVC or Aluminium?",
    faq_a3: "For residential bedrooms and living rooms, <strong>UPVC with double glazing</strong> is the best choice because it blocks outdoor traffic noise and maintains cooler room temperatures during summer heat. Aluminium is best for large commercial storefronts, slim partitions, and high-impact structural portals.",
    faq_q4: "How do modular aluminium kitchen racks prevent termites and water damage?",
    faq_a4: "Unlike plywood or MDF boards that swell, warp, and get infested with termites in humid kitchens, our modular racks use 100% anodized architectural aluminium framing and waterproof aluminium composite panels (ACP) that can be washed directly with water without any damage.",
    faq_q5: "How long does manufacturing and installation take?",
    faq_a5: "Standard residential window and door orders are completed in <strong>3 to 5 business days</strong>. Commercial facade glazing, large temple gates, and custom modular kitchens are scheduled as per site milestones with prompt delivery.",
    lightbox_btn_inquire: "Direct WhatsApp Inquiry (+977 9817658719)",
    chat_welcome: "Namaste! 🙏 Welcome to Annapurna Aluminium & UPVC Udhyog. How can I assist your building project today?",
    board_title: "Our Workshop — Murli Chowk, Janakpur Dham-8",
    board_sub: "On the Airport Road · Open 9:00 AM – 7:00 PM, all 7 days",
    board_directions: "Get Directions",
    board_note: "“यहाँ आल्मुनियम र UPVC को झ्याल, ढोका, पार्टिसन, किचन रैक तथा स्टील रेलिङको काम गरिन्छ।” — Aluminium & UPVC windows, doors, partitions, kitchen racks and steel railing work, all under one roof."
  }},
  ne: {{
    top_open: "हप्ताको सातै दिन खुला · बिहान ९:०० देखि साँझ ७:०० सम्म",
    top_loc: "मुरली चोक (एयरपोर्ट रोड), जनकपुरधाम-८, धनुषा",
    nav_subtitle: "जनकपुरधाम · झ्याल, ढोका, ग्लास र स्टिल फेब्रिकेसन",
    nav_projects: "वास्तविक कामहरू (४०+)",
    nav_catalog: "१०२+ डिजाइन क्याटलग",
    nav_workflow: "प्रक्रिया तथा गुणस्तर",
    nav_standards: "सामग्री मापदण्ड",
    nav_consult: "साइट भिजिट बुक गर्नुहोस्",
    nav_about: "हाम्रोबारे",
    btn_whatsapp: "ह्वाट्सएप सोधपुछ (+९त्७ ९८१७६५८७१९)",
    hero_badge: "जनकपुरधामको #१ प्रमाणित यूपीभीसी, आल्मुनियम तथा स्टिल फेब्रिकेसन केन्द्र",
    hero_h1_1: "विश्वस्तरीय गुणस्तर",
    hero_h1_2: "यूपीभीसी, आल्मुनियम र ग्लास",
    hero_h1_3: "उत्कृष्ट निर्माण",
    hero_desc: "जनकपुरधाममा निर्मित १०२+ भन्दा बढी प्रिमियम डिजाइनहरू: जर्मन यूपीभीसी झ्याल, आल्मुनियम ढोका र पार्टिसन, एसएस ३०४ मन्दिर गेट, भर्याङ रेलिङ, मोड्युलर किचन र्याक र एसीपी ग्लास फसाड।",
    hero_btn_whatsapp: "ह्वाट्सएप डायरेक्ट सम्पर्क (+९७७ ९८१७६५८७१९)",
    hero_btn_catalog: "१०२+ डिजाइन क्याटलग",
    hero_btn_projects: "वास्तविक कामहरू हेर्नुहोस्",
    stat_designs: "अद्वितीय प्रिमियम डिजाइनहरू",
    stat_sites: "वर्कसपका वास्तविक परियोजनाहरू",
    stat_quality: "एसएस ३०४ खिया नलाग्ने ग्यारेन्टी",
    stat_exp: "वर्षको अनुभव र दक्षता",
    workflow_title: "हाम्रो ४-चरणको अत्याधुनिक निर्माण प्रक्रिया",
    workflow_subtitle: "निःशुल्क नाप जाँचदेखि अत्याधुनिक मेसिनबाट कटिङ, वेल्डिङ र फिटिङसम्मको प्रक्रिया।",
    wf_s1_t: "निःशुल्क साइट नाप जाँच",
    wf_s1_d: "हाम्रो मुख्य इन्जिनियर लेजर मिटर र वास्तविक प्रोफाइल स्याम्पल लिएर तपाईंको साइटमा आउनुहुन्छ।",
    wf_s2_t: "३डी क्याड र नक्सा डिजाइन",
    wf_s2_d: "तपाईंको आवश्यकता अनुसार मिलिमिटर नापमा सटीक प्राविधिक नक्सा तयार पारिन्छ।",
    wf_s3_t: "वर्कसप मेसिन फेब्रिकेसन",
    wf_s3_d: "मुरली चोक वर्कसपमा कटिङ, वेल्डिङ, र EPDM रबर सिल सहितको जडान कार्य।",
    wf_s4_t: "साइटमा दक्ष फिटिङ",
    wf_s4_d: "अनुभवी प्राविधिकहरूद्वारा १० वर्षको गुणस्तर ग्यारेन्टी सहित सफा फिटिङ।",
    projects_title: "जनकपुरधाममा निर्मित वास्तविक परियोजनाहरू",
    projects_subtitle: "मुरली चोक वर्कसपमा तयार गरिएका व्यापारिक फसाड, मन्दिर गेट, यूपीभीसी झ्याल, र किचन र्याकहरूको तस्विर।",
    catalog_title: "१०२+ मास्टर प्रोडक्ट डिजाइनहरू",
    catalog_subtitle: "प्रत्येक डिजाइन तपाईंको घरको नाप अनुसार बनाउन सकिने र विभिन्न फिनिसिङमा उपलब्ध।",
    catalog_view_mode: "हेर्ने मोड:",
    view_photo: "वास्तविक फोटो",
    view_blueprint: "क्याड नक्सा (ब्लुप्रिन्ट)",
    factory_title: "मेसिनरी तथा कच्चा पदार्थको गुणस्तर",
    factory_subtitle: "हामी धातुको बाक्लोपना र गुणस्तरमा कुनै सम्झौता गर्दैनौं।",
    mat_1_title: "जर्मन मल्टि-च्याम्बर यूपीभीसी",
    mat_1_desc: "आवाज र तातो रोक्ने साउन्डप्रुफ यूपीभीसी प्रोफाइल।",
    mat_2_title: "६०६३-टी५ ओरिजिनल आल्मुनियम",
    mat_2_desc: "पाउडर कोटेड घाम र पानीले नबिग्रिने आल्मुनियम।",
    mat_3_title: "ओरिजिनल एसएस ३०४ स्टिल",
    mat_3_desc: "१००% खिया नलाग्ने उच्च क्वालिटी स्टेनलेस स्टिल।",
    booking_title: "निःशुल्क नाप जाँच बुक गर्नुहोस्",
    booking_desc: "जनकपुरधाम वा आसपासका जिल्लाहरूमा घर, होटेल वा शोरुम बनाउँदै हुनुहुन्छ भने ह्वाट्सएपमा सीधा म्यासेज गर्नुहोस्।",
    form_title: "साइट भिजिट र कोटेशन फारम",
    form_label_name: "तपाईंको पूरा नाम *",
    form_label_phone: "ह्वाट्सएप नम्बर *",
    form_label_city: "साइटको ठेगाना / जिल्ला *",
    form_label_service: "चाहिएको फेब्रिकेसन काम",
    form_label_notes: "झ्याल/ढोकाको संख्या वा विवरण",
    bk_benefit_1_t: "सिधा ह्वाट्सएप पठाइन्छ",
    bk_benefit_1_d: "बुकिङ तुरुन्तै मुख्य इन्जिनियरसम्म पुग्छ (+९७७ ९८१७६५८७१९)",
    bk_benefit_2_t: "साइटमै वास्तविक नमुना प्रदर्शन",
    bk_benefit_2_d: "लेजर नापसहित यूपीभीसी, आल्मुनियम र ग्लासका वास्तविक नमुनाहरू",
    bk_benefit_3_t: "तुरुन्त कोटेशन + ३डी सल्लाह",
    bk_benefit_3_d: "घटनास्थलमै संरचनात्मक कोटेशन र ३डी नक्सा सल्लाह",
    bk_how_title: "कसरी काम गर्छ",
    bk_step_1: "अनुरोध",
    bk_step_2: "समय पक्का",
    bk_step_3: "साइट भिजिट",
    bk_step_4: "कोटेशन र ब्लुप्रिन्ट",
    bk_form_sub: "१००% निःशुल्क · १५ मिनेटभित्र जवाफ",
    bk_submit: "ह्वाट्सएपमा बुकिङ पठाउनुहोस्",
    about_tag: "संस्थापक तथा मुख्य फेब्रिकेटर",
    about_bio_1: '"हामीले जनकपुरधाममा युरोपियन स्तरको झ्याल र स्टिल फेब्रिकेसन direct factory मूल्यमा उपलब्ध गराउने लक्ष्य राखेका छौं।"',
    about_bio_2: "श्री नव दुर्गा मन्दिर दुहबा गेटदेखि व्यापारिक कम्प्लेक्सहरूसम्म, हाम्रा दक्ष प्राविधिकहरू हरेक काममा पूर्ण ध्यान दिन्छन्।",
    faq_title: "धेरै सोधिने प्रश्नहरू",
    faq_q1: "मेरो घर वा भवनको लागि रेट कसरी पाउन सकिन्छ?",
    faq_a1: "तपाईंको झ्याल वा ढोकाको सम्भावित नाप लिएर ह्वाट्सएप नम्बर <strong>+९७७ ९८१७६५८७१९</strong> मा म्यासेज गर्नुहोस्।",
    faq_q2: "नेपालमा यूपीभीसी झ्यालको मूल्य कति पर्छ?",
    faq_a2: "नेपालमा यूपीभीसी झ्यालको मूल्य प्रति स्क्वायर फिट रु. ४५० देखि ८५० सम्म पर्छ।",
    faq_q3: "घरको लागि यूपीभीसी कि आल्मुनियम कुन राम्रो?",
    faq_a3: "घरको बेडरुमको लागि साउन्डप्रुफ यूपीभीसी उत्तम हुन्छ।",
    faq_q4: "आल्मुनियम किचन र्याकमा धमिरा वा पानीले असर गर्छ कि गर्दैन?",
    faq_a4: "हाम्रा मोड्युलर आल्मुनियम र्याक १००% वाटरप्रुफ र धमिरा-मुक्त हुन्छन्।",
    faq_q5: "सामान तयार हुन कति समय लाग्छ?",
    faq_a5: "साधारणतया ३ देखि ५ दिन भित्र सामान तयार गरी फिटिङ गरिन्छ।",
    lightbox_btn_inquire: "ह्वाट्सएपमा सोधपुछ गर्नुहोस् (+९७७ ९८१७६५८७१९)",
    chat_welcome: "नमस्ते! 🙏 अन्नपूर्णा आल्मुनियम तथा यूपीभीसी उद्योगमा स्वागत छ। आज तपाईंलाई कसरी सहयोग गर्न सक्छु?",
    board_title: "हाम्रो कारखाना — मुरली चौक, जनकपुरधाम-८",
    board_sub: "एयरपोर्ट जाने बाटोमा · बिहान ९:०० देखि साँझ ७:०० सम्म, सातै दिन खुला",
    board_directions: "रास्ता देखाउनुहोस्",
    board_note: "“यहाँ आल्मुनियम र UPVC को झ्याल, ढोका, पार्टिसन, किचन रैक तथा स्टील रेलिङको काम गरिन्छ।” — एउटै छत तल सबै काम।"
  }}
}};

let currentLang = 'en';

function setLanguage(lang) {{
  if (!I18N[lang]) return;
  currentLang = lang;
  
  const btnEn = document.getElementById('lang-btn-en');
  const btnNe = document.getElementById('lang-btn-ne');
  
  if (lang === 'en') {{
    if (btnEn) btnEn.className = 'px-2.5 py-1 rounded-md font-bold bg-emerald-500 text-white transition-all shadow-sm';
    if (btnNe) btnNe.className = 'px-2.5 py-1 rounded-md font-bold text-slate-300 hover:text-white transition-all';
  }} else {{
    if (btnNe) btnNe.className = 'px-2.5 py-1 rounded-md font-bold bg-emerald-500 text-white transition-all shadow-sm';
    if (btnEn) btnEn.className = 'px-2.5 py-1 rounded-md font-bold text-slate-300 hover:text-white transition-all';
  }}

  document.querySelectorAll('[data-i18n]').forEach(el => {{
    const key = el.getAttribute('data-i18n');
    if (I18N[lang][key]) {{
      el.innerHTML = I18N[lang][key];
    }}
  }});

  renderRealProjects();
  renderCatalogCategoryPills();
  renderCatalog();
}}

/* ==================== CHATBOT BOT LOGIC & WHATSAPP CALL ==================== */
function toggleChatbot() {{
  const win = document.getElementById('chatbot-window');
  if (win) win.classList.toggle('hidden');
}}

const CHAT_ANSWERS = {{
  q1: {{
    q: "Which is better: UPVC or Aluminium?",
    a: "For residential bedrooms and homes, <strong>UPVC with double glazing</strong> is superior for heat insulation and noise reduction. For large commercial storefronts and slim dividers, <strong>6063-T5 Aluminium</strong> offers high structural strength.",
    cta: "Consult Founder Prof. Nageshwar Thakur on WhatsApp regarding profile choice"
  }},
  q2: {{
    q: "Do you offer free site visit & measurement in Janakpur?",
    a: "Yes! Our master fabricator visits your building site in Janakpur Dham, Dhanusha, Mahottari, Sarlahi, Lahan & nearby districts with physical profile & glass samples for free laser-guided measurement.",
    cta: "Book Free Site Measurement on WhatsApp (+977 9817658719)"
  }},
  q3: {{
    q: "Are modular kitchen racks 100% waterproof?",
    a: "Yes! Our modular kitchen racks use 100% heavy anodized aluminium frames and waterproof ACP composite panels that never warp, swell, or get infested with termites.",
    cta: "Inquire Kitchen Rack Models on WhatsApp"
  }},
  q4: {{
    q: "What grade steel is used for Temple Gates?",
    a: "We use exclusively authentic <strong>SS 304 marine-grade stainless steel</strong> with full nickel content, argon TIG welding, and diamond compound mirror polishing that never rusts under rain.",
    cta: "Inquire Temple Gate Fabrication on WhatsApp"
  }},
  owner: {{
    q: "Direct Call / Chat with Owner Prof. Nageshwar Thakur",
    a: "Connecting you directly to Founder Prof. Nageshwar Thakur on WhatsApp (+977 9817658719)...",
    cta: "Click here to Chat / Call Founder on WhatsApp"
  }}
}};

function askChatQuestion(key) {{
  const data = CHAT_ANSWERS[key];
  if (!data) return;

  const container = document.getElementById('chat-messages-container');

  // Append user message
  const userHtml = `
    <div class="flex items-end justify-end gap-2 my-2">
      <div class="p-3 rounded-2xl bg-emerald-600 text-white font-medium max-w-[85%] text-xs shadow-md">
        ${{data.q}}
      </div>
    </div>
  `;
  container.insertAdjacentHTML('beforeend', userHtml);
  container.scrollTop = container.scrollHeight;

  // Append typing indicator
  const typingId = 'typing-' + Date.now();
  const typingHtml = `
    <div id="${{typingId}}" class="flex items-start gap-2.5 my-2">
      <div class="w-7 h-7 rounded-full overflow-hidden bg-slate-900 border border-emerald-400/40 flex-shrink-0">
        <img src="uploads/chatbot_icon.png" alt="AI" class="w-full h-full object-cover">
      </div>
      <div class="p-3 rounded-2xl bg-slate-900 text-slate-400 text-xs animate-pulse">
        Annapurna AI Assistant is typing...
      </div>
    </div>
  `;
  container.insertAdjacentHTML('beforeend', typingHtml);
  container.scrollTop = container.scrollHeight;

  setTimeout(() => {{
    const typingEl = document.getElementById(typingId);
    if (typingEl) typingEl.remove();

    const waMsg = `Namaste%20Prof.%20Nageshwar%20Thakur,%20I%20have%20a%20question%20regarding:%20${{encodeURIComponent(data.q)}}`;

    const botHtml = `
      <div class="flex items-start gap-2.5 my-2">
        <div class="w-7 h-7 rounded-full overflow-hidden bg-slate-900 border border-emerald-400/40 flex-shrink-0">
          <img src="uploads/chatbot_icon.png" alt="AI" class="w-full h-full object-cover">
        </div>
        <div class="p-3.5 rounded-2xl bg-slate-900 text-slate-200 border border-white/10 space-y-3 max-w-[88%] shadow-lg">
          <p>${{data.a}}</p>
          <a href="https://wa.me/${{SHOP.whatsapp}}?text=${{waMsg}}" target="_blank" rel="noopener" class="block text-center py-2.5 px-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs shadow-md transition-all">
            💬 ${{data.cta}} (+977 9817658719)
          </a>
        </div>
      </div>
    `;
    container.insertAdjacentHTML('beforeend', botHtml);
    container.scrollTop = container.scrollHeight;
  }}, 600);
}}

function handleChatSubmit(e) {{
  e.preventDefault();
  const input = document.getElementById('chat-user-input');
  const val = input.value.trim();
  if (!val) return;

  const container = document.getElementById('chat-messages-container');
  const userHtml = `
    <div class="flex items-end justify-end gap-2 my-2">
      <div class="p-3 rounded-2xl bg-emerald-600 text-white font-medium max-w-[85%] text-xs shadow-md">
        ${{val}}
      </div>
    </div>
  `;
  container.insertAdjacentHTML('beforeend', userHtml);
  input.value = '';
  container.scrollTop = container.scrollHeight;

  const waMsg = `Namaste%20Annapurna,%20I%20have%20this%20architectural%20query:%20${{encodeURIComponent(val)}}`;

  setTimeout(() => {{
    const botHtml = `
      <div class="flex items-start gap-2.5 my-2">
        <div class="w-7 h-7 rounded-full overflow-hidden bg-slate-900 border border-emerald-400/40 flex-shrink-0">
          <img src="uploads/chatbot_icon.png" alt="AI" class="w-full h-full object-cover">
        </div>
        <div class="p-3.5 rounded-2xl bg-slate-900 text-slate-200 border border-white/10 space-y-3 max-w-[88%] shadow-lg">
          <p>Thank you for your inquiry! I can forward your exact question to Founder Prof. Nageshwar Thakur directly on WhatsApp for an immediate response.</p>
          <a href="https://wa.me/${{SHOP.whatsapp}}?text=${{waMsg}}" target="_blank" rel="noopener" class="block text-center py-2.5 px-3 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs shadow-md transition-all">
            💬 Speak Directly with Founder on WhatsApp (+977 9817658719)
          </a>
        </div>
      </div>
    `;
    container.insertAdjacentHTML('beforeend', botHtml);
    container.scrollTop = container.scrollHeight;
  }}, 600);
}}

/* ==================== AUTOMATIC INFINITE MARQUEE CAROUSEL ==================== */
function renderAutoMarquee() {{
  const track = document.getElementById('auto-marquee-track');
  if (!track) return;

  const items = REAL_PROJECTS.slice(0, 12);
  const list = [...items, ...items];

  track.innerHTML = list.map(p => `
    <div onclick="openLightboxProject('${{p.id}}')" class="w-72 sm:w-80 flex-shrink-0 glass-card rounded-2xl overflow-hidden border border-white/10 hover:border-emerald-400 cursor-pointer transition-all group">
      <div class="relative h-44 overflow-hidden bg-slate-950">
        <img src="catalog_assets/real_projects/${{p.thumb || p.image}}" alt="${{p.title}}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy">
        <div class="absolute top-2.5 left-2.5 px-2 py-0.5 rounded bg-slate-950/85 text-[10px] font-extrabold text-emerald-400 border border-emerald-400/30">
          ${{p.category}}
        </div>
      </div>
      <div class="p-3.5 bg-slate-950/90">
        <h4 class="font-bold text-xs text-white truncate mb-1">${{p.title}}</h4>
        <div class="flex items-center justify-between text-[11px] text-slate-400">
          <span>📍 ${{p.location}}</span>
          <span class="text-emerald-400 font-bold hover:underline">View →</span>
        </div>
      </div>
    </div>
  `).join('');
}}

/* ==================== REAL PROJECTS GALLERY ==================== */
let currentProjectFilter = 'all';

function renderRealProjects() {{
  const container = document.getElementById('real-projects-grid');
  if (!container) return;

  const filtered = REAL_PROJECTS.filter(p => {{
    if (currentProjectFilter === 'all') return true;
    return p.cat_key === currentProjectFilter;
  }});

  container.innerHTML = filtered.map(p => {{
    const title = currentLang === 'ne' && p.title_ne ? p.title_ne : p.title;
    const category = currentLang === 'ne' && p.category_ne ? p.category_ne : p.category;
    const location = currentLang === 'ne' && p.location_ne ? p.location_ne : p.location;

    return `
      <article class="glass-card rounded-2xl overflow-hidden group border border-white/10 hover:border-emerald-400/50 transition-all flex flex-col justify-between">
        
        <div class="relative overflow-hidden cursor-pointer" onclick="openLightboxProject('${{p.id}}')">
          <img src="catalog_assets/real_projects/${{p.thumb || p.image}}" alt="${{title}} — Annapurna Aluminium Janakpur" class="w-full h-56 object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy">
          
          <div class="absolute inset-0 bg-gradient-to-t from-slate-950/90 via-slate-950/20 to-transparent opacity-80 group-hover:opacity-60 transition-opacity"></div>
          
          <div class="absolute top-3 left-3 flex flex-wrap gap-1.5">
            <span class="px-2.5 py-0.5 rounded-md text-[10px] font-extrabold uppercase bg-slate-950/90 text-emerald-400 border border-emerald-400/30">
              ${{category}}
            </span>
          </div>

          <div class="absolute bottom-3 left-3 right-3 text-xs text-amber-300 font-semibold flex items-center gap-1">
            <span>📍</span> <span>${{location}}</span>
          </div>
        </div>

        <div class="p-5 flex-1 flex flex-col justify-between space-y-3">
          <div>
            <h3 class="font-bold text-white text-base leading-snug mb-2 hover:text-emerald-400 transition-colors cursor-pointer" onclick="openLightboxProject('${{p.id}}')">
              ${{title}}
            </h3>

            <div class="flex flex-wrap gap-1 mb-3">
              ${{p.specs.map(s => `<span class="px-2 py-0.5 rounded bg-slate-900 text-[10px] text-slate-300 border border-white/5">${{s}}</span>`).join('')}}
            </div>
          </div>

          <div class="pt-2 border-t border-white/5 flex items-center justify-between text-xs font-bold">
            <button onclick="openLightboxProject('${{p.id}}')" class="text-emerald-400 hover:text-emerald-300 flex items-center gap-1">
              <span>${{currentLang === 'ne' ? 'फोटो तथा विवरण' : 'View Details'}}</span> <span>→</span>
            </button>

            <a href="https://wa.me/${{SHOP.whatsapp}}?text=Namaste%20Annapurna,%20I%20saw%20this%20project:%20${{encodeURIComponent(title)}}%20and%20want%20a%20quote." target="_blank" class="text-emerald-400 hover:underline flex items-center gap-1">
              <span>💬</span> <span>WhatsApp Quote</span>
            </a>
          </div>
        </div>

      </article>
    `;
  }}).join('');
}}

function filterRealProjects(filter) {{
  currentProjectFilter = filter;
  document.querySelectorAll('.proj-pill').forEach(btn => {{
    if (btn.getAttribute('data-pfilter') === filter) {{
      btn.className = 'proj-pill px-3 py-1.5 rounded-xl text-xs font-bold bg-emerald-500 text-white shadow-md';
    }} else {{
      btn.className = 'proj-pill px-3 py-1.5 rounded-xl text-xs font-bold text-slate-300 hover:text-white';
    }}
  }});
  renderRealProjects();
}}

/* ==================== 102+ CATALOG EXPLORER ==================== */
let currentCatalogCategory = 'ALL';
let currentCatalogSearch = '';
let currentCatalogViewMode = 'photo';

function renderCatalogCategoryPills() {{
  const container = document.getElementById('catalog-category-pills');
  if (!container) return;

  let html = `
    <button onclick="filterCatalog('ALL')" data-cat="ALL" class="cat-pill px-4 py-2 rounded-xl text-xs font-bold whitespace-nowrap bg-emerald-500 text-white shadow-md">
      ${{currentLang === 'ne' ? 'सबै १०२+ डिजाइनहरू' : 'All 102+ Designs'}}
    </button>
  `;

  CATS.forEach(c => {{
    const meta = CAT_META[c.key] || {{}};
    const badge = (currentLang === 'ne' && meta.badge_ne) ? meta.badge_ne : (meta.badge || c.name);

    html += `
      <button onclick="filterCatalog('${{c.key}}')" data-cat="${{c.key}}" class="cat-pill px-4 py-2 rounded-xl text-xs font-bold whitespace-nowrap bg-slate-900 text-slate-300 hover:text-white border border-white/10 transition-all">
        <span>${{meta.icon || '⬚'}}</span> <span>${{badge}}</span>
      </button>
    `;
  }});

  container.innerHTML = html;
}}

function renderCatalog() {{
  const container = document.getElementById('catalog-grid');
  if (!container) return;

  const q = currentCatalogSearch.trim().toLowerCase();

  const filtered = PRODUCTS.filter(p => {{
    if (currentCatalogCategory !== 'ALL' && p.cat !== currentCatalogCategory) return false;
    
    if (q) {{
      const text = (p.code + ' ' + p.name + ' ' + p.desc + ' ' + (p.finishes||[]).join(' ')).toLowerCase();
      if (!text.includes(q)) return false;
    }}
    return true;
  }});

  const countEl = document.getElementById('catalog-count');
  if (countEl) {{
    countEl.innerText = `${{filtered.length}} / ${{PRODUCTS.length}} ${{currentLang === 'ne' ? 'डिजाइनहरू' : 'Designs Available'}}`;
  }}

  if (filtered.length === 0) {{
    container.innerHTML = `
      <div class="col-span-full py-12 text-center glass-card p-8 rounded-2xl">
        <div class="text-4xl mb-3">🔍</div>
        <h4 class="text-lg font-bold text-white mb-1">${{currentLang === 'ne' ? 'कुनै डिजाइन भेटिएन' : 'No matching designs found'}}</h4>
        <p class="text-xs text-slate-400">${{currentLang === 'ne' ? 'अन्य शब्द वा क्याटेगोरी छानेर खोज्नुहोस्।' : 'Try searching for "sliding", "gate", "kitchen", or click "All 102+ Designs".'}}</p>
      </div>
    `;
    return;
  }}

  container.innerHTML = filtered.map(p => {{
    const catBadge = (currentLang === 'ne' && p.meta.badge_ne) ? p.meta.badge_ne : (p.meta.badge || p.cat);
    const catColor = p.meta.color || '#10b981';
    const svgCode = getProductSvg(p.art_key, p.art_params);

    return `
      <article class="glass-card rounded-2xl overflow-hidden border border-white/10 hover:border-emerald-400/50 transition-all flex flex-col justify-between group">
        
        <div>
          <!-- Media Header (Photo / Ultra High-Tech CAD Blueprint Mode) -->
          <div class="relative h-48 overflow-hidden">
            
            ${{currentCatalogViewMode === 'photo' ? `
              <div class="w-full h-full bg-slate-950 relative">
                <img src="${{p.photo}}" alt="${{p.name}} — Model ${{p.code}} Annapurna Aluminium Janakpur" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy">
                <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent"></div>
              </div>
            ` : `
              <div class="cad-blueprint-box w-full h-full flex items-center justify-center p-4">
                <div class="corner-bracket cb-tl"></div>
                <div class="corner-bracket cb-tr"></div>
                <div class="corner-bracket cb-bl"></div>
                <div class="corner-bracket cb-br"></div>
                
                <div class="absolute top-2.5 right-2.5 px-2 py-0.5 rounded bg-slate-950/90 border border-cyan-500/40 text-[9px] font-mono font-bold text-amber-300 z-10 shadow-md">
                  📐 ISO 9001:2026 CAD
                </div>

                <svg class="cad-art" viewBox="0 0 200 160" preserveAspectRatio="xMidYMid meet" aria-label="${{p.name}} CAD Blueprint">
                  ${{svgCode}}
                </svg>

                <div class="cad-title-stamp">
                  <div class="stamp-header">ANNAPURNA ARCHITECTURAL CAD</div>
                  <div class="flex justify-between gap-2 font-mono text-[7px] text-cyan-200">
                    <span>DWG: AP-${{p.code}}</span>
                    <span>SCALE: 1:10</span>
                  </div>
                  <div class="font-mono text-[6.5px] text-emerald-400 font-bold">
                    TOLERANCE ±0.05mm · AL6063-T6
                  </div>
                </div>
              </div>
            `}}

            <!-- Top Badges -->
            <div class="absolute top-3 left-3 flex items-center gap-1.5 z-10">
              <span class="px-2.5 py-0.5 rounded-md text-[10px] font-black font-mono uppercase bg-slate-950/90 text-white border border-white/10 shadow-lg">
                ${{p.code}}
              </span>
              <span class="px-2.5 py-0.5 rounded-md text-[10px] font-bold text-slate-950 shadow-md" style="background-color: ${{catColor}}">
                ${{catBadge}}
              </span>
            </div>

            <!-- Card View Toggle -->
            <button onclick="toggleSingleCardView('${{p.code}}')" class="absolute top-3 right-3 z-10 px-2 py-1 rounded-lg bg-slate-950/85 hover:bg-slate-900 text-[10px] font-bold text-slate-300 hover:text-emerald-400 border border-white/10 transition-all" title="Toggle Blueprint / Photo">
              ${{currentCatalogViewMode === 'photo' ? '📐 CAD Blueprint' : '📸 Photo'}}
            </button>

          </div>

          <!-- Product Info -->
          <div class="p-5 space-y-3">
            <h3 class="font-bold font-display text-base text-white leading-snug">${{p.name}}</h3>
            <p class="text-xs text-slate-300 leading-relaxed">${{p.desc}}</p>

            <!-- Standard Sizes -->
            <div class="text-[11px]">
              <span class="text-slate-400 font-semibold block mb-1">${{currentLang === 'ne' ? 'मानक आकारहरू:' : 'Standard Sizes:'}}</span>
              <div class="flex flex-wrap gap-1">
                ${{p.sizes.map(s => `<span class="px-2 py-0.5 rounded bg-slate-950 text-slate-300 border border-white/5 font-mono">${{s}}</span>`).join('')}}
              </div>
            </div>

            <!-- Key Features -->
            <div class="space-y-1 text-[11px] text-slate-400 border-t border-white/5 pt-2">
              ${{p.extras.slice(0, 2).map(e => `<div class="flex items-center gap-1.5"><span class="text-emerald-400 font-bold">✓</span><span>${{e}}</span></div>`).join('')}}
            </div>
          </div>
        </div>

        <!-- Footer CTA (Direct to WhatsApp) -->
        <div class="p-4 bg-slate-950/80 border-t border-white/5 flex items-center justify-between gap-2">
          <a href="#booking" class="text-xs font-bold text-emerald-400 hover:underline">
            ${{currentLang === 'ne' ? 'नाप जाँच बुक' : 'Book Measurement'}}
          </a>
          
          <a href="https://wa.me/${{SHOP.whatsapp}}?text=Namaste%20Annapurna,%20I%20want%20to%20order/inquire%20Product%20Code:%20${{p.code}}%20(${{encodeURIComponent(p.name)}})" target="_blank" rel="noopener" class="px-3 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs flex items-center gap-1 shadow-md">
            <span>💬</span> <span>${{currentLang === 'ne' ? 'ह्वाट्सएप' : 'WhatsApp'}}</span>
          </a>
        </div>

      </article>
    `;
  }}).join('');
}}

function filterCatalog(cat) {{
  currentCatalogCategory = cat;
  document.querySelectorAll('.cat-pill').forEach(pill => {{
    if (pill.getAttribute('data-cat') === cat) {{
      pill.className = 'cat-pill px-4 py-2 rounded-xl text-xs font-bold whitespace-nowrap bg-emerald-500 text-white shadow-md';
    }} else {{
      pill.className = 'cat-pill px-4 py-2 rounded-xl text-xs font-bold whitespace-nowrap bg-slate-900 text-slate-300 hover:text-white border border-white/10 transition-all';
    }}
  }});
  renderCatalog();
}}

function handleCatalogSearch() {{
  const val = document.getElementById('catalog-search').value;
  currentCatalogSearch = val;
  const clearBtn = document.getElementById('clear-search-btn');
  if (clearBtn) {{
    if (val) clearBtn.classList.remove('hidden');
    else clearBtn.classList.add('hidden');
  }}
  renderCatalog();
}}

function clearCatalogSearch() {{
  document.getElementById('catalog-search').value = '';
  currentCatalogSearch = '';
  document.getElementById('clear-search-btn').classList.add('hidden');
  renderCatalog();
}}

function setCatalogViewMode(mode) {{
  currentCatalogViewMode = mode;
  const photoBtn = document.getElementById('view-mode-photo');
  const blueprintBtn = document.getElementById('view-mode-blueprint');
  
  if (mode === 'photo') {{
    photoBtn.className = 'px-3 py-1.5 rounded-lg bg-emerald-500 text-white transition-all flex items-center gap-1.5';
    blueprintBtn.className = 'px-3 py-1.5 rounded-lg text-slate-400 hover:text-white transition-all flex items-center gap-1.5';
  }} else {{
    blueprintBtn.className = 'px-3 py-1.5 rounded-lg bg-emerald-500 text-white transition-all flex items-center gap-1.5';
    photoBtn.className = 'px-3 py-1.5 rounded-lg text-slate-400 hover:text-white transition-all flex items-center gap-1.5';
  }}
  renderCatalog();
}}

function toggleSingleCardView(code) {{
  setCatalogViewMode(currentCatalogViewMode === 'photo' ? 'blueprint' : 'photo');
}}

/* ==================== LIGHTBOX SYSTEM WITH CAROUSEL ==================== */
let activeLightboxIndex = -1;

function openLightboxProject(id) {{
  const index = REAL_PROJECTS.findIndex(p => p.id === id);
  if (index === -1) return;
  activeLightboxIndex = index;
  updateLightboxContent();
  document.getElementById('lightbox-modal').classList.remove('hidden');
  document.body.style.overflow = 'hidden';
}}

function updateLightboxContent() {{
  if (activeLightboxIndex < 0 || activeLightboxIndex >= REAL_PROJECTS.length) return;
  const proj = REAL_PROJECTS[activeLightboxIndex];
  
  const title = currentLang === 'ne' && proj.title_ne ? proj.title_ne : proj.title;
  const category = currentLang === 'ne' && proj.category_ne ? proj.category_ne : proj.category;
  const location = currentLang === 'ne' && proj.location_ne ? proj.location_ne : proj.location;
  const desc = currentLang === 'ne' && proj.desc_ne ? proj.desc_ne : proj.desc;

  document.getElementById('lightbox-img').src = 'catalog_assets/real_projects/' + proj.image;
  document.getElementById('lightbox-cat').innerText = category;
  document.getElementById('lightbox-title').innerText = title;
  document.getElementById('lightbox-loc').innerText = '📍 ' + location;
  document.getElementById('lightbox-desc').innerText = desc;
  document.getElementById('lightbox-counter').innerText = `${{activeLightboxIndex + 1}} / ${{REAL_PROJECTS.length}}`;
  
  const specsContainer = document.getElementById('lightbox-specs');
  specsContainer.innerHTML = proj.specs.map(s => `<div class="flex items-center gap-1.5"><span class="text-emerald-400 font-bold">✓</span><span>${{s}}</span></div>`).join('');
}}

function prevLightbox() {{
  if (activeLightboxIndex > 0) {{
    activeLightboxIndex--;
    updateLightboxContent();
  }} else {{
    activeLightboxIndex = REAL_PROJECTS.length - 1;
    updateLightboxContent();
  }}
}}

function nextLightbox() {{
  if (activeLightboxIndex < REAL_PROJECTS.length - 1) {{
    activeLightboxIndex++;
    updateLightboxContent();
  }} else {{
    activeLightboxIndex = 0;
    updateLightboxContent();
  }}
}}

function closeLightbox() {{
  document.getElementById('lightbox-modal').classList.add('hidden');
  document.body.style.overflow = 'auto';
}}

function inquireLightboxItem() {{
  if (activeLightboxIndex < 0) return;
  const item = REAL_PROJECTS[activeLightboxIndex];
  const msg = `Namaste Annapurna,%0A%0AI saw this project on your website and want something similar for my building:%0A• Title: ${{encodeURIComponent(item.title)}}%0A• Location Reference: ${{encodeURIComponent(item.location)}}%0A%0APlease schedule a site visit for measurement.`;
  window.open(`https://wa.me/${{SHOP.whatsapp}}?text=${{msg}}`, '_blank');
}}

document.addEventListener('keydown', (e) => {{
  if (!document.getElementById('lightbox-modal').classList.contains('hidden')) {{
    if (e.key === 'ArrowLeft') prevLightbox();
    if (e.key === 'ArrowRight') nextLightbox();
    if (e.key === 'Escape') closeLightbox();
  }}
}});

/* ==================== FAQ ACCORDION ==================== */
function toggleFaq(num) {{
  const content = document.getElementById('faq-content-' + num);
  const icon = document.getElementById('faq-icon-' + num);
  if (!content) return;

  if (content.classList.contains('hidden')) {{
    content.classList.remove('hidden');
    icon.innerText = '−';
  }} else {{
    content.classList.add('hidden');
    icon.innerText = '+';
  }}
}}

/* ==================== CONTACT FORM HANDLER ==================== */
function handleContactSubmit(e) {{
  e.preventDefault();
  const name = document.getElementById('form-name').value;
  const phone = document.getElementById('form-phone').value;
  const city = document.getElementById('form-city').value;
  const service = document.getElementById('form-service').value;
  const notes = document.getElementById('form-notes').value;

  const msg = `Namaste Annapurna Aluminium,%0A%0AI would like to request a free site visit / measurement:%0A• Name: ${{name}}%0A• Phone/WhatsApp: ${{phone}}%0A• Location: ${{city}}%0A• Requirement: ${{service}}%0A• Details: ${{notes}}%0A%0APlease contact me to confirm the schedule.`;

  window.open(`https://wa.me/${{SHOP.whatsapp}}?text=${{msg}}`, '_blank');
}}

function toggleMobileMenu() {{
  const menu = document.getElementById('mobile-menu');
  if (menu) menu.classList.toggle('hidden');
}}

/* ==================== PREMIUM BACKGROUND PRODUCT SHOWCASE SLIDESHOW ENGINE (v3.4 · Cinematic Crossfade · 4.5s Auto-Slide) ==================== */
const bgProductSlides = [
  {{ img: "catalog_assets/products/ALW-01.jpg", name: "ALW-01 Heavy Duty Sliding Window System", cat: "Aluminium Windows" }},
  {{ img: "catalog_assets/products/UWC-01.jpg", name: "UWC-01 German Profile Thermal UPVC Casement Window", cat: "UPVC Windows" }},
  {{ img: "catalog_assets/products/GLZ-01.jpg", name: "GLZ-01 Commercial Structural Curtain Wall Glazing", cat: "Curtain Glazing" }},
  {{ img: "catalog_assets/products/RLS-01.jpg", name: "RLS-01 Toughened Glass Balcony Railing Profile", cat: "Glass Railings" }},
  {{ img: "catalog_assets/products/MOD-01.jpg", name: "MOD-01 Waterproof Modular Kitchen Aluminium Rack", cat: "Modular Kitchen" }},
  {{ img: "catalog_assets/products/STF-01.jpg", name: "STF-01 304 Grade Stainless Steel Main Security Gate", cat: "SS Security Gates" }},
  {{ img: "catalog_assets/products/UWD-01.jpg", name: "UWD-01 Soundproof Double Glazed UPVC Entry Door", cat: "UPVC Doors" }},
  {{ img: "catalog_assets/products/ALD-01.jpg", name: "ALD-01 Modern Luxury Aluminium Entry Door", cat: "Aluminium Doors" }},
  {{ img: "catalog_assets/products/ALP-01.jpg", name: "ALP-01 Acoustic Glass Interior Partition Profile", cat: "Glass Partitions" }},
  {{ img: "catalog_assets/products/MST-01.jpg", name: "MST-01 Anti-Mosquito SS Mesh Security Window", cat: "Mesh Screens" }},
  {{ img: "catalog_assets/products/SLS-01.jpg", name: "SLS-01 Exterior Architectural Louver & Sunshade", cat: "Sunshades & Louvers" }},
  {{ img: "catalog_assets/products/ALW-04.jpg", name: "ALW-04 Panoramic 3-Track Slider Window", cat: "Aluminium Windows" }},
  {{ img: "catalog_assets/products/UWC-05.jpg", name: "UWC-05 Tilt & Turn Insulation UPVC Window", cat: "UPVC Windows" }},
  {{ img: "catalog_assets/products/GLZ-03.jpg", name: "GLZ-03 High-Rise ACP Cladding Facade", cat: "Curtain Glazing" }},
  {{ img: "catalog_assets/products/RLS-03.jpg", name: "RLS-03 Frameless Spigot Glass Balustrade", cat: "Glass Railings" }},
  {{ img: "catalog_assets/products/STF-05.jpg", name: "STF-05 Custom Stainless Steel Spiral Staircase", cat: "SS Railings & Stairs" }},
  {{ img: "catalog_assets/products/ALD-04.jpg", name: "ALD-04 Slimline Folding Sliding Glass Door", cat: "Aluminium Doors" }}
];

let currentBgIdx = 0;

/* v3.4 · Premium background engine — one 4.5s slide interval, smooth 1.8s crossfade,
   Ken Burns motion on the photo layer only (content stays rock-steady & readable). */
const BG_SLIDE_INTERVAL_MS = 4500;

function initBgSlideshow() {{
  const layerA = document.getElementById('bg-slide-a');
  const layerB = document.getElementById('bg-slide-b');
  const ticker = document.getElementById('bg-slide-ticker');
  const counter = document.getElementById('bg-slide-counter');
  const progress = document.getElementById('bg-slide-progress');
  if (!layerA || !layerB) return;

  const reducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const layers = [layerA, layerB];
  let activeLayer = 0;

  const imgOf = (layer) => layer.querySelector('.hero-slide-img');
  const pad = (n) => String(n).padStart(2, '0');

  function updateTicker(slide, index) {{
    if (ticker) {{
      ticker.innerHTML = `<span class="px-1.5 py-0.5 rounded bg-emerald-500/15 text-emerald-300 text-[9px] font-bold uppercase tracking-wider mr-1.5 border border-emerald-400/25">${{slide.cat}}</span> 📸 <span class="text-amber-300 font-bold">${{slide.name}}</span>`;
    }}
    if (counter) {{
      counter.innerText = `${{pad(index + 1)}} / ${{pad(bgProductSlides.length)}}`;
    }}
  }}

  function restartProgress() {{
    if (!progress) return;
    progress.style.animation = 'none';
    void progress.offsetWidth;
    progress.style.animation = '';
  }}

  function showSlide(layer, slide, index, animate, onRevealed) {{
    const img = imgOf(layer);
    const reveal = () => {{
      img.style.backgroundImage = `url('${{slide.img}}')`;
      if (!reducedMotion) {{
        img.classList.remove('play');
        void img.offsetWidth;
        img.classList.add('play');
      }}
      layer.classList.add('is-active');
      updateTicker(slide, index);
      restartProgress();
      if (typeof onRevealed === 'function') onRevealed();
    }};
    const pre = new Image();
    pre.onload = reveal;
    pre.onerror = reveal;
    pre.src = slide.img;
  }}

  // Initial slide
  imgOf(layerA).style.backgroundImage = `url('${{bgProductSlides[0].img}}')`;
  layerA.classList.add('is-active');
  if (!reducedMotion) imgOf(layerA).classList.add('play');
  updateTicker(bgProductSlides[0], 0);
  restartProgress();

  setInterval(() => {{
    currentBgIdx = (currentBgIdx + 1) % bgProductSlides.length;
    const prevLayer = layers[activeLayer];
    activeLayer = (activeLayer + 1) % 2;
    showSlide(layers[activeLayer], bgProductSlides[currentBgIdx], currentBgIdx, true, () => {{
      // Let the new photo settle on top, then let the old one dissolve away (no hard cut)
      setTimeout(() => prevLayer.classList.remove('is-active'), 1000);
    }});
  }}, BG_SLIDE_INTERVAL_MS);
}}

/* v3.6 · Animated count-up for hero stats (starts when the stat band enters the viewport) */
function initHeroCounters() {{
  const counters = document.querySelectorAll('[data-count-target]');
  if (!counters.length) return;

  const setFinal = (el) => {{
    const target = Number(el.getAttribute('data-count-target') || 0);
    const suffix = el.getAttribute('data-count-suffix') || '';
    el.textContent = target + suffix;
  }};

  const reducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const animateOne = (el) => {{
    const target = Number(el.getAttribute('data-count-target') || 0);
    const suffix = el.getAttribute('data-count-suffix') || '';
    const duration = 1500;
    const start = performance.now();
    const easeOutExpo = (t) => t === 1 ? 1 : 1 - Math.pow(2, -10 * t);

    if (reducedMotion) {{
      setFinal(el);
      return;
    }}

    const tick = (now) => {{
      const progress = Math.min((now - start) / duration, 1);
      const value = Math.round(easeOutExpo(progress) * target);
      el.textContent = value + suffix;
      if (progress < 1) requestAnimationFrame(tick);
      else setFinal(el);
    }};
    requestAnimationFrame(tick);
  }};

  if (!('IntersectionObserver' in window)) {{
    counters.forEach(setFinal);
    return;
  }}

  const observer = new IntersectionObserver((entries) => {{
    entries.forEach((entry) => {{
      if (!entry.isIntersecting) return;
      animateOne(entry.target);
      observer.unobserve(entry.target);
    }});
  }}, {{ threshold: 0.3 }});
  counters.forEach((el) => observer.observe(el));
}}

/* ==================== INITIALIZATION ==================== */
document.addEventListener('DOMContentLoaded', () => {{
  initBgSlideshow();
  initHeroCounters();
  renderAutoMarquee();
  renderRealProjects();
  renderCatalogCategoryPills();
  renderCatalog();
}});
</script>

</body>
</html>
"""

# Janakpur-area local SEO: keyword-first title, crawlable hub, extra FAQs
from seo_janakpur import enhance_homepage, generate_local_seo  # noqa: E402

html_content = enhance_homepage(html_content, SHOP)

# Write root index.html
index_path = ROOT / "index.html"
index_path.write_text(html_content, encoding="utf-8")
print(f"Successfully generated root website: {index_path} ({len(html_content)} bytes)")

# Write catalog/catalog.html
catalog_html_path = CATALOG_DIR / "catalog.html"
catalog_html_content = html_content.replace("catalog_assets/", "../catalog_assets/").replace("uploads/", "../uploads/")
catalog_html_path.write_text(catalog_html_content, encoding="utf-8")
print(f"Successfully generated catalog version: {catalog_html_path}")

# Sync Cloudflare deployment folder (dist) so every build automatically updates deployable assets
def sync_dist_html() -> None:
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "index.html", DIST_DIR / "index.html")
    shutil.copytree(ASSETS, DIST_DIR / "catalog_assets")
    (DIST_DIR / "catalog").mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "catalog" / "catalog.html", DIST_DIR / "catalog" / "catalog.html")
    for name in ("_headers", "robots.txt", "sitemap.xml", "favicon.ico"):
        src = ROOT / name
        if src.exists():
            shutil.copy2(src, DIST_DIR / name)
    uploads_src = ROOT / "uploads"
    if uploads_src.exists():
        uploads_dst = DIST_DIR / "uploads"
        uploads_dst.mkdir(parents=True, exist_ok=True)
        # Only copy files that are referenced by the site; the rest live in root uploads/ (not deployed).
        for name in ("chatbot_icon.png", "owner_image.jpg", "owner_professional.jpg"):
            src = uploads_src / name
            if src.exists():
                shutil.copy2(src, uploads_dst / name)
    print(f"Synced deployed dist/ assets: {DIST_DIR}")

sync_dist_html()
generate_local_seo(ROOT, DIST_DIR, SHOP)

print("Master Portal with Ultra-Premium AI Chatbot execution complete!")
