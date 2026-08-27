# -*- coding: utf-8 -*-
# 102 premium product designs for Aluminium + Steel + UPVC Glass workshop showcase

CATS = [
    {"key": "UWC", "name": "UPVC Windows", "tag": "Multi-chamber uPVC · Double glazing · Weatherproof"},
    {"key": "UWD", "name": "UPVC Doors", "tag": "German profile doors · SS hardware · Soundproof"},
    {"key": "ALW", "name": "Aluminium Windows", "tag": "Slim profiles · Powder coated · Durable"},
    {"key": "ALD", "name": "Aluminium Doors", "tag": "Lightweight · Corrosion resistant · Modern"},
    {"key": "ALP", "name": "Aluminium Partitions", "tag": "Office & home partitioning · Glass walls"},
    {"key": "GLZ", "name": "Glass Solutions", "tag": "Toughened · Laminated · Safety glass"},
    {"key": "STF", "name": "Storefront & Facade", "tag": "Shop fronts · Curtain walls · ACP cladding"},
    {"key": "MST", "name": "MS & Steel Works", "tag": "Gates · Grills · Security · Fabrication"},
    {"key": "SLS", "name": "Stainless Steel", "tag": "SS 304 railing · Gates · Handrails"},
    {"key": "RLS", "name": "Railings & Stairs", "tag": "Staircases · Balustrades · Guard rails"},
    {"key": "MOD", "name": "Modular & Special", "tag": "Wardrobes · Cabins · Pergolas · Enclosures"},
]

BASE_FEATS = {
    "UWC": ["Premium multi-chamber uPVC profile (imported grade)", "5mm toughened + insulated double glazing", "EPDM gaskets, SS rollers & branded hardware", "Complete dust-proof & rain-proof sealing"],
    "UWD": ["German-engineered uPVC profile with steel reinforcement", "Multi-point locking with SS handles", "Double-glazed sound & heat insulation", "Warranty-backed profiles & hardware"],
    "ALW": ["High-grade aluminium alloy (6063-T5) powder coated", "Slim sight lines for maximum glass view", "Custom anodized / textured finishes", "Rust-proof, zero-maintenance frames"],
    "ALD": ["Powder-coated aluminium with SS hinges", "Smooth glide tracks & premium locks", "Slim, elegant European profiles", "Suitable for villa, office & hotel use"],
    "ALP": ["Powder-coated aluminium framework", "10-12mm toughened glass panels", "Clean, modern office partitioning", "Quick installation, flexible layouts"],
    "GLZ": ["8-12mm toughened / laminated safety glass", "SS glass clamps & fittings", "Tempered as per Indian/Nepal safety norms", "Crystal-clear, scratch-resistant finish"],
    "STF": ["Floor-to-ceiling glazing systems", "Structural silicone & SS fittings", "High-impact ACP / glass cladding", "Weather-tight, long-life facade"],
    "MST": ["Heavy-duty MS sections, galvanized or painted", "Anti-rust primer + premium PU paint", "Welded & ground smooth joints", "Custom ornamental designs"],
    "SLS": ["SS 304 mirror finish, 2B or brushed", "Precision laser-cut & welded joints", "No rust, no corrosion – lifetime shine", "Polished to mirror finish on site"],
    "RLS": ["Designed for safety + style", "SS / aluminium / glass combinations", "Welded or clamp-fixed systems", "Complies with building safety standards"],
    "MOD": ["Tailor-made to your space", "Premium hardware & fittings", "Combines glass, aluminium & steel", "Factory-finished, fast installation"],
}

# Each product: code, cat, name, desc, sizes, finishes, extras, art(key, params)
P = []
def add(cat, num, name, desc, sizes, finishes, extras, art):
    P.append({"code": "%s-%02d" % (cat, num), "cat": cat, "name": name, "desc": desc,
              "sizes": sizes, "finishes": finishes, "extras": extras, "art": art})

# ============ UPVC WINDOWS (12) ============
add("UWC", 1, "AeroGlide 3-Track Sliding Window",
    "Triple-track sliding window with 6 glass panes for wide, smooth ventilation control.",
    ["1800 × 1200 mm", "2400 × 1500 mm"], ["White", "Wood Grain", "Matte Grey"],
    ["3 independent tracks – maximum airflow control", "Interlock profiles for security"],
    ["winSliding", {"panes": 3}])
