"""Ghép các slide trong src/ thành một file index.html trình chiếu được và xuất lời dẫn.

Chạy từ root repo:  python presentation/gate2a/build_html.py
Chỉ dùng thư viện chuẩn của Python.
"""
import html
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / 'src'

deck = json.loads((SRC / 'deck.json').read_text(encoding='utf-8'))
css = (SRC / 'deck.css').read_text(encoding='utf-8')
fonts = ''.join(f'<link rel="stylesheet" href="{f["href"]}">\n'
                for f in deck['faces'].values() if 'href' in f)

sections, notes = [], []
for i, sid in enumerate(deck['order'], start=1):
    text = (SRC / 'slides' / f'{sid}.html').read_text(encoding='utf-8').strip()
    sections.append(text)
    aside = re.search(r'<aside>(.*?)</aside>', text, re.S)
    title = (re.search(r'<h[12][^>]*>(.*?)</h[12]>', text, re.S)
             or re.search(r'<p class="eyebrow">(.*?)</p>', text, re.S))
    notes.append((i, sid, html.unescape(re.sub('<[^>]+>', '', title.group(1))) if title else sid,
                  html.unescape(aside.group(1).strip()) if aside else ''))

VIEWER = """
html, body { margin:0; height:100%; background:#0B1222; overflow:hidden; }
#stage { position:absolute; left:50%; top:50%; width:1920px; height:1080px;
         transform-origin:center center; }
#stage > section { position:absolute; inset:0; width:1920px; height:1080px; display:none; }
#stage > section.active { display:flex; }
#stage aside { display:none; }
#stage table { border-collapse:collapse; }
#stage th, #stage td { padding:.4em .6em; vertical-align:top;
                       border-bottom:1px solid rgba(128,128,128,.35); }
body.static .in { animation:none !important; }
#hud { position:fixed; right:16px; bottom:12px; font:14px Inter, Arial, sans-serif;
       color:#BCC6D8; opacity:.8; }
#notes { position:fixed; left:0; right:0; bottom:0; max-height:30%; overflow:auto; display:none;
         background:rgba(11,18,34,.95); color:#F6F4EE; font:18px/1.5 Inter, Arial, sans-serif;
         padding:16px 24px; }
body.show-notes #notes { display:block; }
@media print {
  html, body { overflow:visible; height:auto; background:none; }
  #hud, #notes { display:none !important; }
  #stage { position:static; transform:none !important; }
  #stage > section { position:relative; display:flex !important; page-break-after:always; }
  .in { animation:none !important; }
  @page { size:1920px 1080px; margin:0; }
}
"""

SCRIPT = """
const slides = [...document.querySelectorAll('#stage > section')];
const stage = document.getElementById('stage');
const hud = document.getElementById('hud');
const notes = document.getElementById('notes');
let cur = Math.max(0, Math.min(slides.length - 1, (parseInt(location.hash.slice(1)) || 1) - 1));
function fit() {
  const s = Math.min(innerWidth / 1920, innerHeight / 1080);
  stage.style.transform = `translate(-50%, -50%) scale(${s})`;
}
function show(i) {
  cur = Math.max(0, Math.min(slides.length - 1, i));
  slides.forEach((el, k) => el.classList.toggle('active', k === cur));
  hud.textContent = `${cur + 1} / ${slides.length} · ← → chuyển slide · N lời dẫn · F toàn màn hình`;
  const a = slides[cur].querySelector('aside');
  notes.textContent = a ? a.textContent : '';
  history.replaceState(null, '', '#' + (cur + 1));
}
if (location.search.includes('static')) document.body.classList.add('static');
addEventListener('resize', fit);
addEventListener('keydown', e => {
  if (['ArrowRight', 'PageDown', ' ', 'Enter'].includes(e.key)) show(cur + 1);
  else if (['ArrowLeft', 'PageUp', 'Backspace'].includes(e.key)) show(cur - 1);
  else if (e.key === 'Home') show(0);
  else if (e.key === 'End') show(slides.length - 1);
  else if (e.key === 'n' || e.key === 'N') document.body.classList.toggle('show-notes');
  else if (e.key === 'f' || e.key === 'F') document.documentElement.requestFullscreen?.();
});
addEventListener('click', e => show(cur + (e.clientX > innerWidth / 2 ? 1 : -1)));
fit(); show(cur);
"""

page = f"""<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(deck['title'])}</title>
{fonts}<style>
{css}
{VIEWER}
</style>
</head>
<body>
<div id="stage">
{chr(10).join(sections)}
</div>
<div id="hud"></div>
<div id="notes"></div>
<script>{SCRIPT}</script>
</body>
</html>
"""
(HERE / 'index.html').write_text(page, encoding='utf-8')

lines = [f'# Lời dẫn · {deck["title"]}', '',
         'Xuất tự động từ phần ghi chú (`<aside>`) của từng slide bằng `build_html.py`.', '']
for i, sid, title, note in notes:
    lines += [f'## {i:02d} · {title}', '', note or '(không có ghi chú)', '']
(HERE / 'loi_dan.md').write_text('\n'.join(lines), encoding='utf-8')

print(f'Đã ghi index.html ({len(sections)} slide) và loi_dan.md')
