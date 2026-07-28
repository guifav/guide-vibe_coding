#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pranchas do episódio 01 - Deploy do Zero ao Ar.
Uma prancha por passagem visual do roteiro (seções "Mostrar").
Design system: Midnight Grid (ver midnight_kit.py).
"""

from midnight_kit import (W, H, INK, SECONDARY, MUTED, BORDER, ACCENT,
                          SURFACE, ELEVATED, ST_OPEN, ST_GUIDED, ST_RESTRICTED,
                          export, header, title, caption, txt, caps, line,
                          rrect, circle, path, glow, glow_def, arrow, card,
                          chip, xmark, check, dim_bracket_v)

OUT = "../../episodes/01-deploy-do-zero-ao-ar/pranchas"
KICKER = "EP 01 · Deploy do zero ao ar"
N = 13


def fig(n):
    return f"prancha {n:02d}/{N}"


# ---------------------------------------------------------------- 01
def p01_duas_jornadas():
    """Abertura: as duas jornadas, publicação e uso."""
    b = header(KICKER, fig(1))
    b += title(W / 2, 230, "Duas jornadas entre o código e você")
    b += glow(480, 560, 330, "g1")

    # Jornada 1: publicação (esquerda -> direita, em cima)
    b += caps(110, 400, "Fluxo de publicação", 24, ACCENT)
    steps1 = ["código", "git", "build", "deploy", "no ar"]
    x0, y1, wc, gap = 110, 450, 280, 62
    for i, s in enumerate(steps1):
        x = x0 + i * (wc + gap)
        b += card(x, y1, wc, 110, s)
        if i < len(steps1) - 1:
            b += arrow(x + wc + 8, y1 + 55, x + wc + gap - 8, y1 + 55,
                       SECONDARY, 2.5)

    # Jornada 2: uso (em baixo)
    b += caps(110, 700, "Fluxo de uso", 24, SECONDARY)
    steps2 = ["navegador", "domínio", "servidor", "api · banco", "resposta"]
    y2 = 750
    for i, s in enumerate(steps2):
        x = x0 + i * (wc + gap)
        b += card(x, y2, wc, 110, s)
        if i < len(steps2) - 1:
            b += arrow(x + wc + 8, y2 + 55, x + wc + gap - 8, y2 + 55,
                       SECONDARY, 2.5)

    b += caption(W / 2, 975, "Você publica uma vez. O mundo usa a cada clique.")
    export(b, f"{OUT}/01-duas-jornadas", defs=glow_def("g1"))


# ---------------------------------------------------------------- 02
def p02_html_css_js():
    """ATO 1: os três arquivos que o navegador entende."""
    b = header(KICKER, fig(2))
    b += title(W / 2, 230, "Três arquivos, três trabalhos")
    cols = [("HTML", "o que aparece", "texto, botão, imagem"),
            ("CSS", "como aparece", "cor, tamanho, posição"),
            ("JS", "o que acontece", "clicou, mudou, calculou")]
    wc, hc, gap = 480, 380, 80
    x0 = (W - 3 * wc - 2 * gap) / 2
    y0 = 340
    b += glow(x0 + wc / 2, y0 + hc / 2, 300, "g1")
    for i, (nome, papel, ex) in enumerate(cols):
        x = x0 + i * (wc + gap)
        b += card(x, y0, wc, hc)
        b += txt(x + wc / 2, y0 + 150, nome, 64, ACCENT if i == 0 else INK,
                 anchor="middle", weight="800", spacing=-1.6)
        b += txt(x + wc / 2, y0 + 230, papel, 30, INK, anchor="middle",
                 weight="600")
        b += txt(x + wc / 2, y0 + 290, ex, 24, SECONDARY, anchor="middle")
    b += caption(W / 2, 880, "O navegador lê os três e monta a página.")
    export(b, f"{OUT}/02-html-css-js", defs=glow_def("g1"))


# ---------------------------------------------------------------- 03
def p03_git_fotos():
    """ATO 1: git como fotos no tempo; commit, branch, merge."""
    b = header(KICKER, fig(3))
    b += title(W / 2, 230, "Git: fotos do código no tempo")
    yM, xA, xB = 560, 240, 1680
    b += glow(1180, yM, 260, "g1")
    # linha principal
    b += line(xA, yM, xB, yM, INK, 3)
    for i, x in enumerate(range(360, 1681, 220)):
        b += circle(x, yM, 16, fill=SURFACE, stroke=INK, sw=3)
    b += caps(xA, yM + 70, "main · a linha principal", 20, SECONDARY)
    # branch paralela
    bx0, bx1 = 580, 1240
    b += path(f"M{bx0} {yM} C {bx0+90} {yM-150}, {bx0+90} {yM-150}, {bx0+180} {yM-150} "
              f"L {bx1-180} {yM-150} C {bx1-90} {yM-150}, {bx1-90} {yM-150}, {bx1} {yM}",
              stroke=ACCENT, w=3)
    for x in (bx0 + 240, bx0 + 440):
        b += circle(x, yM - 150, 14, fill=SURFACE, stroke=ACCENT, sw=3)
    b += caps(bx0 + 340, yM - 200, "branch · linha paralela", 20, ACCENT,
              anchor="middle")
    b += caps(bx1 + 30, yM - 60, "merge", 20, SECONDARY)
    # legenda
    b += circle(660, 810, 14, fill=SURFACE, stroke=INK, sw=3)
    b += txt(700, 820, "commit: a foto do código em um momento", 26, SECONDARY)
    b += caption(W / 2, 950, "Quebrou? Volta para a foto anterior.")
    export(b, f"{OUT}/03-git-fotos-no-tempo", defs=glow_def("g1"))


# ---------------------------------------------------------------- 04
def p04_servidor():
    """ATO 2: por que o computador de casa não serve o site."""
    b = header(KICKER, fig(4))
    b += title(W / 2, 230, "Seu computador não é um servidor")
    y0, hc = 380, 420
    # casa (esquerda)
    b += card(200, y0, 600, hc, "computador de casa")
    itens = [("desliga", 150), ("troca de IP", 230), ("atrás do roteador", 310)]
    for s, dy in itens:
        b += xmark(300, y0 + dy - 8, 14, ST_RESTRICTED, 3.5)
        b += txt(340, y0 + dy, s, 27, SECONDARY)
    # servidor (direita)
    b += glow(1420, y0 + hc / 2, 320, "g1")
    b += card(1120, y0, 600, hc, "servidor", label_fill=ACCENT)
    itens2 = [("ligado 24 horas", 150), ("endereço estável", 230),
              ("responde a muitos pedidos", 310)]
    for s, dy in itens2:
        b += check(1220, y0 + dy - 8, 14, ST_OPEN, 3.5)
        b += txt(1260, y0 + dy, s, 27, SECONDARY)
    b += arrow(830, y0 + hc / 2, 1090, y0 + hc / 2, INK, 3, "o código viaja")
    b += caption(W / 2, 950, "Servidor é outro computador, feito para nunca dormir.")
    export(b, f"{OUT}/04-servidor", defs=glow_def("g1"))


# ---------------------------------------------------------------- 05
def p05_request_response():
    """ATO 2: o pedido e a resposta."""
    b = header(KICKER, fig(5))
    b += title(W / 2, 230, "Toda a web é uma conversa")
    y0, hc, wc = 420, 340, 480
    b += card(180, y0, wc, hc, "navegador")
    b += glow(1500, y0 + hc / 2, 300, "g1")
    b += card(1260, y0, wc, hc, "servidor", label_fill=ACCENT)
    b += txt(180 + wc / 2, y0 + 200, "pede", 40, INK, anchor="middle", weight="700")
    b += txt(1260 + wc / 2, y0 + 200, "responde", 40, INK, anchor="middle",
             weight="700")
    b += arrow(700, y0 + 110, 1220, y0 + 110, INK, 3, "request · o pedido")
    b += arrow(1220, y0 + 250, 700, y0 + 250, SECONDARY, 3,
               "response · a resposta")
    b += caption(W / 2, 950, "Pedido vai, resposta volta. Sempre.")
    export(b, f"{OUT}/05-request-response", defs=glow_def("g1"))


# ---------------------------------------------------------------- 06
def p06_api_balcao():
    """ATO 2: API como balcão de atendimento."""
    b = header(KICKER, fig(6))
    b += title(W / 2, 230, "API: o balcão do servidor")
    y0 = 400
    b += card(180, y0, 420, 320, "navegador")
    b += txt(390, y0 + 175, "“quero a lista", 26, SECONDARY, anchor="middle")
    b += txt(390, y0 + 213, "de produtos”", 26, SECONDARY, anchor="middle")
    # balcão: card elevated na frente do servidor
    b += glow(1050, y0 + 160, 280, "g1")
    b += card(870, y0 - 40, 360, 400, None, elevated=True)
    b += caps(1050, y0 + 10, "API", 26, ACCENT, anchor="middle")
    b += txt(1050, y0 + 180, "o contrato:", 24, SECONDARY, anchor="middle")
    b += txt(1050, y0 + 220, "que pedido aceito,", 24, SECONDARY, anchor="middle")
    b += txt(1050, y0 + 256, "que resposta devolvo", 24, SECONDARY, anchor="middle")
    b += card(1330, y0, 420, 320, "servidor")
    b += txt(1540, y0 + 175, "executa, busca,", 26, SECONDARY, anchor="middle")
    b += txt(1540, y0 + 213, "devolve", 26, SECONDARY, anchor="middle")
    b += arrow(620, y0 + 110, 850, y0 + 110, INK, 3, "request")
    b += arrow(850, y0 + 250, 620, y0 + 250, SECONDARY, 3, "response · JSON")
    b += caption(W / 2, 950, "JSON é só texto organizado com chaves e listas.")
    export(b, f"{OUT}/06-api-balcao", defs=glow_def("g1"))


# ---------------------------------------------------------------- 07
def p07_banco():
    """ATO 2: banco de dados, a memória de longo prazo."""
    b = header(KICKER, fig(7))
    b += title(W / 2, 230, "Banco: a memória que não some")
    y0 = 400
    b += card(240, y0, 480, 320, "servidor")
    b += txt(480, y0 + 175, "processa pedidos,", 26, SECONDARY, anchor="middle")
    b += txt(480, y0 + 213, "esquece depois", 26, SECONDARY, anchor="middle")
    b += glow(1440, y0 + 160, 300, "g1")
    # banco como cilindro
    cx, cy = 1440, y0 + 160
    b += path(f"M{cx-190} {cy-120} a 190 46 0 0 0 380 0 l 0 240 "
              f"a 190 46 0 0 1 -380 0 Z", stroke=BORDER, w=2, fill=SURFACE)
    b += path(f"M{cx-190} {cy-120} a 190 46 0 0 0 380 0", stroke=ACCENT, w=2.5)
    b += caps(cx, cy + 20, "banco de dados", 22, ACCENT, anchor="middle")
    b += txt(cx, cy + 70, "usuários · produtos · pedidos", 24, SECONDARY,
             anchor="middle")
    b += arrow(740, y0 + 110, 1200, y0 + 110, INK, 3, "consulta")
    b += arrow(1200, y0 + 250, 740, y0 + 250, SECONDARY, 3, "dado")
    b += caption(W / 2, 950,
                 "Tudo que precisa sobreviver entre um request e outro mora aqui.")
    export(b, f"{OUT}/07-banco-de-dados", defs=glow_def("g1"))


# ---------------------------------------------------------------- 08
def p08_auth():
    """ATO 2: autenticação vs autorização."""
    b = header(KICKER, fig(8))
    b += title(W / 2, 230, "Auth são duas perguntas, não uma")
    wc, hc, gap = 720, 400, 120
    x0 = (W - 2 * wc - gap) / 2
    y0 = 360
    b += glow(x0 + wc / 2, y0 + hc / 2, 320, "g1")
    b += card(x0, y0, wc, hc)
    b += caps(x0 + wc / 2, y0 + 70, "autenticação", 24, ACCENT, anchor="middle")
    b += txt(x0 + wc / 2, y0 + 180, "Quem é você?", 44, INK, anchor="middle",
             weight="800")
    b += txt(x0 + wc / 2, y0 + 260, "login · senha · token (o crachá)", 26,
             SECONDARY, anchor="middle")
    x1 = x0 + wc + gap
    b += card(x1, y0, wc, hc)
    b += caps(x1 + wc / 2, y0 + 70, "autorização", 24, SECONDARY, anchor="middle")
    b += txt(x1 + wc / 2, y0 + 180, "O que você pode?", 44, INK, anchor="middle",
             weight="800")
    b += txt(x1 + wc / 2, y0 + 260, "ver · editar · apagar · administrar", 26,
             SECONDARY, anchor="middle")
    b += arrow(x0 + wc + 14, y0 + hc / 2, x1 - 14, y0 + hc / 2, INK, 3)
    b += caption(W / 2, 950,
                 "Se a IA propõe remover auth: perigo. Pergunte o que deixa de ser verificado.")
    export(b, f"{OUT}/08-auth", defs=glow_def("g1"))


# ---------------------------------------------------------------- 09
def p09_build():
    """ATO 3: build, a cozinha do restaurante."""
    b = header(KICKER, fig(9))
    b += title(W / 2, 230, "Build: a cozinha entre o cru e o servido")
    y0 = 420
    # ingredientes (vários arquivos)
    for i, dy in enumerate((0, 40, 80)):
        b += rrect(240 + i * 14, y0 + dy - i * 6, 300, 200, 12, fill=SURFACE,
                   stroke=BORDER, sw=2)
    b += caps(400, y0 + 260, "seu código · cru", 20, SECONDARY, anchor="middle")
    # build no centro
    b += glow(960, y0 + 100, 280, "g1")
    b += card(800, y0 - 40, 320, 280, None, elevated=True)
    b += caps(960, y0 + 20, "build", 26, ACCENT, anchor="middle")
    b += txt(960, y0 + 90, "otimiza", 24, SECONDARY, anchor="middle")
    b += txt(960, y0 + 128, "junta arquivos", 24, SECONDARY, anchor="middle")
    b += txt(960, y0 + 166, "remove o que sobra", 24, SECONDARY, anchor="middle")
    # prato pronto
    b += rrect(1380, y0, 300, 200, 12, fill=SURFACE, stroke=ACCENT, sw=2.5)
    b += caps(1530, y0 + 260, "versão final · servível", 20, SECONDARY,
              anchor="middle")
    b += arrow(560, y0 + 100, 780, y0 + 100, INK, 3)
    b += arrow(1140, y0 + 100, 1360, y0 + 100, INK, 3)
    b += caption(W / 2, 950, "Nem todo projeto precisa. Com framework, quase sempre.")
    export(b, f"{OUT}/09-build", defs=glow_def("g1"))


# ---------------------------------------------------------------- 10
def p10_cicd():
    """ATO 3: CI/CD, o cano com portões verde/vermelho."""
    b = header(KICKER, fig(10))
    b += title(W / 2, 230, "CI/CD: o portão automático")
    steps = [("commit", None), ("lint", ST_OPEN), ("testes", ST_OPEN),
             ("build", ST_RESTRICTED), ("deploy", None)]
    wc, gap = 290, 60
    x0 = (W - 5 * wc - 4 * gap) / 2
    y0 = 430
    b += glow(x0 + 3 * (wc + gap) + wc / 2, y0 + 90, 240, "g1")
    for i, (s, st) in enumerate(steps):
        x = x0 + i * (wc + gap)
        dim = (i == 4)
        b += card(x, y0, wc, 180, s)
        if st:
            mark = check if st == ST_OPEN else xmark
            b += mark(x + wc / 2, y0 + 120, 20, st, 4)
        if dim:
            b += caps(x + wc / 2, y0 + 130, "bloqueado", 18, MUTED,
                      anchor="middle")
        if i < 4:
            b += arrow(x + wc + 6, y0 + 90, x + wc + gap - 6, y0 + 90,
                       SECONDARY, 2.5)
    b += txt(W / 2, 760, "Vermelho em qualquer etapa: o cano para. Nada quebrado chega ao ar.",
             28, SECONDARY, anchor="middle")
    b += caption(W / 2, 950, "“CI verde” é isso: todas as conferências passaram.")
    export(b, f"{OUT}/10-ci-cd", defs=glow_def("g1"))


# ---------------------------------------------------------------- 11
def p11_deploy():
    """ATO 3: deploy troca a versão que está no servidor."""
    b = header(KICKER, fig(11))
    b += title(W / 2, 230, "Deploy: trocar a versão que está no ar")
    y0 = 400
    b += card(320, y0, 460, 320, "servidor · antes")
    b += chip(550, y0 + 180, "versão 12", SECONDARY)
    b += glow(1370, y0 + 160, 300, "g1")
    b += card(1140, y0, 460, 320, "servidor · depois", label_fill=ACCENT)
    b += chip(1370, y0 + 180, "versão 13", ACCENT)
    b += arrow(800, y0 + 160, 1120, y0 + 160, INK, 3, "deploy")
    b += caption(W / 2, 950, "O código vive no servidor. Deploy é trocar o que vive lá.")
    export(b, f"{OUT}/11-deploy", defs=glow_def("g1"))


# ---------------------------------------------------------------- 12
def p12_dns():
    """ATO 3: domínio e DNS, a lista telefônica."""
    b = header(KICKER, fig(12))
    b += title(W / 2, 230, "DNS: a lista telefônica da internet")
    y0 = 400
    b += card(220, y0, 460, 320, "o que você digita")
    b += txt(450, y0 + 190, "meuapp.com", 40, INK, anchor="middle", weight="700")
    b += glow(960, y0 + 160, 240, "g1")
    b += card(800, y0 + 40, 320, 240, None, elevated=True)
    b += caps(960, y0 + 110, "DNS", 26, ACCENT, anchor="middle")
    b += txt(960, y0 + 180, "traduz nome", 24, SECONDARY, anchor="middle")
    b += txt(960, y0 + 216, "em endereço", 24, SECONDARY, anchor="middle")
    b += card(1240, y0, 460, 320, "onde o servidor está")
    b += txt(1470, y0 + 190, "203.0.113.7", 40, SECONDARY, anchor="middle",
             weight="700")
    b += arrow(700, y0 + 160, 780, y0 + 160, INK, 3)
    b += arrow(1140, y0 + 160, 1220, y0 + 160, INK, 3)
    b += caption(W / 2, 950,
                 "No deploy comum, o DNS nem muda: o nome continua apontando para o mesmo lugar.")
    export(b, f"{OUT}/12-dominio-dns", defs=glow_def("g1"))


# ---------------------------------------------------------------- 13
def p13_fluxo_de_uso():
    """Encerramento: a volta final, o fluxo de uso completo."""
    b = header(KICKER, fig(13))
    b += title(W / 2, 230, "A volta final: alguém acessa")
    steps = ["digita a URL", "DNS traduz", "request na API",
             "banco · auth", "response", "renderiza"]
    wc, gap = 272, 44
    x0 = (W - 6 * wc - 5 * gap) / 2
    y0 = 440
    b += glow(x0 + 5 * (wc + gap) + wc / 2, y0 + 80, 240, "g1")
    for i, s in enumerate(steps):
        x = x0 + i * (wc + gap)
        b += card(x, y0, wc, 160, None)
        b += txt(x + wc / 2, y0 + 68, str(i + 1), 30, ACCENT if i == 5 else MUTED,
                 anchor="middle", weight="800")
        b += txt(x + wc / 2, y0 + 116, s, 23, INK, anchor="middle", weight="600")
        if i < 5:
            b += arrow(x + wc + 5, y0 + 80, x + wc + gap - 5, y0 + 80,
                       SECONDARY, 2.5)
    b += txt(W / 2, 740, "Esse ciclo acontece a cada interação. Cada clique pode ser uma nova conversa.",
             28, SECONDARY, anchor="middle")
    b += caption(W / 2, 950,
                 "Publicar é a metade. O uso é a outra jornada, a cada acesso.")
    export(b, f"{OUT}/13-fluxo-de-uso", defs=glow_def("g1"))


if __name__ == "__main__":
    p01_duas_jornadas()
    p02_html_css_js()
    p03_git_fotos()
    p04_servidor()
    p05_request_response()
    p06_api_balcao()
    p07_banco()
    p08_auth()
    p09_build()
    p10_cicd()
    p11_deploy()
    p12_dns()
    p13_fluxo_de_uso()