add("UWC", 2, "Classic 2-Track Sliding Window",
    "Compact two-track slider — the perfect economical window for homes & offices.",
    ["1200 × 1200 mm", "1500 × 1200 mm"], ["White", "Golden Oak"],
    ["Smooth SS ball-bearing rollers", "Fiber mesh provision"],
    ["winSliding", {"panes": 2}])
add("UWC", 3, "Regency Casement Window",
    "Inward-opening casement with multi-point lock — elegant and 100% airtight.",
    ["900 × 1200 mm", "1200 × 1200 mm"], ["White", "Silver Grey"],
    ["Multi-point locking system", "Trickle ventilator option"],
    ["winCasement", {"leaves": 2}])
add("UWC", 4, "Ventura Tilt & Turn Window",
    "European tilt-and-turn: tilt for safe ventilation, turn for full clean access.",
    ["900 × 1400 mm", "1200 × 1500 mm"], ["White", "Anthracite Grey"],
    ["2-in-1 tilt & turn mechanism", "Child-safe restrictor option"],
    ["winTiltTurn", {}])
add("UWC", 5, "Horizon Top-Hung Window",
    "Top-hung outward opening with rain-proof ventilation, ideal for bedrooms.",
    ["600 × 900 mm", "900 × 1200 mm"], ["White", "Wood Grain"],
    ["Opens outward – zero space loss", "Rain guard hood"],
    ["winTopHung", {}])
add("UWC", 6, "Breeze Awning Window",
    "Push-out awning style with bottom hinge — ventilates even during light rain.",
    ["800 × 1000 mm", "1000 × 1200 mm"], ["White", "Dune Beige"],
    ["Hinged at bottom for shelter", "Friction stay arms hold any angle"],
    ["winAwning", {}])
add("UWC", 7, "Grand Bay Window",
    "Three-panel panoramic bay that floods the room with light and view.",
    ["3000 × 1500 mm", "3600 × 1500 mm"], ["White", "Wood Grain"],
    ["Panoramic 3-side view", "Built-in sill shelf"],
    ["winBay", {}])
add("UWC", 8, "Palace Arch Window",
    "Arched-top uPVC window for luxury villas, temples & premium facades.",
    ["1200 × 1800 mm", "1500 × 2100 mm"], ["White", "Golden Oak"],
    ["Custom arch fabrication", "Reinforced arch profile"],
    ["winArch", {}])
add("UWC", 9, "Combo-Flex Window",
    "Fixed glass + casement combo — big view with a ventilation leaf.",
    ["1800 × 1200 mm", "2400 × 1500 mm"], ["White", "Matte Grey"],
    ["Large fixed pane + opening leaf", "Ideal for living rooms"],
    ["winCombo", {}])
add("UWC", 10, "CornerView 90° Window",
    "Corner-to-corner glazing unit that removes the column view block.",
    ["1800 × 1500 mm", "Custom size"], ["White", "Anthracite"],
    ["90° corner glazing system", "Corner mullion reinforcement"],
    ["winCorner", {}])
add("UWC", 11, "GardenBay Window",
    "Box-bay window with wide sill — perfect for plants, seating & display.",
    ["1500 × 1200 mm", "1800 × 1500 mm"], ["White", "Wood Grain"],
    ["Extra-wide sill for plants & decor", "Fully sealed box construction"],
    ["winGarden", {}])
add("UWC", 12, "WhisperLouve uPVC Ventilator",
    "Fixed louvre ventilator for bathrooms & kitchens — silent, permanent airflow.",
    ["600 × 300 mm", "900 × 400 mm"], ["White", "Dune Beige"],
    ["Rain-proof angled blades", "Insect mesh option"],
    ["winLouver", {}])

# ============ UPVC DOORS (10) ============
add("UWD", 1, "Imperial Main Door",
    "Grand 2-panel uPVC entrance door with double glazing and steel core.",
    ["1000 × 2100 mm", "1200 × 2400 mm"], ["White", "Golden Oak", "Teak Grain"],
    ["Steel-reinforced sash for strength", "Multi-point lock + SS handle"],
    ["doorSingle", {"pattern": "2panel"}])
add("UWD", 2, "Royal French Door",
    "French-style uPVC door with glass grid — classic elegance for living rooms.",
    ["900 × 2100 mm", "1200 × 2100 mm"], ["White", "Wood Grain"],
    ["2×3 decorative glass grid", "Brass-tone SS hardware"],
    ["doorFrench", {}])
add("UWD", 3, "SlideMaster Sliding Door",
    "Smooth 2-pane sliding uPVC door with quiet rollers — space-saver for balconies.",
    ["1800 × 2100 mm", "2400 × 2200 mm"], ["White", "Anthracite Grey"],
    ["Super-smooth quiet rollers", "Lift & slide security lock"],
    ["doorSliding", {}])
