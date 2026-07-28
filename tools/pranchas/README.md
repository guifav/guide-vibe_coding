# Pranchas — Midnight Grid

Kit e geradores das pranchas (SVG + PNG, 1920×1080) usadas na tela durante os vídeos.

Design system: [Midnight Grid](https://github.com/guifav/gui-brain/blob/main/design-systems/midnight-grid/DESIGN.md) (gui-brain).

## Uso

```bash
pip install cairosvg
cd tools/pranchas
python3 gerar_ep01.py   # regenera episodes/01-.../pranchas/
```

Requer a fonte Inter instalada no sistema (letter-spacing e itálico dependem dela).

## Conteúdo

| Arquivo | Papel |
|---|---|
| `midnight_kit.py` | Tokens, canvas, primitivas (card, seta, glow, caps…) |
| `gerar_epNN.py` | Metáforas bespoke de cada episódio |

Saída: `episodes/NN-.../pranchas/NN-slug.{svg,png}`.

## Regras fixas do kit

- Fundo preto + grade de engenharia (~3% branco)
- Um acento amarelo `#FFBE00` por prancha + no máximo um glow (opacidade ≤ 0.11)
- Escala verde/âmbar/vermelho só para níveis ordenados ou certo/errado
- Inter em tudo; rodapé obrigatório; sem moldura
