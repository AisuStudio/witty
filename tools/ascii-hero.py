#!/usr/bin/env python3
"""witty ASCII-Hero-Generator.

Erzeugt das Hero-Porträt (Wittgenstein 1929, gemeinfrei) aus den Buchstaben
w/y/t/i/! — Helligkeit -> Dichte, POSITIV gemappt (hell im Foto = dichte
Letter), weil die Seite Vanilla-Zeichen auf Blueberry rendert.

Quelle: https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Ludwig_Wittgenstein_1929.jpg/960px-Ludwig_Wittgenstein_1929.jpg
Nutzung: python3 tools/ascii-hero.py wittgenstein.jpg > art.txt
Danach den Inhalt in index.html in <pre class="hero-ascii"> einsetzen.
124x42 Zeichen = 16:9 bei 0.6em Zeichenbreite / 1.0 line-height.
"""
import sys
from PIL import Image, ImageOps

COLS, ROWS = 124, 42
RAMP = ['w', 'y', 't', 'i', '!', ' ']  # dicht -> leer

im = Image.open(sys.argv[1]).convert('L')
W, H = im.size
# Enger Gesichts-Crop (Braue bis unter die Lippen), 16:9
cy, ch = int(0.265 * H), int(0.235 * H)
cw = int(ch * 16 / 9)
cx = int(0.505 * W)
face = ImageOps.autocontrast(im.crop((cx - cw//2, cy - ch//2, cx + cw//2, cy + ch//2)), cutoff=1)
px = face.resize((COLS, ROWS)).load()
for r in range(ROWS):
    print(''.join(RAMP[min(5, (255 - px[c, r]) * 6 // 256)] for c in range(COLS)))
