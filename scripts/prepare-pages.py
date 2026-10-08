from pathlib import Path
import re
import sys

folder = Path(sys.argv[1])
base = sys.argv[2].rstrip('/')
if base and not re.fullmatch(r'/[A-Za-z0-9_./-]+', base):
    raise SystemExit('Percorso Pages non valido')
page = folder / '404.html'
text = page.read_text(encoding='utf-8')
for relative in ('styles.css', 'index.html'):
    text = text.replace(f'href="{relative}"', f'href="{base}/{relative}"')
page.write_text(text, encoding='utf-8')
print('Pagina 404 pronta per il percorso GitHub Pages.')