add("UWD", 4, "Accordion Fold Door",
    "Space-saving folding uPVC door that opens the room fully to the terrace.",
    ["2400 × 2100 mm", "3600 × 2200 mm"], ["White", "Wood Grain"],
    ["Folds to 1/4 space", "Full-height double glazing"],
    ["doorFolding", {}])
add("UWD", 5, "Vista Balcony Door",
    "Full-glass balcony door with slim uPVC frame — unobstructed outdoor view.",
    ["900 × 2100 mm", "1200 × 2400 mm"], ["White", "Silver Grey"],
    ["Full-height clear glazing", "Laminated glass safety option"],
    ["doorBalcony", {}])
add("UWD", 6, "PivotGrande Door",
    "Statement pivot uPVC door with heavy-duty pivot hinges for premium entrances.",
    ["1100 × 2400 mm", "1400 × 2700 mm"], ["White", "Matte Black"],
    ["Floor-to-ceiling pivot action", "Premium designer handles"],
    ["doorPivot", {}])
add("UWD", 7, "ArchWay Door",
    "Arched uPVC door matching the villa's architectural arches.",
    ["1000 × 2400 mm", "1200 × 2700 mm"], ["White", "Golden Oak"],
    ["Custom arch fabrication", "Tempered glass inserts"],
    ["doorArch", {}])
add("UWD", 8, "Security Grill Door",
    "uPVC door with integrated MS grill panel — ventilation with security.",
    ["1000 × 2100 mm", "1200 × 2400 mm"], ["White", "Teak Grain"],
    ["Integrated steel grille", "Dual-lock security"],
    ["doorGrill", {}])
add("UWD", 9, "SlimLine Lift Door",
    "Slim-framed uPVC door for lift lobbies & showrooms — modern, minimal.",
    ["900 × 2200 mm", "1000 × 2400 mm"], ["White", "Anthracite"],
    ["Ultra-slim sight line", "Reinforced for high traffic"],
    ["doorSlim", {}])
add("UWD", 10, "TwinLeaf Showcase Door",
    "Double-leaf uPVC door with centre meeting stile for wide entrances.",
    ["1800 × 2100 mm", "2400 × 2400 mm"], ["White", "Wood Grain"],
    ["Two-leaf symmetry", "Centre lock + top/bottom bolts"],
    ["doorDouble", {}])

# ============ ALUMINIUM WINDOWS (10) ============
add("ALW", 1, "Aero-Slim Sliding Window",
    "Ultra-slim aluminium slider with 2/3 panes — maximum glass, minimal frame.",
    ["1500 × 1200 mm", "2100 × 1500 mm"], ["Silver", "Black", "Bronze"],
    ["26mm slim profiles", "Nylon glides for silent run"],
    ["winSliding", {"panes": 2}])
add("ALW", 2, "AluCasement Window",
    "Powder-coated aluminium casement with SS friction hinges.",
    ["900 × 1200 mm", "1200 × 1400 mm"], ["White", "Grey", "Brown"],
    ["SS friction stay hinges", "Multi-lock handle"],
    ["winCasement", {"leaves": 2}])
add("ALW", 3, "SkyFix Fixed Glazing",
    "Large fixed aluminium glass pane for staircases, lobbies & picture windows.",
    ["1800 × 1800 mm", "Custom size"], ["Silver", "Black"],
    ["10mm toughened glass", "Concealed fixing"],
    ["winFixed", {}])
add("ALW", 4, "Breeze Alu Awning",
    "Aluminium awning window with bottom hinge — perfect above kitchen sinks.",
    ["800 × 1000 mm", "1000 × 1200 mm"], ["White", "Silver"],
    ["Bottom-hinged push-out", "Rain-safe ventilation"],
    ["winAwning", {}])
add("ALW", 5, "LouverShade Aluminium",
    "Aluminium louvre window for permanent ventilation with privacy.",
    ["900 × 600 mm", "1200 × 900 mm"], ["Silver", "Black"],
    ["Anodized louvre blades", "Bathroom & kitchen special"],
    ["winLouver", {}])
add("ALW", 6, "Projected Window",
    "Side-hung projected aluminium window with multiple glass rows.",
    ["900 × 1500 mm", "1200 × 1800 mm"], ["White", "Bronze"],
    ["3-row glass layout", "Opens for easy cleaning"],
    ["winProjected", {}])
