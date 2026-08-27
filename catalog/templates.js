/* ==================== SVG ART TEMPLATES ==================== */
/* Every product gets a unique technical line-art drawing.     */
var TEMPLATES = (function () {
  var SW = "#33404f";        // frame stroke
  var SWL = "#8fa3b8";       // light stroke
  var GOLD = "#b98a2f";      // accent
  var GL = "rgba(172,207,235,.42)";
  var GL2 = "rgba(150,195,225,.30)";

  function RX(x, y, w, h, r) { r = r || 2; return '<rect x="' + x + '" y="' + y + '" width="' + w + '" height="' + h + '" rx="' + r + '"/>'; }
  function glass(x, y, w, h, f) { f = f || GL; return '<rect x="' + x + '" y="' + y + '" width="' + w + '" height="' + h + '" fill="' + f + '" stroke="' + SWL + '" stroke-width="1.1"/>'; }
  function sheen(x, y, w, h) { return '<line x1="' + x + '" y1="' + (y + h * 0.78) + '" x2="' + (x + w * 0.62) + '" y2="' + (y + h * 0.22) + '" stroke="rgba(255,255,255,.8)" stroke-width="7" stroke-linecap="round"/>'; }
  function frame(x, y, w, h) { return '<rect x="' + x + '" y="' + y + '" width="' + w + '" height="' + h + '" fill="none" stroke="' + SW + '" stroke-width="2.4"/>'; }
  function handle(x, y, v) { v = v || 0; return '<g stroke="' + SW + '" stroke-width="2" fill="none"><circle cx="' + x + '" cy="' + y + '" r="2.2"/><line x1="' + x + '" y1="' + y + '" x2="' + (v ? x : x + 12) + '" y2="' + (v ? y + 12 : y) + '"/></g>'; }
  function hinge(x, y) { return '<circle cx="' + x + '" cy="' + y + '" r="2.4" fill="' + GOLD + '" stroke="' + SW + '" stroke-width="1.2"/>'; }
  function dashArc(x1, y1, x2, y2, rx, ry) { return '<path d="M ' + x1 + ' ' + y1 + ' A ' + rx + ' ' + ry + ' 0 0 1 ' + x2 + ' ' + y2 + '" fill="none" stroke="' + GOLD + '" stroke-width="1.6" stroke-dasharray="4 3"/>'; }
  function mull(x1, y1, x2, y2, w) { w = w || 3.4; return '<line x1="' + x1 + '" y1="' + y1 + '" x2="' + x2 + '" y2="' + y2 + '" stroke="' + SW + '" stroke-width="' + w + '"/>'; }

  /* ---------- WINDOWS ---------- */
  function winSliding(p) {
    var n = p.panes || 2, s = "";
    var w = 180 / n;
    for (var i = 0; i < n; i++) {
      var x = 12 + i * w;
      s += glass(x, 14, w - 6, 110) + sheen(x, 14, w - 6, 110);
    }
    return frame(8, 8, 184, 122) + s +
      mull(12, 14, 12, 124) + mull(188 - 8, 14, 188 - 8, 124) +
      '<line x1="8" y1="130" x2="192" y2="130" stroke="' + SW + '" stroke-width="1.4"/>' +
      '<line x1="12" y1="134" x2="188" y2="134" stroke="' + SW + '" stroke-width="1.4"/>' +
      handle(12 + w * (n - 1) + 6, 66, 1) + handle(12 + w * (n - 1) - 14, 86, 1);
  }
  function winCasement(p) {
    var leaves = p.leaves || 2, s = "";
    var w = 168 / leaves;
    for (var i = 0; i < leaves; i++) {
      var x = 16 + i * w;
      s += glass(x + 3, 17, w - 6, 106) + sheen(x + 3, 17, w - 6, 106);
      if (i > 0) s += hinge(x, 22) + hinge(x, 118);
      s += handle(x + w - 22, 70);
    }
    return frame(10, 10, 180, 120) + s +
      dashArc(176, 20, 190, 70, 18, 30) + dashArc(190, 70, 176, 120, 18, 30);
  }
  function winTiltTurn(p) {
    var s = glass(20, 18, 160, 102) + sheen(20, 18, 160, 102);
    return frame(12, 12, 176, 116) + s +
      hinge(20, 24) + hinge(20, 114) + handle(150, 66) +
      '<path d="M 96 6 l 9 -8 l 9 8 M 96 6 l 9 8 l 9 -8" fill="none" stroke="' + GOLD + '" stroke-width="1.6"/>' +
      dashArc(30, 128, 96, 134, 40, 20) +
      '<path d="M 30 128 Q 60 142 96 134" fill="none" stroke="' + GOLD + '" stroke-width="1.6" stroke-dasharray="4 3"/>';
  }
  function winTopHung(p) {
    var s = glass(20, 18, 160, 102) + sheen(20, 18, 160, 102);
    return frame(12, 12, 176, 116) + s +
      hinge(40, 20) + hinge(160, 20) + handle(100, 116) +
      dashArc(190, 60, 190, 110, 26, 30) + dashArc(10, 60, 10, 110, 26, 30);
  }
  function winAwning(p) {
    var s = '<path d="M 22 126 L 178 126 L 166 44 L 34 44 Z" fill="' + GL + '" stroke="' + SWL + '" stroke-width="1.2"/>' + sheen(34, 44, 132, 82);
    return frame(14, 12, 172, 116) + s +
      hinge(22, 126) + hinge(178, 126) + handle(100, 60) +
      dashArc(24, 44, 34, 44, 30, 10) + dashArc(176, 44, 166, 44, 30, 10);
  }
  function winBay(p) {
    var s = '<polygon points="34,34 74,24 74,118 34,128" fill="' + GL + '" stroke="' + SWL + '" stroke-width="1.2"/>' +
      '<polygon points="126,24 166,34 166,128 126,118" fill="' + GL + '" stroke="' + SWL + '" stroke-width="1.2"/>' +
      glass(78, 22, 44, 98) + sheen(78, 22, 44, 98);
    return frame(8, 10, 184, 122) + s +
      mull(34, 34, 74, 24) + mull(34, 128, 74, 118) + mull(126, 24, 166, 34) + mull(126, 118, 166, 128) +
      '<line x1="8" y1="132" x2="192" y2="132" stroke="' + SW + '" stroke-width="1.4"/>';
  }
  function winArch(p) {
    var s = '<path d="M 22 132 L 22 58 A 78 34 0 0 1 178 58 L 178 132 Z" fill="' + GL + '" stroke="' + SWL + '" stroke-width="1.2"/>' + sheen(30, 40, 140, 90);
    return '<path d="M 12 132 L 12 54 A 88 40 0 0 1 188 54 L 188 132 Z" fill="none" stroke="' + SW + '" stroke-width="2.4"/>' + s +
      mull(100, 26, 100, 132) + '<line x1="12" y1="136" x2="188" y2="136" stroke="' + SW + '" stroke-width="1.4"/>';
  }
  function winCorner(p) {
    var s = glass(20, 20, 96, 84) + sheen(20, 20, 96, 84) + glass(120, 30, 60, 96) + sheen(120, 30, 60, 96);
    return frame(14, 14, 108, 96) + frame(114, 24, 72, 108) + s +
      mull(20, 20, 20, 104) + mull(116, 30, 116, 126) + mull(120, 24, 120, 126) +
      '<line x1="108" y1="110" x2="114" y2="108" stroke="' + GOLD + '" stroke-width="3"/>';
  }
  function winFixed(p) {
    return frame(10, 10, 180, 120) + glass(16, 16, 168, 108) + sheen(16, 16, 168, 108) +
      '<path d="M 16 16 L 48 124 M 70 16 L 100 124 M 124 16 L 152 124" stroke="rgba(255,255,255,.55)" stroke-width="2"/>';
  }
  function winProjected(p) {
    var s = "";
    for (var i = 0; i < 3; i++) s += glass(20, 20 + i * 36, 160, 30) + sheen(20, 20 + i * 36, 160, 30);
    return frame(12, 12, 176, 116) + s +
      hinge(20, 38) + hinge(20, 74) + hinge(20, 110) + handle(166, 66) +
      dashArc(184, 30, 190, 66, 20, 22) + dashArc(190, 66, 184, 102, 20, 22);
  }
  function winCombo(p) {
    var s = glass(20, 18, 72, 102) + sheen(20, 18, 72, 102) + glass(106, 18, 72, 102) + sheen(106, 18, 72, 102);
    return frame(12, 12, 176, 116) + s +
      hinge(106, 26) + hinge(106, 112) + handle(162, 66) +
      dashArc(178, 40, 190, 70, 16, 22) + dashArc(190, 70, 178, 100, 16, 22);
  }
  function winGarden(p) {
    var s = '<polygon points="30,42 70,34 70,124 30,132" fill="' + GL + '" stroke="' + SWL + '" stroke-width="1.2"/>' +
      '<polygon points="130,34 170,42 170,132 130,124" fill="' + GL + '" stroke="' + SWL + '" stroke-width="1.2"/>' +
      glass(74, 32, 52, 94) + sheen(74, 32, 52, 94);
    return frame(8, 10, 184, 124) + s +
      mull(30, 42, 70, 34) + mull(30, 132, 70, 124) + mull(130, 34, 170, 42) + mull(130, 124, 170, 132) +
      '<path d="M 8 10 L 192 10 L 192 16 L 8 16 Z" fill="' + SW + '" opacity=".85"/>';
  }
  function winLouver(p) {
    var s = "";
    for (var i = 0; i < 5; i++) {
      var y = 26 + i * 20;
      s += '<path d="M 22 ' + y + ' L 40 ' + (y - 6) + ' L 178 ' + (y - 6) + ' L 178 ' + (y + 4) + ' L 40 ' + (y + 4) + ' Z" fill="' + GL + '" stroke="' + SWL + '" stroke-width="1.2"/>';
    }
    return frame(12, 12, 176, 116) + s + mull(100, 12, 100, 128);
  }

  /* ---------- DOORS ---------- */
  function doorBase(p) { // p.pattern: 'solid' | '2panel' | '4panel' | 'glass' | 'arch'
    var s = "";
    if (p.pattern === '2panel') {
      s = '<path d="M 70 16 L 130 16 L 130 64 L 70 64 Z M 70 74 L 130 74 L 130 138 L 70 138 Z" fill="' + GL + '" stroke="' + SWL + '" stroke-width="1.1"/>';
    } else if (p.pattern === '4panel') {
      s = '<path d="M 70 16 L 96 16 L 96 62 L 70 62 Z M 104 16 L 130 16 L 130 62 L 104 62 Z M 70 72 L 96 72 L 96 138 L 70 138 Z M 104 72 L 130 72 L 130 138 L 104 138 Z" fill="' + GL + '" stroke="' + SWL + '" stroke-width="1.1"/>';
    } else if (p.pattern === 'glass') {
      s = glass(72, 16, 56, 118) + sheen(72, 16, 56, 118);
    } else if (p.pattern === 'arch') {
      s = '<path d="M 72 138 L 72 52 A 28 24 0 0 1 128 52 L 128 138 Z" fill="' + GL + '" stroke="' + SWL + '" stroke-width="1.1"/>' + sheen(76, 40, 48, 96);
    } else {
      s = '<rect x="70" y="16" width="60" height="122" fill="#e8ecf1" stroke="' + SWL + '" stroke-width="1.1"/>';
    }
    return s;
  }
  function doorSingle(p) {
    var s = doorBase(p);
    return frame(64, 6, 72, 148) + s + mull(64, 6, 64, 154) + handle(134, 80) +
      '<line x1="64" y1="154" x2="136" y2="154" stroke="' + SW + '" stroke-width="2"/>' +
      hinge(66, 30) + hinge(66, 130);
  }
  function doorDouble(p) {
    var s = '<path d="M 66 14 L 96 14 L 96 142 L 66 142 Z M 104 14 L 134 14 L 134 142 L 104 142 Z" fill="' + GL + '" stroke="' + SWL + '" stroke-width="1.1"/>';
    return frame(60, 6, 80, 148) + s + mull(100, 6, 100, 154) +
      handle(96, 80) + handle(104, 80) + hinge(62, 26) + hinge(138, 26) + hinge(62, 132) + hinge(138, 132);
  }
  function doorFrench(p) {
    var s = "";
    for (var r = 0; r < 2; r++) for (var c = 0; c < 3; c++) s += glass(70 + c * 20, 20 + r * 58, 17, 54) + sheen(70 + c * 20, 20 + r * 58, 17, 54);
    return frame(64, 6, 72, 148) + s + handle(134, 80) + hinge(66, 28) + hinge(66, 132);
  }
  function doorSliding(p) {
    var s = glass(26, 14, 76, 116) + sheen(26, 14, 76, 116) + glass(98, 14, 76, 116) + sheen(98, 14, 76, 116);
    return frame(20, 8, 160, 128) + s +
      '<line x1="20" y1="136" x2="180" y2="136" stroke="' + SW + '" stroke-width="1.4"/>' +
      '<line x1="24" y1="140" x2="176" y2="140" stroke="' + SW + '" stroke-width="1.4"/>' +
      handle(104, 60, 1) + handle(170, 80);
  }
  function doorFolding(p) {
    var s = "";
    for (var i = 0; i < 4; i++) {
      var x = 22 + i * 40;
      s += glass(x + 3, 16 + (i % 2) * 6, 34, 110) + sheen(x + 3, 16 + (i % 2) * 6, 34, 110);
      if (i > 0) s += hinge(x, 20) + hinge(x, 122);
    }
    return frame(16, 8, 168, 128) + s + handle(180, 72) + mull(16, 8, 16, 136);
  }
  function doorBalcony(p) {
    var s = glass(66, 12, 68, 130) + sheen(66, 12, 68, 130) + mull(100, 12, 100, 142);
    return frame(60, 6, 80, 148) + s + handle(130, 78) + hinge(62, 28) + hinge(62, 132);
  }
  function doorPivot(p) {
    var s = glass(74, 16, 52, 120) + sheen(74, 16, 52, 120) + mull(100, 16, 100, 136);
    return frame(60, 6, 80, 148) + s + handle(122, 78) +
      '<circle cx="100" cy="8" r="3" fill="' + GOLD + '"/><circle cx="100" cy="152" r="3" fill="' + GOLD + '"/>';
  }
  function doorArch(p) {
    var s = '<path d="M 70 138 L 70 44 A 30 26 0 0 1 130 44 L 130 138 Z" fill="' + GL + '" stroke="' + SWL + '" stroke-width="1.1"/>' + sheen(74, 30, 52, 106);
    return '<path d="M 64 150 L 64 40 A 36 30 0 0 1 136 40 L 136 150 Z" fill="none" stroke="' + SW + '" stroke-width="2.4"/>' + s +
      handle(134, 86) + hinge(66, 40) + hinge(66, 130);
  }
  function doorGrill(p) {
    var s = '<rect x="68" y="14" width="64" height="126" fill="#eef1f5" stroke="' + SWL + '" stroke-width="1.1"/>';
    for (var i = -1; i < 2; i++) s += '<line x1="68" y1="' + (77 + i * 38) + '" x2="132" y2="' + (77 - i * 38) + '" stroke="' + SW + '" stroke-width="3"/>';
    return frame(62, 6, 76, 148) + s + handle(136, 80) + hinge(64, 28) + hinge(64, 132);
  }
  function doorSlim(p) {
    var s = glass(70, 14, 60, 124) + sheen(70, 14, 60, 124);
    return frame(64, 6, 72, 148) + s + handle(132, 78) + hinge(66, 30) + hinge(66, 130);
  }
  function doorBiFold(p) {
    var s = '<polygon points="62,8 100,8 100,152 62,152" fill="' + GL + '" stroke="' + SWL + '" stroke-width="1.1"/>' +
      '<polygon points="102,14 140,20 136,158 98,152" fill="' + GL + '" stroke="' + SWL + '" stroke-width="1.1"/>' +
      sheen(66, 12, 30, 136);
    return frame(56, 4, 88, 152) + s + hinge(100, 20) + hinge(100, 140) + handle(132, 82) + mull(56, 4, 56, 156);
  }

  /* ---------- PARTITIONS ---------- */
  function partGrid(p) {
    var cols = p.cols || 4, rows = p.rows || 2, s = "";
    var w = 168 / cols, h = 108 / rows;
    for (var r = 0; r < rows; r++) for (var c = 0; c < cols; c++) s += glass(16 + c * w, 16 + r * h, w - 4, h - 4);
    return frame(10, 10, 180, 120) + s;
  }
  function partFrameless(p) {
    var s = "";
    for (var i = 0; i < 3; i++) {
      s += glass(12 + i * 60, 14, 54, 108) + sheen(12 + i * 60, 14, 54, 108);
      s += '<circle cx="' + (14 + i * 60) + '" cy="18" r="2" fill="' + GOLD + '"/><circle cx="' + (14 + i * 60) + '" cy="118" r="2" fill="' + GOLD + '"/>';
    }
    return '<line x1="10" y1="10" x2="190" y2="10" stroke="' + SW + '" stroke-width="1.6"/>' +
      '<line x1="10" y1="130" x2="190" y2="130" stroke="' + SW + '" stroke-width="1.6"/>' + s;
  }
  function partCubicle(p) {
    var s = '<rect x="12" y="44" width="44" height="96" fill="#eef1f5" stroke="' + SW + '" stroke-width="2"/>' +
      '<rect x="144" y="44" width="44" height="96" fill="#eef1f5" stroke="' + SW + '" stroke-width="2"/>' +
      glass(60, 16, 80, 124) + sheen(60, 16, 80, 124) +
      '<line x1="60" y1="44" x2="140" y2="44" stroke="' + SW + '" stroke-width="2"/>' +
      '<line x1="20" y1="140" x2="180" y2="140" stroke="' + SW + '" stroke-width="2.4"/>';
    return frame(8, 8, 184, 136) + s;
  }
  function partSliding(p) {
    var s = "";
    for (var i = 0; i < 3; i++) s += glass(16 + i * 52, 18 + i * 10, 48, 96) + sheen(16 + i * 52, 18 + i * 10, 48, 96);
    return frame(10, 10, 180, 120) + s +
      '<line x1="10" y1="10" x2="190" y2="10" stroke="' + SW + '" stroke-width="3"/>' +
      '<line x1="14" y1="14" x2="186" y2="14" stroke="' + SWL + '" stroke-width="1"/>';
  }
  function partHalf(p) {
    var s = '<rect x="16" y="70" width="168" height="56" fill="#dfe5ec" stroke="' + SWL + '" stroke-width="1.1"/>' + glass(16, 16, 168, 52);
    return frame(10, 10, 180, 120) + s + mull(16, 70, 184, 70);
  }
  function partBlind(p) {
    var s = glass(20, 16, 76, 104) + glass(104, 16, 76, 104);
    for (var i = 0; i < 6; i++) {
      var y = 28 + i * 15;
      s += '<line x1="24" y1="' + y + '" x2="92" y2="' + y + '" stroke="' + SWL + '" stroke-width="2"/>';
      s += '<line x1="108" y1="' + y + '" x2="176" y2="' + y + '" stroke="' + SWL + '" stroke-width="2"/>';
    }
    return frame(10, 10, 180, 120) + s + mull(100, 10, 100, 130);
  }
  function partCurve(p) {
    var s = '<path d="M 24 26 Q 100 6 176 26" fill="none" stroke="' + SW + '" stroke-width="2.4"/>' +
      '<path d="M 24 124 Q 100 104 176 124" fill="none" stroke="' + SW + '" stroke-width="2.4"/>';
    for (var i = 0; i < 5; i++) {
      var x = 40 + i * 30;
      var t = i / 4;
      var yt = 26 - 18 * Math.sin(Math.PI * t);
      var yb = 124 - 18 * Math.sin(Math.PI * t);
      s += mull(x, yt, x, yb, 2.6);
      s += '<path d="M ' + (x - 14) + ' ' + (yt + 2) + ' Q ' + x + ' ' + (yt - 8) + ' ' + (x + 14) + ' ' + (yt + 2) + ' L ' + (x + 14) + ' ' + (yb - 2) + ' Q ' + x + ' ' + (yb + 8) + ' ' + (x - 14) + ' ' + (yb - 2) + ' Z" fill="' + GL + '" stroke="' + SWL + '" stroke-width="1"/>';
    }
    return s;
  }
  function partOfficeWall(p) {
    var s = glass(16, 16, 118, 108) + sheen(16, 16, 118, 108) + glass(146, 16, 38, 108) + sheen(146, 16, 38, 108);
    return frame(10, 10, 180, 120) + s + mull(134, 10, 134, 130) + mull(184, 10, 184, 130) + handle(144, 68);
  }

  /* ---------- GLASS ---------- */
  function glassStairRail(p) {
    var s = '<path d="M 14 146 L 14 118 L 44 118 L 44 90 L 74 90 L 74 62 L 104 62 L 104 34 L 134 34 L 134 22" fill="none" stroke="' + SW + '" stroke-width="3"/>' +
      '<line x1="14" y1="146" x2="134" y2="146" stroke="' + SW + '" stroke-width="2"/>';
    for (var i = 0; i < 4; i++) {
      var x1 = 14 + i * 30, y1 = 146 - i * 28;
      s += '<polygon points="' + x1 + ',' + (y1 - 12) + ' ' + (x1 + 30) + ',' + (y1 - 12) + ' ' + (x1 + 30) + ',' + y1 + ' ' + x1 + ',' + y1 + '" fill="' + GL + '" stroke="' + SWL + '" stroke-width="1.1"/>';
    }
    return '<line x1="14" y1="24" x2="134" y2="24" stroke="' + SW + '" stroke-width="2.6"/>' +
      '<line x1="14" y1="34" x2="134" y2="34" stroke="' + SW + '" stroke-width="1.6"/>' + s;
  }
  function glassBalcony(p) {
    var s = glass(14, 34, 172, 78) + sheen(14, 34, 172, 78);
    for (var i = 0; i < 4; i++) s += mull(48 + i * 36, 34, 48 + i * 36, 112, 2.2);
    return frame(10, 30, 180, 86) + s +
      '<line x1="10" y1="22" x2="190" y2="22" stroke="' + SW + '" stroke-width="2.6"/>' +
      '<rect x="10" y="116" width="180" height="10" fill="#dfe5ec" stroke="' + SWL + '" stroke-width="1"/>';
  }
  function glassShower(p) {
    return '<line x1="10" y1="150" x2="190" y2="150" stroke="' + SW + '" stroke-width="2.6"/>' +
      '<rect x="18" y="18" width="8" height="120" fill="' + GL + '" stroke="' + SWL + '" stroke-width="1.2"/>' +
      '<rect x="18" y="126" width="120" height="8" fill="' + GL + '" stroke="' + SWL + '" stroke-width="1.2"/>' +
      '<path d="M 26 126 A 72 72 0 0 1 126 26 L 126 18" fill="none" stroke="' + GOLD + '" stroke-width="1.8" stroke-dasharray="5 3"/>' +
      '<circle cx="150" cy="30" r="10" fill="none" stroke="' + SW + '" stroke-width="2"/>' +
      '<line x1="150" y1="40" x2="150" y2="80" stroke="' + SW + '" stroke-width="2"/>' +
      '<line x1="138" y1="62" x2="162" y2="62" stroke="' + SW + '" stroke-width="2"/>' +
      handle(128, 66);
  }
  function glassShopfront(p) {
    var s = glass(14, 34, 66, 102) + glass(86, 34, 44, 102) + glass(136, 34, 50, 102);
    s += sheen(14, 34, 66, 102) + sheen(136, 34, 50, 102);
    return frame(10, 30, 180, 110) + s + mull(80, 30, 80, 140) + mull(130, 30, 130, 140) +
      '<rect x="10" y="10" width="180" height="20" fill="#2c3a4a" opacity=".9"/>' +
      '<line x1="30" y1="20" x2="170" y2="20" stroke="#c9a227" stroke-width="2"/>' +
      handle(104, 84) + handle(112, 84);
  }
  function glassDoorSingle(p) {
    var s = glass(72, 14, 56, 122) + sheen(72, 14, 56, 122);
    return frame(64, 6, 72, 148) + s + handle(126, 80) + hinge(66, 30) + hinge(66, 132);
  }
  function glassMirror(p) {
    var s = "";
    for (var i = 0; i < 3; i++) {
      var x = 16 + i * 58;
      s += '<rect x="' + x + '" y="16" width="52" height="104" fill="url(#mg)' + '" stroke="' + SWL + '" stroke-width="1.2"/>';
      s += '<line x1="' + (x + 10) + '" y1="' + (16 + 16) + '" x2="' + (x + 26) + '" y2="' + (16 + 8) + '" stroke="rgba(255,255,255,.9)" stroke-width="5" stroke-linecap="round"/>';
    }
    return '<defs><linearGradient id="mg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#dde6ef"/><stop offset=".5" stop-color="#9fb4c8"/><stop offset="1" stop-color="#c9d6e2"/></linearGradient></defs>' +
      frame(10, 10, 180, 116) + s;
  }
  function glassFloor(p) {
    var s = "";
    for (var r = 0; r < 3; r++) for (var c = 0; c < 4; c++) {
      s += '<rect x="' + (12 + c * 45) + '" y="' + (14 + r * 40) + '" width="43" height="38" fill="' + (r % 2 ? GL2 : GL) + '" stroke="' + SWL + '" stroke-width="1.2"/>';
    }
    return '<rect x="8" y="8" width="184" height="124" fill="none" stroke="' + SW + '" stroke-width="2.2"/>' + s +
      '<circle cx="100" cy="140" r="4" fill="' + GOLD + '"/><circle cx="40" cy="140" r="4" fill="' + GOLD + '"/><circle cx="160" cy="140" r="4" fill="' + GOLD + '"/>';
  }
  function glassSkylight(p) {
    var s = '<polygon points="22,60 178,60 160,26 40,26" fill="' + GL + '" stroke="' + SWL + '" stroke-width="1.2"/>' + sheen(40, 26, 120, 34);
    for (var i = 1; i < 4; i++) {
      var x = 40 + i * 30;
      s += mull(x, 26 + (x - 40) * 0.27, x + 18, 60 + (x - 40) * 0.27, 2.4);
    }
    return '<polygon points="14,66 186,66 166,20 34,20" fill="none" stroke="' + SW + '" stroke-width="2.4"/>' + s +
      '<line x1="30" y1="100" x2="170" y2="100" stroke="' + SW + '" stroke-width="1.6"/>' +
      '<line x1="26" y1="112" x2="174" y2="112" stroke="' + SW + '" stroke-width="1.6"/>';
  }
  function glassCanopy(p) {
    var s = '<polygon points="30,28 170,28 186,52 14,52" fill="' + GL + '" stroke="' + SWL + '" stroke-width="1.2"/>' + sheen(30, 28, 140, 24);
    for (var i = 1; i < 5; i++) s += mull(14 + i * 34, 52, 30 + i * 28, 28, 2.2);
    return '<polygon points="22,22 178,22 194,58 6,58" fill="none" stroke="' + SW + '" stroke-width="2.4"/>' + s +
      '<rect x="70" y="58" width="60" height="6" fill="' + SW + '"/>' +
      '<rect x="76" y="64" width="48" height="60" fill="#e8ecf1" stroke="' + SWL + '" stroke-width="1.1"/>' +
      '<circle cx="100" cy="94" r="6" fill="' + GOLD + '"/>' +
      '<rect x="70" y="124" width="8" height="18" fill="' + SW + '"/><rect x="122" y="124" width="8" height="18" fill="' + SW + '"/>';
  }
  function glassDoorTough(p) {
    var s = glass(70, 14, 60, 122) + sheen(70, 14, 60, 122);
    return frame(64, 6, 72, 148) + s + handle(128, 78) +
      '<circle cx="100" cy="9" r="3.4" fill="' + GOLD + '"/><circle cx="100" cy="151" r="3.4" fill="' + GOLD + '"/>' +
      '<line x1="100" y1="16" x2="100" y2="136" stroke="' + SWL + '" stroke-width="1.4" stroke-dasharray="3 3"/>';
  }

  /* ---------- STOREFRONT / FACADE ---------- */
  function sfShopfront(p) {
    var s = glass(16, 44, 54, 88) + glass(76, 44, 38, 88) + glass(120, 44, 64, 88);
    s += sheen(16, 44, 54, 88) + sheen(120, 44, 64, 88);
    return frame(10, 40, 180, 96) + s + mull(70, 40, 70, 136) + mull(114, 40, 114, 136) +
      '<rect x="10" y="10" width="180" height="28" fill="#2c3a4a"/>' +
      '<line x1="40" y1="24" x2="160" y2="24" stroke="#c9a227" stroke-width="2.4"/>' +
      handle(92, 86) + handle(98, 86) +
      '<rect x="10" y="136" width="180" height="6" fill="' + SW + '"/>';
  }
  function sfCurtainwall(p) {
    var s = "";
    for (var r = 0; r < 4; r++) for (var c = 0; c < 6; c++) s += glass(16 + c * 28, 16 + r * 28, 25, 25);
    return frame(10, 10, 180, 120) + s;
  }
  function sfACP(p) {
    var s = '<rect x="16" y="16" width="80" height="54" fill="#dfe5ec" stroke="' + SWL + '" stroke-width="1.2"/>' +
      '<rect x="104" y="16" width="80" height="54" fill="#cdd6e0" stroke="' + SWL + '" stroke-width="1.2"/>' +
      '<rect x="16" y="78" width="80" height="54" fill="#cdd6e0" stroke="' + SWL + '" stroke-width="1.2"/>' +
      '<rect x="104" y="78" width="80" height="54" fill="#dfe5ec" stroke="' + SWL + '" stroke-width="1.2"/>';
    for (var i = 0; i < 3; i++) s += mull(16 + i * 28, 16, 16 + i * 28, 132, 2);
    return '<rect x="10" y="10" width="180" height="120" fill="none" stroke="' + SW + '" stroke-width="2.4"/>' + s +
      '<line x1="10" y1="76" x2="190" y2="76" stroke="' + SW + '" stroke-width="1.6"/>';
  }
  function sfStructural(p) {
    var s = glass(18, 18, 164, 104) + sheen(18, 18, 164, 104);
    for (var i = 0; i < 5; i++) s += mull(30 + i * 36, 14, 30 + i * 36, 126, 4);
    return frame(10, 10, 180, 120) + s;
  }
  function sfFinwall(p) {
    var s = "";
    for (var i = 0; i < 4; i++) s += glass(24 + i * 42, 20, 34, 100) + sheen(24 + i * 42, 20, 34, 100);
    return frame(10, 10, 180, 120) + s +
      '<rect x="14" y="14" width="6" height="112" fill="' + SW + '"/>' +
      '<rect x="60" y="14" width="6" height="112" fill="' + SW + '"/>' +
      '<rect x="102" y="14" width="6" height="112" fill="' + SW + '"/>' +
      '<rect x="144" y="14" width="6" height="112" fill="' + SW + '"/>' +
      '<rect x="180" y="14" width="6" height="112" fill="' + SW + '"/>';
  }
  function sfLobby(p) {
    var s = glass(16, 30, 168, 74) + sheen(16, 30, 168, 74) + glass(16, 108, 168, 26) + sheen(16, 108, 168, 26);
    return frame(10, 26, 180, 112) + s +
      mull(100, 26, 100, 138) + handle(90, 80) + handle(110, 80) +
      '<polygon points="6,26 194,26 170,12 30,12" fill="' + SW + '" opacity=".9"/>' +
      '<line x1="60" y1="19" x2="140" y2="19" stroke="#c9a227" stroke-width="2"/>' +
      '<line x1="10" y1="138" x2="190" y2="138" stroke="' + SW + '" stroke-width="3"/>';
  }
  function sfCanopy(p) {
    var s = '<polygon points="26,26 174,26 190,50 10,50" fill="' + GL + '" stroke="' + SWL + '" stroke-width="1.2"/>' + sheen(26, 26, 148, 24);
    for (var i = 1; i < 5; i++) s += mull(10 + i * 36, 50, 26 + i * 30, 26, 2.2);
    return '<polygon points="18,20 182,20 196,56 4,56" fill="none" stroke="' + SW + '" stroke-width="2.4"/>' + s +
      '<rect x="20" y="56" width="8" height="76" fill="' + SW + '"/><rect x="172" y="56" width="8" height="76" fill="' + SW + '"/>' +
      '<line x1="16" y1="132" x2="184" y2="132" stroke="' + SW + '" stroke-width="2"/>' +
      '<rect x="80" y="62" width="40" height="64" fill="#e8ecf1" stroke="' + SWL + '" stroke-width="1.1"/>' + handle(114, 94);
  }
  function sfColumn(p) {
    var s = '<rect x="76" y="14" width="48" height="118" fill="#dfe5ec" stroke="' + SWL + '" stroke-width="1.1"/>';
    for (var i = 0; i < 6; i++) s += mull(76, 30 + i * 18, 124, 30 + i * 18, 1.6);
    return '<polygon points="66,8 134,8 150,148 50,148" fill="none" stroke="' + SW + '" stroke-width="2.4"/>' + s +
      '<rect x="50" y="148" width="100" height="8" fill="' + SW + '"/>' +
      '<line x1="50" y1="14" x2="150" y2="14" stroke="' + GOLD + '" stroke-width="2"/>';
  }

  /* ---------- MS / STEEL ---------- */
  function msDoubleGate(p) {
    var s = '<rect x="14" y="36" width="82" height="96" fill="#eef1f5" stroke="' + SW + '" stroke-width="2"/>' +
      '<rect x="104" y="36" width="82" height="96" fill="#eef1f5" stroke="' + SW + '" stroke-width="2"/>';
    for (var i = -1; i < 2; i++) {
      s += '<line x1="18" y1="' + (84 + i * 30) + '" x2="92" y2="' + (84 - i * 30) + '" stroke="' + SWL + '" stroke-width="2"/>';
      s += '<line x1="108" y1="' + (84 + i * 30) + '" x2="182" y2="' + (84 - i * 30) + '" stroke="' + SWL + '" stroke-width="2"/>';
    }
    return frame(10, 32, 180, 104) + s +
      '<line x1="10" y1="140" x2="190" y2="140" stroke="' + SW + '" stroke-width="2.4"/>' +
      '<rect x="80" y="20" width="40" height="12" fill="' + SW + '" opacity=".85"/>' +
      handle(98, 84) + handle(102, 84);
  }
  function msSlidingGate(p) {
    var s = "";
    for (var i = 0; i < 8; i++) s += mull(20 + i * 22, 26, 20 + i * 22, 92, 3);
    for (var i = 0; i < 3; i++) s += mull(14, 40 + i * 22, 186, 40 + i * 22, 2);
    return frame(10, 22, 180, 76) + s +
      '<line x1="6" y1="104" x2="194" y2="104" stroke="' + SW + '" stroke-width="2.4"/>' +
      '<circle cx="40" cy="104" r="5" fill="none" stroke="' + SW + '" stroke-width="2.2"/><circle cx="96" cy="104" r="5" fill="none" stroke="' + SW + '" stroke-width="2.2"/><circle cx="152" cy="104" r="5" fill="none" stroke="' + SW + '" stroke-width="2.2"/>' +
      '<rect x="160" y="14" width="26" height="8" fill="' + GOLD + '"/>';
  }
  function msWindowGrill(p) {
    var s = "";
    for (var i = 0; i < 5; i++) s += mull(20 + i * 33, 16, 20 + i * 33, 116, 3.4);
    for (var i = 0; i < 2; i++) s += mull(16, 52 + i * 40, 184, 52 + i * 40, 3);
    return frame(10, 10, 180, 112) + s +
      '<line x1="10" y1="122" x2="190" y2="122" stroke="' + SW + '" stroke-width="2"/>';
  }
  function msSecurityDoor(p) {
    var s = '<rect x="68" y="12" width="64" height="128" fill="#39424f" stroke="' + SWL + '" stroke-width="1.2"/>';
    for (var i = 0; i < 4; i++) s += '<line x1="70" y1="' + (30 + i * 26) + '" x2="130" y2="' + (30 + i * 26) + '" stroke="#8fa3b8" stroke-width="2"/>';
    return frame(62, 6, 76, 148) + s + handle(132, 78) + hinge(64, 28) + hinge(64, 132) +
      '<circle cx="100" cy="150" r="4" fill="' + GOLD + '"/><circle cx="100" cy="10" r="4" fill="' + GOLD + '"/>';
  }
  function msStair(p) {
    var s = '<path d="M 12 142 L 12 114 L 42 114 L 42 86 L 72 86 L 72 58 L 102 58 L 102 30 L 132 30 L 132 14" fill="none" stroke="' + SW + '" stroke-width="3"/>' +
      '<line x1="12" y1="142" x2="132" y2="142" stroke="' + SW + '" stroke-width="2.4"/>';
    for (var i = 0; i < 4; i++) {
      var x = 12 + i * 30, y = 142 - i * 28;
      s += '<line x1="' + x + '" y1="' + y + '" x2="' + (x + 30) + '" y2="' + y + '" stroke="' + SWL + '" stroke-width="2.4"/>';
    }
    return s + '<line x1="12" y1="22" x2="132" y2="22" stroke="' + SW + '" stroke-width="2.6"/>' +
      '<line x1="16" y1="28" x2="16" y2="118" stroke="' + SW + '" stroke-width="2"/><line x1="128" y1="28" x2="128" y2="34" stroke="' + SW + '" stroke-width="2"/>';
  }
  function msPergola(p) {
    var s = '<rect x="20" y="20" width="160" height="10" fill="' + SW + '"/>' +
      '<rect x="20" y="44" width="160" height="8" fill="' + SW + '"/>' +
      '<rect x="20" y="68" width="160" height="8" fill="' + SW + '"/>';
    for (var i = 0; i < 5; i++) s += mull(28 + i * 38, 30, 28 + i * 38, 76, 3);
    return s + '<rect x="26" y="76" width="8" height="62" fill="' + SW + '"/><rect x="166" y="76" width="8" height="62" fill="' + SW + '"/>' +
      '<rect x="96" y="76" width="8" height="62" fill="' + SW + '"/>' +
      '<line x1="14" y1="138" x2="186" y2="138" stroke="' + SW + '" stroke-width="2"/>';
  }
  function msCanopy(p) {
    var s = '<polygon points="16,34 184,34 172,14 28,14" fill="#dfe5ec" stroke="' + SWL + '" stroke-width="1.2"/>';
    for (var i = 0; i < 3; i++) s += mull(40 + i * 46, 14, 40 + i * 46, 34, 2.4);
    return '<polygon points="10,40 190,40 176,8 24,8" fill="none" stroke="' + SW + '" stroke-width="2.4"/>' + s +
      '<rect x="26" y="40" width="9" height="84" fill="' + SW + '"/><rect x="165" y="40" width="9" height="84" fill="' + SW + '"/>' +
      '<line x1="20" y1="40" x2="30" y2="66" stroke="' + SWL + '" stroke-width="2.4"/><line x1="180" y1="40" x2="170" y2="66" stroke="' + SWL + '" stroke-width="2.4"/>' +
      '<line x1="14" y1="128" x2="186" y2="128" stroke="' + SW + '" stroke-width="2.2"/>';
  }
  function msBalconyGrill(p) {
    var s = "";
    for (var i = 0; i < 10; i++) s += mull(18 + i * 18, 30, 18 + i * 18, 104, 3);
    return '<line x1="10" y1="26" x2="190" y2="26" stroke="' + SW + '" stroke-width="3"/>' +
      '<line x1="10" y1="48" x2="190" y2="48" stroke="' + SW + '" stroke-width="2"/>' +
      '<line x1="10" y1="108" x2="190" y2="108" stroke="' + SW + '" stroke-width="2.4"/>' + s +
      '<rect x="10" y="112" width="180" height="10" fill="#dfe5ec" stroke="' + SWL + '" stroke-width="1"/>';
  }
  function msGrille(p) {
    var s = '<rect x="18" y="18" width="164" height="104" fill="#eef1f5" stroke="' + SWL + '" stroke-width="1.2"/>';
    for (var i = -3; i <= 3; i++) {
      s += '<line x1="18" y1="' + (70 + i * 12) + '" x2="182" y2="' + (70 - i * 12) + '" stroke="' + SW + '" stroke-width="2.2"/>';
      s += '<line x1="100" y1="' + (70 + i * 12) + '" x2="100" y2="' + (70 - i * 12) + '" stroke="' + SW + '" stroke-width="2.2"/>';
    }
    return frame(10, 10, 180, 120) + s + '<circle cx="100" cy="70" r="7" fill="none" stroke="' + GOLD + '" stroke-width="2.4"/>';
  }
  function msFence(p) {
    var s = "";
    for (var i = 0; i < 8; i++) s += mull(18 + i * 23, 34, 18 + i * 23, 106, 3);
    return '<line x1="10" y1="30" x2="190" y2="30" stroke="' + SW + '" stroke-width="3"/>' +
      '<line x1="10" y1="110" x2="190" y2="110" stroke="' + SW + '" stroke-width="3"/>' +
      '<line x1="14" y1="70" x2="186" y2="70" stroke="' + SWL + '" stroke-width="2"/>' + s +
      '<rect x="12" y="114" width="176" height="8" fill="#dfe5ec"/>';
  }

  /* ---------- STAINLESS STEEL ---------- */
  function ssRailing(p) {
    var s = "";
    for (var i = 0; i < 7; i++) s += mull(22 + i * 26, 40, 22 + i * 26, 100, 2.6);
    return '<line x1="12" y1="34" x2="188" y2="34" stroke="' + SW + '" stroke-width="3.2"/>' +
      '<line x1="12" y1="52" x2="188" y2="52" stroke="' + SW + '" stroke-width="2"/>' +
      '<line x1="12" y1="106" x2="188" y2="106" stroke="' + SW + '" stroke-width="2.6"/>' + s +
      '<rect x="12" y="110" width="176" height="8" fill="#dfe5ec"/>';
  }
  function ssHandrail(p) {
    return '<line x1="14" y1="30" x2="186" y2="30" stroke="#c0c8d2" stroke-width="4"/>' +
      '<line x1="14" y1="30" x2="186" y2="30" stroke="' + SW + '" stroke-width="1.4"/>' +
      '<rect x="44" y="30" width="8" height="88" fill="' + SW + '"/><rect x="148" y="30" width="8" height="88" fill="' + SW + '"/>' +
      '<rect x="96" y="30" width="8" height="88" fill="' + SW + '"/>' +
      '<line x1="10" y1="122" x2="190" y2="122" stroke="' + SW + '" stroke-width="2.2"/>';
  }
  function ssGate(p) {
    var s = "";
    for (var i = 0; i < 8; i++) s += mull(24 + i * 20, 30, 24 + i * 20, 104, 2.6);
    return '<line x1="12" y1="26" x2="188" y2="26" stroke="' + SW + '" stroke-width="3"/>' +
      '<line x1="12" y1="46" x2="188" y2="46" stroke="' + SW + '" stroke-width="2"/>' +
      '<line x1="12" y1="108" x2="188" y2="108" stroke="' + SW + '" stroke-width="2.6"/>' + s +
      '<circle cx="100" cy="80" r="5" fill="' + GOLD + '"/>' +
      '<rect x="10" y="112" width="180" height="9" fill="#dfe5ec"/>';
  }
  function ssStair(p) {
    var s = '<path d="M 12 140 L 12 112 L 42 112 L 42 84 L 72 84 L 72 56 L 102 56 L 102 28 L 132 28" fill="none" stroke="' + SW + '" stroke-width="3"/>' +
      '<line x1="12" y1="140" x2="132" y2="140" stroke="' + SW + '" stroke-width="2.2"/>';
    for (var i = 0; i < 4; i++) s += '<line x1="' + (12 + i * 30) + '" y1="' + (140 - i * 28) + '" x2="' + (42 + i * 30) + '" y2="' + (140 - i * 28) + '" stroke="' + SWL + '" stroke-width="2.4"/>';
    return s + '<line x1="12" y1="18" x2="132" y2="18" stroke="' + SW + '" stroke-width="3"/>' +
      '<line x1="16" y1="24" x2="16" y2="112" stroke="' + SW + '" stroke-width="2.2"/>' +
      '<rect x="128" y="14" width="7" height="18" fill="' + SW + '"/>';
  }
  function ssPartition(p) {
    var s = glass(22, 18, 60, 100) + sheen(22, 18, 60, 100) + glass(118, 18, 60, 100) + sheen(118, 18, 60, 100);
    return frame(14, 10, 172, 116) + s + mull(82, 10, 82, 126, 5) + mull(118, 10, 118, 126, 5);
  }
  function ssGlassClamp(p) {
    var s = glass(14, 24, 82, 90) + glass(104, 24, 82, 90) + sheen(14, 24, 82, 90) + sheen(104, 24, 82, 90);
    for (var i = 0; i < 4; i++) {
      var x = 18 + i * 56;
      s += '<circle cx="' + x + '" cy="26" r="3" fill="' + GOLD + '" stroke="' + SW + '"/><circle cx="' + x + '" cy="112" r="3" fill="' + GOLD + '" stroke="' + SW + '"/>';
    }
    return '<line x1="10" y1="18" x2="190" y2="18" stroke="' + SW + '" stroke-width="3"/>' + s +
      '<rect x="10" y="118" width="180" height="9" fill="#dfe5ec"/>';
  }
  function ssBalcony(p) {
    var s = glass(14, 36, 172, 72) + sheen(14, 36, 172, 72);
    return '<line x1="10" y1="24" x2="190" y2="24" stroke="' + SW + '" stroke-width="3"/>' +
      '<line x1="10" y1="112" x2="190" y2="112" stroke="' + SW + '" stroke-width="2.6"/>' + s +
      '<circle cx="30" cy="34" r="3.4" fill="' + GOLD + '"/><circle cx="170" cy="34" r="3.4" fill="' + GOLD + '"/>' +
      '<rect x="10" y="116" width="180" height="9" fill="#dfe5ec"/>';
  }
  function ssRack(p) {
    var s = '<rect x="14" y="14" width="6" height="120" fill="' + SW + '"/><rect x="180" y="14" width="6" height="120" fill="' + SW + '"/>';
    for (var i = 0; i < 4; i++) {
      var y = 26 + i * 28;
      s += '<line x1="14" y1="' + y + '" x2="186" y2="' + y + '" stroke="' + SW + '" stroke-width="3"/>';
      s += glass(22, y + 4, 156, 18);
    }
    return s + '<line x1="10" y1="138" x2="190" y2="138" stroke="' + SW + '" stroke-width="2.4"/>';
  }

  /* ---------- RAILINGS & STAIRS ---------- */
  function rlCable(p) {
    var s = "";
    for (var i = 0; i < 4; i++) s += '<line x1="16" y1="' + (36 + i * 18) + '" x2="184" y2="' + (36 + i * 18) + '" stroke="#aeb9c6" stroke-width="1.4"/>';
    return '<line x1="14" y1="28" x2="186" y2="28" stroke="' + SW + '" stroke-width="3"/>' +
      '<line x1="14" y1="112" x2="186" y2="112" stroke="' + SW + '" stroke-width="2.6"/>' + s +
      '<rect x="30" y="28" width="7" height="84" fill="' + SW + '"/><rect x="163" y="28" width="7" height="84" fill="' + SW + '"/>' +
      '<rect x="96" y="28" width="7" height="84" fill="' + SW + '"/>';
  }
  function rlAlu(p) {
    var s = "";
    for (var i = 0; i < 5; i++) s += '<rect x="' + (26 + i * 32) + '" y="36" width="6" height="72" fill="' + SW + '"/>';
    return '<rect x="12" y="30" width="176" height="8" fill="' + SW + '"/>' +
      '<rect x="12" y="48" width="176" height="5" fill="' + SWL + '"/>' +
      '<rect x="12" y="104" width="176" height="7" fill="' + SW + '"/>' + s +
      '<rect x="12" y="112" width="176" height="8" fill="#dfe5ec"/>';
  }
  function rlWoodCombo(p) {
    var s = '<rect x="12" y="26" width="176" height="12" fill="#a97b4e" stroke="' + SW + '" stroke-width="1.6"/>';
    for (var i = 0; i < 5; i++) s += '<rect x="' + (28 + i * 34) + '" y="42" width="6" height="66" fill="' + SW + '"/>';
    return s + '<rect x="12" y="104" width="176" height="7" fill="' + SW + '"/>' +
      '<rect x="12" y="112" width="176" height="8" fill="#dfe5ec"/>' +
      '<line x1="20" y1="38" x2="180" y2="38" stroke="#8a5f37" stroke-width="1.6"/>';
  }
  function rlSpiral(p) {
    var s = '<circle cx="100" cy="80" r="58" fill="none" stroke="' + SW + '" stroke-width="2.4"/>' +
      '<circle cx="100" cy="80" r="14" fill="none" stroke="' + SW + '" stroke-width="3"/>';
    for (var i = 0; i < 8; i++) {
      var a = i * Math.PI / 4;
      s += '<line x1="' + (100 + 14 * Math.cos(a)) + '" y1="' + (80 + 14 * Math.sin(a)) + '" x2="' + (100 + 58 * Math.cos(a)) + '" y2="' + (80 + 58 * Math.sin(a)) + '" stroke="' + SWL + '" stroke-width="1.6"/>';
    }
    return s + '<circle cx="100" cy="80" r="70" fill="none" stroke="' + GOLD + '" stroke-width="1.6" stroke-dasharray="5 4"/>' +
      '<path d="M 30 80 L 14 80 M 186 80 L 170 80" stroke="' + SW + '" stroke-width="2"/>';
  }
  function rlStraight(p) {
    var s = '<path d="M 12 140 L 12 108 L 44 108 L 44 76 L 76 76 L 76 44 L 108 44 L 108 22 L 132 22" fill="none" stroke="' + SW + '" stroke-width="3"/>' +
      '<line x1="12" y1="140" x2="132" y2="140" stroke="' + SW + '" stroke-width="2.2"/>';
    for (var i = 0; i < 4; i++) s += '<line x1="' + (12 + i * 32) + '" y1="' + (140 - i * 32) + '" x2="' + (44 + i * 32) + '" y2="' + (140 - i * 32) + '" stroke="' + SWL + '" stroke-width="2.4"/>';
    return s + '<line x1="12" y1="20" x2="132" y2="20" stroke="' + SW + '" stroke-width="3"/>' +
      '<line x1="16" y1="26" x2="16" y2="108" stroke="' + SW + '" stroke-width="2.2"/>' +
      '<line x1="44" y1="26" x2="44" y2="76" stroke="' + SW + '" stroke-width="2.2"/>';
  }
  function rlRooftop(p) {
    var s = '<rect x="10" y="112" width="180" height="16" fill="#dfe5ec" stroke="' + SWL + '" stroke-width="1.2"/>';
    for (var i = 0; i < 8; i++) s += '<rect x="' + (18 + i * 23) + '" y="38" width="5" height="74" fill="' + SW + '"/>';
    return '<rect x="10" y="32" width="180" height="8" fill="' + SW + '"/>' +
      '<rect x="10" y="48" width="180" height="4" fill="' + SWL + '"/>' +
      '<rect x="10" y="104" width="180" height="6" fill="' + SW + '"/>' + s;
  }
  function rlFrameless(p) {
    var s = glass(16, 30, 168, 80) + sheen(16, 30, 168, 80);
    for (var i = 0; i < 3; i++) {
      var x = 30 + i * 66;
      s += '<circle cx="' + x + '" cy="34" r="3" fill="' + GOLD + '" stroke="' + SW + '"/><circle cx="' + x + '" cy="106" r="3" fill="' + GOLD + '" stroke="' + SW + '"/>';
    }
    return '<line x1="10" y1="22" x2="190" y2="22" stroke="' + SW + '" stroke-width="2.8"/>' + s +
      '<rect x="10" y="114" width="180" height="9" fill="#dfe5ec"/>';
  }
  function rlMinimal(p) {
    var s = glass(20, 34, 160, 74) + sheen(20, 34, 160, 74);
    return '<rect x="10" y="26" width="180" height="6" fill="' + SW + '"/>' + s +
      '<rect x="14" y="110" width="172" height="7" fill="' + SW + '"/>' +
      '<rect x="10" y="118" width="180" height="8" fill="#dfe5ec"/>' +
      '<circle cx="100" cy="52" r="3" fill="' + GOLD + '"/>';
  }

  /* ---------- MODULAR ---------- */
  function mdWardrobe(p) {
    var s = glass(20, 16, 78, 116) + glass(102, 16, 78, 116) + sheen(20, 16, 78, 116) + sheen(102, 16, 78, 116);
    return frame(12, 10, 176, 126) + s + mull(98, 10, 98, 136) +
      handle(30, 66, 1) + handle(168, 86) +
      '<line x1="12" y1="10" x2="188" y2="10" stroke="' + SW + '" stroke-width="3.4"/>' +
      '<line x1="12" y1="136" x2="188" y2="136" stroke="' + SW + '" stroke-width="2.6"/>' +
      '<rect x="64" y="2" width="72" height="8" fill="' + GOLD + '" opacity=".9"/>';
  }
  function mdCabin(p) {
    var s = glass(84, 24, 100, 44) + sheen(84, 24, 100, 44) + glass(84, 72, 100, 62) + sheen(84, 72, 100, 62);
    return '<rect x="12" y="12" width="72" height="122" fill="#e8ecf1" stroke="' + SW + '" stroke-width="2"/>' +
      '<rect x="84" y="12" width="104" height="122" fill="none" stroke="' + SW + '" stroke-width="2"/>' + s +
      mull(84, 24, 84, 134) + mull(184, 24, 184, 134) + mull(84, 68, 184, 68) +
      '<rect x="146" y="40" width="38" height="56" fill="#eef1f5" stroke="' + SWL + '" stroke-width="1.2"/>' + handle(142, 68) +
      '<rect x="24" y="96" width="48" height="5" fill="' + SWL + '"/><rect x="24" y="106" width="48" height="5" fill="' + SWL + '"/><rect x="24" y="116" width="48" height="5" fill="' + SWL + '"/>';
  }
  function mdKitchen(p) {
    var s = '<rect x="12" y="60" width="176" height="62" fill="#e8ecf1" stroke="' + SW + '" stroke-width="2"/>' +
      '<rect x="12" y="122" width="176" height="8" fill="' + SWL + '"/>';
    for (var i = 0; i < 4; i++) {
      var x = 20 + i * 42;
      s += mull(x, 60, x, 122, 2.6);
      if (i % 2 === 0) s += glass(x + 4, 66, 34, 50) + sheen(x + 4, 66, 34, 50);
      s += '<circle cx="' + (x + 8) + '" cy="90" r="2.4" fill="' + GOLD + '"/>';
    }
    return s + '<rect x="12" y="52" width="176" height="8" fill="' + SW + '"/>' +
      '<rect x="40" y="20" width="8" height="32" fill="' + SW + '"/><rect x="152" y="20" width="8" height="32" fill="' + SW + '"/>' +
      '<line x1="12" y1="20" x2="188" y2="20" stroke="' + SW + '" stroke-width="2.2"/>';
  }
  function mdVerandah(p) {
    var s = '<rect x="12" y="96" width="176" height="8" fill="' + SW + '"/>' +
      '<rect x="12" y="60" width="176" height="36" fill="#eef1f5" stroke="' + SWL + '" stroke-width="1.2"/>';
    for (var i = 0; i < 6; i++) s += mull(24 + i * 30, 60, 24 + i * 30, 96, 2.6);
    return '<rect x="8" y="20" width="184" height="10" fill="' + SW + '"/>' +
      '<rect x="8" y="30" width="184" height="26" fill="' + GL + '" stroke="' + SWL + '" stroke-width="1.2"/>' + sheen(12, 32, 176, 22) +
      '<rect x="8" y="56" width="184" height="5" fill="' + SW + '"/>' + s +
      '<rect x="16" y="104" width="8" height="34" fill="' + SW + '"/><rect x="176" y="104" width="8" height="34" fill="' + SW + '"/>' +
      '<line x1="8" y1="140" x2="192" y2="140" stroke="' + SW + '" stroke-width="2.2"/>';
  }
  function mdBalconyEnclose(p) {
    var s = glass(16, 30, 82, 96) + glass(102, 30, 82, 96) + sheen(16, 30, 82, 96) + sheen(102, 30, 82, 96);
    return '<rect x="10" y="22" width="180" height="8" fill="' + SW + '"/>' + s +
      mull(98, 22, 98, 126) + handle(38, 80, 1) + handle(120, 80, 1) +
      '<rect x="10" y="128" width="180" height="10" fill="#dfe5ec" stroke="' + SWL + '" stroke-width="1"/>' +
      '<rect x="10" y="138" width="180" height="8" fill="' + SW + '"/>';
  }
  function mdLouverPergola(p) {
    var s = '<rect x="18" y="16" width="164" height="8" fill="' + SW + '"/>' +
      '<rect x="18" y="44" width="164" height="8" fill="' + SW + '"/>' +
      '<rect x="18" y="72" width="164" height="8" fill="' + SW + '"/>';
    for (var i = 0; i < 4; i++) {
      var x = 34 + i * 38;
      s += '<path d="M ' + x + ' 24 L ' + (x + 30) + ' 28 L ' + (x + 26) + ' 52 L ' + (x - 4) + ' 48 Z" fill="' + GL + '" stroke="' + SWL + '" stroke-width="1.2"/>';
      s += '<path d="M ' + x + ' 52 L ' + (x + 30) + ' 56 L ' + (x + 26) + ' 80 L ' + (x - 4) + ' 76 Z" fill="' + GL + '" stroke="' + SWL + '" stroke-width="1.2"/>';
    }
    return s + '<rect x="26" y="80" width="8" height="58" fill="' + SW + '"/><rect x="166" y="80" width="8" height="58" fill="' + SW + '"/>' +
      '<rect x="96" y="80" width="8" height="58" fill="' + SW + '"/>' +
      '<line x1="14" y1="140" x2="186" y2="140" stroke="' + SW + '" stroke-width="2"/>';
  }
  function mdGazebo(p) {
    var s = '<polygon points="100,14 172,54 28,54" fill="#dfe5ec" stroke="' + SWL + '" stroke-width="1.2"/>' +
      '<line x1="100" y1="14" x2="100" y2="54" stroke="' + SWL + '" stroke-width="1.6"/>' +
      '<line x1="100" y1="14" x2="64" y2="54" stroke="' + SWL + '" stroke-width="1.6"/>' +
      '<line x1="100" y1="14" x2="136" y2="54" stroke="' + SWL + '" stroke-width="1.6"/>' +
      '<polygon points="24,54 176,54 168,60 32,60" fill="' + SW + '" opacity=".85"/>';
    for (var i = 0; i < 6; i++) s += mull(36 + i * 26, 60, 36 + i * 26, 104, 2.6);
    return s + '<rect x="28" y="60" width="7" height="64" fill="' + SW + '"/><rect x="165" y="60" width="7" height="64" fill="' + SW + '"/>' +
      '<rect x="96" y="60" width="7" height="64" fill="' + SW + '"/>' +
      '<line x1="16" y1="128" x2="184" y2="128" stroke="' + SW + '" stroke-width="2.4"/>' +
      '<rect x="84" y="76" width="32" height="26" fill="none" stroke="' + SWL + '" stroke-width="1.6"/>';
  }
  function mdCarport(p) {
    var s = '<rect x="16" y="24" width="168" height="10" fill="' + SW + '"/>' +
      '<rect x="16" y="24" width="168" height="5" fill="' + SWL + '"/>' +
      '<rect x="34" y="34" width="6" height="66" fill="' + SW + '"/><rect x="160" y="34" width="6" height="66" fill="' + SW + '"/>' +
      '<line x1="16" y1="34" x2="184" y2="34" stroke="' + SW + '" stroke-width="2"/>';
    var car = '<path d="M 66 116 L 72 100 L 128 100 L 134 116 L 148 116 L 148 122 L 52 122 L 52 116 Z" fill="#39424f"/>' +
      '<circle cx="70" cy="122" r="7" fill="none" stroke="' + SW + '" stroke-width="2.4"/><circle cx="130" cy="122" r="7" fill="none" stroke="' + SW + '" stroke-width="2.4"/>';
    return s + car + '<line x1="14" y1="134" x2="186" y2="134" stroke="' + SW + '" stroke-width="2.2"/>';
  }
  function mdMosquito(p) {
    var s = glass(16, 16, 168, 96);
    for (var i = 0; i < 8; i++) s += '<line x1="16" y1="' + (22 + i * 13) + '" x2="184" y2="' + (22 + i * 13) + '" stroke="#aeb9c6" stroke-width="1"/>';
    for (var i = 0; i < 8; i++) s += '<line x1="' + (22 + i * 21) + '" y1="16" x2="' + (22 + i * 21) + '" y2="112" stroke="#aeb9c6" stroke-width="1"/>';
    return frame(10, 10, 180, 112) + s + '<line x1="10" y1="122" x2="190" y2="122" stroke="' + SW + '" stroke-width="2"/>' +
      handle(60, 66, 1) + '<rect x="168" y="24" width="14" height="20" fill="' + GOLD + '" opacity=".9"/>';
  }
  function mdShutter(p) {
    var s = '<circle cx="100" cy="22" r="12" fill="#e8ecf1" stroke="' + SW + '" stroke-width="2.2"/>';
    for (var i = 0; i < 7; i++) {
      var y = 34 + i * 15;
      s += '<path d="M 24 ' + y + ' L 176 ' + y + ' L 176 ' + (y + 9) + ' L 24 ' + (y + 9) + ' Z" fill="#dfe5ec" stroke="' + SWL + '" stroke-width="1.2"/>';
    }
    return '<rect x="14" y="16" width="172" height="124" fill="none" stroke="' + SW + '" stroke-width="2.4"/>' + s +
      '<line x1="14" y1="22" x2="186" y2="22" stroke="' + SWL + '" stroke-width="1.4"/>';
  }

  return {
    winSliding: winSliding, winCasement: winCasement, winTiltTurn: winTiltTurn, winTopHung: winTopHung,
    winAwning: winAwning, winBay: winBay, winArch: winArch, winCorner: winCorner, winFixed: winFixed,
    winProjected: winProjected, winCombo: winCombo, winGarden: winGarden, winLouver: winLouver,
    doorSingle: doorSingle, doorDouble: doorDouble, doorFrench: doorFrench, doorSliding: doorSliding,
    doorFolding: doorFolding, doorBalcony: doorBalcony, doorPivot: doorPivot, doorArch: doorArch,
    doorGrill: doorGrill, doorSlim: doorSlim, doorBiFold: doorBiFold,
    partGrid: partGrid, partFrameless: partFrameless, partCubicle: partCubicle, partSliding: partSliding,
    partHalf: partHalf, partBlind: partBlind, partCurve: partCurve, partOfficeWall: partOfficeWall,
    glassStairRail: glassStairRail, glassBalcony: glassBalcony, glassShower: glassShower,
    glassShopfront: glassShopfront, glassDoorSingle: glassDoorSingle, glassMirror: glassMirror,
    glassFloor: glassFloor, glassSkylight: glassSkylight, glassCanopy: glassCanopy, glassDoorTough: glassDoorTough,
    sfShopfront: sfShopfront, sfCurtainwall: sfCurtainwall, sfACP: sfACP, sfStructural: sfStructural,
    sfFinwall: sfFinwall, sfLobby: sfLobby, sfCanopy: sfCanopy, sfColumn: sfColumn,
    msDoubleGate: msDoubleGate, msSlidingGate: msSlidingGate, msWindowGrill: msWindowGrill,
    msSecurityDoor: msSecurityDoor, msStair: msStair, msPergola: msPergola, msCanopy: msCanopy,
    msBalconyGrill: msBalconyGrill, msGrille: msGrille, msFence: msFence,
    ssRailing: ssRailing, ssHandrail: ssHandrail, ssGate: ssGate, ssStair: ssStair, ssPartition: ssPartition,
    ssGlassClamp: ssGlassClamp, ssBalcony: ssBalcony, ssRack: ssRack,
    rlCable: rlCable, rlAlu: rlAlu, rlWoodCombo: rlWoodCombo, rlSpiral: rlSpiral, rlStraight: rlStraight,
    rlRooftop: rlRooftop, rlFrameless: rlFrameless, rlMinimal: rlMinimal,
    mdWardrobe: mdWardrobe, mdCabin: mdCabin, mdKitchen: mdKitchen, mdVerandah: mdVerandah,
    mdBalconyEnclose: mdBalconyEnclose, mdLouverPergola: mdLouverPergola, mdGazebo: mdGazebo,
    mdCarport: mdCarport, mdMosquito: mdMosquito, mdShutter: mdShutter
  };
})();
