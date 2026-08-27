const fs = require('fs');
const path = require('path');

const tplPath = path.join(__dirname, 'templates.js');
const tplContent = fs.readFileSync(tplPath, 'utf8');

// Evaluate TEMPLATES
const m = tplContent.match(/var TEMPLATES = \(function \(\) \{([\s\S]*?)\}\)\(\);/);
if (!m) {
  process.exit(1);
}

const TEMPLATES = eval('(function () {\n' + m[1] + '\n})()');

function renderTemplate(key, params) {
  if (!TEMPLATES[key]) return '';
  try {
    return TEMPLATES[key](params || {});
  } catch (e) {
    return '';
  }
}

// Read products_data or products_list
const prodListPath = path.join(__dirname, 'products_list.json');
if (fs.existsSync(prodListPath)) {
  const prods = JSON.parse(fs.readFileSync(prodListPath, 'utf8'));
  const out = {};
  for (const pr of prods) {
    out[pr.code] = renderTemplate(pr.art_key, pr.art_params);
  }
  fs.writeFileSync(path.join(__dirname, 'svg_art_map.json'), JSON.stringify(out, null, 2), 'utf8');
  console.log(`Rendered ${Object.keys(out).length} SVGs to svg_art_map.json`);
}