add("ALW", 7, "PivotView Window",
    "Centre-pivot aluminium window that rotates 180° for easy outside cleaning.",
    ["900 × 1200 mm", "1200 × 1500 mm"], ["Silver", "Black"],
    ["180° pivot rotation", "Perfect for high floors"],
    ["winCorner", {}])
add("ALW", 8, "CornerGlaze Window",
    "Aluminium corner window joining two walls — modern corner view.",
    ["1800 × 1500 mm", "Custom"], ["Black", "Silver"],
    ["Seamless corner joint", "Thermal break option"],
    ["winCorner", {}])
add("ALW", 9, "BayRidge Window",
    "Aluminium bay window adding depth and elegance to the facade.",
    ["2400 × 1500 mm", "3000 × 1500 mm"], ["White", "Grey"],
    ["3-panel bay geometry", "Sill seat integrated"],
    ["winBay", {}])
add("ALW", 10, "ArchGlaze Window",
    "Arched aluminium window with curved frame extrusion for premium villas.",
    ["1200 × 1800 mm", "1500 × 2100 mm"], ["Black", "Bronze"],
    ["Curved profile bending", "Toughened arch glass"],
    ["winArch", {}])

# ============ ALUMINIUM DOORS (8) ============
add("ALD", 1, "SlimHinge Alu Door",
    "Slim aluminium hinged door with clear glass — modern interior classic.",
    ["900 × 2100 mm", "1000 × 2400 mm"], ["Silver", "Black"],
    ["36mm slim frame", "SS concealed hinges"],
    ["doorSlim", {}])
add("ALD", 2, "AluSlide Door",
    "Aluminium sliding door with 2 smooth-running glass panels.",
    ["1800 × 2100 mm", "2400 × 2200 mm"], ["Black", "Silver"],
    ["Heavy-duty bottom track", "Lockable handles"],
    ["doorSliding", {}])
add("ALD", 3, "Folia Bi-Fold Door",
    "Two-panel aluminium bi-fold that opens the balcony fully.",
    ["1200 × 2100 mm", "1800 × 2200 mm"], ["White", "Black"],
    ["Folds flat against wall", "Floor-mounted pivot"],
    ["doorBiFold", {}])
add("ALD", 4, "SwingLine Door",
    "Single aluminium swing door with glass for offices & shops.",
    ["900 × 2100 mm", "1000 × 2100 mm"], ["Silver", "Bronze"],
    ["Spring/floor hinge ready", "Push plate + handle set"],
    ["doorSingle", {"pattern": "glass"}])
add("ALD", 5, "PivotAlu Door",
    "Heavy-gauge aluminium pivot door for showrooms and grand entrances.",
    ["1100 × 2400 mm", "1500 × 2700 mm"], ["Black", "Grey"],
    ["Heavy pivot hinge system", "Full-height design"],
    ["doorPivot", {}])
add("ALD", 6, "HotelPlus Door",
    "Durable aluminium door for hotels & commercial — high traffic rated.",
    ["900 × 2100 mm", "1000 × 2400 mm"], ["Silver", "Black"],
    ["Anti-theft locking", "Scratch-resistant coating"],
    ["doorSingle", {"pattern": "2panel"}])
add("ALD", 7, "StoreGlide Door",
    "Single glass aluminium door for shop front entrances with SS frame.",
    ["900 × 2100 mm", "1200 × 2400 mm"], ["Silver", "Gold"],
    ["Heavy glass with SS fittings", "Suitable for automatic operator"],
    ["doorSlim", {}])
add("ALD", 8, "DualSwing Door",
    "Double aluminium door with center meeting — wide commercial entrance.",
    ["1800 × 2100 mm", "2400 × 2400 mm"], ["Silver", "Black"],
    ["Panic-bar ready", "Symmetrical twin leaves"],
    ["doorDouble", {}])

# ============ ALUMINIUM PARTITIONS (8) ============
add("ALP", 1, "GridWall Partition",
    "Aluminium grid glass partition — the classic office space divider.",
    ["Panel 1200 mm wide", "Custom lengths"], ["Silver", "Black", "White"],
    ["12mm toughened glass", "Level-adjustable base"],
    ["partGrid", {"cols": 4, "rows": 2}])
add("ALP", 2, "FrameLess Glass Partition",
    "Minimal frameless partition with SS clamps — pure glass look.",
    ["Panel 1000 mm wide", "Custom heights"], ["Silver", "Clear glass"],
    ["10mm frameless glass", "SS clamp fittings"],
    ["partFrameless", {}])
