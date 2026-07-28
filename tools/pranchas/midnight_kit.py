#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kit de pranchas conceituais no design system Midnight Grid
(gui-brain/design-systems/midnight-grid/DESIGN.md), adaptado para os
episódios da série vibe coding do canal ia-aplicada.

Fixa o que NÃO pode variar:
  - fundo preto #000000 com grade de engenharia sutil (células de 60px, ~3% branco);
  - tinta branca, secundário #A0A0A0, muted #666666, hairline #2A2A2A;
  - UM acento amarelo #FFBE00 por prancha (além do kicker), com glow suave
    (opacidade máxima do glow: 0.11 — acima disso vira neblina);
  - escala verde/âmbar/vermelho SOMENTE para níveis ordenados;
  - Inter em tudo (sem serifa, sem segunda família);
  - labels caps com tracking 0.12em ficam ~40% mais largos: conferir colisões;
  - rodapé sempre presente, texto puro, canto inferior esquerdo;
  - sem moldura, sem risco sobre o rodapé.

A METÁFORA de cada prancha é bespoke (ver gerar_epNN.py).

PNG: preferimos rsvg-convert (brew install librsvg); o cairosvg fica como
fallback, mas quebra as ligaduras fi/fl do itálico nas legendas.

Uso:
    python3 gerar_ep01.py   (a partir de tools/pranchas/)
"""

import os
import shutil
import subprocess
from xml.sax.saxutils import escape

try:
    import cairosvg
except ImportError:
    cairosvg = None

# rsvg-convert (librsvg/Pango/HarfBuzz) resolve as ligaduras fi/fl do itálico,
# que o cairosvg quebra ("f ica", "conf lito"); por isso é o rasterizador
# preferido quando presente no sistema.
RSVG = shutil.which("rsvg-convert")

# ---- Midnight Grid (fixo) ----
BG = "#000000"
SURFACE = "#0D0D0D"
ELEVATED = "#1A1A1A"
INK = "#FFFFFF"
SECONDARY = "#A0A0A0"
MUTED = "#666666"
BORDER = "#2A2A2A"
ACCENT = "#FFBE00"          # amarelo-sinal: um acento por prancha
ST_OPEN = "#34D399"         # verde   } escala de níveis ordenados,
ST_GUIDED = "#FBBF24"       # âmbar   } nunca decorativa
ST_RESTRICTED = "#F87171"   # vermelho}
FONT = "Inter, DejaVu Sans, sans-serif"
FOOTER = "guifav.github.io   ·   guilhermefavaron.com.br   ·   youtube: ia-aplicada"
GRID_CELL = 60

W, H = 1920, 1080


def grid(width=W, height=H, cell=GRID_CELL, opacity=0.03):
    """Grade de engenharia sutil (~3% branco)."""
    out = []
    for x in range(0, width + 1, cell):
        out.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{height}" '
                   f'stroke="{INK}" stroke-opacity="{opacity}" stroke-width="1"/>')
    for y in range(0, height + 1, cell):
        out.append(f'<line x1="0" y1="{y}" x2="{width}" y2="{y}" '
                   f'stroke="{INK}" stroke-opacity="{opacity}" stroke-width="1"/>')
    return "".join(out)


def canvas(body_svg, defs="", width=W, height=H):
    """Fundo preto + grade + rodapé obrigatório. Sem moldura."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">'
        f'<defs>{defs}</defs>'
        f'<rect width="{width}" height="{height}" fill="{BG}"/>'
        f'{grid(width, height)}'
        f'{body_svg}'
        f'<text x="110" y="{height-42}" font-family="{FONT}" font-size="21" '
        f'fill="{MUTED}">{escape(FOOTER)}</text>'
        f'</svg>'
    )


def export(body_svg, path, defs="", width=W, height=H):
    svg = canvas(body_svg, defs, width, height)
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    base = os.path.splitext(path)[0]
    with open(base + ".svg", "w", encoding="utf-8") as f:
        f.write(svg)
    if RSVG:
        subprocess.run([RSVG, "-w", str(width), "-h", str(height),
                        "-o", base + ".png"],
                       input=svg.encode("utf-8"), check=True)
        print(f"[ok] {base}.png  (rsvg)")
        return
    if cairosvg is None:
        print(f"[svg] {base}.svg  (rsvg-convert e cairosvg ausentes: PNG não gerado)")
        return
    cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=base + ".png",
                     output_width=width, output_height=height)
    print(f"[ok] {base}.png  (cairosvg: ligaduras do itálico podem quebrar)")


# ---- Primitivas ----
def txt(x, y, s, size=24, fill=INK, anchor="start", weight="400",
        italic=False, spacing=None, opacity=1.0):
    style = ' font-style="italic"' if italic else ""
    sp = f' letter-spacing="{spacing}"' if spacing is not None else ""
    op = f' fill-opacity="{opacity}"' if opacity < 1.0 else ""
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"'
            f'{style}{sp}{op}>{escape(s)}</text>')


def caps(x, y, s, size=22, fill=SECONDARY, anchor="start", weight="600"):
    """label-caps: caixa alta, tracking largo (0.12em). Fica ~40% mais largo."""
    return txt(x, y, s.upper(), size, fill, anchor, weight,
               spacing=round(size * 0.12, 1))


