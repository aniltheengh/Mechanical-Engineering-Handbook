// Optional equation-syntax check with a real TeX renderer.
// npm install --prefix .tools --no-package-lock --ignore-scripts katex@0.19.1
// node scripts/check_math.cjs
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const katexRoot = process.env.HANDBOOK_KATEX_DIR || path.join(root, '.tools');
const katex = require(path.join(katexRoot, 'node_modules/katex/dist/katex.js'));
const files = fs.readdirSync(path.join(root, 'chapters')).filter(n => /^\d\d-.*\.md$/.test(n)).map(n => 'chapters/' + n);
files.push('CAPSTONE.md', 'VISUAL_GUIDE.md');
let count = 0, display = 0;
const errors = [];
function render(tex, mode, file) {
  try {
    katex.renderToString(tex, { displayMode: mode, throwOnError: true, strict: 'error', trust: false, output: 'htmlAndMathml' });
    count++;
    if (mode) display++;
  } catch (e) { errors.push(`${file}: ${tex.slice(0, 140)}\n${e.message}`); }
}
for (const file of files) {
  let text = fs.readFileSync(path.join(root, file), 'utf8').replace(/```[\s\S]*?```/g, '');
  text = text.replace(/\$\$([\s\S]+?)\$\$/g, (_, tex) => { render(tex, true, file); return ''; });
  text.replace(/(?<!\\)\$([^$\n]+?)(?<!\\)\$/g, (_, tex) => { render(tex, false, file); return ''; });
}
if (errors.length) { console.error(errors.join('\n\n')); process.exit(1); }
console.log(`PASS: ${count} TeX expressions (${display} display blocks) parsed and rendered to HTML/MathML with KaTeX ${katex.version}; ${files.length} source documents.`);