add("ALP", 3, "OfficeCubicle System",
    "Modular work-station cubicles with glass top and solid lower panel.",
    ["1500 × 1500 mm modules"], ["Grey", "White"],
    ["Cable-managed panels", "Desk integration"],
    ["partCubicle", {}])
add("ALP", 4, "SlidePart Partition",
    "Sliding glass partition panels that stack away to open the space.",
    ["Panel 900 mm wide"], ["Silver", "Black"],
    ["Top-hung sliding track", "Stackable panels"],
    ["partSliding", {}])
add("ALP", 5, "HalfWall Partition",
    "Glass-top + solid-bottom partition — privacy with light.",
    ["Panel 1200 mm wide"], ["Grey", "Oak"],
    ["Solid laminated lower panel", "Glare-free glass top"],
    ["partHalf", {}])
add("ALP", 6, "BlindLine Partition",
    "Glass partition with integrated blinds inside the glass cavity.",
    ["Panel 1200 mm wide"], ["White blinds", "Grey blinds"],
    ["Dust-free internal blinds", "Magnetic control"],
    ["partBlind", {}])
add("ALP", 7, "CurveWall Partition",
    "Curved glass-aluminium partition wall for reception & lobby drama.",
    ["Custom radius"], ["Silver", "Black"],
    ["Curved glass panels", "Precision bent frames"],
    ["partCurve", {}])
add("ALP", 8, "MeetingRoom Glass Wall",
    "Full glass wall with door leaf — sound-smart meeting rooms.",
    ["Custom room size"], ["Clear glass", "Frosted film"],
    ["With integrated door", "Frosted film option for privacy"],
    ["partOfficeWall", {}])

# ============ GLASS SOLUTIONS (10) ============
add("GLZ", 1, "StairGlass Railing",
    "Toughened glass railing along staircases with SS handrail on top.",
    ["Custom staircase"], ["Clear", "Frosted", "Bronze tint"],
    ["12mm toughened glass", "SS base shoe & clamps"],
    ["glassStairRail", {}])
add("GLZ", 2, "Balcony Glass Railing",
    "Floor-to-ceiling glass balcony railing with minimal SS top rail.",
    ["Custom balcony size"], ["Clear", "Green tint"],
    ["Frameless panoramic view", "Wind-load tested fixing"],
    ["glassBalcony", {}])
add("GLZ", 3, "RainShower Enclosure",
    "Corner shower cubicle with 8mm toughened glass & SS hinges.",
    ["900 × 900 mm", "1200 × 900 mm"], ["Clear glass", "Patterned glass"],
    ["Water-tight profile system", "Quick-drain base option"],
    ["glassShower", {}])
add("GLZ", 4, "ShopFront Glazing",
    "Floor-to-ceiling toughened glass shop front with swing door.",
    ["Custom shop size"], ["Clear", "Tinted"],
    ["10-12mm toughened glass", "SS door + push bar"],
    ["glassShopfront", {}])
add("GLZ", 5, "FullView Glass Door",
    "Single leaf frameless glass door with SS patch fittings.",
    ["900 × 2100 mm"], ["Clear glass", "Frosted"],
    ["SS patch fitting system", "Floor spring option"],
    ["glassDoorSingle", {}])
add("GLZ", 6, "MirrorWall Panels",
    "Wall-to-wall mirror panels with silver backing for gyms, salons & lobbies.",
    ["Panel 1200 × 2400 mm"], ["Plain", "Beveled", "Antique"],
    ["5mm mirror quality glass", "Frameless edge-polished"],
    ["glassMirror", {}])
add("GLZ", 7, "GlassFloor Walkway",
    "Structural glass floor panels with SS frame — dramatic mezzanine touch.",
    ["Panel 800 × 800 mm"], ["Sandwich glass"],
    ["Laminated structural glass", "Anti-slip finish option"],
    ["glassFloor", {}])
add("GLZ", 8, "SkyLite Skylight",
    "Sloped glass skylight with aluminium frame — natural light all day.",
    ["Custom roof size"], ["Clear", "Solar-control glass"],
    ["Leak-proof glazing system", "Heat-reflective glass option"],
    ["glassSkylight", {}])
add("GLZ", 9, "Entry Glass Canopy",
    "Sloped glass canopy over entrance doors — stylish & weather-proof.",
    ["1200 × 1500 mm", "Custom"], ["Clear glass", "Laminated"],
    ["SS brackets & supports", "Self-cleaning glass option"],
    ["glassCanopy", {}])
