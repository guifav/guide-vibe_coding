#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Consolida as pranchas PNG de cada episódio em um PDF de apresentação
(1 página = 1 prancha, ordem numérica).

Uso:
    cd tools/pranchas
    python3 gerar_pdfs.py          # todos os episódios
    python3 gerar_pdfs.py 01 08    # só os episódios pedidos

Saída: episodes/NN-slug/apresentacao.pdf
"""

from __future__ import annotations

import sys
from pathlib import Path

import img2pdf

ROOT = Path(__file__).resolve().parents[2]
EPISODES = ROOT / "episodes"


def episode_dirs(wanted: list[str] | None = None) -> list[Path]:
    dirs = sorted(p for p in EPISODES.iterdir() if p.is_dir() and (p / "pranchas").is_dir())
    if not wanted:
        return dirs
    out = []
    for d in dirs:
        for w in wanted:
            if d.name.startswith(w.zfill(2) if w.isdigit() else w):
                out.append(d)
                break
    return out


def pngs_in_order(pranchas: Path) -> list[Path]:
    files = sorted(pranchas.glob("*.png"))
    # só as numeradas NN-slug.png (ignora lixo)
    return [p for p in files if len(p.name) >= 3 and p.name[:2].isdigit()]


def build_pdf(ep_dir: Path) -> Path:
    pngs = pngs_in_order(ep_dir / "pranchas")
    if not pngs:
        raise SystemExit(f"sem PNGs em {ep_dir / 'pranchas'}")
    out = ep_dir / "apresentacao.pdf"
    # página no tamanho nativo da prancha (1920×1080) — ideal para fullscreen
    with open(out, "wb") as f:
        f.write(img2pdf.convert([str(p) for p in pngs]))
    return out


def main(argv: list[str]) -> None:
    wanted = argv[1:] or None
    dirs = episode_dirs(wanted)
    if not dirs:
        raise SystemExit("nenhum episódio encontrado")
    for d in dirs:
        out = build_pdf(d)
        n = len(pngs_in_order(d / "pranchas"))
        kb = out.stat().st_size // 1024
        print(f"[ok] {out.relative_to(ROOT)}  ({n} páginas, {kb} KB)")


if __name__ == "__main__":
    main(sys.argv)