def header(kicker, fig, width=W):
    """Kicker amarelo (topo-esquerdo) + fig. NN (topo-direito). Sem régua."""
    return (caps(110, 112, kicker, 24, ACCENT) +
            caps(width - 110, 112, fig, 24, MUTED, anchor="end"))


def title(cx, y, s, size=54):
    """Título da prancha, display pesado centralizado."""
    return txt(cx, y, s, size, INK, anchor="middle", weight="800",
               spacing=round(-0.025 * size, 1))


def caption(cx, y, s, size=37):
    """Frase de fecho em Inter itálico, centralizada."""
    return txt(cx, y, s, size, INK, anchor="middle", weight="400", italic=True)


def glow_def(gid, color=ACCENT, op=0.11):
    """Gradiente radial para glow suave (atmosférico, nunca neon). op <= 0.11."""
    return (f'<radialGradient id="{gid}"><stop offset="0%" stop-color="{color}" '
            f'stop-opacity="{op}"/><stop offset="70%" stop-color="{color}" '
            f'stop-opacity="{op*0.4:.3f}"/><stop offset="100%" stop-color="{color}" '
            f'stop-opacity="0"/></radialGradient>')


def glow(cx, cy, r, gid):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{gid})"/>'


def line(x1, y1, x2, y2, stroke=INK, w=2, dash=None, opacity=1.0):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    op = f' stroke-opacity="{opacity}"' if opacity < 1.0 else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="{w}"{d}{op}/>')


def rrect(x, y, w, h, r=16, fill="none", stroke=BORDER, sw=2, opacity=1.0):
    op = f' opacity="{opacity}"' if opacity < 1.0 else ""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{op}/>')


def circle(cx, cy, r, fill="none", stroke=INK, sw=2, opacity=1.0):
    op = f' opacity="{opacity}"' if opacity < 1.0 else ""
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"{op}/>')


def path(d, stroke=INK, w=2, fill="none", dash=None, opacity=1.0):
    dd = f' stroke-dasharray="{dash}"' if dash else ""
    op = f' opacity="{opacity}"' if opacity < 1.0 else ""
    return (f'<path d="{d}" fill="{fill}" stroke="{stroke}" '
            f'stroke-width="{w}"{dd}{op}/>')


def arrow(x1, y1, x2, y2, stroke=INK, w=2.5, label=None, label_fill=None,
          label_size=22, dash=None, opacity=1.0):
    """Seta reta horizontal/vertical/diagonal com ponta triangular e rótulo opcional."""
    import math
    ang = math.atan2(y2 - y1, x2 - x1)
    ah = 14  # tamanho da ponta
    p1 = (x2 - ah * math.cos(ang - 0.45), y2 - ah * math.sin(ang - 0.45))
    p2 = (x2 - ah * math.cos(ang + 0.45), y2 - ah * math.sin(ang + 0.45))
    out = line(x1, y1, x2, y2, stroke, w, dash, opacity)
    out += (f'<path d="M{x2} {y2} L{p1[0]:.1f} {p1[1]:.1f} L{p2[0]:.1f} {p2[1]:.1f} Z" '
            f'fill="{stroke}"' + (f' opacity="{opacity}"' if opacity < 1.0 else "") + '/>')
    if label:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        out += caps(mx, my - 14, label, label_size, label_fill or SECONDARY,
                    anchor="middle")
    return out


def card(x, y, w, h, label=None, label_fill=SECONDARY, elevated=False, r=16):
    """Card do sistema: superfície quase-preta com hairline. Rótulo caps opcional."""
    fill = ELEVATED if elevated else SURFACE
    out = rrect(x, y, w, h, r, fill=fill, stroke=BORDER, sw=2)
    if label:
        out += caps(x + w / 2, y + 44, label, 20, label_fill, anchor="middle")
    return out


def chip(cx, cy, s, color=SECONDARY, size=18):
    """Chip pill com texto caps colorido sobre elevated (badge do sistema)."""
    wpx = len(s) * size * 0.62 * 1.4 + 44   # tracking 0.12em ~ +40%
    out = rrect(cx - wpx / 2, cy - size * 1.1, wpx, size * 2.2, 9999,
                fill=ELEVATED, stroke=BORDER, sw=1.5)
    out += caps(cx, cy + size * 0.36, s, size, color, anchor="middle")
    return out


def dim_bracket_v(x, y, h, label, color=ACCENT, size=22):
    """Colchete vertical de dimensão com rótulo rotacionado."""
    b = path(f"M{x} {y} h-20 V{y+h} h20", stroke=color, w=2.5)
    t = (f'<text x="{x-46}" y="{y+h/2}" font-family="{FONT}" font-size="{size}" '
         f'font-weight="600" fill="{color}" text-anchor="middle" '
         f'letter-spacing="{round(size*0.08,1)}" '
         f'transform="rotate(-90 {x-46} {y+h/2})">{escape(label.upper())}</text>')
    return b + t


def xmark(cx, cy, r=22, color=ST_RESTRICTED, w=4):
    return (line(cx - r, cy - r, cx + r, cy + r, color, w) +
            line(cx - r, cy + r, cx + r, cy - r, color, w))


def check(cx, cy, r=22, color=ST_OPEN, w=4):
    return path(f"M{cx-r} {cy} L{cx-r*0.2} {cy+r*0.7} L{cx+r} {cy-r*0.6}",
                stroke=color, w=w)