add("GLZ", 10, "Toughened Safety Door",
    "12mm toughened glass door with pivot fittings for premium interiors.",
    ["900 × 2100 mm", "1000 × 2400 mm"], ["Clear", "Bronze tint"],
    ["12mm toughened glass", "Heavy-duty pivot set"],
    ["glassDoorTough", {}])

# ============ STOREFRONT & FACADE (8) ============
add("STF", 1, "ShopFront Signature",
    "Complete shop front system: glass + signage zone + entry door.",
    ["Custom shop size"], ["Black frames", "Silver frames"],
    ["Signage band integrated", "Showcase lighting provision"],
    ["sfShopfront", {}])
add("STF", 2, "CurtainWall System",
    "Aluminium curtain wall grid glazing for multi-storey buildings.",
    ["Custom facade"], ["Silver", "Black", "Custom RAL"],
    ["4/6-side structural glazing", "Thermal break option"],
    ["sfCurtainwall", {}])
add("STF", 3, "ACP Cladding",
    "Aluminium composite panel cladding for modern building facades.",
    ["Panel 1220 × 2440 mm"], ["Silver", "Gold", "Wood", "Brushed"],
    ["Fire-retardant ACP grade", "Rain-screen fixing system"],
    ["sfACP", {}])
add("STF", 4, "Structural Glazing",
    "Glass-to-glass structural glazing with minimal aluminium support.",
    ["Custom facade"], ["Clear", "Reflective"],
    ["Structural silicone bond", "Concealed fixing"],
    ["sfStructural", {}])
add("STF", 5, "Glass Fin Wall",
    "Glass fin supported wall — uninterrupted all-glass storefront.",
    ["Custom size"], ["Clear glass"],
    ["12mm glass fins", "Zero visible mullions"],
    ["sfFinwall", {}])
add("STF", 6, "Entrance Lobby Glazing",
    "Grand double-height glass entrance with canopy for offices & malls.",
    ["Custom lobby"], ["Clear", "Solar glass"],
    ["Double-height glazing", "Automatic door provision"],
    ["sfLobby", {}])
add("STF", 7, "Canopy Marquee",
    "Sloped glass marquee canopy on steel posts for building entrances.",
    ["1800 × 2400 mm", "Custom"], ["Clear glass", "Polycarbonate option"],
    ["Wind-load designed", "LED light provision"],
    ["sfCanopy", {}])
add("STF", 8, "Column Cladding",
    "ACP/aluminium column covers that transform plain pillars into design features.",
    ["Custom column size"], ["Brushed", "Stone", "Wood"],
    ["Shaped panel fabrication", "Fire-safe core"],
    ["sfColumn", {}])

# ============ MS & STEEL WORKS (10) ============
add("MST", 1, "Royal Double Gate",
    "Ornamental MS double gate with lattice design for villas & farms.",
    ["2400 × 1800 mm", "3600 × 2400 mm"], ["Black", "Antique Brown", "Custom"],
    ["Diagonal lattice panels", "Heavy-duty hinges + lock box"],
    ["msDoubleGate", {}])
add("MST", 2, "SlideRunner MS Gate",
    "Rolling MS sliding gate on wheels — best for driveways & plots.",
    ["3000 × 1800 mm", "Custom"], ["Black", "Green", "Grey"],
    ["Wheel & track system", "Self-supporting cantilever option"],
    ["msSlidingGate", {}])
add("MST", 3, "Ornate Window Grill",
    "Classic MS window grill with vertical bars & locking frame.",
    ["1200 × 1200 mm", "1500 × 1500 mm"], ["Black", "White", "Brown"],
    ["Removable/hinged option", "Anti-cut round bars"],
    ["msWindowGrill", {}])
add("MST", 4, "Fortress Security Door",
    "Solid MS security door with ribbed panels and heavy locks.",
    ["1000 × 2100 mm", "1200 × 2400 mm"], ["Black", "Grey", "Wood-finish"],
    ["Reinforced frame & shutters", "Double-bolt locking"],
    ["msSecurityDoor", {}])
add("MST", 5, "Steel Staircase",
    "MS staircase with chequered plate steps & SS handrail — industrial chic.",
    ["Custom flight"], ["Black", "Primer + PU paint"],
    ["Chequered plate treads", "Stringer beam structure"],
    ["msStair", {}])
add("MST", 6, "Pergola Luxe",
    "MS pergola frame for garden & rooftop — ready for cladding or vines.",
    ["3000 × 3000 mm", "Custom"], ["Black", "White", "Wood tone"],
    ["Beam & purlin grid", "Base plates with anchors"],
    ["msPergola", {}])
