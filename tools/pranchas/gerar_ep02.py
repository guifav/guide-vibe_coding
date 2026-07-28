#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pranchas do episódio 02 - Front-end e Estado.
Uma prancha por passagem visual do roteiro (seções "Mostrar").
Design system: Midnight Grid (ver midnight_kit.py).
"""

from midnight_kit import (W, H, INK, SECONDARY, MUTED, BORDER, ACCENT,
                          SURFACE, ELEVATED, ST_OPEN, ST_GUIDED, ST_RESTRICTED,
                          export, header, title, caption, txt, caps, line,
                          rrect, circle, path, glow, glow_def, arrow, card,
                          chip, xmark, check, dim_bracket_v)

OUT = "../../episodes/02-front-end-e-estado/pranchas"
KICKER = "EP 02 · Front-end e estado"
N = 13


def fig(n):
    return f"prancha {n:02d}/{N}"


# ---------------------------------------------------------------- 01
def p01_entrando_na_camada():
    """Abertura: o mapa do ep01 com a camada do navegador destacada."""
    b = header(KICKER, fig(1))
    b += title(W / 2, 230, "Hoje a gente entra na primeira camada")
    camadas = ["navegador", "servidor", "banco de dados", "deploy"]
    wc, hc, gap = 380, 180, 60
    x0, y0 = 110, 500
    b += glow(x0 + wc / 2, y0 + hc / 2, 320, "g1")
    for i, s in enumerate(camadas):
        x = x0 + i * (wc + gap)
        if i == 0:
            b += rrect(x, y0, wc, hc, 16, fill=SURFACE, stroke=ACCENT, sw=2.5)
            b += caps(x + wc / 2, y0 + hc / 2 + 8, s, 24, ACCENT,
                      anchor="middle")
        else:
            b += rrect(x, y0, wc, hc, 16, fill=SURFACE, stroke=BORDER, sw=2)
            b += caps(x + wc / 2, y0 + hc / 2 + 8, s, 24, SECONDARY,
                      anchor="middle")
        if i < 3:
            b += line(x + wc + 10, y0 + hc / 2, x + wc + gap - 10,
                      y0 + hc / 2, MUTED, 2)
    b += caps(x0 + wc / 2, y0 - 90, "hoje: aqui dentro", 22, ACCENT,
              anchor="middle")
    b += arrow(x0 + wc / 2, y0 - 70, x0 + wc / 2, y0 - 14, ACCENT, 2.5)
    b += txt(W / 2, 800, "A camada que você toca primeiro. Onde a IA mais escreve código.",
             28, SECONDARY, anchor="middle")
    b += caption(W / 2, 950,
                 "Se você não enxerga o mecanismo, aceita o resultado sem saber o risco.")
    export(b, f"{OUT}/01-entrando-no-navegador", defs=glow_def("g1"))


# ---------------------------------------------------------------- 02
def p02_arquivos_de_texto():
    """ATO 1, cena 1: o pedido sai, os arquivos chegam."""
    b = header(KICKER, fig(2))
    b += title(W / 2, 230, "O servidor responde com arquivos de texto")
    y0, hc, wc = 350, 280, 420
    b += card(180, y0, wc, hc, "navegador")
    b += txt(180 + wc / 2, y0 + 175, "digita, aperta enter", 26, SECONDARY,
             anchor="middle")
    b += card(1320, y0, wc, hc, "servidor")
    b += txt(1320 + wc / 2, y0 + 175, "devolve os arquivos", 26, SECONDARY,
             anchor="middle")
    b += arrow(620, y0 + 100, 1300, y0 + 100, INK, 3, "pedido")
    b += arrow(1300, y0 + 200, 620, y0 + 200, ACCENT, 3,
               "resposta · três arquivos", ACCENT)
    # os três arquivos, em baixo
    b += glow(W / 2, 790, 300, "g1")
    arquivos = [("HTML", "o que aparece"), ("CSS", "como aparece"),
                ("JS", "o que acontece")]
    wa, ha, gapa = 380, 130, 70
    xa0 = (W - 3 * wa - 2 * gapa) / 2
    ya = 720
    for i, (nome, papel) in enumerate(arquivos):
        x = xa0 + i * (wa + gapa)
        b += rrect(x, ya, wa, ha, 12, fill=SURFACE, stroke=BORDER, sw=2)
        b += txt(x + wa / 2, ya + 56, nome, 32, INK, anchor="middle",
                 weight="800")
        b += txt(x + wa / 2, ya + 98, papel, 23, SECONDARY, anchor="middle")
    b += caption(W / 2, 950, "Texto puro. O navegador lê e monta tudo daí.")
    export(b, f"{OUT}/02-arquivos-de-texto", defs=glow_def("g1"))


# ---------------------------------------------------------------- 03
def p03_dom_arvore():
    """ATO 1, cena 2: o DOM como árvore de elementos."""
    b = header(KICKER, fig(3))
    b += title(W / 2, 230, "DOM: a árvore que o navegador monta")
    nw, nh = 180, 64

    def node(cx, cy, s, accent=False):
        stroke = ACCENT if accent else BORDER
        fill_t = ACCENT if accent else INK
        return (rrect(cx - nw / 2, cy - nh / 2, nw, nh, 12, fill=SURFACE,
                      stroke=stroke, sw=2.5 if accent else 2) +
                txt(cx, cy + 9, s, 26, fill_t, anchor="middle", weight="600"))

    b += glow(840, 740, 220, "g1")
    # ligações (antes dos nós)
    b += line(960, 402, 960, 458, MUTED, 2)
    b += line(960, 522, 700, 583, MUTED, 2)
    b += line(960, 522, 1220, 583, MUTED, 2)
    b += line(700, 647, 560, 708, MUTED, 2)
    b += line(700, 647, 840, 708, MUTED, 2)
    # nós
    b += node(960, 370, "<html>")
    b += node(960, 490, "<body>")
    b += node(700, 615, "<div>")
    b += node(1220, 615, "<img>")
    b += node(560, 740, "<p>")
    b += node(840, 740, "<button>", accent=True)
    # anotações laterais
    b += caps(1090, 378, "o tronco", 20, SECONDARY)
    b += caps(1520, 748, "cada elemento", 20, SECONDARY)
    b += caps(1520, 782, "é um nó", 20, SECONDARY)
    b += txt(W / 2, 880, "Renderizar: o navegador pinta os pixels na tela a partir dessa árvore.",
             28, SECONDARY, anchor="middle")
    b += caption(W / 2, 950, "O JavaScript não escreve na tela. Ele mexe no DOM.")
    export(b, f"{OUT}/03-dom-arvore", defs=glow_def("g1"))


# ---------------------------------------------------------------- 04
def p04_estrutura_aparencia_comportamento():
    """ATO 1, cena 3: a divisão de três, com a tradução do que a IA fala."""
    b = header(KICKER, fig(4))
    b += title(W / 2, 230, "Estrutura, aparência, comportamento")
    cols = [("HTML", "estrutura", "o que existe na página",
             "“adicionar um botão”"),
            ("CSS", "aparência", "cor, tamanho, posição",
             "“mudar o estilo”"),
            ("JS", "comportamento", "clicou, digitou, arrastou",
             "“quando clicar, faz isso”")]
    wc, hc, gap = 480, 400, 80
    x0 = (W - 3 * wc - 2 * gap) / 2
    y0 = 330
    b += glow(x0 + 2 * (wc + gap) + wc / 2, y0 + hc / 2, 300, "g1")
    for i, (nome, papel, ex, ia) in enumerate(cols):
        x = x0 + i * (wc + gap)
        b += card(x, y0, wc, hc)
        b += txt(x + wc / 2, y0 + 110, nome, 56, ACCENT if i == 2 else INK,
                 anchor="middle", weight="800", spacing=-1.4)
        b += caps(x + wc / 2, y0 + 170, papel, 22, SECONDARY, anchor="middle")
        b += txt(x + wc / 2, y0 + 240, ex, 25, SECONDARY, anchor="middle")
        b += line(x + 70, y0 + 290, x + wc - 70, y0 + 290, BORDER, 1.5)
        b += txt(x + wc / 2, y0 + 345, ia, 24, INK, anchor="middle",
                 weight="600")
    b += txt(W / 2, 830, "Quando a IA fala assim, é nessa camada que ela mexe.",
             28, SECONDARY, anchor="middle")
    b += caption(W / 2, 950, "Três camadas diferentes dentro do mesmo navegador.")
    export(b, f"{OUT}/04-estrutura-aparencia-comportamento", defs=glow_def("g1"))


# ---------------------------------------------------------------- 05
def p05_pagina_viva():
    """ATO 1, cena 4: o DOM é vivo — a página muda sem recarregar."""
    b = header(KICKER, fig(5))
    b += title(W / 2, 230, "A página muda sem recarregar")
    y0, wp, hp = 400, 560, 360

    def page(x):
        out = rrect(x, y0, wp, hp, 16, fill=SURFACE, stroke=BORDER, sw=2)
        out += line(x, y0 + 56, x + wp, y0 + 56, BORDER, 1.5)
        for i in range(3):
            out += circle(x + 34 + i * 26, y0 + 28, 6, fill=ELEVATED,
                          stroke=BORDER, sw=1.5)
        return out

    # antes
    b += page(200)
    b += rrect(260, y0 + 104, 28, 28, 6, fill="none", stroke=SECONDARY, sw=2)
    b += txt(310, y0 + 126, "mostrar detalhes", 26, SECONDARY)
    b += rrect(260, y0 + 180, 440, 120, 12, fill="none", stroke=BORDER,
               sw=2, opacity=0.7)
    b += caps(480, y0 + 248, "nada aqui", 18, MUTED, anchor="middle")
    # depois
    b += glow(1440, y0 + hp / 2, 300, "g1")
    b += page(1160)
    b += rrect(1220, y0 + 104, 28, 28, 6, fill=ELEVATED, stroke=SECONDARY, sw=2)
    b += check(1234, y0 + 118, 9, INK, 3)
    b += txt(1270, y0 + 126, "mostrar detalhes", 26, INK, weight="600")
    b += rrect(1220, y0 + 180, 440, 120, 12, fill=SURFACE, stroke=ACCENT,
               sw=2.5)
    b += txt(1440, y0 + 248, "bloco novo na tela", 25, ACCENT, anchor="middle",
             weight="600")
    b += arrow(780, y0 + hp / 2, 1140, y0 + hp / 2, INK, 3, "clique")
    b += txt(W / 2, 860, "O JavaScript mudou o DOM por baixo. O navegador repintou só essa parte.",
             28, SECONDARY, anchor="middle")
    b += caption(W / 2, 950, "A página muda porque tem memória. Essa memória tem nome: estado.")
    export(b, f"{OUT}/05-pagina-viva", defs=glow_def("g1"))


# ---------------------------------------------------------------- 06
def p06_estado_contador():
    """ATO 2, cena 1: o que é estado — o contador."""
    b = header(KICKER, fig(6))
    b += title(W / 2, 230, "Estado: a memória da página")
    wc, hc = 400, 300
    y0 = 400
    xs = [160, 760, 1360]
    nums = ["0", "1", "2"]
    b += glow(xs[2] + wc / 2, y0 + hc / 2, 280, "g1")
    for i, x in enumerate(xs):
        b += card(x, y0, wc, hc)
        b += txt(x + wc / 2, y0 + 150, nums[i], 90,
                 ACCENT if i == 2 else INK, anchor="middle", weight="800")
        b += rrect(x + wc / 2 - 70, y0 + 190, 140, 56, 9999, fill=ELEVATED,
                   stroke=BORDER, sw=1.5)
        b += txt(x + wc / 2, y0 + 226, "+1", 26, INK, anchor="middle",
                 weight="600")
        if i < 2:
            b += arrow(x + wc + 20, y0 + hc / 2, x + wc + 180, y0 + hc / 2,
                       SECONDARY, 2.5, "clique")
    b += txt(W / 2, 830, "Recarregou? Volta para zero. Esse número vive enquanto a página está aberta.",
             28, SECONDARY, anchor="middle")
    b += caption(W / 2, 950, "Uma página morta só mostra. Uma página viva lembra e reage.")
    export(b, f"{OUT}/06-estado-contador", defs=glow_def("g1"))


# ---------------------------------------------------------------- 07
def p07_onde_o_estado_mora():
    """ATO 2, cena 2: as quatro categorias de estado."""
    b = header(KICKER, fig(7))
    b += title(W / 2, 230, "Onde o estado mora")
    cats = [("variável local", "contador",
             ("some quando", "a página fecha")),
            ("hook", "lista aberta",
             ("vive enquanto o", "componente existe")),
            ("store", "usuário logado",
             ("compartilhado entre", "as partes da tela")),
            ("servidor", "perfil salvo",
             ("sobrevive", "entre sessões"))]
    wc, hc, gap = 380, 330, 53
    x0, y0 = 120, 380
    b += glow(x0 + 3 * (wc + gap) + wc / 2, y0 + hc / 2, 280, "g1")
    for i, (nome, ex, vida) in enumerate(cats):
        x = x0 + i * (wc + gap)
        b += card(x, y0, wc, hc)
        b += caps(x + wc / 2, y0 + 56, nome, 20,
                  ACCENT if i == 3 else SECONDARY, anchor="middle")
        b += txt(x + wc / 2, y0 + 145, ex, 30, INK, anchor="middle",
                 weight="700")
        b += txt(x + wc / 2, y0 + 220, vida[0], 22, SECONDARY, anchor="middle")
        b += txt(x + wc / 2, y0 + 254, vida[1], 22, SECONDARY, anchor="middle")
        if i == 3:
            b += caps(x + wc / 2, y0 + 302, "próximo episódio", 15, MUTED,
                      anchor="middle")
    b += arrow(140, 800, 1780, 800, SECONDARY, 2.5, "sobrevive por mais tempo")
    b += caption(W / 2, 950,
                 "Quanto mais partes precisam do valor, mais longe da tela ele mora.")
    export(b, f"{OUT}/07-onde-o-estado-mora", defs=glow_def("g1"))


# ---------------------------------------------------------------- 08
def p08_ciclo():
    """ATO 2, cena 3: o coração do vídeo — evento, estado, re-render."""
    b = header(KICKER, fig(8))
    b += title(W / 2, 230, "O ciclo: evento, estado, re-render")
    passos = [("evento", ("você interage;", "o navegador avisa")),
              ("estado", ("o valor muda na", "variável, hook ou store")),
              ("re-render", ("o DOM atualiza; a tela", "repinta o que mudou"))]
    wc, hc, gap = 440, 240, 90
    x0, y0 = 120, 420
    b += glow(x0 + wc + gap + wc / 2, y0 + hc / 2, 280, "g1")
    for i, (nome, linhas) in enumerate(passos):
        x = x0 + i * (wc + gap)
        b += card(x, y0, wc, hc)
        b += caps(x + wc / 2, y0 + 62, nome, 24,
                  ACCENT if i == 1 else SECONDARY, anchor="middle")
        b += txt(x + wc / 2, y0 + 132, linhas[0], 26, INK, anchor="middle")
        b += txt(x + wc / 2, y0 + 170, linhas[1], 26, INK, anchor="middle")
        if i < 2:
            b += arrow(x + wc + 8, y0 + hc / 2, x + wc + gap - 8,
                       y0 + hc / 2, INK, 3)
    # laço de retorno
    cxa, cxc = x0 + wc / 2, x0 + 2 * (wc + gap) + wc / 2
    b += line(cxc, y0 + hc, cxc, 760, MUTED, 2)
    b += line(cxc, 760, cxa, 760, MUTED, 2)
    b += arrow(cxa, 760, cxa, y0 + hc + 8, MUTED, 2)
    b += caps(W / 2, 800, "próxima interação: o ciclo repete", 20, SECONDARY,
              anchor="middle")
    b += txt(W / 2, 870, "Quem liga o estado ao DOM é o código, seu ou do framework. O navegador só repinta.",
             27, SECONDARY, anchor="middle")
    b += caption(W / 2, 950, "Reatividade é isso: a tela se atualiza sozinha quando o estado muda.")
    export(b, f"{OUT}/08-ciclo-evento-estado-rerender", defs=glow_def("g1"))


# ---------------------------------------------------------------- 09
def p09_pergunta_em_tres_partes():
    """ATO 2, cena 4: a pergunta que isola o problema."""
    b = header(KICKER, fig(9))
    b += title(W / 2, 230, "Quando quebra, pergunte em três partes")
    linhas = [("O evento está disparando?",
               "se não, o clique não está chegando ao código"),
              ("O estado está mudando?",
               "se não, o problema é a lógica que trata o evento"),
              ("A tela está re-renderizando?",
               "se não, o problema é a ligação entre estado e tela")]
    xr, wr, hr = 380, 1160, 130
    ys = [360, 525, 690]
    b += glow(W / 2, 585, 340, "g1")
    b += line(460, ys[0] + hr / 2, 460, ys[2] + hr / 2, ACCENT, 3)
    for i, (q, hint) in enumerate(linhas):
        y = ys[i]
        b += card(xr, y, wr, hr)
        b += circle(460, y + hr / 2, 30, fill=ELEVATED, stroke=BORDER, sw=2)
        b += txt(460, y + hr / 2 + 10, str(i + 1), 28, INK, anchor="middle",
                 weight="700")
        b += txt(540, y + 60, q, 32, INK, weight="600")
        b += txt(540, y + 100, hint, 21, SECONDARY)
    b += txt(W / 2, 880, "Cole as três perguntas na conversa com a IA: a resposta isola o problema.",
             28, SECONDARY, anchor="middle")
    b += caption(W / 2, 950, "Três perguntas, três suspeitos. Um deles é o culpado.")
    export(b, f"{OUT}/09-pergunta-em-tres-partes", defs=glow_def("g1"))


# ---------------------------------------------------------------- 10
def p10_cinco_estados():
    """ATO 3: os cinco estados que a IA esquece."""
    b = header(KICKER, fig(10))
    b += title(W / 2, 230, "Os cinco estados que a IA esquece")
    estados = [("loading", "ainda não chegou", ("mostre que está", "esperando")),
               ("empty", "veio vazio", ("não é loading:", "o dado chegou")),
               ("error", "não vai chegar", ("sem tratar: spinner", "girando para sempre")),
               ("partial", "veio pela metade", ("3 itens de 10;", "campo faltando")),
               ("stale", "envelheceu", ("o servidor mudou;", "a tela não"))]
    wc, hc, gap = 300, 300, 40
    x0, y0 = 130, 380
    b += glow(x0 + 4 * (wc + gap) + wc / 2, y0 + hc / 2, 240, "g1")
    for i, (nome, gist, nota) in enumerate(estados):
        x = x0 + i * (wc + gap)
        b += card(x, y0, wc, hc)
        b += caps(x + wc / 2, y0 + 56, nome, 22,
                  ACCENT if i == 4 else SECONDARY, anchor="middle")
        b += txt(x + wc / 2, y0 + 145, gist, 26, INK, anchor="middle",
                 weight="700")
        b += txt(x + wc / 2, y0 + 210, nota[0], 20, SECONDARY, anchor="middle")
        b += txt(x + wc / 2, y0 + 243, nota[1], 20, SECONDARY, anchor="middle")
    b += txt(W / 2, 830, "A IA entrega o caminho feliz: dado chegou, lista cheia. O resto é com você.",
             28, SECONDARY, anchor="middle")
    b += caption(W / 2, 950, "Toda tela que mostra dados tem cinco momentos, não um.")
    export(b, f"{OUT}/10-cinco-estados", defs=glow_def("g1"))


# ---------------------------------------------------------------- 11
def p11_checklist():
    """ATO 3, cena 5: a checklist para usar com IA."""
    b = header(KICKER, fig(11))
    b += title(W / 2, 230, "A checklist antes de aceitar a tela")
    itens = ["Tratei o loading?", "Tratei o empty?", "Tratei o error?",
             "Tratei o partial?", "Tratei o stale?"]
    y0, step = 400, 88
    b += glow(W / 2, 575, 340, "g1")
    b += dim_bracket_v(540, y0 - 40, 4 * step + 60, "antes de aceitar")
    for i, s in enumerate(itens):
        y = y0 + i * step
        b += check(630, y - 10, 16, ST_OPEN, 4)
        b += txt(690, y, s, 34, INK, weight="600")
    b += txt(W / 2, 880, "Se a resposta for não, peça: trate também loading, empty, error, partial e stale.",
             28, SECONDARY, anchor="middle")
    b += caption(W / 2, 950, "A diferença entre demo e produto é tratar o que dá errado.")
    export(b, f"{OUT}/11-checklist", defs=glow_def("g1"))


# ---------------------------------------------------------------- 12
def p12_estado_que_viaja():
    """ATO 3, cena 6: o estado que precisa ir para o servidor."""
    b = header(KICKER, fig(12))
    b += title(W / 2, 230, "Nem todo estado pode morar no navegador")
    y0, wc, hc = 380, 560, 380
    b += card(200, y0, wc, hc, "navegador")
    for j, s in enumerate(("o contador", "a aba aberta", "o filtro escolhido")):
        b += txt(200 + wc / 2, y0 + 130 + j * 46, s, 26, SECONDARY,
                 anchor="middle")
    b += caps(200 + wc / 2, y0 + 320, "pode sumir", 20, MUTED, anchor="middle")
    b += glow(1160 + wc / 2, y0 + hc / 2, 320, "g1")
    b += card(1160, y0, wc, hc, "servidor", label_fill=ACCENT)
    for j, s in enumerate(("seu perfil", "seu histórico", "suas preferências")):
        b += txt(1160 + wc / 2, y0 + 130 + j * 46, s, 26, INK,
                 anchor="middle", weight="600")
    b += caps(1160 + wc / 2, y0 + 320, "não pode sumir", 20, SECONDARY,
              anchor="middle")
    b += arrow(780, y0 + hc / 2, 1140, y0 + hc / 2, INK, 3, "o estado viaja")
    b += caption(W / 2, 950,
                 "O estado que sobrevive entre sessões mora no servidor. Próximo episódio.")
    export(b, f"{OUT}/12-estado-que-viaja", defs=glow_def("g1"))


# ---------------------------------------------------------------- 13
def p13_ciclo_e_os_cinco_estados():
    """Fechamento do ATO 3: o ciclo no centro, os cinco estados em volta."""
    b = header(KICKER, fig(13))
    b += title(W / 2, 230, "O ciclo no centro, os estados em volta")

    # ciclo compacto (evento -> estado -> re-render, com volta)
    wc, hc, gap = 380, 150, 110
    x0 = (W - 3 * wc - 2 * gap) / 2
    y0 = 470
    b += glow(W / 2, y0 + hc / 2, 340, "g1")
    nomes = [("evento", SECONDARY), ("estado", ACCENT), ("re-render", SECONDARY)]
    for i, (nome, cor) in enumerate(nomes):
        x = x0 + i * (wc + gap)
        b += card(x, y0, wc, hc)
        b += caps(x + wc / 2, y0 + hc / 2 + 8, nome, 24, cor, anchor="middle")
        if i < 2:
            b += arrow(x + wc + 12, y0 + hc / 2, x + wc + gap - 12,
                       y0 + hc / 2, INK, 2.5)
    # volta do ciclo
    xa, xb = x0 + wc / 2, x0 + 2 * (wc + gap) + wc / 2
    b += path(f"M{xb} {y0 + hc} V {y0 + hc + 80} H {xa} V {y0 + hc + 14}",
              stroke=BORDER, w=2)
    b += arrow(xa, y0 + hc + 40, xa, y0 + hc + 12, SECONDARY, 2)
    b += caps(W / 2, y0 + hc + 72, "a cada interação, o ciclo repete", 18,
              MUTED, anchor="middle")

    # os cinco estados em volta (acima do ciclo)
    estados = ["loading", "empty", "error", "partial", "stale"]
    for i, nome in enumerate(estados):
        b += chip(360 + i * 300, 372, nome, SECONDARY, 19)

    b += txt(W / 2, 830,
             "O ciclo desenha a tela. Os cinco estados decidem o que ela mostra.",
             28, SECONDARY, anchor="middle")
    b += caption(W / 2, 950,
                 "O ciclo é simples. Os cinco estados são o que a IA esquece.")
    export(b, f"{OUT}/13-ciclo-e-os-cinco-estados", defs=glow_def("g1"))


if __name__ == "__main__":
    p01_entrando_na_camada()
    p02_arquivos_de_texto()
    p03_dom_arvore()
    p04_estrutura_aparencia_comportamento()
    p05_pagina_viva()
    p06_estado_contador()
    p07_onde_o_estado_mora()
    p08_ciclo()
    p09_pergunta_em_tres_partes()
    p10_cinco_estados()
    p11_checklist()
    p12_estado_que_viaja()
    p13_ciclo_e_os_cinco_estados()
