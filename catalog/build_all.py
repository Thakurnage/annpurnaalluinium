#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Annapurna Aluminium & UPVC — Ultra-Premium Master Website Builder
Features:
- Ultra-luxury modern architectural glassmorphism design
- Seamless Dual-Language Support (English & नेपाली)
- Authentic Real Workshop Projects Gallery (40+ high-res photos with Lightbox)
- 102+ Master Product Catalog with Blueprint / Photo dual-view toggle
- Free Site Visit & Architectural Consultation Booking
- Factory Standards & Material Quality Matrix
- Google Business Profile & Nepal-wide service area
- Fully removed PAN references and Price Calculator
"""
import base64
import html
import io
import json
import os
import re
import subprocess
import sys
from pathlib import Path

# Workspace paths
ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "catalog_assets"
REAL_PROJ_DIR = ASSETS / "real_projects"
PRODUCTS_DIR = ASSETS / "products"
CATALOG_DIR = ROOT / "catalog"
sys.path.insert(0, str(CATALOG_DIR))

from products_data import P, CATS, BASE_FEATS  # noqa: E402

# Business details (PAN completely removed)
SHOP = {
    "name": "Annapurna Aluminium & UPVC",
    "legal_name": "Annapurna Aluminium & UPVC Udhyog",
    "tagline": "UPVC Windows & Doors · Aluminium Partitions · Toughened Glass · SS Steel Works",
    "owner_name": "Prof. Nageshwar Thakur",
    "phone1": "+977 9817658719",
    "phone2": "+977 9817667115",
    "phone1_raw": "9817658719",
    "phone2_raw": "9817667115",
    "whatsapp": "9779817658719",
    "address": "Janakpur Dham-8, Murli Chowk (Airport Road), Dhanusha, Madhesh Province, Nepal",
    "address_short": "Murli Chowk (Airport Road), Janakpur Dham-8, Dhanusha",
    "gmaps_url": "https://maps.google.com/?q=Murli+Chowk+Airport+Road+Janakpur+Nepal",
    "hours": "Sunday – Saturday: 9:00 AM – 7:00 PM (All 7 Days Open)",
    "province": "Madhesh Province",
    "country": "Nepal",
    "service_areas": [
        "Janakpur Dham", "Dhanusha", "Mahottari (Jaleshwor)", "Sarlahi (Malangwa)",
        "Siraha (Lahan)", "Sindhuli (Bardibas)", "Udayapur (Gaighat)", "Rajbiraj",
        "Birgunj", "Hetauda", "Kathmandu", "Nepal-Wide Supply & Installation"
    ]
}

# Real projects catalog data
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
        "desc": "Stunning internal staircase balustrade featuring solid black acrylic inserts, mirror-finish SS 304 handrails, and round crystal finials.",
        "desc_ne": "कालो एक्रिलिक पिलर, क्रिस्टल बल र ५० मिमी एसएस ३०४ ह्यान्डरेल जडित आकर्षक भर्याङ रेलिङ।",
        "specs": ["SS 304 50mm Round Handrail", "Crystal & Acrylic Balusters", "Core-Drilled Anchoring", "Rigid Wobble-Free Safety"]
    },
    {
        "id": "rp-10",
        "image": "crystal_acrylic_ss_pillars.jpg",
        "thumb": "thumb_crystal_acrylic_ss_pillars.jpg",
        "title": "Amber Gold, Royal Blue & Clear Crystal Acrylic Master Pillars",
        "title_ne": "एम्बर गोल्ड, रोयल ब्लु र क्रिस्टल डायमण्ड मास्टर पिलरहरू",
        "category": "Luxury Pillars & Hardware",
        "category_ne": "लक्जरी पिलर र फिटिङ्स",
        "cat_key": "SLS",
        "location": "Workshop Hardware Collection",
        "location_ne": "वर्कशप प्रिमियम कलेक्सन",
        "desc": "Premium hand-cut crystal acrylic newel posts with internal light-refracting bubbles and stainless steel mirror-polished bases.",
        "desc_ne": "भर्याङको सुरुवाती पिलरको लागि विभिन्न रङ्गका आकर्षक क्रिस्टल एक्रिलिक मास्टर पिलरहरू।",
        "specs": ["Solid High-Grade Acrylic", "SS 304 Flange Mounts", "Prism Light Refraction", "Exclusive Luxury Styling"]
    },
    {
        "id": "rp-11",
        "image": "office_partition_corridor.jpg",
        "thumb": "thumb_office_partition_corridor.jpg",
        "title": "Corporate Office Corridor Black Aluminium & Glass Partition",
        "title_ne": "कर्पोरेट अफिस कोरिडोर कालो आल्मुनियम र ग्लास पार्टिसन",
        "category": "Aluminium Partitions",
        "category_ne": "आल्मुनियम पार्टिसन",
        "cat_key": "ALP",
        "location": "Commercial Office, Madhesh",
        "location_ne": "कर्पोरेट अफिस, मधेश प्रदेश",
        "desc": "Floor-to-ceiling sleek black powder-coated aluminium partition walls with acoustic sound reduction and tempered glass viewports.",
        "desc_ne": "म्याट ब्ल्याक पाउडर कोटेड आल्मुनियम फ्रेम र १० मिमी टफन्ड ग्लास जडित अफिस केबिन पार्टिसन।",
        "specs": ["Matte Black Powder Coating", "10mm Toughened Glass", "Acoustic Dampening", "Modular Relocatable System"]
    },
    {
        "id": "rp-12",
        "image": "commercial_frosted_partition.jpg",
        "thumb": "thumb_commercial_frosted_partition.jpg",
        "title": "Commercial Entrance Partition with Frosted Privacy Panels",
        "title_ne": "व्यावसायिक प्रवेशद्वार पार्टिसन फ्रोस्टेड ग्लास सहित",
        "category": "Aluminium Partitions",
        "category_ne": "आल्मुनियम पार्टिसन",
        "cat_key": "ALP",
        "location": "Janakpur Retail Store",
        "location_ne": "जनकपुरधाम रिटेल स्टोर",
        "desc": "Heavy-duty commercial glass entrance with upper glass transom and frosted bottom panels for customer flow and privacy.",
        "desc_ne": "माथिल्लो भागमा पारदर्शी ग्लास र तल्लो भागमा फ्रोस्टेड प्राइभेसी प्यानल भएको कमर्सियल प्रवेशद्वार।",
        "specs": ["Heavy Commercial Sections", "Sandblasted Privacy Panels", "Overhead Transom Glazing", "Smooth Pivot Door"]
    },
    {
        "id": "rp-13",
        "image": "stair_ss_horizontal_railing.jpg",
        "thumb": "thumb_stair_ss_horizontal_railing.jpg",
        "title": "Modern SS 304 Staircase Railing with 4-Line Safety Pipes",
        "title_ne": "आधुनिक एसएस ३०४ भर्याङ रेलिङ ४-लाइन सुरक्षा पाइप",
        "category": "Stainless Steel Railings",
        "category_ne": "स्टेनलेस स्टील रेलिङ",
        "cat_key": "SLS",
        "location": "Residential Home, Janakpur",
        "location_ne": "जनकपुरधाम नयाँ आवास",
        "desc": "Sleek minimalist stainless steel handrail system with 4 horizontal intermediate safety guards and mirror-buffed finish.",
        "desc_ne": "बालबालिकाको पूर्ण सुरक्षाको लागि ४ वटा होरिजोन्टल पाइप र मिरर फिनिश एसएस ३०४ भर्याङ रेलिङ।",
        "specs": ["Continuous Ergonomic Handrail", "4-Line Horizontal Guards", "TIG Welded & Buffed", "Lifetime Anti-Rust Guarantee"]
    },
    {
        "id": "rp-14",
        "image": "balcony_ss_wave_railing.jpg",
        "thumb": "thumb_balcony_ss_wave_railing.jpg",
        "title": "Contemporary Stainless Steel Balcony Safety Railing (Wave Design)",
        "title_ne": "समकालीन स्टेनलेस स्टील बालकनी रेलिङ (वेभ डिजाइन)",
        "category": "Stainless Steel Railings",
        "category_ne": "स्टेनलेस स्टील रेलिङ",
        "cat_key": "RLS",
        "location": "First Floor Balcony, Dhanusha",
        "location_ne": "पहिलो तला बालकनी, धनुषा",
        "desc": "Decorative exterior balcony guard with interlocking laser-cut wave bars and circular accents in all-weather SS 304.",
        "desc_ne": "घरको बाहिरी सौन्दर्य बढाउने घुमाउरो वेभ बुट्टा भएको बलियो एसएस ३०४ बालकनी रेलिङ।",
        "specs": ["High Wind Load Rating", "Artistic Wave Motifs", "Heavy Base Anchors", "Weatherproof Shine"]
    },
    {
        "id": "rp-15",
        "image": "balcony_ss_arc_railing.jpg",
        "thumb": "thumb_balcony_ss_arc_railing.jpg",
        "title": "Architectural Curved Arc SS 304 Balcony Guard Railing",
        "title_ne": "आर्किटेक्चरल घुमाउरो एसएस ३०४ बालकनी गार्ड रेलिङ",
        "category": "Stainless Steel Railings",
        "category_ne": "स्टेनलेस स्टील रेलिङ",
        "cat_key": "RLS",
        "location": "Private Residence, Janakpur",
        "location_ne": "जनकपुरधाम निवास",
        "desc": "Precision-bent stainless steel arcs create an open, airy feeling while exceeding standard parapet safety height regulations.",
        "desc_ne": "आधुनिक आर्किटेक्चरल आर्क डिजाइनमा निर्मित उच्च सुरक्षा भएको स्टेनलेस स्टील बालकनी रेलिङ।",
        "specs": ["Exceeds Safety Standards", "Precision Pipe Bending", "SS 304 Marine Quality", "Zero Rust in Heavy Rains"]
    },
    {
        "id": "rp-16",
        "image": "window_upvc_colonial_grid.jpg",
        "thumb": "thumb_window_upvc_colonial_grid.jpg",
        "title": "Premium White UPVC 2-Track Sliding Window with Georgian Grids",
        "title_ne": "प्रिमियम सेतो यूपीभीसी २-ट्र्याक स्लाइडिङ झ्याल जर्जियन ग्रिड सहित",
        "category": "UPVC Windows",
        "category_ne": "यूपीभीसी झ्यालहरू",
        "cat_key": "UWC",
        "location": "Showcase Unit, Workshop",
        "location_ne": "वर्कशप शोकेस युनिट",
        "desc": "European styling with internal colonial muntin bars sealed inside the double glass unit for zero-dust cleaning and maximum elegance.",
        "desc_ne": "डबल ग्लास भित्र सिल गरिएको जर्जियन ग्रिड भएको प्रिमियम युरोपेली डिजाइनको यूपीभीसी स्लाइडिङ झ्याल।",
        "specs": ["Internal Georgian Grids", "Double Sealed uPVC Sash", "Smooth Bearing Rollers", "Sound & Heat Insulation"]
    },
    {
        "id": "rp-17",
        "image": "window_upvc_reflective_slider.jpg",
        "thumb": "thumb_window_upvc_reflective_slider.jpg",
        "title": "German-Profile UPVC Sliding Window with Blue Solar Reflective Glass",
        "title_ne": "यूपीभीसी स्लाइडिङ झ्याल निलो सौर्य परावर्तक गिलास",
        "category": "UPVC Windows",
        "category_ne": "यूपीभीसी झ्यालहरू",
        "cat_key": "UWC",
        "location": "Residential Installation",
        "location_ne": "जनकपुरधाम आवासीय भवन",
        "desc": "High thermal efficiency sliding window with solar-control blue reflective glass that keeps interiors 5-7°C cooler during Janakpur summer heat.",
        "desc_ne": "गर्मीको समयमा कोठालाई शीतल राख्ने निलो रिफ्लेक्टिभ ग्लास जडित जर्मन प्रोफाइल यूपीभीसी झ्याल।",
        "specs": ["Solar Heat Rejection", "Multi-Chamber Insulation", "Security Interlocking", "Mosquito Mesh Ready"]
    },
    {
        "id": "rp-18",
        "image": "window_woodgrain_casement_batch.jpg",
        "thumb": "thumb_window_woodgrain_casement_batch.jpg",
        "title": "Golden Oak Woodgrain Finished Casement Windows Ready for Delivery",
        "title_ne": "गोल्डेन ओक काठको फिनिश भएको विन्डो ब्याच डेलिभरीको लागि तयार",
        "category": "UPVC Windows",
        "category_ne": "यूपीभीसी झ्यालहरू",
        "cat_key": "UWC",
        "location": "Workshop Dispatch Area",
        "location_ne": "वर्कशप डेलिभरी एरिया",
        "desc": "Batch of luxury woodgrain laminated casement windows with blue tinted safety glass, ready for on-site villa installation.",
        "desc_ne": "काठ जस्तै देखिने आकर्षक गोल्डेन ओक ल्यामिनेटेड यूपीभीसी केसमेन्ट (पल्ला खोल्ने) झ्यालहरू।",
        "specs": ["UV-Resistant German Foil", "Friction Stay Hinges", "Multi-Point Espag Locking", "100% Termite Proof"]
    },
    {
        "id": "rp-19",
        "image": "window_aluminium_blue_slider.jpg",
        "thumb": "thumb_window_aluminium_blue_slider.jpg",
        "title": "Aluminium 2-Track Sliding Window with Blue Toughened Glass",
        "title_ne": "आल्मुनियम २-ट्र्याक स्लाइडिङ झ्याल निलो गिलास सहित",
        "category": "Aluminium Windows",
        "category_ne": "आल्मुनियम झ्यालहरू",
        "cat_key": "ALW",
        "location": "Residential Installation",
        "location_ne": "जनकपुरधाम आवास",
        "desc": "Precision powder-coated white aluminium sliding window with top fixed viewing transom and solar reflective blue safety glass.",
        "specs": ["Slim Aluminium Sightlines", "6063-T5 Architectural Alloy", "Smooth Glide Bottom Tracks", "Dual Flush Locks"]
    },
    {
        "id": "rp-20",
        "image": "door_woodgrain_teak_finish.jpg",
        "thumb": "thumb_door_woodgrain_teak_finish.jpg",
        "title": "Teak Woodgrain Finish Flush Door with UPVC Perimeter Frame",
        "title_ne": "सागवान काठको फिनिश भएको फ्लस ढोका यूपीभीसी फ्रेम सहित",
        "category": "UPVC Doors",
        "category_ne": "यूपीभीसी ढोकाहरू",
        "cat_key": "UWD",
        "location": "Bedroom Entry, Janakpur",
        "location_ne": "बेडरुम प्रवेशद्वार, जनकपुरधाम",
        "desc": "Elegant interior flush door combining real teak wood texture aesthetic with the zero-warp, zero-rot durability of uPVC framing.",
        "specs": ["Zero Warping or Swelling", "SS Lever Handles", "Gasketed Door Stop", "Maintenance-Free Surface"]
    },
    {
        "id": "rp-21",
        "image": "door_eurobond_panel.jpg",
        "thumb": "thumb_door_eurobond_panel.jpg",
        "title": "Eurobond Aluminium Composite Panel & Frosted Glass Door",
        "title_ne": "यूरोबोन्ड आल्मुनियम कम्पोजिट प्यानल र फ्रोस्टेड ढोका",
        "category": "Aluminium Doors",
        "category_ne": "आल्मुनियम ढोकाहरू",
        "cat_key": "ALD",
        "location": "Balcony / Washroom Door",
        "location_ne": "बाथरुम तथा बालकनी ढोका",
        "desc": "Durable interior/exterior door featuring Eurobond branded composite base panel and frosted obscure privacy glass top section.",
        "specs": ["Eurobond Certified ACP", "Frosted Obscure Privacy", "Heavy Aluminium Frame", "Water & Rust Proof"]
    },
    {
        "id": "rp-22",
        "image": "hardware_ss_glass_spigots.jpg",
        "thumb": "thumb_hardware_ss_glass_spigots.jpg",
        "title": "Heavy Duty SS 304 Solid Glass Spigots for Frameless Railings",
        "title_ne": "एसएस ३०४ सोलिड ग्लास स्पिगटहरू फ्रेमलेस रेलिङका लागि",
        "category": "Luxury Pillars & Hardware",
        "category_ne": "लक्जरी पिलर र फिटिङ्स",
        "cat_key": "GLZ",
        "location": "Hardware Warehouse Stock",
        "location_ne": "हार्डवेयर गोदाम",
        "desc": "Solid casting grade 304 stainless steel base clamps designed to clamp 10mm-15mm toughened glass panels securely without drilling glass.",
        "specs": ["Solid Casting SS 304", "Friction Clamp (No Drilling)", "Mirror / Satin Finish", "Supports 10-15mm Glass"]
    },
    {
        "id": "rp-23",
        "image": "glass_etched_palm_tree.jpg",
        "thumb": "thumb_glass_etched_palm_tree.jpg",
        "title": "Artistic Etched & Frosted Decorative Glass Panel (Palm Tree Art)",
        "title_ne": "कलात्मक नक्काशी गरिएको सजावटी फ्रोस्टेड ग्लास प्यानल",
        "category": "Glass Solutions",
        "category_ne": "ग्लास सोलुसन्स",
        "cat_key": "GLZ",
        "location": "Custom Glass Studio",
        "location_ne": "कस्टम ग्लास स्टुडियो",
        "desc": "Precision acid-etched and color-infilled frosted toughened glass panel depicting a tropical coconut palm tree for luxury doors and partitions.",
        "specs": ["Acid-Etched Permanent Art", "8mm Safety Toughened Glass", "Non-Fading Color Infill", "Custom Art Engraving Ready"]
    },
    {
        "id": "rp-24",
        "image": "workshop_live_fabrication.jpg",
        "thumb": "thumb_workshop_live_fabrication.jpg",
        "title": "Live Factory Fabrication: Master Craftsman Assembling UPVC Window Sash",
        "title_ne": "प्रत्यक्ष वर्कशप उत्पादन: मास्टर मिस्त्री द्वारा यूपीभीसी झ्याल निर्माण",
        "category": "Workshop & Team",
        "category_ne": "वर्कशप र टिम",
        "cat_key": "UWC",
        "location": "Janakpur Workshop, Murli Chowk",
        "location_ne": "मुरली चोक वर्कशप, जनकपुरधाम",
        "desc": "Precision miter cutting and fusion welding of multi-chamber uPVC profiles at our Janakpur Dham workshop.",
        "specs": ["Calibrated 45° Miter Cuts", "Thermal Fusion Welding", "Galvanized Steel Core", "100% Quality Inspection"]
    },
    {
        "id": "rp-25",
        "image": "onsite_ss_welding_installation.jpg",
        "thumb": "thumb_onsite_ss_welding_installation.jpg",
        "title": "On-Site Professional SS Railing TIG Welding & Mirror Buffing",
        "title_ne": "साइटमा एसएस रेलिङ टीआईजी वेल्डिङ र मिरर पोलिसिङ कार्य",
        "category": "Workshop & Team",
        "category_ne": "वर्कशप र टिम",
        "cat_key": "SLS",
        "location": "Client Installation Site",
        "location_ne": "ग्राहकको निर्माण स्थल",
        "desc": "Our skilled technicians perform inert gas TIG welding and multiple stages of diamond compound buffing to create flawless invisible joints.",
        "specs": ["Argon Shielded TIG Welding", "Diamond Compound Buffing", "Laser Level Alignment", "Clean Handover"]
    },
    {
        "id": "rp-26",
        "image": "shop_front_signboard.jpg",
        "thumb": "thumb_shop_front_signboard.jpg",
        "title": "Annapurna Aluminium & UPVC Udhyog Official Workshop Signboard",
        "title_ne": "अन्नपूर्णा आल्मुनियम एण्ड यूपीभीसी उद्योग आधिकारिक साइनबोर्ड",
        "category": "Workshop & Team",
        "category_ne": "वर्कशप र टिम",
        "cat_key": "STF",
        "location": "Murli Chowk Airport Road, Janakpur",
        "location_ne": "मुरली चोक एयरपोर्ट रोड, जनकपुरधाम",
        "desc": "Our established physical workshop in Janakpur Dham-8, trusted by thousands across Madhesh Province since inception.",
        "specs": ["Established Workshop", "Full Machinery Setup", "Direct Factory Price", "Open 9 AM - 7 PM Daily"]
    }
]

# Product to real photo mapping for rich visual fidelity
PRODUCT_REAL_PHOTO_MAP = {
    # UPVC Windows
    "UWC-01": "facade_commercial_plaza.jpg",
    "UWC-02": "window_upvc_colonial_grid.jpg",
    "UWC-03": "window_woodgrain_casement_batch.jpg",
    "UWC-04": "villa_upvc_doors_windows.jpg",
    "UWC-05": "window_upvc_installed_ventilator.jpg",
    "UWC-06": "window_upvc_reflective_slider.jpg",
    "UWC-07": "facade_glass_tower.jpg",
    "UWC-08": "door_islamic_arch_entry.jpg",
    "UWC-09": "window_aluminium_panoramic_corner.jpg",
    "UWC-10": "window_aluminium_panoramic_corner.jpg",
    "UWC-11": "villa_upvc_doors_windows.jpg",
    "UWC-12": "window_upvc_installed_ventilator.jpg",
    # UPVC Doors
    "UWD-01": "door_woodgrain_teak_finish.jpg",
    "UWD-02": "door_upvc_mosaic_glass.jpg",
    "UWD-03": "villa_upvc_doors_windows.jpg",
    "UWD-04": "commercial_frosted_partition.jpg",
    "UWD-05": "door_upvc_frosted_texture.jpg",
    "UWD-06": "villa_upvc_doors_windows.jpg",
    "UWD-07": "door_eurobond_panel.jpg",
    "UWD-08": "door_woodgrain_teak_finish.jpg",
    "UWD-09": "door_3d_floral_glass.jpg",
    "UWD-10": "door_islamic_arch_entry.jpg",
    # Aluminium Windows
    "ALW-01": "window_aluminium_blue_slider.jpg",
    "ALW-02": "window_aluminium_panoramic_corner.jpg",
    "ALW-03": "office_partition_corridor.jpg",
    "ALW-04": "window_aluminium_blue_slider.jpg",
    "ALW-05": "window_upvc_colonial_grid.jpg",
    "ALW-06": "commercial_frosted_partition.jpg",
    "ALW-07": "facade_glass_tower.jpg",
    "ALW-08": "facade_commercial_plaza.jpg",
    "ALW-09": "window_aluminium_panoramic_corner.jpg",
    "ALW-10": "window_upvc_installed_ventilator.jpg",
    # Aluminium Doors
    "ALD-01": "door_eurobond_panel.jpg",
    "ALD-02": "door_3d_floral_glass.jpg",
    "ALD-03": "door_islamic_arch_entry.jpg",
    "ALD-04": "commercial_frosted_partition.jpg",
    "ALD-05": "facade_islamic_triple_arches.jpg",
    "ALD-06": "door_woodgrain_teak_finish.jpg",
    "ALD-07": "door_upvc_frosted_texture.jpg",
    "ALD-08": "office_partition_corridor.jpg",
    # Aluminium Partitions
    "ALP-01": "office_partition_corridor.jpg",
    "ALP-02": "commercial_frosted_partition.jpg",
    "ALP-03": "office_partition_corridor.jpg",
    "ALP-04": "commercial_frosted_partition.jpg",
    "ALP-05": "facade_glass_tower.jpg",
    "ALP-06": "office_partition_corridor.jpg",
    "ALP-07": "commercial_frosted_partition.jpg",
    "ALP-08": "office_partition_corridor.jpg",
    # Glass Solutions
    "GLZ-01": "hardware_ss_glass_spigots.jpg",
    "GLZ-02": "hardware_ss_glass_clamps.jpg",
    "GLZ-03": "glass_etched_palm_tree.jpg",
    "GLZ-04": "facade_glass_tower.jpg",
    "GLZ-05": "facade_commercial_plaza.jpg",
    "GLZ-06": "hardware_ss_glass_spigots.jpg",
    "GLZ-07": "stair_black_marble_ss.jpg",
    "GLZ-08": "hardware_ss_glass_clamps.jpg",
    "GLZ-09": "glass_etched_palm_tree.jpg",
    "GLZ-10": "facade_glass_tower.jpg",
    # Storefront & Facade
    "STF-01": "facade_commercial_plaza.jpg",
    "STF-02": "facade_glass_tower.jpg",
    "STF-03": "onsite_acp_cladding_highrise.jpg",
    "STF-04": "facade_islamic_triple_arches.jpg",
    "STF-05": "commercial_frosted_partition.jpg",
    "STF-06": "facade_commercial_plaza.jpg",
    "STF-07": "facade_glass_tower.jpg",
    "STF-08": "shop_front_signboard.jpg",
    # MS & Steel Works
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
    # Stainless Steel
    "SLS-01": "stair_ss_horizontal_railing.jpg",
    "SLS-02": "stair_black_marble_ss.jpg",
    "SLS-03": "crystal_acrylic_ss_pillars.jpg",
    "SLS-04": "stair_wood_ss_newel_posts.jpg",
    "SLS-05": "crystal_balusters_showcase.jpg",
    "SLS-06": "balcony_ss_wave_railing.jpg",
    "SLS-07": "balcony_ss_arc_railing.jpg",
    "SLS-08": "onsite_ss_welding_installation.jpg",
    # Railings & Stairs
    "RLS-01": "balcony_ss_wave_railing.jpg",
    "RLS-02": "balcony_ss_arc_railing.jpg",
    "RLS-03": "balcony_ss_sunburst.jpg",
    "RLS-04": "stair_ss_horizontal_railing.jpg",
    "RLS-05": "stair_black_marble_ss.jpg",
    "RLS-06": "facade_glass_tower.jpg",
    "RLS-07": "stair_ss_horizontal_railing.jpg",
    "RLS-08": "balcony_ss_wave_railing.jpg",
    # Modular & Special
    "MOD-01": "kitchen_modular_lshape.jpg",
    "MOD-02": "kitchen_aluminium_racks.jpg",
    "MOD-03": "kitchen_installed_counter.jpg",
    "MOD-04": "kitchen_wall_cabinet.jpg",
    "MOD-05": "kitchen_modular_lshape.jpg",
    "MOD-06": "kitchen_aluminium_racks.jpg",
    "MOD-07": "kitchen_installed_counter.jpg",
    "MOD-08": "kitchen_wall_cabinet.jpg",
    "MOD-09": "kitchen_modular_lshape.jpg",
    "MOD-10": "kitchen_aluminium_racks.jpg",
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
    """Load pre-rendered SVGs from json."""
    svg_map_file = CATALOG_DIR / "svg_art_map.json"
    if svg_map_file.exists():
        try:
            return json.loads(svg_map_file.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}

print("Building Ultra-Premium Annapurna Website...")
svg_map = load_svg_map()
print(f"Loaded {len(svg_map)} technical SVG blueprints.")

# Read templates.js directly for client-side rendering
templates_js_raw = (CATALOG_DIR / "templates.js").read_text(encoding="utf-8")

# Convert products into rich JSON
products_list = []
for pr in P:
    code = pr["code"]
    cat = pr["cat"]
    real_photo = PRODUCT_REAL_PHOTO_MAP.get(code, "facade_commercial_plaza.jpg")
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

# Schema LocalBusiness (without PAN)
schema_local_business = {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": SHOP["legal_name"],
    "image": "catalog_assets/real_projects/facade_commercial_plaza.jpg",
    "@id": "https://annapurna-upvc-janakpur.com/#business",
    "url": "https://annapurna-upvc-janakpur.com/",
    "telephone": SHOP["phone1"],
    "priceRange": "$$",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Murli Chowk (Airport Road)",
        "addressLocality": "Janakpur Dham",
        "addressRegion": "Madhesh Province",
        "postalCode": "45600",
        "addressCountry": "NP"
    },
    "geo": {
        "@type": "GeoCoordinates",
        "latitude": 26.7288,
        "longitude": 85.9248
    },
    "openingHoursSpecification": {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "opens": "09:00",
        "closes": "19:00"
    },
    "founder": {
        "@type": "Person",
        "name": SHOP["owner_name"]
    }
}

schema_item_list = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "102+ UPVC, Aluminium, Glass & Steel Architectural Designs",
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
            "name": "What is the difference between UPVC and Aluminium windows?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "UPVC windows feature multi-chamber insulated profiles with superior acoustic soundproofing, zero heat transfer (thermal efficiency), and 100% weather sealing without maintenance. Aluminium windows offer ultra-slim aesthetic frames, immense structural rigidity, and custom powder-coated finishes suitable for large architectural spans and commercial storefronts."
            }
        },
        {
            "@type": "Question",
            "name": "Do you provide free site visits and custom measurement in Janakpur and nearby areas?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes! We provide free on-site measurement and consultation in Janakpur Dham, Dhanusha, Mahottari (Jaleshwor), Sarlahi (Malangwa), Siraha (Lahan), Sindhuli, and surrounding regions. Simply call or WhatsApp +977 9817658719 to book a visit."
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
        }
    ]
}

# Generate Ultra-Premium HTML
html_content = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Annapurna Aluminium &amp; UPVC | Janakpur Dham, Nepal | 102+ Custom Architectural Designs &amp; Real Workshop Gallery</title>
<meta name="description" content="Official website of Annapurna Aluminium &amp; UPVC Udhyog, Murli Chowk (Airport Road), Janakpur Dham. 102+ custom designs: German-profile UPVC windows, aluminium doors, toughened glass railings, SS 304 temple gates, modular kitchen racks, ACP facade glazing. Free site visit &amp; fast Nepal-wide delivery.">
<meta name="keywords" content="UPVC window Janakpur, UPVC window Nepal, aluminium door Janakpur, glass railing Nepal, SS 304 railing Janakpur, modular kitchen Nepal, ACP cladding Janakpur, temple gate fabrication Nepal, Murli Chowk Airport Road, Dhanusha glass works, Prof Nageshwar Thakur, Annapurna Aluminium">
<meta name="author" content="Annapurna Aluminium &amp; UPVC — Janakpur Dham">
<meta name="theme-color" content="#060a14">
<meta name="geo.region" content="NP-P2">
<meta name="geo.placename" content="Janakpur Dham, Dhanusha, Nepal">
<meta name="geo.position" content="26.7288;85.9248">

<!-- Open Graph / Meta -->
<meta property="og:type" content="website">
<meta property="og:title" content="Annapurna Aluminium &amp; UPVC | 102+ Custom Designs | Janakpur Dham, Nepal">
<meta property="og:description" content="Explore real workshop projects and 102+ custom designs of UPVC windows, aluminium partitions, SS 304 railings, temple gates, and modular kitchen racks in Janakpur Dham, Nepal.">
<meta property="og:image" content="catalog_assets/real_projects/facade_commercial_plaza.jpg">
<meta property="og:locale" content="en_US">
<meta property="og:locale:alternate" content="ne_NP">

<!-- Google Fonts (Plus Jakarta Sans & Outfit) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800;900&family=Noto+Sans+Devanagari:wght@400;500;600;700;800&display=swap" rel="stylesheet">

<!-- Tailwind CSS CDN -->
<script src="https://cdn.tailwindcss.com"></script>
<script>
tailwind.config = {{
  darkMode: 'class',
  theme: {{
    extend: {{
      fontFamily: {{
        sans: ['Plus Jakarta Sans', 'Noto Sans Devanagari', 'system-ui', 'sans-serif'],
        display: ['Outfit', 'Noto Sans Devanagari', 'sans-serif'],
      }},
      colors: {{
        luxury: {{
          950: '#040711',
          900: '#080d1a',
          850: '#0e1626',
          800: '#142036',
          700: '#1e2e4a',
          cyan: '#00d2ff',
          cyanGlow: 'rgba(0, 210, 255, 0.35)',
          gold: '#f59e0b',
          goldGlow: 'rgba(245, 158, 11, 0.35)',
          emerald: '#10b981',
          emeraldGlow: 'rgba(16, 185, 129, 0.35)',
        }}
      }},
      animation: {{
        'pulse-slow': 'pulse 3.5s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'float': 'float 6s ease-in-out infinite',
      }},
      keyframes: {{
        float: {{
          '0%, 100%': {{ transform: 'translateY(0)' }},
          '50%': {{ transform: 'translateY(-8px)' }},
        }}
      }}
    }}
  }}
}}
</script>

<style>
:root {{
  --bg-dark: #040711;
  --panel-bg: rgba(14, 22, 38, 0.75);
  --glass-border: rgba(255, 255, 255, 0.08);
  --cyan-glow: rgba(0, 210, 255, 0.3);
  --gold-glow: rgba(245, 158, 11, 0.3);
}}

body {{
  background-color: #040711;
  color: #f1f5f9;
  font-family: 'Plus Jakarta Sans', 'Noto Sans Devanagari', sans-serif;
  overflow-x: hidden;
}}

/* Ultra-Luxury Glassmorphism */
.glass-panel {{
  background: rgba(14, 22, 38, 0.72);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.08);
}}

.glass-nav {{
  background: rgba(4, 7, 17, 0.88);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}}

.glass-card {{
  background: linear-gradient(145deg, rgba(20, 32, 54, 0.65) 0%, rgba(8, 13, 26, 0.85) 100%);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.07);
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}}

.glass-card:hover {{
  transform: translateY(-6px);
  border-color: rgba(0, 210, 255, 0.4);
  box-shadow: 0 20px 40px -12px rgba(0, 210, 255, 0.18);
}}

.gold-card:hover {{
  border-color: rgba(245, 158, 11, 0.45);
  box-shadow: 0 20px 40px -12px rgba(245, 158, 11, 0.2);
}}

/* Blueprint SVG Container */
.blueprint-box {{
  background: radial-gradient(circle at center, #0e2440 0%, #061120 100%);
  border: 1px dashed rgba(0, 210, 255, 0.3);
  position: relative;
}}
.blueprint-box::before {{
  content: "";
  position: absolute;
  inset: 0;
  background-size: 24px 24px;
  background-image: 
    linear-gradient(to right, rgba(0, 210, 255, 0.06) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(0, 210, 255, 0.06) 1px, transparent 1px);
  pointer-events: none;
}}

.art {{
  width: 100%;
  height: 100%;
  max-height: 175px;
  filter: drop-shadow(0 4px 10px rgba(0,0,0,0.6));
}}

/* Custom scrollbar */
::-webkit-scrollbar {{
  width: 7px;
  height: 7px;
}}
::-webkit-scrollbar-track {{
  background: #040711;
}}
::-webkit-scrollbar-thumb {{
  background: #1e2e4a;
  border-radius: 4px;
}}
::-webkit-scrollbar-thumb:hover {{
  background: #00d2ff;
}}
</style>

<!-- JSON-LD Structured Data -->
<script type="application/ld+json">
{json.dumps(schema_local_business, ensure_ascii=False)}
</script>
<script type="application/ld+json">
{json.dumps(schema_faq, ensure_ascii=False)}
</script>
<script type="application/ld+json">
{json.dumps(schema_item_list, ensure_ascii=False)}
</script>
</head>

<body class="antialiased selection:bg-cyan-500 selection:text-black">

<!-- TOP NOTIFICATION & HOTLINE BAR -->
<div class="bg-gradient-to-r from-luxury-950 via-luxury-900 to-luxury-950 border-b border-white/5 py-2 px-4 text-xs">
  <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3 text-slate-300">
    
    <div class="flex items-center gap-3.5 flex-wrap">
      <span class="inline-flex items-center gap-1.5 px-3 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 font-semibold text-[11px]">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
        <span data-i18n="top_open">Workshop Open 7 Days · 9:00 AM – 7:00 PM</span>
      </span>
      <span class="hidden sm:inline text-slate-400 font-medium">📍 <span data-i18n="top_loc">Murli Chowk (Airport Road), Janakpur Dham-8, Dhanusha</span></span>
    </div>

    <div class="flex items-center gap-4">
      <!-- Dual Language Toggle (EN / नेपाली) -->
      <div class="flex items-center bg-slate-900/90 rounded-xl p-0.5 border border-white/10 text-xs shadow-inner">
        <button onclick="setLanguage('en')" id="lang-btn-en" class="px-2.5 py-1 rounded-lg font-bold bg-cyan-500 text-black transition-all shadow-sm">English</button>
        <button onclick="setLanguage('ne')" id="lang-btn-ne" class="px-2.5 py-1 rounded-lg font-bold text-slate-300 hover:text-white transition-all">नेपाली</button>
      </div>

      <!-- Direct Phone Call -->
      <a href="tel:{SHOP['phone1']}" class="flex items-center gap-1.5 text-cyan-400 font-bold hover:text-cyan-300 transition-colors text-xs">
        <span>📞</span> <span class="hidden sm:inline">{SHOP['phone1']}</span>
      </a>
    </div>

  </div>
</div>

<!-- MAIN NAVIGATION -->
<nav class="sticky top-0 z-50 glass-nav transition-all">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-20">
      
      <!-- Brand Logo -->
      <a href="#" class="flex items-center gap-3.5 group">
        <div class="w-12 h-12 rounded-2xl bg-gradient-to-tr from-cyan-500 via-blue-600 to-amber-400 p-0.5 shadow-xl group-hover:shadow-cyan-500/30 transition-all">
          <div class="w-full h-full bg-luxury-950 rounded-[14px] flex items-center justify-center text-xl font-black text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-amber-300">
            A
          </div>
        </div>
        <div>
          <div class="font-display font-extrabold text-lg sm:text-xl tracking-tight text-white flex items-center gap-1.5">
            Annapurna <span class="text-cyan-400 font-medium">Alu &amp; UPVC</span>
          </div>
          <p class="text-[11px] text-slate-400 tracking-wide font-medium" data-i18n="nav_subtitle">Janakpur Dham · Windows, Doors, Glass &amp; Steel Works</p>
        </div>
      </a>

      <!-- Desktop Nav Links -->
      <div class="hidden lg:flex items-center gap-6 text-sm font-semibold text-slate-300">
        <a href="#projects" class="hover:text-cyan-400 transition-colors flex items-center gap-1.5">
          <span class="text-cyan-400">✦</span> <span data-i18n="nav_projects">Real Projects (40+)</span>
        </a>
        <a href="#catalog" class="hover:text-cyan-400 transition-colors flex items-center gap-1.5">
          <span class="text-amber-400">◈</span> <span data-i18n="nav_catalog">102+ Design Catalog</span>
        </a>
        <a href="#standards" class="hover:text-cyan-400 transition-colors" data-i18n="nav_standards">Material Quality</a>
        <a href="#consultation" class="hover:text-cyan-400 transition-colors flex items-center gap-1">
          <span class="text-emerald-400">📝</span> <span data-i18n="nav_consult">Book Site Visit</span>
        </a>
        <a href="#founder" class="hover:text-cyan-400 transition-colors" data-i18n="nav_about">About &amp; Team</a>
        <a href="#contact" class="hover:text-cyan-400 transition-colors" data-i18n="nav_contact">Contact</a>
      </div>

      <!-- Quick Action Buttons -->
      <div class="hidden sm:flex items-center gap-3">
        <a href="https://wa.me/{SHOP['whatsapp']}?text=Namaste%20Annapurna%20Aluminium,%20I%20want%20to%20get%20a%20quote%20for%20my%20building%20project." target="_blank" rel="noopener" class="flex items-center gap-2 px-4 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition-all shadow-lg hover:shadow-emerald-500/25">
          <span>💬</span> <span data-i18n="btn_whatsapp">WhatsApp Quote</span>
        </a>
        <a href="tel:{SHOP['phone1']}" class="flex items-center gap-2 px-4 py-2.5 rounded-xl bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-extrabold text-xs transition-all shadow-lg hover:shadow-cyan-500/25">
          <span>📞</span> <span data-i18n="btn_call">Call Workshop</span>
        </a>
      </div>

      <!-- Mobile Menu Button -->
      <button onclick="toggleMobileMenu()" class="lg:hidden p-2.5 rounded-xl bg-slate-900 border border-white/10 text-slate-300 hover:text-white" aria-label="Toggle Navigation">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path></svg>
      </button>

    </div>
  </div>

  <!-- Mobile Dropdown -->
  <div id="mobile-menu" class="hidden lg:hidden border-t border-white/5 bg-luxury-950/98 backdrop-blur-2xl px-5 pt-4 pb-6 space-y-3 shadow-2xl">
    <a href="#projects" onclick="toggleMobileMenu()" class="block py-2 text-slate-200 hover:text-cyan-400 font-semibold">🌟 Real Projects Gallery (40+)</a>
    <a href="#catalog" onclick="toggleMobileMenu()" class="block py-2 text-slate-200 hover:text-cyan-400 font-semibold">📦 102+ Design Catalog</a>
    <a href="#standards" onclick="toggleMobileMenu()" class="block py-2 text-slate-200 hover:text-cyan-400 font-semibold">🔬 Material &amp; Factory Standards</a>
    <a href="#consultation" onclick="toggleMobileMenu()" class="block py-2 text-slate-200 hover:text-cyan-400 font-semibold">📝 Free Site Visit &amp; Measurement</a>
    <a href="#founder" onclick="toggleMobileMenu()" class="block py-2 text-slate-200 hover:text-cyan-400 font-semibold">👤 Founder &amp; Workshop Heritage</a>
    <a href="#contact" onclick="toggleMobileMenu()" class="block py-2 text-slate-200 hover:text-cyan-400 font-semibold">📍 Location &amp; Contact</a>
    <div class="pt-3 flex gap-2">
      <a href="https://wa.me/{SHOP['whatsapp']}?text=Namaste%20Annapurna%20Aluminium,%20I%20want%20to%20get%20a%20quote." target="_blank" class="flex-1 text-center py-3 rounded-xl bg-emerald-600 text-white font-bold text-xs">💬 WhatsApp</a>
      <a href="tel:{SHOP['phone1']}" class="flex-1 text-center py-3 rounded-xl bg-cyan-500 text-black font-extrabold text-xs">📞 Call Directly</a>
    </div>
  </div>
</nav>

<!-- HERO SECTION -->
<section class="relative min-h-[92vh] flex items-center justify-center overflow-hidden py-16 lg:py-24">
  <!-- Subtle Background Real Photo Mosaic -->
  <div class="absolute inset-0 z-0">
    <div class="absolute inset-0 bg-gradient-to-t from-luxury-950 via-luxury-950/85 to-luxury-950/65 z-10"></div>
    <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-cyan-950/30 via-transparent to-transparent z-10"></div>
    <img src="catalog_assets/real_projects/facade_commercial_plaza.jpg" alt="Annapurna Commercial Plaza Project" class="w-full h-full object-cover object-center filter blur-[2px] scale-105 opacity-35">
  </div>

  <div class="relative z-20 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
    
    <!-- Top Verified Pill -->
    <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 text-xs sm:text-sm font-bold mb-8 backdrop-blur-md shadow-xl shadow-cyan-500/10">
      <span class="text-amber-400">★ ★ ★ ★ ★</span>
      <span data-i18n="hero_badge">#1 Certified UPVC, Aluminium &amp; SS Fabrication Center · Janakpur Dham, Nepal</span>
    </div>

    <!-- Main Title -->
    <h1 class="font-display text-4xl sm:text-6xl lg:text-7xl font-black tracking-tight text-white max-w-5xl mx-auto leading-[1.12] mb-6">
      <span class="text-transparent bg-clip-text bg-gradient-to-r from-white via-slate-100 to-slate-300" data-i18n="hero_h1_1">World-Class</span> 
      <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-teal-300 to-blue-500" data-i18n="hero_h1_2">UPVC, Aluminium &amp; Glass</span> 
      <span class="text-transparent bg-clip-text bg-gradient-to-r from-amber-300 to-yellow-500" data-i18n="hero_h1_3">Craftsmanship</span>
    </h1>

    <!-- Subtitle in Multi-language -->
    <p class="text-base sm:text-xl text-slate-300 max-w-3xl mx-auto mb-10 leading-relaxed font-normal" data-i18n="hero_desc">
      102+ Custom Designs manufactured at our Janakpur workshop: German-profile UPVC windows, modern aluminium doors &amp; partitions, SS 304 temple gates, balustrades, modular kitchen racks, and commercial ACP glass facades.
    </p>

    <!-- Action Buttons -->
    <div class="flex flex-wrap items-center justify-center gap-4 mb-16">
      <a href="#projects" class="px-8 py-4 rounded-2xl bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-slate-950 font-black text-sm sm:text-base transition-all shadow-xl shadow-cyan-500/25 hover:shadow-cyan-500/40 hover:-translate-y-1 flex items-center gap-2">
        <span>📸</span> <span data-i18n="hero_btn_projects">Explore Real Project Photos</span>
      </a>
      <a href="#catalog" class="px-8 py-4 rounded-2xl bg-slate-900/90 hover:bg-slate-850 text-white font-bold text-sm sm:text-base border border-white/10 hover:border-cyan-500/40 transition-all backdrop-blur-md hover:-translate-y-1 flex items-center gap-2">
        <span>📐</span> <span data-i18n="hero_btn_catalog">Browse 102+ Catalog</span>
      </a>
      <a href="https://wa.me/{SHOP['whatsapp']}?text=Namaste%20Annapurna%20Aluminium,%20I%20want%20free%20site%20measurement%20and%20consultation." target="_blank" rel="noopener" class="px-8 py-4 rounded-2xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-sm sm:text-base transition-all shadow-xl shadow-emerald-600/25 hover:-translate-y-1 flex items-center gap-2">
        <span>💬</span> <span data-i18n="hero_btn_estimate">Free Site Measurement</span>
      </a>
    </div>

    <!-- Quick Stats Grid -->
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4 max-w-4xl mx-auto text-left">
      <div class="glass-panel p-5 rounded-2xl border border-white/10">
        <div class="text-3xl sm:text-4xl font-black font-display text-cyan-400 mb-1">102+</div>
        <div class="text-xs text-slate-400 font-semibold" data-i18n="stat_designs">Unique Custom Designs</div>
      </div>
      <div class="glass-panel p-5 rounded-2xl border border-white/10">
        <div class="text-3xl sm:text-4xl font-black font-display text-amber-400 mb-1">1,200+</div>
        <div class="text-xs text-slate-400 font-semibold" data-i18n="stat_sites">Completed Sites in Nepal</div>
      </div>
      <div class="glass-panel p-5 rounded-2xl border border-white/10">
        <div class="text-3xl sm:text-4xl font-black font-display text-emerald-400 mb-1">15+ Yrs</div>
        <div class="text-xs text-slate-400 font-semibold" data-i18n="stat_exp">Engineering Experience</div>
      </div>
      <div class="glass-panel p-5 rounded-2xl border border-white/10">
        <div class="text-3xl sm:text-4xl font-black font-display text-purple-400 mb-1">100%</div>
        <div class="text-xs text-slate-400 font-semibold" data-i18n="stat_quality">SS 304 &amp; Virgin Profiles</div>
      </div>
    </div>

  </div>
</section>

<!-- SECTION: REAL WORKSHOP & ON-SITE PROJECTS GALLERY -->
<section id="projects" class="py-20 relative bg-luxury-950/70 border-t border-white/5">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <!-- Section Header -->
    <div class="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-6">
      <div>
        <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/20 text-cyan-400 text-xs font-bold uppercase tracking-wider mb-3">
          🌟 Authentic Workshop &amp; Site Photos
        </div>
        <h2 class="text-3xl sm:text-5xl font-extrabold font-display text-white tracking-tight" data-i18n="projects_title">
          Real Projects by Annapurna
        </h2>
        <p class="text-slate-400 text-sm sm:text-base mt-2 max-w-2xl" data-i18n="projects_subtitle">
          Explore actual completed commercial facades, temple gates, modern residences, staircases, and modular kitchens fabricated right here at our Murli Chowk workshop.
        </p>
      </div>

      <!-- Live Filter Pills -->
      <div class="flex items-center gap-2 overflow-x-auto pb-2 max-w-full" id="project-filters">
        <button onclick="filterProjects('all')" class="proj-filter-btn px-4 py-2.5 rounded-xl text-xs font-bold transition-all bg-cyan-500 text-black shadow-lg shadow-cyan-500/20" data-cat="all" data-i18n="filter_all">All Projects (26)</button>
        <button onclick="filterProjects('STF')" class="proj-filter-btn px-4 py-2.5 rounded-xl text-xs font-bold transition-all bg-slate-900 text-slate-300 hover:text-white border border-white/10" data-cat="STF" data-i18n="filter_stf">Facades &amp; ACP</button>
        <button onclick="filterProjects('UWC')" class="proj-filter-btn px-4 py-2.5 rounded-xl text-xs font-bold transition-all bg-slate-900 text-slate-300 hover:text-white border border-white/10" data-cat="UWC" data-i18n="filter_uwc">UPVC Windows</button>
        <button onclick="filterProjects('SLS')" class="proj-filter-btn px-4 py-2.5 rounded-xl text-xs font-bold transition-all bg-slate-900 text-slate-300 hover:text-white border border-white/10" data-cat="SLS" data-i18n="filter_sls">SS Railings</button>
        <button onclick="filterProjects('MST')" class="proj-filter-btn px-4 py-2.5 rounded-xl text-xs font-bold transition-all bg-slate-900 text-slate-300 hover:text-white border border-white/10" data-cat="MST" data-i18n="filter_mst">Temple Gates</button>
        <button onclick="filterProjects('MOD')" class="proj-filter-btn px-4 py-2.5 rounded-xl text-xs font-bold transition-all bg-slate-900 text-slate-300 hover:text-white border border-white/10" data-cat="MOD" data-i18n="filter_mod">Kitchen Racks</button>
        <button onclick="filterProjects('ALP')" class="proj-filter-btn px-4 py-2.5 rounded-xl text-xs font-bold transition-all bg-slate-900 text-slate-300 hover:text-white border border-white/10" data-cat="ALP" data-i18n="filter_alp">Partitions</button>
      </div>
    </div>

    <!-- Projects Grid -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6" id="real-projects-grid">
      <!-- Rendered via JS dynamically for filtering & lightbox -->
    </div>

    <!-- View Full Photo Archive Trigger -->
    <div class="mt-12 text-center">
      <p class="text-xs text-slate-400 mb-3" data-i18n="projects_more_note">Looking for a specific architectural design or have your own custom blueprint?</p>
      <a href="https://wa.me/{SHOP['whatsapp']}?text=Namaste%20Annapurna,%20I%20have%20custom%20drawings%20for%20my%20building.%20Please%20review%20and%20quote." target="_blank" class="inline-flex items-center gap-2 px-6 py-3.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-cyan-400 border border-cyan-500/30 font-bold text-xs tracking-wide transition-all shadow-lg hover:shadow-cyan-500/15">
        <span>📤</span> <span data-i18n="projects_send_custom">Send Your Custom Blueprints on WhatsApp</span>
      </a>
    </div>

  </div>
</section>

<!-- SECTION: 102+ PRODUCT CATALOG EXPLORER -->
<section id="catalog" class="py-20 relative bg-luxury-950 border-t border-white/5">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <!-- Header -->
    <div class="text-center max-w-3xl mx-auto mb-12">
      <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-amber-500/10 border border-amber-500/20 text-amber-400 text-xs font-bold uppercase tracking-wider mb-3">
        📐 Complete Manufacturing Catalog
      </div>
      <h2 class="text-3xl sm:text-5xl font-extrabold font-display text-white tracking-tight" data-i18n="catalog_title">
        102+ Master Product Designs
      </h2>
      <p class="text-slate-400 text-sm sm:text-base mt-2" data-i18n="catalog_subtitle">
        Every product is precision-engineered, customizable to your exact structural measurements, and available in multiple finishes and glass configurations.
      </p>
    </div>

    <!-- Search & View Mode Controls -->
    <div class="glass-panel p-4 rounded-2xl mb-8 flex flex-col md:flex-row items-center justify-between gap-4">
      
      <!-- Instant Search Input -->
      <div class="relative w-full md:w-96">
        <input type="text" id="catalog-search" oninput="handleCatalogSearch()" placeholder="Search by name, code (e.g. UWC-01, Sliding, Gate)..." class="w-full px-4 py-2.5 pl-10 rounded-xl bg-slate-950/80 border border-white/10 text-white text-sm focus:outline-none focus:border-cyan-400 transition-colors">
        <span class="absolute left-3 top-2.5 text-slate-400">🔍</span>
        <button id="clear-search-btn" onclick="clearCatalogSearch()" class="hidden absolute right-3 top-2.5 text-xs text-slate-400 hover:text-white">✕</button>
      </div>

      <!-- View Switcher -->
      <div class="flex items-center gap-2 w-full md:w-auto justify-end">
        <span class="text-xs text-slate-400 font-semibold" data-i18n="catalog_view_mode">View Mode:</span>
        <div class="bg-slate-950 p-1 rounded-xl border border-white/10 flex items-center text-xs font-bold">
          <button onclick="setCatalogViewMode('photo')" id="view-mode-photo" class="px-3 py-1.5 rounded-lg bg-cyan-500 text-slate-950 transition-all flex items-center gap-1.5">
            <span>📸</span> <span data-i18n="view_photo">Photos</span>
          </button>
          <button onclick="setCatalogViewMode('blueprint')" id="view-mode-blueprint" class="px-3 py-1.5 rounded-lg text-slate-400 hover:text-white transition-all flex items-center gap-1.5">
            <span>📐</span> <span data-i18n="view_blueprint">Blueprint</span>
          </button>
        </div>
      </div>

    </div>

    <!-- Category Filter Tabs -->
    <div class="flex items-center gap-2 overflow-x-auto pb-4 mb-8" id="catalog-category-pills">
      <button onclick="filterCatalog('ALL')" class="cat-pill px-4 py-2.5 rounded-xl text-xs font-bold whitespace-nowrap bg-cyan-500 text-black shadow-lg shadow-cyan-500/20 transition-all" data-cat="ALL">
        All 102 Designs
      </button>
      {"".join([f'''<button onclick="filterCatalog('{c['key']}')" class="cat-pill px-4 py-2.5 rounded-xl text-xs font-bold whitespace-nowrap bg-slate-900/90 text-slate-300 hover:text-white border border-white/10 transition-all" data-cat="{c['key']}">
        {c['name']}
      </button>''' for c in CATS])}
    </div>

    <!-- Catalog Counter -->
    <div class="flex items-center justify-between text-xs text-slate-400 mb-6 px-1">
      <div>Showing <span id="catalog-count" class="font-bold text-cyan-400">102</span> products</div>
      <div class="text-slate-500 italic" data-i18n="custom_sizes_note">Custom sizes &amp; finishes fabricated for all models</div>
    </div>

    <!-- Catalog Products Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" id="products-container">
      <!-- Dynamically generated by JS -->
    </div>

  </div>
</section>

<!-- SECTION: MATERIAL & ENGINEERING STANDARDS MATRIX -->
<section id="standards" class="py-20 relative bg-luxury-950/80 border-t border-white/5">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <div class="text-center max-w-3xl mx-auto mb-16">
      <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/20 text-cyan-400 text-xs font-bold uppercase tracking-wider mb-3">
        🔬 Engineering Standards &amp; Materials
      </div>
      <h2 class="text-3xl sm:text-5xl font-extrabold font-display text-white tracking-tight" data-i18n="factory_title">
        Factory Machinery &amp; Raw Material Quality
      </h2>
      <p class="text-slate-400 text-sm sm:text-base mt-2" data-i18n="factory_subtitle">
        We never compromise on metal thickness, uPVC wall gauge, or welding standards. Here is how we ensure lifetime durability.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-16">
      
      <!-- Feature 1 -->
      <div class="glass-card p-7 rounded-3xl">
        <div class="w-14 h-14 rounded-2xl bg-cyan-500/20 text-cyan-400 flex items-center justify-center text-3xl mb-6 shadow-inner">
          🔬
        </div>
        <h3 class="text-lg font-bold text-white mb-2" data-i18n="mat_1_title">German Multi-Chamber UPVC</h3>
        <p class="text-slate-400 text-xs leading-relaxed mb-5" data-i18n="mat_1_desc">
          Multi-cavity internal chambers trap air pockets for maximum thermal &amp; sound insulation. Reinforced with galvanized steel inserts to prevent frame distortion in hot Janakpur summers.
        </p>
        <ul class="text-xs text-slate-300 space-y-2 border-t border-white/5 pt-4">
          <li class="flex items-center gap-2"><span class="text-cyan-400">✓</span> <span>100% Lead-Free Eco Formulation</span></li>
          <li class="flex items-center gap-2"><span class="text-cyan-400">✓</span> <span>UV-Resistant Titanium Dioxide Enriched</span></li>
          <li class="flex items-center gap-2"><span class="text-cyan-400">✓</span> <span>Dual EPDM Gasket Weather Seals</span></li>
        </ul>
      </div>

      <!-- Feature 2 -->
      <div class="glass-card p-7 rounded-3xl">
        <div class="w-14 h-14 rounded-2xl bg-amber-500/20 text-amber-400 flex items-center justify-center text-3xl mb-6 shadow-inner">
          ✦
        </div>
        <h3 class="text-lg font-bold text-white mb-2" data-i18n="mat_2_title">Virgin 6063-T5 Aluminium Alloy</h3>
        <p class="text-slate-400 text-xs leading-relaxed mb-5" data-i18n="mat_2_desc">
          Manufactured using high-strength architectural aluminium alloy with 60-80 micron electro-powder coating that withstands harsh sun, monsoons, and everyday impacts.
        </p>
        <ul class="text-xs text-slate-300 space-y-2 border-t border-white/5 pt-4">
          <li class="flex items-center gap-2"><span class="text-amber-400">✓</span> <span>No Recycled Scrap — 100% Virgin Alloy</span></li>
          <li class="flex items-center gap-2"><span class="text-amber-400">✓</span> <span>Scratch &amp; Chip Resistant Coating</span></li>
          <li class="flex items-center gap-2"><span class="text-amber-400">✓</span> <span>Heavy Gauge Wall for Structural Rigidity</span></li>
        </ul>
      </div>

      <!-- Feature 3 -->
      <div class="glass-card p-7 rounded-3xl">
        <div class="w-14 h-14 rounded-2xl bg-purple-500/20 text-purple-400 flex items-center justify-center text-3xl mb-6 shadow-inner">
          🛡️
        </div>
        <h3 class="text-lg font-bold text-white mb-2" data-i18n="mat_3_title">Authentic SS 304 Rust-Free Steel</h3>
        <p class="text-slate-400 text-xs leading-relaxed mb-5" data-i18n="mat_3_desc">
          Every stainless steel railing, temple gate, and staircase pillar is crafted from genuine SS 304 with full nickel content, assembled with inert gas TIG welding and diamond compound polishing.
        </p>
        <ul class="text-xs text-slate-300 space-y-2 border-t border-white/5 pt-4">
          <li class="flex items-center gap-2"><span class="text-purple-400">✓</span> <span>Chemical Acid Tested SS 304 Quality</span></li>
          <li class="flex items-center gap-2"><span class="text-purple-400">✓</span> <span>Multi-Stage Diamond Polish Mirror Shine</span></li>
          <li class="flex items-center gap-2"><span class="text-purple-400">✓</span> <span>Solid Casting Spigots &amp; Newel Posts</span></li>
        </ul>
      </div>

    </div>

    <!-- Live Workshop Action Photos -->
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
      <div class="relative group rounded-2xl overflow-hidden glass-panel aspect-[4/3]">
        <img src="catalog_assets/real_projects/workshop_live_fabrication.jpg" alt="Workshop live fabrication" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
        <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-transparent flex items-end p-3.5">
          <span class="text-xs font-bold text-white">Window Sash Assembly</span>
        </div>
      </div>
      <div class="relative group rounded-2xl overflow-hidden glass-panel aspect-[4/3]">
        <img src="catalog_assets/real_projects/onsite_ss_welding_installation.jpg" alt="On-site SS welding" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
        <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-transparent flex items-end p-3.5">
          <span class="text-xs font-bold text-white">SS TIG Welding &amp; Polish</span>
        </div>
      </div>
      <div class="relative group rounded-2xl overflow-hidden glass-panel aspect-[4/3]">
        <img src="catalog_assets/real_projects/workshop_raw_profiles_stock.jpg" alt="Raw Profile Stock" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
        <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-transparent flex items-end p-3.5">
          <span class="text-xs font-bold text-white">Warehouse Profile Inventory</span>
        </div>
      </div>
      <div class="relative group rounded-2xl overflow-hidden glass-panel aspect-[4/3]">
        <img src="catalog_assets/real_projects/workshop_ready_dispatch.jpg" alt="Dispatch yard" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
        <div class="absolute inset-0 bg-gradient-to-t from-black/85 via-transparent to-transparent flex items-end p-3.5">
          <span class="text-xs font-bold text-white">Protected Logistics Dispatch</span>
        </div>
      </div>
    </div>

  </div>
</section>

<!-- SECTION: FREE SITE VISIT & ARCHITECTURAL CONSULTATION -->
<section id="consultation" class="py-20 relative bg-luxury-950 border-t border-white/5">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
      
      <!-- Left info -->
      <div class="lg:col-span-5">
        <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs font-bold uppercase tracking-wider mb-3">
          📝 Free Measurement &amp; Estimate
        </div>
        <h2 class="text-3xl sm:text-5xl font-extrabold font-display text-white tracking-tight mb-4" data-i18n="booking_title">
          Book Free On-Site Measurement
        </h2>
        <p class="text-slate-300 text-sm sm:text-base leading-relaxed mb-6" data-i18n="booking_desc">
          Building a new house, commercial showroom, or renovating your hotel in Janakpur Dham or nearby districts? Our master engineer will visit your site with actual profile and glass samples for laser-guided measurement.
        </p>

        <div class="space-y-3.5 mb-8 text-xs sm:text-sm text-slate-300">
          <div class="flex items-center gap-3">
            <span class="w-6 h-6 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-xs">✓</span>
            <span>Free On-Site Laser Measurement in Janakpur, Dhanusha &amp; Mahottari</span>
          </div>
          <div class="flex items-center gap-3">
            <span class="w-6 h-6 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-xs">✓</span>
            <span>Direct Workshop Factory Price — Zero Middleman Markup</span>
          </div>
          <div class="flex items-center gap-3">
            <span class="w-6 h-6 rounded-full bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-xs">✓</span>
            <span>Complete Quotation with Profile Guarantees Within 24 Hours</span>
          </div>
        </div>

        <div class="glass-panel p-4 rounded-2xl border border-white/10 text-xs text-slate-400">
          📍 <strong class="text-slate-200">Janakpur Workshop Helpline:</strong> <a href="tel:{SHOP['phone1']}" class="text-cyan-400 font-bold hover:underline">{SHOP['phone1']}</a> / <a href="tel:{SHOP['phone2']}" class="text-slate-300 font-bold hover:underline">{SHOP['phone2']}</a>
        </div>
      </div>

      <!-- Right Form -->
      <div class="lg:col-span-7">
        <div class="glass-panel p-7 sm:p-9 rounded-3xl border border-white/10 shadow-2xl">
          <h3 class="text-xl font-bold font-display text-white mb-2" data-i18n="form_title">
            Request Site Visit &amp; Custom Quote
          </h3>
          <p class="text-xs text-slate-400 mb-6" data-i18n="form_subtitle">
            Fill in your details below and we will confirm your appointment via WhatsApp immediately.
          </p>

          <form onsubmit="handleContactSubmit(event)" class="space-y-4">
            <div>
              <label class="block text-xs font-bold text-slate-300 mb-1.5" data-i18n="form_label_name">Your Full Name *</label>
              <input type="text" id="form-name" required placeholder="e.g. Ramesh Kumar / Sahadev Chaudhary" class="w-full px-4 py-3 rounded-xl bg-slate-950 border border-white/10 text-white text-sm focus:outline-none focus:border-cyan-400">
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label class="block text-xs font-bold text-slate-300 mb-1.5" data-i18n="form_label_phone">Phone / WhatsApp Number *</label>
                <input type="tel" id="form-phone" required placeholder="e.g. 9817658719" class="w-full px-4 py-3 rounded-xl bg-slate-950 border border-white/10 text-white text-sm focus:outline-none focus:border-cyan-400">
              </div>
              <div>
                <label class="block text-xs font-bold text-slate-300 mb-1.5" data-i18n="form_label_city">Project Location / District *</label>
                <input type="text" id="form-city" required placeholder="e.g. Janakpur Dham / Lahan / Malangwa" class="w-full px-4 py-3 rounded-xl bg-slate-950 border border-white/10 text-white text-sm focus:outline-none focus:border-cyan-400">
              </div>
            </div>

            <div>
              <label class="block text-xs font-bold text-slate-300 mb-1.5" data-i18n="form_label_service">Primary Architectural Requirement</label>
              <select id="form-service" class="w-full px-4 py-3 rounded-xl bg-slate-950 border border-white/10 text-white text-sm focus:outline-none focus:border-cyan-400">
                <option value="UPVC Windows & Doors">UPVC Windows &amp; Doors (German Profile)</option>
                <option value="Aluminium Windows & Partitions">Aluminium Sliding Windows &amp; Office Partitions</option>
                <option value="SS Railings & Staircases">Stainless Steel (SS 304) Railings &amp; Glass Balustrades</option>
                <option value="Temple Gate & Steel Grills">Temple Entrance Gate / Heavy Security Gate</option>
                <option value="Modular Kitchen Storage Racks">Modular Aluminium Kitchen Storage Racks</option>
                <option value="Storefront Glass & ACP Cladding">Commercial Glass Facade &amp; ACP Cladding</option>
                <option value="Complete Building Aperture Package">Complete New Building Aperture Package (All-in-One)</option>
              </select>
            </div>

            <div>
              <label class="block text-xs font-bold text-slate-300 mb-1.5" data-i18n="form_label_notes">Approximate Size / Number of Openings</label>
              <textarea id="form-notes" rows="3" placeholder="e.g. 10 Windows (5x4 ft), 4 Bathroom Doors, 40 ft Staircase Railing..." class="w-full px-4 py-3 rounded-xl bg-slate-950 border border-white/10 text-white text-sm focus:outline-none focus:border-cyan-400"></textarea>
            </div>

            <button type="submit" class="w-full py-4 rounded-xl bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-slate-950 font-black text-sm uppercase tracking-wider transition-all shadow-xl shadow-cyan-500/25">
              Submit Request via WhatsApp →
            </button>
          </form>

        </div>
      </div>

    </div>

  </div>
</section>

<!-- SECTION: FOUNDER & ABOUT US -->
<section id="founder" class="py-20 relative bg-luxury-950/80 border-t border-white/5">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <div class="glass-panel p-8 sm:p-12 rounded-3xl border border-white/10 max-w-5xl mx-auto">
      <div class="grid grid-cols-1 md:grid-cols-12 gap-8 items-center">
        
        <!-- Signboard & Workshop Badge -->
        <div class="md:col-span-5 text-center">
          <div class="relative inline-block rounded-2xl overflow-hidden border-2 border-amber-400/40 shadow-2xl mb-4 group">
            <img src="catalog_assets/real_projects/shop_front_signboard.jpg" alt="Annapurna Aluminium & UPVC Signboard" class="w-full max-w-sm mx-auto object-cover group-hover:scale-105 transition-transform duration-500">
          </div>
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-900 border border-white/10 text-xs text-amber-300 font-bold">
            📍 Murli Chowk (Airport Road), Janakpur
          </div>
        </div>

        <!-- Founder Info -->
        <div class="md:col-span-7">
          <div class="text-xs font-bold text-cyan-400 uppercase tracking-widest mb-1" data-i18n="about_tag">Founder &amp; Master Fabricator</div>
          <h3 class="text-2xl sm:text-3xl font-extrabold font-display text-white mb-4">
            {SHOP['owner_name']}
          </h3>
          <p class="text-slate-300 text-sm leading-relaxed mb-4" data-i18n="about_bio_1">
            "We started <strong>Annapurna Aluminium &amp; UPVC</strong> in Janakpur Dham with a singular mission: to deliver European-grade window insulation, modern aluminium elegance, and unyielding steel security at direct factory prices to every home and enterprise in Nepal."
          </p>
          <p class="text-slate-400 text-xs leading-relaxed mb-6" data-i18n="about_bio_2">
            From the sacred doors of <em>Sri Nav Durga Mandir Duhaba</em> to commercial plazas across Madhesh Province, our team of seasoned craftsmen takes personal pride in every single weld, miter cut, and glass installation.
          </p>

          <div class="grid grid-cols-2 gap-4 border-t border-white/10 pt-4 text-xs">
            <div>
              <span class="text-slate-500 block">Primary WhatsApp / Call:</span>
              <a href="tel:{SHOP['phone1']}" class="text-cyan-400 font-bold text-sm hover:underline">{SHOP['phone1']}</a>
            </div>
            <div>
              <span class="text-slate-500 block">Secondary Line:</span>
              <a href="tel:{SHOP['phone2']}" class="text-slate-200 font-bold text-sm hover:underline">{SHOP['phone2']}</a>
            </div>
          </div>
        </div>

      </div>
    </div>

  </div>
</section>

<!-- SECTION: SERVICE AREA & GOOGLE MAPS COVERAGE -->
<section class="py-16 relative bg-luxury-950 border-t border-white/5">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center max-w-3xl mx-auto mb-10">
      <h3 class="text-2xl sm:text-3xl font-extrabold font-display text-white" data-i18n="coverage_title">
        Service &amp; Installation Coverage Across Nepal
      </h3>
      <p class="text-slate-400 text-xs sm:text-sm mt-1" data-i18n="coverage_subtitle">
        Free site measurement and consultation available across Madhesh Province districts. Safe transit &amp; installation provided nationwide.
      </p>
    </div>

    <div class="flex flex-wrap items-center justify-center gap-2.5 max-w-4xl mx-auto">
      {"".join([f'''<div class="px-4 py-2.5 rounded-xl bg-slate-900/90 border border-white/10 text-xs font-semibold text-slate-300 hover:border-cyan-500/40 transition-colors flex items-center gap-2 shadow-sm">
        <span class="text-cyan-400">📍</span> <span>{area}</span>
      </div>''' for area in SHOP["service_areas"]])}
    </div>
  </div>
</section>

<!-- SECTION: FAQ ACCORDION -->
<section class="py-20 relative bg-luxury-950/80 border-t border-white/5">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <div class="text-center mb-12">
      <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/20 text-cyan-400 text-xs font-bold uppercase tracking-wider mb-3">
        ❓ Frequently Asked Questions
      </div>
      <h2 class="text-3xl sm:text-4xl font-extrabold font-display text-white tracking-tight" data-i18n="faq_title">
        Got Questions? We Have Answers.
      </h2>
    </div>

    <div class="space-y-4" id="faq-container">
      
      <!-- FAQ 1 -->
      <div class="glass-card rounded-2xl overflow-hidden">
        <button onclick="toggleFaq(1)" class="w-full p-5 text-left font-bold text-white text-sm sm:text-base flex items-center justify-between gap-4">
          <span data-i18n="faq_q1">How can I get an exact price quote for my house or commercial building?</span>
          <span id="faq-icon-1" class="text-cyan-400 font-extrabold text-lg">+</span>
        </button>
        <div id="faq-content-1" class="hidden p-5 pt-0 text-slate-300 text-xs sm:text-sm leading-relaxed border-t border-white/5" data-i18n="faq_a1">
          Simply call or message us on WhatsApp at <strong>+977 9817658719</strong> with your rough room window/door dimensions or architectural floor plan. If you are in Janakpur Dham, Dhanusha, or nearby districts, our engineer will visit your site directly for free measurement.
        </div>
      </div>

      <!-- FAQ 2 -->
      <div class="glass-card rounded-2xl overflow-hidden">
        <button onclick="toggleFaq(2)" class="w-full p-5 text-left font-bold text-white text-sm sm:text-base flex items-center justify-between gap-4">
          <span data-i18n="faq_q2">What is the price of UPVC windows in Nepal?</span>
          <span id="faq-icon-2" class="text-cyan-400 font-extrabold text-lg">+</span>
        </button>
        <div id="faq-content-2" class="hidden p-5 pt-0 text-slate-300 text-xs sm:text-sm leading-relaxed border-t border-white/5" data-i18n="faq_a2">
          UPVC window pricing depends on track configuration (2-track vs 3-track with mesh), profile grade (multi-chamber German profile), and glass selection (single float, tinted reflective, or insulated double glazing). We offer the most competitive factory-direct rates in Nepal starting from NRs 450 - 850 per sq.ft.
        </div>
      </div>

      <!-- FAQ 3 -->
      <div class="glass-card rounded-2xl overflow-hidden">
        <button onclick="toggleFaq(3)" class="w-full p-5 text-left font-bold text-white text-sm sm:text-base flex items-center justify-between gap-4">
          <span data-i18n="faq_q3">Which is better for home bedrooms: UPVC or Aluminium?</span>
          <span id="faq-icon-3" class="text-cyan-400 font-extrabold text-lg">+</span>
        </button>
        <div id="faq-content-3" class="hidden p-5 pt-0 text-slate-300 text-xs sm:text-sm leading-relaxed border-t border-white/5" data-i18n="faq_a3">
          For residential bedrooms and living rooms, <strong>UPVC with double glazing</strong> is the best choice because it blocks outdoor traffic noise and maintains cooler room temperatures during summer heat. Aluminium is best for large commercial storefronts, slim partitions, and high-impact structural portals.
        </div>
      </div>

      <!-- FAQ 4 -->
      <div class="glass-card rounded-2xl overflow-hidden">
        <button onclick="toggleFaq(4)" class="w-full p-5 text-left font-bold text-white text-sm sm:text-base flex items-center justify-between gap-4">
          <span data-i18n="faq_q4">How do modular aluminium kitchen racks prevent termites and water damage?</span>
          <span id="faq-icon-4" class="text-cyan-400 font-extrabold text-lg">+</span>
        </button>
        <div id="faq-content-4" class="hidden p-5 pt-0 text-slate-300 text-xs sm:text-sm leading-relaxed border-t border-white/5" data-i18n="faq_a4">
          Unlike plywood or MDF boards that swell, warp, and get infested with termites in humid kitchens, our modular racks use 100% anodized architectural aluminium framing and waterproof aluminium composite panels (ACP) that can be washed directly with water without any damage.
        </div>
      </div>

      <!-- FAQ 5 -->
      <div class="glass-card rounded-2xl overflow-hidden">
        <button onclick="toggleFaq(5)" class="w-full p-5 text-left font-bold text-white text-sm sm:text-base flex items-center justify-between gap-4">
          <span data-i18n="faq_q5">How long does manufacturing and installation take?</span>
          <span id="faq-icon-5" class="text-cyan-400 font-extrabold text-lg">+</span>
        </button>
        <div id="faq-content-5" class="hidden p-5 pt-0 text-slate-300 text-xs sm:text-sm leading-relaxed border-t border-white/5" data-i18n="faq_a5">
          Standard residential window and door orders are completed in <strong>3 to 5 business days</strong>. Commercial facade glazing, large temple gates, and custom modular kitchens are scheduled as per site milestones with prompt delivery.
        </div>
      </div>

    </div>

  </div>
</section>

<!-- SECTION: CONTACT & GOOGLE MAPS -->
<section id="contact" class="py-20 relative bg-luxury-950 border-t border-white/5">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-10">
      
      <!-- Contact Info -->
      <div class="lg:col-span-5">
        <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-cyan-500/10 border border-cyan-500/20 text-cyan-400 text-xs font-bold uppercase tracking-wider mb-3">
          📍 Visit Our Workshop
        </div>
        <h2 class="text-3xl sm:text-4xl font-extrabold font-display text-white tracking-tight mb-4" data-i18n="contact_title">
          Get in Touch Today
        </h2>
        <p class="text-slate-300 text-sm leading-relaxed mb-8" data-i18n="contact_subtitle">
          Visit our workshop to inspect live profile samples, toughened glass options, and crystal balusters in person, or contact our helpline directly.
        </p>

        <div class="space-y-4 text-sm">
          <div class="glass-panel p-4 rounded-2xl flex items-start gap-4">
            <span class="text-2xl text-cyan-400">📍</span>
            <div>
              <strong class="text-white block font-bold" data-i18n="contact_label_addr">Physical Address:</strong>
              <span class="text-slate-300">{SHOP['address']}</span>
            </div>
          </div>

          <div class="glass-panel p-4 rounded-2xl flex items-start gap-4">
            <span class="text-2xl text-emerald-400">📞</span>
            <div>
              <strong class="text-white block font-bold" data-i18n="contact_label_phone">Direct Phone Numbers:</strong>
              <div class="space-y-0.5 mt-1">
                <a href="tel:{SHOP['phone1']}" class="text-cyan-400 font-bold block hover:underline">{SHOP['phone1']} (WhatsApp Same)</a>
                <a href="tel:{SHOP['phone2']}" class="text-slate-300 font-medium block hover:underline">{SHOP['phone2']}</a>
              </div>
            </div>
          </div>

          <div class="glass-panel p-4 rounded-2xl flex items-start gap-4">
            <span class="text-2xl text-amber-400">🕒</span>
            <div>
              <strong class="text-white block font-bold" data-i18n="contact_label_hours">Workshop Working Hours:</strong>
              <span class="text-slate-300">{SHOP['hours']}</span>
            </div>
          </div>
        </div>

        <div class="mt-8 flex gap-3">
          <a href="{SHOP['gmaps_url']}" target="_blank" rel="noopener" class="flex-1 py-3.5 px-4 rounded-xl bg-slate-900 hover:bg-slate-800 border border-white/10 text-cyan-400 font-bold text-xs text-center transition-all shadow-md">
            🗺️ Open Google Maps Directions
          </a>
          <a href="https://wa.me/{SHOP['whatsapp']}" target="_blank" rel="noopener" class="flex-1 py-3.5 px-4 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs text-center transition-all shadow-md">
            💬 Chat on WhatsApp
          </a>
        </div>
      </div>

      <!-- Right Direct Action Card -->
      <div class="lg:col-span-7 flex flex-col justify-center">
        <div class="glass-panel p-8 sm:p-10 rounded-3xl border border-white/10 relative overflow-hidden">
          <div class="absolute -right-16 -bottom-16 w-64 h-64 rounded-full bg-cyan-500/10 filter blur-3xl pointer-events-none"></div>

          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-500/10 text-cyan-400 text-xs font-bold mb-4">
            ⚡ Quick Direct Hotline
          </div>

          <h3 class="text-2xl sm:text-3xl font-extrabold font-display text-white mb-4" data-i18n="hotline_h3">
            Speak Directly with Master Engineer Prof. Nageshwar Thakur
          </h3>
          <p class="text-slate-300 text-sm leading-relaxed mb-8" data-i18n="hotline_p">
            Get instant technical recommendations on profile gauge, glass thickness, wind load requirements, and site visit scheduling across Janakpur Dham, Dhanusha, and all Nepal.
          </p>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <a href="tel:{SHOP['phone1']}" class="p-5 rounded-2xl bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-black text-center text-sm transition-all shadow-xl shadow-cyan-500/20 flex flex-col items-center justify-center gap-1">
              <span class="text-xs font-bold text-slate-800 uppercase">Primary Hotline</span>
              <span class="text-lg tracking-wide">{SHOP['phone1']}</span>
            </a>
            <a href="https://wa.me/{SHOP['whatsapp']}?text=Namaste%20Prof.%20Nageshwar%20Thakur,%20I%20want%20consultation%20for%20my%20building%20project." target="_blank" rel="noopener" class="p-5 rounded-2xl bg-emerald-600 hover:bg-emerald-500 text-white font-black text-center text-sm transition-all shadow-xl shadow-emerald-600/20 flex flex-col items-center justify-center gap-1">
              <span class="text-xs font-bold text-emerald-200 uppercase">Direct WhatsApp</span>
              <span class="text-lg tracking-wide">+977 9817658719</span>
            </a>
          </div>

        </div>
      </div>

    </div>

  </div>
</section>

<!-- FOOTER -->
<footer class="bg-luxury-950 text-slate-400 text-xs border-t border-white/5 py-12">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-12">
      
      <!-- Brand column -->
      <div class="md:col-span-2 space-y-3">
        <div class="font-display font-extrabold text-lg text-white">
          Annapurna Aluminium &amp; UPVC Udhyog
        </div>
        <p class="text-xs text-slate-400 max-w-md leading-relaxed">
          Certified fabricator and installer of German-profile UPVC windows, architectural aluminium doors, frameless glass railings, SS 304 temple gates, and modular kitchen storage racks in Janakpur Dham, Dhanusha, Nepal.
        </p>
        <div class="text-xs text-slate-500">
          Founder: <strong>Prof. Nageshwar Thakur</strong> · Murli Chowk (Airport Road), Janakpur Dham-8
        </div>
      </div>

      <!-- Quick Links -->
      <div>
        <h4 class="text-white font-bold text-sm mb-3">Product Categories</h4>
        <ul class="space-y-2 text-xs">
          <li><a href="#catalog" onclick="filterCatalog('UWC')" class="hover:text-cyan-400 transition-colors">UPVC Windows (12 Designs)</a></li>
          <li><a href="#catalog" onclick="filterCatalog('UWD')" class="hover:text-cyan-400 transition-colors">UPVC Doors (10 Designs)</a></li>
          <li><a href="#catalog" onclick="filterCatalog('ALW')" class="hover:text-cyan-400 transition-colors">Aluminium Windows (10 Designs)</a></li>
          <li><a href="#catalog" onclick="filterCatalog('SLS')" class="hover:text-cyan-400 transition-colors">Stainless Steel 304 Railings</a></li>
          <li><a href="#catalog" onclick="filterCatalog('MST')" class="hover:text-cyan-400 transition-colors">Temple &amp; Compound Gates</a></li>
          <li><a href="#catalog" onclick="filterCatalog('MOD')" class="hover:text-cyan-400 transition-colors">Modular Kitchen Racks</a></li>
        </ul>
      </div>

      <!-- Contact summary -->
      <div>
        <h4 class="text-white font-bold text-sm mb-3">Contact Helpline</h4>
        <p class="text-xs mb-1">📍 Murli Chowk (Airport Road)</p>
        <p class="text-xs mb-3">Janakpur Dham-8, Dhanusha, Nepal</p>
        <p class="text-xs text-cyan-400 font-bold mb-1">📞 +977 9817658719</p>
        <p class="text-xs text-slate-300 font-medium mb-3">📞 +977 9817667115</p>
        <span class="inline-block px-3 py-1 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 text-[11px] font-semibold">
          Open 7 Days a Week
        </span>
      </div>

    </div>

    <div class="border-t border-white/5 pt-6 flex flex-col sm:flex-row items-center justify-between gap-3 text-[11px] text-slate-500">
      <div>
        © 2026 Annapurna Aluminium &amp; UPVC Udhyog. All rights reserved.
      </div>
      <div class="flex gap-4">
        <a href="#projects" class="hover:text-slate-300">Real Projects</a>
        <a href="#catalog" class="hover:text-slate-300">102+ Catalog</a>
        <a href="#consultation" class="hover:text-slate-300">Free Measurement</a>
        <a href="{SHOP['gmaps_url']}" target="_blank" class="hover:text-slate-300">Google Map</a>
      </div>
    </div>
  </div>
</footer>

<!-- LIGHTBOX MODAL (FOR ZOOMING PROJECT & PRODUCT IMAGES) -->
<div id="lightbox-modal" class="fixed inset-0 z-[100] hidden bg-black/95 backdrop-blur-md flex items-center justify-center p-4" onclick="closeLightbox(event)">
  <div class="relative max-w-5xl w-full bg-slate-900 border border-white/10 rounded-3xl overflow-hidden shadow-2xl" onclick="event.stopPropagation()">
    
    <!-- Close Button -->
    <button onclick="closeLightbox()" class="absolute top-4 right-4 z-10 w-10 h-10 rounded-full bg-slate-950/80 text-white hover:bg-red-600 flex items-center justify-center text-lg font-bold transition-all border border-white/10">
      ✕
    </button>

    <div class="grid grid-cols-1 md:grid-cols-12 max-h-[85vh] overflow-y-auto">
      
      <!-- Image Display -->
      <div class="md:col-span-8 bg-slate-950 flex items-center justify-center min-h-[350px] p-2">
        <img id="lightbox-img" src="" alt="Zoomed view" class="max-h-[75vh] w-auto max-w-full object-contain rounded-xl">
      </div>

      <!-- Detail Sidebar -->
      <div class="md:col-span-4 p-6 flex flex-col justify-between bg-slate-900 border-t md:border-t-0 md:border-l border-white/10">
        <div>
          <span id="lightbox-cat" class="px-2.5 py-1 rounded-md text-[11px] font-bold uppercase tracking-wider bg-cyan-500/20 text-cyan-400 border border-cyan-500/30 mb-3 inline-block">
            Category
          </span>
          <h3 id="lightbox-title" class="text-xl font-bold font-display text-white mb-2 leading-snug">
            Project Title
          </h3>
          <p id="lightbox-loc" class="text-xs text-amber-400 font-semibold mb-3">
            📍 Location
          </p>
          <p id="lightbox-desc" class="text-xs text-slate-300 leading-relaxed mb-4">
            Description
          </p>
          <div id="lightbox-specs" class="space-y-1 text-xs text-slate-400 border-t border-white/5 pt-3">
            <!-- Dynamic Specs -->
          </div>
        </div>

        <div class="pt-6 mt-4 border-t border-white/10">
          <button id="lightbox-quote-btn" onclick="inquireLightboxItem()" class="w-full py-3.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs uppercase tracking-wider transition-all flex items-center justify-center gap-2 shadow-lg">
            <span>💬</span> <span data-i18n="lightbox_btn_inquire">Inquire on WhatsApp</span>
          </button>
        </div>

      </div>

    </div>

  </div>
</div>

<!-- FLOATING SPEED-DIAL BUTTONS -->
<div class="fixed bottom-6 right-6 z-40 flex flex-col gap-3">
  
  <!-- WhatsApp Floating Speed Dial -->
  <a href="https://wa.me/{SHOP['whatsapp']}?text=Namaste%20Annapurna%20Aluminium,%20I%20am%20interested%20in%20your%20products." target="_blank" rel="noopener" aria-label="Chat on WhatsApp" class="w-14 h-14 rounded-full bg-emerald-500 hover:bg-emerald-400 text-white flex items-center justify-center text-3xl shadow-2xl hover:scale-110 transition-all animate-bounce">
    💬
  </a>

  <!-- Call Speed Dial -->
  <a href="tel:{SHOP['phone1']}" aria-label="Call Directly" class="w-12 h-12 rounded-full bg-cyan-500 hover:bg-cyan-400 text-slate-950 flex items-center justify-center text-xl font-black shadow-xl hover:scale-110 transition-all">
    📞
  </a>

</div>

<!-- EMBEDDED JAVASCRIPT APP LOGIC & DATASETS -->
<script>
/* ==================== GLOBAL DATASETS ==================== */
const SHOP = {json.dumps(SHOP, ensure_ascii=False)};
const REAL_PROJECTS = {json.dumps(REAL_PROJECTS, ensure_ascii=False)};
const PRODUCTS = {json.dumps(products_list, ensure_ascii=False)};
const CATS = {json.dumps(CATS, ensure_ascii=False)};

// SVG Template engine for client-side drawing
{templates_js_raw}

// Client-side SVG renderer helper
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

/* ==================== DUAL LANGUAGE TRANSLATIONS (EN & नेपाली) ==================== */
const I18N = {{
  en: {{
    top_open: "Workshop Open 7 Days · 9:00 AM – 7:00 PM",
    top_loc: "Murli Chowk (Airport Road), Janakpur Dham-8, Dhanusha",
    nav_subtitle: "Janakpur Dham · Windows, Doors, Glass & Steel Works",
    nav_projects: "Real Projects (40+)",
    nav_catalog: "102+ Design Catalog",
    nav_standards: "Material Quality",
    nav_consult: "Book Site Visit",
    nav_about: "About & Team",
    nav_contact: "Contact",
    btn_whatsapp: "WhatsApp Quote",
    btn_call: "Call Workshop",
    hero_badge: "#1 Certified UPVC, Aluminium & SS Fabrication Center · Janakpur Dham, Nepal",
    hero_h1_1: "World-Class",
    hero_h1_2: "UPVC, Aluminium & Glass",
    hero_h1_3: "Craftsmanship",
    hero_desc: "102+ Custom Designs manufactured at our Janakpur workshop: German-profile UPVC windows, modern aluminium doors & partitions, SS 304 temple gates, balustrades, modular kitchen racks, and commercial ACP glass facades.",
    hero_btn_projects: "Explore Real Project Photos",
    hero_btn_catalog: "Browse 102+ Catalog",
    hero_btn_estimate: "Free Site Measurement",
    stat_designs: "Unique Custom Designs",
    stat_sites: "Completed Sites in Nepal",
    stat_exp: "Engineering Experience",
    stat_quality: "SS 304 & Virgin Profiles",
    projects_title: "Real Projects by Annapurna",
    projects_subtitle: "Explore actual completed commercial facades, temple gates, modern residences, staircases, and modular kitchens fabricated right here at our Murli Chowk workshop.",
    filter_all: "All Projects (26)",
    filter_stf: "Facades & ACP",
    filter_uwc: "UPVC Windows",
    filter_sls: "SS Railings",
    filter_mst: "Temple Gates",
    filter_mod: "Kitchen Racks",
    filter_alp: "Partitions",
    projects_more_note: "Looking for a specific architectural design or have your own custom blueprint?",
    projects_send_custom: "Send Your Custom Blueprints on WhatsApp",
    catalog_title: "102+ Master Product Designs",
    catalog_subtitle: "Every product is precision-engineered, customizable to your exact structural measurements, and available in multiple finishes and glass configurations.",
    catalog_view_mode: "View Mode:",
    view_photo: "Photos",
    view_blueprint: "Blueprint",
    custom_sizes_note: "Custom sizes & finishes fabricated for all models",
    factory_title: "Factory Machinery & Raw Material Quality",
    factory_subtitle: "We never compromise on metal thickness, uPVC wall gauge, or welding standards. Here is how we ensure lifetime durability.",
    mat_1_title: "German Multi-Chamber UPVC",
    mat_1_desc: "Multi-cavity internal chambers trap air pockets for maximum thermal & sound insulation. Reinforced with galvanized steel inserts to prevent frame distortion in hot Janakpur summers.",
    mat_2_title: "Virgin 6063-T5 Aluminium Alloy",
    mat_2_desc: "Manufactured using high-strength architectural aluminium alloy with 60-80 micron electro-powder coating that withstands harsh sun, monsoons, and everyday impacts.",
    mat_3_title: "Authentic SS 304 Rust-Free Steel",
    mat_3_desc: "Every stainless steel railing, temple gate, and staircase pillar is crafted from genuine SS 304 with full nickel content, assembled with inert gas TIG welding and diamond compound polishing.",
    booking_title: "Book Free On-Site Measurement",
    booking_desc: "Building a new house, commercial showroom, or renovating your hotel in Janakpur Dham or nearby districts? Our master engineer will visit your site with actual profile and glass samples for laser-guided measurement.",
    form_title: "Request Site Visit & Custom Quote",
    form_subtitle: "Fill in your details below and we will confirm your appointment via WhatsApp immediately.",
    form_label_name: "Your Full Name *",
    form_label_phone: "Phone / WhatsApp Number *",
    form_label_city: "Project Location / District *",
    form_label_service: "Primary Architectural Requirement",
    form_label_notes: "Approximate Size / Number of Openings",
    about_tag: "Founder & Master Fabricator",
    about_bio_1: '"We started Annapurna Aluminium & UPVC in Janakpur Dham with a singular mission: to deliver European-grade window insulation, modern aluminium elegance, and unyielding steel security at direct factory prices to every home and enterprise in Nepal."',
    about_bio_2: "From the sacred doors of Sri Nav Durga Mandir Duhaba to commercial plazas across Madhesh Province, our team of seasoned craftsmen takes personal pride in every single weld, miter cut, and glass installation.",
    coverage_title: "Service & Installation Coverage Across Nepal",
    coverage_subtitle: "Free site measurement and consultation available across Madhesh Province districts. Safe transit & installation provided nationwide.",
    faq_title: "Got Questions? We Have Answers.",
    faq_q1: "How can I get an exact price quote for my house or commercial building?",
    faq_a1: "Simply call or message us on WhatsApp at <strong>+977 9817658719</strong> with your rough room window/door dimensions or architectural floor plan. If you are in Janakpur Dham, Dhanusha, or nearby districts, our engineer will visit your site directly for free measurement.",
    faq_q2: "What is the price of UPVC windows in Nepal?",
    faq_a2: "UPVC window pricing depends on track configuration (2-track vs 3-track with mesh), profile grade (multi-chamber German profile), and glass selection (single float, tinted reflective, or insulated double glazing). We offer the most competitive factory-direct rates in Nepal starting from NRs 450 - 850 per sq.ft.",
    faq_q3: "Which is better for home bedrooms: UPVC or Aluminium?",
    faq_a3: "For residential bedrooms and living rooms, <strong>UPVC with double glazing</strong> is the best choice because it blocks outdoor traffic noise and maintains cooler room temperatures during summer heat. Aluminium is best for large commercial storefronts, slim partitions, and high-impact structural portals.",
    faq_q4: "How do modular aluminium kitchen racks prevent termites and water damage?",
    faq_a4: "Unlike plywood or MDF boards that swell, warp, and get infested with termites in humid kitchens, our modular racks use 100% anodized architectural aluminium framing and waterproof aluminium composite panels (ACP) that can be washed directly with water without any damage.",
    faq_q5: "How long does manufacturing and installation take?",
    faq_a5: "Standard residential window and door orders are completed in <strong>3 to 5 business days</strong>. Commercial facade glazing, large temple gates, and custom modular kitchens are scheduled as per site milestones with prompt delivery.",
    contact_title: "Get in Touch Today",
    contact_subtitle: "Visit our workshop to inspect live profile samples, toughened glass options, and crystal balusters in person, or contact our helpline directly.",
    contact_label_addr: "Physical Address:",
    contact_label_phone: "Direct Phone Numbers:",
    contact_label_hours: "Workshop Working Hours:",
    hotline_h3: "Speak Directly with Master Engineer Prof. Nageshwar Thakur",
    hotline_p: "Get instant technical recommendations on profile gauge, glass thickness, wind load requirements, and site visit scheduling across Janakpur Dham, Dhanusha, and all Nepal.",
    lightbox_btn_inquire: "Inquire on WhatsApp"
  }},
  ne: {{
    top_open: "हप्ताको सातै दिन खुला · बिहान ९:०० देखि साँझ ७:०० सम्म",
    top_loc: "मुरली चोक (एयरपोर्ट रोड), जनकपुरधाम-८, धनुषा",
    nav_subtitle: "जनकपुरधाम · झ्याल, ढोका, ग्लास र स्टिल फेब्रिकेसन",
    nav_projects: "वास्तविक कामहरू (४०+)",
    nav_catalog: "१०२+ डिजाइन क्याटलग",
    nav_standards: "गुणस्तर मापदण्ड",
    nav_consult: "साइट भिजिट बुक गर्नुहोस्",
    nav_about: "हाम्रोबारे",
    nav_contact: "सम्पर्क",
    btn_whatsapp: "ह्वाट्सएप कोटेशन",
    btn_call: "फोन गर्नुहोस्",
    hero_badge: "जनकपुरधामको #१ प्रमाणित यूपीभीसी, आल्मुनियम तथा स्टिल फेब्रिकेसन केन्द्र",
    hero_h1_1: "विश्वस्तरीय गुणस्तर",
    hero_h1_2: "यूपीभीसी, आल्मुनियम र ग्लास",
    hero_h1_3: "उत्कृष्ट निर्माण",
    hero_desc: "जनकपुरधाममा निर्मित १०२+ भन्दा बढी प्रिमियम डिजाइनहरू: जर्मन यूपीभीसी झ्याल, आल्मुनियम ढोका र पार्टिसन, एसएस ३०४ मन्दिर गेट, भर्याङ रेलिङ, मोड्युलर किचन र्याक र एसीपी ग्लास फसाड।",
    hero_btn_projects: "वास्तविक कामहरूको फोटो हेर्नुहोस्",
    hero_btn_catalog: "१०२+ डिजाइन क्याटलग",
    hero_btn_estimate: "निःशुल्क नाप जाँच बुक गर्नुहोस्",
    stat_designs: "अद्वितीय प्रिमियम डिजाइनहरू",
    stat_sites: "नेपालभर सम्पन्न परियोजनाहरू",
    stat_exp: "वर्षको इन्जिनियरिङ अनुभव",
    stat_quality: "१००% शुद्ध एसएस ३०४ र कच्चा पदार्थ",
    projects_title: "अन्नपूर्णा द्वारा सम्पन्न वास्तविक कामहरू",
    projects_subtitle: "हाम्रो मुरली चोक वर्कशपमा निर्मित कमर्सियल प्लाजा फसाड, मन्दिरका भव्य गेटहरू, आधुनिक भिल्ला झ्याल-ढोका, मार्बल भर्याङ रेलिङ र किचन र्याकहरू हेर्नुहोस्।",
    filter_all: "सबै कामहरू (२६)",
    filter_stf: "फसाड र एसीपी",
    filter_uwc: "यूपीभीसी झ्याल",
    filter_sls: "एसएस रेलिङ",
    filter_mst: "मन्दिर गेट",
    filter_mod: "किचन र्याक",
    filter_alp: "पार्टिसन",
    projects_more_note: "तपाईंसँग आफ्नै घर वा भवनको नक्सा वा विशेष डिजाइन छ?",
    projects_send_custom: "तपाईंको नक्सा ह्वाट्सएपमा पठाउनुहोस्",
    catalog_title: "१०२+ मास्टर उत्पादन डिजाइनहरू",
    catalog_subtitle: "प्रत्येक उत्पादन तपाईंको भवनको नाप अनुसार फ्याक्ट्रीमा तयार गरिन्छ। विभिन्न फिनिसिङ र ग्लास विकल्पहरू उपलब्ध छन्।",
    catalog_view_mode: "हेर्ने तरिका:",
    view_photo: "फोटोहरू",
    view_blueprint: "नक्सा (ब्लुप्रिन्ट)",
    custom_sizes_note: "सबै मोडलहरूमा आवश्यकता अनुसारको साइज र फिनिसिङ उपलब्ध छ",
    factory_title: "कारखाना, मेसिनरी र गुणस्तर मापदण्ड",
    factory_subtitle: "हामी कहिल्यै पनि धातुको मोटाइ वा यूपीभीसीको गुणस्तरमा सम्झौता गर्दैनौं। जीवनभरको स्थायित्वको ग्यारेन्टी।",
    mat_1_title: "जर्मन मल्टि-च्याम्बर यूपीभीसी",
    mat_1_desc: "आन्तरिक बहु-च्याम्बर हावा पकेटले गर्मी र बाहिरी आवाज पूर्ण रूपमा रोक्दछ। जनकपुरको कडा गर्मीमा पनि आकार नबिग्रिने ग्याल्भेनाइज्ड स्टिल रड जडित।",
    mat_2_title: "शुद्ध ६०६३-T5 आल्मुनियम मिश्रधातु",
    mat_2_desc: "६०-८० माइक्रोन इलेक्ट्रो-पाउडर कोटिङ गरिएको उच्च क्षमताको आर्किटेक्चरल आल्मुनियम, जसले घाम, पानी र खियाबाट पूर्ण सुरक्षा दिन्छ।",
    mat_3_title: "शुद्ध एसएस ३०४ खियामुक्त स्टिल",
    mat_3_desc: "हाम्रा सबै रेलिङ र मन्दिर गेटहरू शुद्ध एसएस ३०४ ग्रेडको स्टेनलेस स्टीलबाट टीआईजी वेल्डिङ र डायमण्ड मिरर पोलिस गरेर बनाइन्छ।",
    booking_title: "निःशुल्क साइट नाप जाँच बुक गर्नुहोस्",
    booking_desc: "नयाँ घर, पसल वा होटल निर्माण गर्दै हुनुहुन्छ? हाम्रा इन्जिनियरले वास्तविक स्याम्पल सहित तपाईंको साइटमा आएर लेजर प्रविधिबाट निःशुल्क नाप जाँच गर्नेछन्।",
    form_title: "साइट भिजिट र कोटेशन अनुरोध फारम",
    form_subtitle: "तलको फारम भर्नुहोस् र हामी तत्काल ह्वाट्सएप मार्फत सम्पर्क गर्नेछौं।",
    form_label_name: "तपाईंको पूरा नाम *",
    form_label_phone: "फोन / ह्वाट्सएप नम्बर *",
    form_label_city: "परियोजनाको ठेगाना / जिल्ला *",
    form_label_service: "चाहिएको प्रमुख उत्पादन",
    form_label_notes: "झ्याल वा ढोकाको संख्या र अनुमानित नाप",
    about_tag: "संस्थापक तथा मुख्य इन्जिनियर",
    about_bio_1: '"हामीले जनकपुरधाममा युरोपेली स्तरको साउन्डप्रुफ झ्याल, आधुनिक आल्मुनियम र बलियो स्टिल सुरक्षा सिधै फ्याक्ट्री मूल्यमा उपलब्ध गराउने लक्ष्यका साथ अन्नपूर्णा आल्मुनियमको स्थापना गरेका हौं।"',
    about_bio_2: "श्री नव दुर्गा मन्दिर दुहबाको पवित्र गेटदेखि मधेश प्रदेशभरिका ठूला प्लाजाहरूसम्म, हाम्रो अनुभवी टिमले प्रत्येक काममा पूर्ण इमानदारीका साथ काम गर्दछ।",
    coverage_title: "नेपालभर सेवा तथा डेलिभरी कभरेज",
    coverage_subtitle: "मधेश प्रदेशभर निःशुल्क साइट भिजिट र नाप जाँच। नेपालका सबै जिल्लामा सुरक्षित ढुवानी र फिटिङ।",
    faq_title: "प्रायः सोधिने प्रश्नहरू",
    faq_q1: "मेरो घर वा भवनको लागि मूल्य कोटेशन कसरी प्राप्त गर्ने?",
    faq_a1: "तपाईंको झ्याल वा ढोकाको नाप लिएर सिधै <strong>+977 9817658719</strong> मा फोन वा ह्वाट्सएप गर्नुहोस्। जनकपुरधाम तथा आसपासका क्षेत्रमा हाम्रो टिमले निःशुल्क साइट भिजिट गर्नेछ।",
    faq_q2: "नेपालमा यूपीभीसी झ्यालको दरभाउ कति पर्छ?",
    faq_a2: "यूपीभीसी झ्यालको मूल्य ट्र्याक संख्या (२-ट्र्याक वा ३-ट्र्याक जाली सहित), प्रोफाइल गुणस्तर र ग्लास अनुसार फरक पर्दछ। हामी नेपालकै प्रतिस्पर्धी फ्याक्ट्री दरमा उपलब्ध गराउँछौं।",
    faq_q3: "घरको बेडरुमको लागि यूपीभीसी कि आल्मुनियम कुन राम्रो?",
    faq_a3: "बेडरुम र बस्ने कोठाको लागि <strong>डबल ग्लाज्ड यूपीभीसी</strong> सबैभन्दा उत्तम हुन्छ किनभने यसले बाहिरको आवाज र गर्मी रोकेर कोठा शान्त र शीतल राख्छ।",
    faq_q4: "मोड्युलर आल्मुनियम किचन र्याक कसरी पानी र धमिराबाट सुरक्षित हुन्छ?",
    faq_a4: "काठ वा प्लाइवुड पानीले बिग्रने र धमिरा लाग्ने भएपनि आल्मुनियम र एसीपी प्यानलबाट बनेका हाम्रा र्याकहरू १००% वाटरप्रुफ हुन्छन् र सिधै पानीले धुन मिल्छ।",
    faq_q5: "अर्डर गरेको कति दिनमा डेलिभरी र फिटिङ हुन्छ?",
    faq_a5: "घरायसी झ्याल र ढोकाहरू सामान्यतया <strong>३ देखि ५ दिन भित्र</strong> तयार गरी साइटमा फिटिङ गरिन्छ। ठूला कमर्सियल फसाड र मन्दिर गेटहरू समय तालिका अनुसार सम्पन्न गरिन्छ।",
    contact_title: "आजै सम्पर्क गर्नुहोस्",
    contact_subtitle: "हाम्रो मुरली चोक वर्कशपमा आएर प्रोफाइल, ग्लास र क्रिस्टल पिलरका नमूनाहरू प्रत्यक्ष हेर्नुहोस्।",
    contact_label_addr: "वर्कशपको ठेगाना:",
    contact_label_phone: "प्रत्यक्ष सम्पर्क नम्बरहरू:",
    contact_label_hours: "काम हुने समय:",
    hotline_h3: "मुख्य इन्जिनियर प्रो. नागेश्वर ठाकुरसँग सिधा कुरा गर्नुहोस्",
    hotline_p: "तपाईंको भवनको लागि उपयुक्त प्रोफाइल, ग्लास मोटाइ र साइट भिजिटको लागि सिधै कुराकानी गर्नुहोस्।",
    lightbox_btn_inquire: "ह्वाट्सएपमा सोधपुछ गर्नुहोस्"
  }}
}};

let currentLang = 'en';

function setLanguage(lang) {{
  if (!I18N[lang]) return;
  currentLang = lang;
  
  // Update button highlights
  const btnEn = document.getElementById('lang-btn-en');
  const btnNe = document.getElementById('lang-btn-ne');
  
  if (lang === 'en') {{
    if (btnEn) btnEn.className = 'px-2.5 py-1 rounded-lg font-bold bg-cyan-500 text-black transition-all shadow-sm';
    if (btnNe) btnNe.className = 'px-2.5 py-1 rounded-lg font-bold text-slate-300 hover:text-white transition-all';
  }} else {{
    if (btnNe) btnNe.className = 'px-2.5 py-1 rounded-lg font-bold bg-cyan-500 text-black transition-all shadow-sm';
    if (btnEn) btnEn.className = 'px-2.5 py-1 rounded-lg font-bold text-slate-300 hover:text-white transition-all';
  }}

  // Update translatable elements
  document.querySelectorAll('[data-i18n]').forEach(el => {{
    const key = el.getAttribute('data-i18n');
    if (I18N[lang][key]) {{
      el.innerHTML = I18N[lang][key];
    }}
  }});

  // Re-render project cards and catalog to apply language changes
  renderRealProjects();
  renderCatalog();
}}

/* ==================== REAL PROJECTS GRID RENDERER ==================== */
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
    const desc = currentLang === 'ne' && p.desc_ne ? p.desc_ne : p.desc;

    return `
      <div class="glass-card rounded-3xl overflow-hidden group cursor-pointer" onclick="openLightboxProject('${{p.id}}')">
        <!-- Image Thumbnail with Zoom Hover -->
        <div class="relative aspect-[4/3] bg-slate-950 overflow-hidden">
          <img src="catalog_assets/real_projects/${{p.thumb}}" alt="${{p.title}}" loading="lazy" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500">
          <div class="absolute inset-0 bg-gradient-to-t from-luxury-950 via-luxury-950/20 to-transparent opacity-85 group-hover:opacity-60 transition-opacity"></div>
          
          <!-- Category & Location Badges -->
          <div class="absolute top-3.5 left-3.5 flex flex-wrap gap-1.5">
            <span class="px-3 py-1 rounded-lg text-[10px] font-extrabold uppercase tracking-wider bg-slate-950/90 text-cyan-400 border border-cyan-500/30 backdrop-blur-md shadow-md">
              ${{category}}
            </span>
          </div>

          <div class="absolute top-3.5 right-3.5 w-9 h-9 rounded-full bg-slate-950/80 text-white flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity shadow-lg">
            🔍
          </div>

          <div class="absolute bottom-3.5 left-3.5 right-3.5">
            <div class="text-[11px] text-amber-400 font-semibold mb-0.5">📍 ${{location}}</div>
            <h4 class="font-bold text-sm sm:text-base text-white leading-snug line-clamp-2">${{title}}</h4>
          </div>
        </div>

        <!-- Card Details -->
        <div class="p-5 bg-luxury-900/60">
          <p class="text-xs text-slate-300 line-clamp-2 mb-4 leading-relaxed">${{desc}}</p>
          
          <!-- Specs tags -->
          <div class="flex flex-wrap gap-1.5 mb-5">
            ${{p.specs.slice(0, 2).map(s => `<span class="px-2.5 py-1 rounded-md bg-slate-950 text-[10px] text-slate-300 border border-white/5 font-medium">${{s}}</span>`).join('')}}
          </div>

          <div class="flex items-center justify-between pt-3 border-t border-white/5 text-xs">
            <span class="text-cyan-400 font-bold hover:underline flex items-center gap-1">
              <span>${{currentLang === 'ne' ? 'विस्तृत विवरण' : 'View Full Details'}}</span> <span>→</span>
            </span>
            <a href="https://wa.me/${{SHOP.whatsapp}}?text=Namaste%20Annapurna,%20I%20am%20interested%20in%20project:%20${{encodeURIComponent(p.title)}}" target="_blank" onclick="event.stopPropagation()" class="px-3 py-1.5 rounded-xl bg-emerald-600/30 hover:bg-emerald-600 text-emerald-400 hover:text-white border border-emerald-500/30 transition-all text-[11px] font-bold flex items-center gap-1 shadow-sm">
              <span>💬 ${{currentLang === 'ne' ? 'सोधपुछ' : 'Quote'}}</span>
            </a>
          </div>
        </div>

      </div>
    `;
  }}).join('');
}}

function filterProjects(cat) {{
  currentProjectFilter = cat;
  document.querySelectorAll('.proj-filter-btn').forEach(btn => {{
    if (btn.getAttribute('data-cat') === cat) {{
      btn.className = 'proj-filter-btn px-4 py-2.5 rounded-xl text-xs font-bold transition-all bg-cyan-500 text-black shadow-lg shadow-cyan-500/20';
    }} else {{
      btn.className = 'proj-filter-btn px-4 py-2.5 rounded-xl text-xs font-bold transition-all bg-slate-900 text-slate-300 hover:text-white border border-white/10';
    }}
  }});
  renderRealProjects();
}}

/* ==================== 102+ CATALOG RENDERER ==================== */
let currentCatalogCategory = 'ALL';
let currentCatalogSearch = '';
let currentCatalogViewMode = 'photo'; // 'photo' or 'blueprint'

function renderCatalog() {{
  const container = document.getElementById('products-container');
  if (!container) return;

  const filtered = PRODUCTS.filter(p => {{
    // Category match
    if (currentCatalogCategory !== 'ALL' && p.cat !== currentCatalogCategory) return false;
    // Search match
    if (currentCatalogSearch) {{
      const q = currentCatalogSearch.toLowerCase();
      const matchCode = p.code.toLowerCase().includes(q);
      const matchName = p.name.toLowerCase().includes(q);
      const matchDesc = p.desc.toLowerCase().includes(q);
      const matchCat = p.cat.toLowerCase().includes(q);
      if (!matchCode && !matchName && !matchDesc && !matchCat) return false;
    }}
    return true;
  }});

  // Update count
  const countEl = document.getElementById('catalog-count');
  if (countEl) countEl.innerText = filtered.length;

  if (filtered.length === 0) {{
    container.innerHTML = `
      <div class="col-span-full py-16 text-center text-slate-400 glass-panel rounded-3xl">
        <div class="text-4xl mb-2">🔍</div>
        <h4 class="text-lg font-bold text-white mb-1">${{currentLang === 'ne' ? 'कुनै उत्पादन भेटिएन' : 'No matching designs found'}}</h4>
        <p class="text-xs text-slate-400">${{currentLang === 'ne' ? 'अन्य शब्द वा क्याटेगोरी छानेर खोज्नुहोस्।' : 'Try searching for "sliding", "casement", "gate", or click "All 102 Designs".'}}</p>
        <button onclick="clearCatalogSearch()" class="mt-4 px-4 py-2 rounded-xl bg-cyan-500 text-black font-bold text-xs">Reset Search</button>
      </div>
    `;
    return;
  }}

  container.innerHTML = filtered.map(p => {{
    const svgCode = p.svg || getProductSvg(p.art_key, p.art_params);
    const catColor = p.meta.color || '#00d2ff';
    const catBadge = (currentLang === 'ne' && p.meta.badge_ne) ? p.meta.badge_ne : (p.meta.badge || p.cat);

    return `
      <div class="glass-card rounded-3xl overflow-hidden flex flex-col justify-between" id="${{p.code.toLowerCase()}}">
        <div>
          
          <!-- Image or Blueprint View -->
          <div class="relative aspect-[16/10] bg-slate-950 overflow-hidden flex items-center justify-center">
            
            ${{currentCatalogViewMode === 'photo' ? `
              <img src="${{p.photo}}" alt="${{p.name}}" loading="lazy" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
            ` : `
              <div class="blueprint-box w-full h-full flex items-center justify-center p-4">
                <svg class="art" viewBox="0 0 200 160" preserveAspectRatio="xMidYMid meet" aria-hidden="true">
                  ${{svgCode}}
                </svg>
              </div>
            `}}

            <!-- Top Badges -->
            <div class="absolute top-3.5 left-3.5 flex items-center gap-1.5">
              <span class="px-2.5 py-0.5 rounded-md text-[10px] font-black uppercase tracking-wider bg-slate-950/90 text-white border border-white/10 shadow-lg">
                ${{p.code}}
              </span>
              <span class="px-2.5 py-0.5 rounded-md text-[10px] font-bold text-slate-950 shadow-md" style="background-color: ${{catColor}}">
                ${{catBadge}}
              </span>
            </div>

            <!-- Single Card View Toggle -->
            <button onclick="toggleSingleCardView('${{p.code}}')" class="absolute top-3.5 right-3.5 px-2.5 py-1 rounded-lg bg-slate-950/85 hover:bg-slate-900 text-[10px] font-bold text-slate-300 hover:text-cyan-400 border border-white/10 shadow-lg transition-all" title="Toggle Blueprint / Photo">
              ${{currentCatalogViewMode === 'photo' ? '📐 Blueprint' : '📸 Photo'}}
            </button>

          </div>

          <!-- Product Details -->
          <div class="p-5">
            <h3 class="font-bold font-display text-base sm:text-lg text-white mb-2 leading-snug">${{p.name}}</h3>
            <p class="text-xs text-slate-300 leading-relaxed mb-4">${{p.desc}}</p>

            <!-- Standard Sizes -->
            <div class="mb-3 text-[11px]">
              <span class="text-slate-400 font-semibold block mb-1">${{currentLang === 'ne' ? 'मानक आकारहरू (आवश्यकता अनुसार बनाइनेछ):' : 'Standard Sizes (Custom Fit Available):'}}</span>
              <div class="flex flex-wrap gap-1">
                ${{p.sizes.map(s => `<span class="px-2.5 py-0.5 rounded-md bg-slate-950 text-slate-300 border border-white/5 font-mono">${{s}}</span>`).join('')}}
              </div>
            </div>

            <!-- Finishes -->
            <div class="mb-4 text-[11px]">
              <span class="text-slate-400 font-semibold block mb-1">${{currentLang === 'ne' ? 'उपलब्ध फिनिसिङहरू:' : 'Available Finishes:'}}</span>
              <div class="flex flex-wrap gap-1">
                ${{p.finishes.map(f => `<span class="px-2.5 py-0.5 rounded-md bg-slate-900 text-cyan-300 border border-cyan-500/10">${{f}}</span>`).join('')}}
              </div>
            </div>

            <!-- Key Features Bullet List -->
            <div class="space-y-1.5 text-[11px] text-slate-400 border-t border-white/5 pt-3">
              ${{p.extras.map(e => `<div class="flex items-center gap-1.5"><span class="text-cyan-400 text-xs font-bold">✓</span><span>${{e}}</span></div>`).join('')}}
            </div>

          </div>
        </div>

        <!-- Footer Action -->
        <div class="p-4 bg-slate-950/70 border-t border-white/5 flex items-center justify-between gap-3">
          <a href="#consultation" class="text-xs font-bold text-cyan-400 hover:text-cyan-300 flex items-center gap-1">
            <span>${{currentLang === 'ne' ? 'नाप जाँच बुक' : 'Book Measurement'}}</span> <span>→</span>
          </a>
          
          <a href="https://wa.me/${{SHOP.whatsapp}}?text=Namaste%20Annapurna,%20I%20would%20like%20a%20quote%20and%20consultation%20for%20Product%20Code:%20${{p.code}}%20(${{encodeURIComponent(p.name)}})" target="_blank" rel="noopener" class="px-4 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs flex items-center gap-1.5 transition-all shadow-md">
            <span>💬</span> <span>${{currentLang === 'ne' ? 'ह्वाट्सएप अर्डर' : 'WhatsApp Order'}}</span>
          </a>
        </div>

      </div>
    `;
  }}).join('');
}}

function filterCatalog(cat) {{
  currentCatalogCategory = cat;
  document.querySelectorAll('.cat-pill').forEach(pill => {{
    if (pill.getAttribute('data-cat') === cat) {{
      pill.className = 'cat-pill px-4 py-2.5 rounded-xl text-xs font-bold whitespace-nowrap bg-cyan-500 text-black shadow-lg shadow-cyan-500/20 transition-all';
    }} else {{
      pill.className = 'cat-pill px-4 py-2.5 rounded-xl text-xs font-bold whitespace-nowrap bg-slate-900/90 text-slate-300 hover:text-white border border-white/10 transition-all';
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
    photoBtn.className = 'px-3 py-1.5 rounded-lg bg-cyan-500 text-slate-950 transition-all flex items-center gap-1.5';
    blueprintBtn.className = 'px-3 py-1.5 rounded-lg text-slate-400 hover:text-white transition-all flex items-center gap-1.5';
  }} else {{
    blueprintBtn.className = 'px-3 py-1.5 rounded-lg bg-cyan-500 text-slate-950 transition-all flex items-center gap-1.5';
    photoBtn.className = 'px-3 py-1.5 rounded-lg text-slate-400 hover:text-white transition-all flex items-center gap-1.5';
  }}
  renderCatalog();
}}

function toggleSingleCardView(code) {{
  setCatalogViewMode(currentCatalogViewMode === 'photo' ? 'blueprint' : 'photo');
}}

/* ==================== LIGHTBOX SYSTEM ==================== */
let activeLightboxItem = null;

function openLightboxProject(id) {{
  const proj = REAL_PROJECTS.find(p => p.id === id);
  if (!proj) return;
  activeLightboxItem = proj;

  const title = currentLang === 'ne' && proj.title_ne ? proj.title_ne : proj.title;
  const category = currentLang === 'ne' && proj.category_ne ? proj.category_ne : proj.category;
  const location = currentLang === 'ne' && proj.location_ne ? proj.location_ne : proj.location;
  const desc = currentLang === 'ne' && proj.desc_ne ? proj.desc_ne : proj.desc;

  document.getElementById('lightbox-img').src = 'catalog_assets/real_projects/' + proj.image;
  document.getElementById('lightbox-cat').innerText = category;
  document.getElementById('lightbox-title').innerText = title;
  document.getElementById('lightbox-loc').innerText = '📍 ' + location;
  document.getElementById('lightbox-desc').innerText = desc;
  
  const specsContainer = document.getElementById('lightbox-specs');
  specsContainer.innerHTML = proj.specs.map(s => `<div class="flex items-center gap-1.5"><span class="text-cyan-400 font-bold">✓</span><span>${{s}}</span></div>`).join('');

  document.getElementById('lightbox-modal').classList.remove('hidden');
  document.body.style.overflow = 'hidden';
}}

function closeLightbox(e) {{
  document.getElementById('lightbox-modal').classList.add('hidden');
  document.body.style.overflow = 'auto';
}}

function inquireLightboxItem() {{
  if (!activeLightboxItem) return;
  const msg = `Namaste Annapurna,%0A%0AI saw this project on your website and want something similar for my building:%0A• Title: ${{encodeURIComponent(activeLightboxItem.title)}}%0A• Location Reference: ${{encodeURIComponent(activeLightboxItem.location)}}%0A%0APlease let me know the details and schedule a site measurement.`;
  window.open(`https://wa.me/${{SHOP.whatsapp}}?text=${{msg}}`, '_blank');
}}

// Keyboard ESC to close lightbox
document.addEventListener('keydown', (e) => {{
  if (e.key === 'Escape') closeLightbox();
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

  const msg = `Namaste Annapurna Aluminium,%0A%0AI would like to request a site visit / measurement:%0A• Name: ${{name}}%0A• Phone: ${{phone}}%0A• Location: ${{city}}%0A• Requirement: ${{service}}%0A• Details: ${{notes}}%0A%0APlease contact me to confirm the schedule.`;

  window.open(`https://wa.me/${{SHOP.whatsapp}}?text=${{msg}}`, '_blank');
}}

function toggleMobileMenu() {{
  const menu = document.getElementById('mobile-menu');
  menu.classList.toggle('hidden');
}}

/* ==================== INITIALIZATION ==================== */
document.addEventListener('DOMContentLoaded', () => {{
  renderRealProjects();
  renderCatalog();
}});
</script>

</body>
</html>
"""

# Write index.html at root
index_path = ROOT / "index.html"
index_path.write_text(html_content, encoding="utf-8")
print(f"Successfully generated root website: {index_path} ({len(html_content)} bytes)")

# Write catalog.html inside catalog/
catalog_html_path = CATALOG_DIR / "catalog.html"
catalog_html_content = html_content.replace('catalog_assets/', '../catalog_assets/')
catalog_html_path.write_text(catalog_html_content, encoding="utf-8")
print(f"Successfully generated catalog version: {catalog_html_path}")

print("Master Website & Catalog Build Complete!")