add("MST", 7, "Shed Canopy MS",
    "Sloped MS sheet canopy for parking, shops & backyards.",
    ["3000 × 4000 mm", "Custom"], ["Galvanized sheet", "Color-coated"],
    ["Gutter & downpipe included", "Brace-designed structure"],
    ["msCanopy", {}])
add("MST", 8, "Balcony Grill Classic",
    "MS balcony railing with vertical bars — safe for kids & pets.",
    ["Custom length"], ["Black", "Brown"],
    ["1200mm safe height", "Anti-climb bar spacing"],
    ["msBalconyGrill", {}])
add("MST", 9, "Diamond Grille Window",
    "Decorative diamond-pattern MS grille for traditional homes.",
    ["900 × 1200 mm", "1200 × 1500 mm"], ["Black", "Antique finish"],
    ["Ornamental diamond weave", "Hinged for cleaning"],
    ["msGrille", {}])
add("MST", 10, "Compound Fence",
    "MS compound fencing with posts & rails for plots and institutions.",
    ["Panel 2400 mm"], ["Green", "Black", "Grey"],
    ["Post + rail system", "Welded panel joints"],
    ["msFence", {}])

# ============ STAINLESS STEEL (8) ============
add("SLS", 1, "MirrorLine SS Railing",
    "SS 304 railing with mirror-finish top rail and slim balusters.",
    ["Custom length"], ["Mirror", "Brushed", "2B"],
    ["Hand-polished mirror finish", "Wall or floor mounting"],
    ["ssRailing", {}])
add("SLS", 2, "WallGlide Handrail",
    "Wall-mounted SS handrail with elegant brackets for corridors & ramps.",
    ["Custom length"], ["Brushed", "Mirror"],
    ["Comfort-grip Ø42mm rail", "Anchored SS brackets"],
    ["ssHandrail", {}])
add("SLS", 3, "PicketPro SS Gate",
    "SS picket gate with flat bar balusters — modern & rust-proof.",
    ["1200 × 2100 mm", "Custom"], ["Brushed", "Mirror"],
    ["Flat-bar pickets", "SS self-closing hinge"],
    ["ssGate", {}])
add("SLS", 4, "StairGuard SS Railing",
    "SS railing following staircase slope with continuous top rail.",
    ["Custom flight"], ["Mirror", "Brushed"],
    ["Continuous seamless rail", "Precision mitered joints"],
    ["ssStair", {}])
add("SLS", 5, "SS Frame Partition",
    "Stainless steel framed partition with glass infill for washrooms & lobbies.",
    ["Panel 1200 mm"], ["Brushed", "Mirror"],
    ["SS frame + 10mm glass", "Moisture-proof"],
    ["ssPartition", {}])
add("SLS", 6, "ClampLine Glass Railing",
    "Glass railing held by SS clamp fittings — frameless luxury look.",
    ["Custom length"], ["SS clamps + clear glass"],
    ["Top-rail or clamp system", "12mm tempered glass"],
    ["ssGlassClamp", {}])
add("SLS", 7, "Balustrade Elegance",
    "SS balustrade with glass infill for mezzanines and stair landings.",
    ["Custom length"], ["Brushed", "Mirror"],
    ["Glass + SS combo", "Knee rail option"],
    ["ssBalcony", {}])
add("SLS", 8, "CrystalRack Display",
    "SS frame display rack with glass shelves for showrooms & shops.",
    ["1200 × 2000 mm", "Custom"], ["Brushed", "Black coating"],
    ["4 glass shelves", "Heavy-duty SS frame"],
    ["ssRack", {}])

# ============ RAILINGS & STAIRS (8) ============
add("RLS", 1, "CableLine Railing",
    "Modern cable railing with SS posts — minimalist, open view.",
    ["Custom length"], ["SS posts + black cables"],
    ["4mm SS cable infill", "Tension-adjustable"],
    ["rlCable", {}])
add("RLS", 2, "AluRail System",
    "Powder-coated aluminium railing — light, rust-free, low maintenance.",
    ["Custom length"], ["Black", "Silver", "White"],
    ["Aluminium post & rail", "Any-angle corner capability"],
    ["rlAlu", {}])
add("RLS", 3, "WoodLine Combo Railing",
    "Warm wood top rail with SS posts — premium hybrid design.",
    ["Custom length"], ["Teak finish", "Walnut finish"],
    ["Real wood or wood-look rail", "SS balusters"],
    ["rlWoodCombo", {}])
add("RLS", 4, "Spiral Staircase",
    "Space-saving spiral staircase in SS/MS with glass or SS railing.",
    ["Ø1500-2000 mm"], ["SS + MS combo"],
    ["Compact footprint", "Step lighting option"],
    ["rlSpiral", {}])
add("RLS", 5, "Straight Flight Stair",
    "Straight staircase with glass railing & wooden or MS treads.",
    ["Custom flight"], ["Glass + SS", "MS + wood"],
    ["Treads: wood / granite / glass", "LED nosing option"],
    ["rlStraight", {}])
add("RLS", 6, "Rooftop Guard Railing",
    "Parapet-top guard railing for rooftops & terraces — safety certified.",
    ["Custom length"], ["Black", "SS", "Grey"],
    ["1100mm safety height", "Wind-load designed posts"],
    ["rlRooftop", {}])
add("RLS", 7, "FrameLess Glass Rail",
    "Fully frameless glass railing with invisible SS fixing.",
    ["Custom length"], ["Clear glass"],
    ["Invisible base shoe fixing", "Continuous glass run"],
    ["rlFrameless", {}])
add("RLS", 8, "MinimalLine Railing",
    "Ultra-minimal thin-profile railing for modern architecture.",
    ["Custom length"], ["Black", "Grey"],
    ["8mm glass with slim rails", "Designer minimalist look"],
    ["rlMinimal", {}])

# ============ MODULAR & SPECIAL (10) ============
add("MOD", 1, "GlideWard Wardrobe",
    "Aluminium-framed wardrobe with sliding glass doors & mirrors.",
    ["2400 × 2400 mm", "Custom"], ["Silver", "Black", "Wood finish"],
    ["Soft-close sliding doors", "Mirror door option"],
    ["mdWardrobe", {}])
add("MOD", 2, "Office Cabin Suite",
    "Complete office cabin: glass partition wall + door + furniture line.",
    ["Room size custom"], ["Clear glass", "Frosted"],
    ["Fully glazed front", "Door with SS handle"],
    ["mdCabin", {}])
add("MOD", 3, "GlassShine Kitchen Shutters",
    "Kitchen cabinet shutters with glass + aluminium frames.",
    ["600 mm module"], ["Aluminium frame + glass"],
    ["Shock-proof glass shutter", "Hydraulic hinge option"],
    ["mdKitchen", {}])
add("MOD", 4, "Verandah Enclosure",
    "Glass + aluminium enclosure for verandahs — outdoor feel, indoor comfort.",
    ["Custom"], ["Clear glass", "Solar glass"],
    ["Rain & dust proof", "Sliding window vents"],
    ["mdVerandah", {}])
add("MOD", 5, "Balcony Seal Enclosure",
    "Full balcony glass enclosure with sliding panels — extra usable room.",
    ["Custom balcony"], ["Clear", "Tinted"],
    ["Top & bottom track system", "Quick-install modules"],
    ["mdBalconyEnclose", {}])
add("MOD", 6, "Louver Roof Pergola",
    "Adjustable louvre roof pergola — open sky or shade at a touch.",
    ["3000 × 3000 mm"], ["Aluminium slats", "Powder coated"],
    ["Adjustable louvre blades", "Rain sensor option"],
    ["mdLouverPergola", {}])
add("MOD", 7, "Royal Gazebo",
    "MS + polycarbonate gazebo for gardens & lawns — instant luxury.",
    ["3000 × 3000 mm"], ["Polycarbonate roof", "Glass roof option"],
    ["Pyramid roof design", "Ventilated top"],
    ["mdGazebo", {}])
add("MOD", 8, "CarPort Canopy",
    "Car parking canopy with MS frame & polycarbonate sheet roof.",
    ["3000 × 5000 mm"], ["Clear PC sheet", "Bronze PC"],
    ["UV-protected sheets", "Rain gutter system"],
    ["mdCarport", {}])
add("MOD", 9, "MeshGuard Mosquito Window",
    "Aluminium frame window with fine SS mesh — insect-free fresh air.",
    ["1200 × 1200 mm"], ["SS mesh", "Fiber mesh"],
    ["Fine SS mesh", "Sliding or fixed type"],
    ["mdMosquito", {}])
add("MOD", 10, "RollSafe Shutter",
    "Rolling shutter for shops & garages — secure, space-saving.",
    ["Custom opening"], ["Galvanized", "Color-coated"],
    ["Lockable bottom bar", "Manual / motorized drive"],
    ["mdShutter", {}])

assert len(P) == 102, "Expected 102 products, got %d" % len(P)
