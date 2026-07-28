#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pranchas do episódio 07 - Build, CI/CD e Deploy.
Uma prancha por passagem visual do roteiro (seções "Mostrar").
Design system: Midnight Grid (ver midnight_kit.py).

CI/CD aprofunda a prancha 10 do ep01 (commit→lint→testes→build→deploy):
aqui o portão, as três verificações, Delivery vs Deployment, ambientes,
estratégias, rollback+schema e o mapa da temporada — sem repetir aquele cano.
"""

from midnight_kit import (W, H, INK, SECONDARY, MUTED, BORDER, ACCENT,
                          SURFACE, ELEVATED, ST_OPEN, ST_GUIDED, ST_RESTRICTED,
                          export, header, title, caption, txt, caps, line,
                          rrect, circle, path, glow, glow_def, arrow, card,
                          chip, xmark, check)

OUT = "../../episodes/07-build-ci-cd-deploy/pranchas"
KICKER = "EP 07 · Build, CI/CD e deploy"
N = 14


def fig(n):
    return f"prancha {n:02d}/{N}"


# ---------------------------------------------------------------- 01
def p01_fonte_vs_buildado():
    """ATO 1: código fonte legível vs versão buildada compacta."""
    b = header(KICKER, fig(1))
    b += title(W / 2, 230, "O que você escreve não é o que sobe")
    wc, hc, gap = 720, 460, 100
    x0 = (W - 2 * wc - gap) / 2
    y0 = 340

    # fonte (esquerda)
    b += card(x0, y0, wc, hc, "código fonte")
    linhas_fonte = [
        (40, "function calcularTotal(itens) {"),
        (70, "  // soma o preço de cada item"),
        (100, "  let total = 0;"),
        (130, "  for (const item of itens) {"),
        (160, "    total += item.preco;"),
        (190, "  }"),
        (220, "  return total;"),
        (250, "}"),
    ]
    for dy, s in linhas_fonte:
        b += txt(x0 + 48, y0 + 100 + dy, s, 22, SECONDARY)

    # buildado (direita)
    b += glow(x0 + wc + gap + wc / 2, y0 + hc / 2, 300, "g1")
    b += card(x0 + wc + gap, y0, wc, hc, "depois do build", label_fill=ACCENT)
    x1 = x0 + wc + gap
    b += txt(x1 + wc / 2, y0 + 160, "function a(b){let c=0;", 24, MUTED,
             anchor="middle")
    b += txt(x1 + wc / 2, y0 + 205, "for(const d of b)c+=d.preco;", 24,
             MUTED, anchor="middle")
    b += txt(x1 + wc / 2, y0 + 250, "return c}", 24, MUTED, anchor="middle")
    b += txt(x1 + wc / 2, y0 + 320, "sem comentários · nomes curtos", 24,
             SECONDARY, anchor="middle")
    b += txt(x1 + wc / 2, y0 + 360, "compacto para a máquina", 24,
             SECONDARY, anchor="middle")

    b += caption(W / 2, 950,
                 "Você escreve para humanos. O build reescreve para a máquina.")
    export(b, f"{OUT}/01-fonte-vs-buildado", defs=glow_def("g1"))


# ---------------------------------------------------------------- 02
def p02_o_que_o_build_faz():
    """ATO 1: três trabalhos do build — traduz, reduz, junta."""
    b = header(KICKER, fig(2))
    b += title(W / 2, 230, "O que o build realmente faz")

    # vários arquivos à esquerda
    for i in range(4):
        b += rrect(160 + i * 12, 400 + i * 10, 220, 160, 12,
                   fill=SURFACE, stroke=BORDER, sw=2)
    b += caps(280, 640, "vários arquivos", 20, SECONDARY, anchor="middle")

    # seta BUILD no centro
    b += glow(960, 520, 260, "g1")
    b += card(760, 380, 400, 280, None, elevated=True)
    b += caps(960, 430, "build", 26, ACCENT, anchor="middle")
    acoes = ["traduz sintaxe", "reduz tamanho", "remove e junta"]
    for i, a in enumerate(acoes):
        b += txt(960, 500 + i * 42, a, 26, SECONDARY, anchor="middle")

    # um arquivo compacto à direita
    b += rrect(1400, 420, 340, 200, 12, fill=SURFACE, stroke=BORDER, sw=2)
    b += caps(1570, 640, "poucos · compactos", 20, SECONDARY, anchor="middle")

    b += arrow(440, 500, 740, 500, INK, 3)
    b += arrow(1180, 500, 1380, 500, INK, 3)

    b += caption(W / 2, 950,
                 "Nem todo build faz tudo. Mas esses três nomes vão aparecer.")
    export(b, f"{OUT}/02-o-que-o-build-faz", defs=glow_def("g1"))


# ---------------------------------------------------------------- 03
def p03_tres_motivos_build_quebrado():
    """ATO 1: sintaxe inválida, erro de tipo, dependência faltando."""
    b = header(KICKER, fig(3))
    b += title(W / 2, 230, "Três motivos de build quebrado")
    cards = [
        ("sintaxe inválida", "a gramática do código",
         "parêntese aberto, vírgula faltando"),
        ("erro de tipo", "categoria do valor",
         "número tratado como texto"),
        ("dependência faltando", "código de outra pessoa",
         "usou e não declarou, ou versão errada"),
    ]
    wc, hc, gap = 520, 400, 60
    x0 = (W - 3 * wc - 2 * gap) / 2
    y0 = 340
    for i, (titulo, sub, ex) in enumerate(cards):
        x = x0 + i * (wc + gap)
        if i == 0:
            b += glow(x + wc / 2, y0 + hc / 2, 260, "g1")
        b += card(x, y0, wc, hc, titulo,
                  label_fill=ACCENT if i == 0 else SECONDARY)
        b += xmark(x + wc / 2, y0 + 150, 26, ST_RESTRICTED, 4.5)
        b += txt(x + wc / 2, y0 + 240, sub, 26, INK, anchor="middle",
                 weight="600")
        b += txt(x + wc / 2, y0 + 300, ex, 23, SECONDARY, anchor="middle")
    b += caption(W / 2, 950,
                 "Build failed: a transformação não terminou. Leia o arquivo e a linha.")
    export(b, f"{OUT}/03-tres-motivos-build-quebrado", defs=glow_def("g1"))


# ---------------------------------------------------------------- 04
def p04_cano_neutro():
    """Fechamento do ATO 1: o cano inteiro, com o build destacado."""
    b = header(KICKER, fig(4))
    b += title(W / 2, 240, "O cano, etapa por etapa")
    etapas = ["push", "lint", "testes", "build", "deploy"]
    destaque = 3
    gap = 48
    wc = (1700 - 4 * gap) / 5
    y0, hc = 470, 130
    b += glow(110 + destaque * (wc + gap) + wc / 2, y0 + hc / 2, 280, "g1")
    for i, s in enumerate(etapas):
        x = 110 + i * (wc + gap)
        on = i == destaque
        b += rrect(x, y0, wc, hc, 16, fill=SURFACE,
                   stroke=INK if on else BORDER, sw=2.5 if on else 2)
        b += caps(x + wc / 2, y0 + hc / 2 + 8, s, 20,
                  INK if on else SECONDARY, anchor="middle")
        if i < 4:
            b += arrow(x + wc + 6, y0 + hc / 2, x + wc + gap - 6,
                       y0 + hc / 2, SECONDARY, 2.5)
    x_build = 110 + destaque * (wc + gap) + wc / 2
    b += caps(x_build, y0 + hc + 56, "a primeira porta", 20, ACCENT,
              anchor="middle")
    b += txt(W / 2, 780, "Cada etapa é uma porta. Vermelho em qualquer uma: "
             "nada segue adiante.", 27, SECONDARY, anchor="middle")
    b += caption(W / 2, 950,
                 "O build é a primeira porta. Se ele não passa, nada passa.")
    export(b, f"{OUT}/04-cano-neutro", defs=glow_def("g1"))


# ---------------------------------------------------------------- 05
def p05_ci_o_portao():
    """ATO 2: CI como portão — aprofunda ep01 (não repete o cano linear)."""
    b = header(KICKER, fig(5))
    b += title(W / 2, 230, "CI: o portão que abre sozinho")

    # lado esquerdo: código chegando
    b += card(120, 400, 360, 280, "código novo")
    b += txt(300, 540, "entra no repo", 28, SECONDARY, anchor="middle")
    b += txt(300, 590, "dispara o cano", 28, SECONDARY, anchor="middle")

    # portão no centro (metáfora, não o pipeline do ep01)
    b += glow(960, 540, 280, "g1")
    b += card(560, 360, 800, 400, None, elevated=True)
    b += caps(960, 420, "portão CI", 28, ACCENT, anchor="middle")
    b += txt(960, 490, "roda sozinho a cada entrada", 26, SECONDARY,
             anchor="middle")

    # duas saídas: verde segue / vermelho para
    b += chip(780, 580, "verde · segue", ST_OPEN)
    b += chip(1140, 580, "vermelho · para", ST_RESTRICTED)
    b += txt(960, 680, "vermelho em qualquer etapa: ninguém publica", 24,
             SECONDARY, anchor="middle")

    # lado direito: destino
    b += card(1440, 400, 360, 280, "próximo passo")
    b += txt(1620, 540, "só passa quem", 28, SECONDARY, anchor="middle")
    b += txt(1620, 590, "abriu o portão", 28, SECONDARY, anchor="middle")

    b += arrow(500, 540, 540, 540, INK, 3)
    b += arrow(1380, 540, 1420, 540, INK, 3)

    b += caption(W / 2, 950,
                 "Humano não confere na mão. O cano confere sozinho.")
    export(b, f"{OUT}/05-ci-o-portao", defs=glow_def("g1"))


# ---------------------------------------------------------------- 06
def p06_tres_verificacoes():
    """ATO 2: lint (estilo), testes (comportamento), build (transformação)."""
    b = header(KICKER, fig(6))
    b += title(W / 2, 230, "Três verificações, três proteções")
    cols = [
        ("lint", "estilo", "como o time combinou escrever",
         "indentação · nomes · aspas"),
        ("testes", "comportamento", "se X, espero Y",
         "o que você prometeu continua"),
        ("build", "transformação", "consegue virar versão servível",
         "se quebra aqui, sinal forte"),
    ]
    wc, hc, gap = 520, 420, 60
    x0 = (W - 3 * wc - 2 * gap) / 2
    y0 = 340
    for i, (nome, protege, frase, detalhe) in enumerate(cols):
        x = x0 + i * (wc + gap)
        if i == 1:
            b += glow(x + wc / 2, y0 + hc / 2, 280, "g1")
        b += card(x, y0, wc, hc)
        b += caps(x + wc / 2, y0 + 60, nome, 26,
                  ACCENT if i == 1 else SECONDARY, anchor="middle")
        b += txt(x + wc / 2, y0 + 150, protege, 36, INK, anchor="middle",
                 weight="800")
        b += txt(x + wc / 2, y0 + 240, frase, 24, SECONDARY, anchor="middle")
        b += txt(x + wc / 2, y0 + 300, detalhe, 22, MUTED, anchor="middle")
    b += caption(W / 2, 950,
                 "CI vermelho: alguém lê o erro, conserta, e o cano tenta de novo.")
    export(b, f"{OUT}/06-tres-verificacoes", defs=glow_def("g1"))


# ---------------------------------------------------------------- 07
def p07_delivery_vs_deployment():
    """ATO 2: Continuous Delivery (botão humano) vs Continuous Deployment."""
    b = header(KICKER, fig(7))
    b += title(W / 2, 230, "CD: duas fronteiras de automação")
    wc, hc, gap = 760, 440, 80
    x0 = (W - 2 * wc - gap) / 2
    y0 = 340

    b += glow(x0 + wc / 2, y0 + hc / 2, 300, "g1")
    b += card(x0, y0, wc, hc)
    b += caps(x0 + wc / 2, y0 + 60, "continuous delivery", 24, ACCENT,
              anchor="middle")
    b += txt(x0 + wc / 2, y0 + 160, "prepara e para", 40, INK,
             anchor="middle", weight="800")
    b += txt(x0 + wc / 2, y0 + 250, "versão publicável pronta", 26,
             SECONDARY, anchor="middle")
    b += txt(x0 + wc / 2, y0 + 300, "humano aperta o botão", 26,
             SECONDARY, anchor="middle")
    b += chip(x0 + wc / 2, y0 + 370, "portão humano", SECONDARY)

    x1 = x0 + wc + gap
    b += card(x1, y0, wc, hc)
    b += caps(x1 + wc / 2, y0 + 60, "continuous deployment", 24, SECONDARY,
              anchor="middle")
    b += txt(x1 + wc / 2, y0 + 160, "publica sozinho", 40, INK,
             anchor="middle", weight="800")
    b += txt(x1 + wc / 2, y0 + 250, "CI verde → já vai ao ar", 26,
             SECONDARY, anchor="middle")
    b += txt(x1 + wc / 2, y0 + 300, "sem decisão humana", 26,
             SECONDARY, anchor="middle")
    b += chip(x1 + wc / 2, y0 + 370, "automático", SECONDARY)

    b += caption(W / 2, 950,
                 "Os dois se chamam CD. O que muda é quem decide publicar.")
    export(b, f"{OUT}/07-delivery-vs-deployment", defs=glow_def("g1"))


# ---------------------------------------------------------------- 08
def p08_quatro_ambientes():
    """ATO 2: local → dev → staging → prod (escala ordenada de risco)."""
    b = header(KICKER, fig(8))
    b += title(W / 2, 230, "Quatro ambientes, um caminho")
    # escala ordenada: local (muted) → open → guided → restricted
    envs = [
        ("local", "seu computador", "só você vê", MUTED),
        ("dev", "teste do time", "quebra a vontade", ST_OPEN),
        ("staging", "ensaio do real", "não se quebra à toa", ST_GUIDED),
        ("prod", "o ar", "usuário acessa", ST_RESTRICTED),
    ]
    wc, hc, gap = 380, 380, 50
    x0 = (W - 4 * wc - 3 * gap) / 2
    y0 = 360
    b += glow(x0 + 3 * (wc + gap) + wc / 2, y0 + hc / 2, 260, "g1")
    for i, (nome, papel, nota, cor) in enumerate(envs):
        x = x0 + i * (wc + gap)
        b += card(x, y0, wc, hc)
        b += caps(x + wc / 2, y0 + 70, nome, 24, cor, anchor="middle")
        b += txt(x + wc / 2, y0 + 180, papel, 28, INK, anchor="middle",
                 weight="700")
        b += txt(x + wc / 2, y0 + 260, nota, 24, SECONDARY, anchor="middle")
        if i < 3:
            b += arrow(x + wc + 6, y0 + hc / 2, x + wc + gap - 6, y0 + hc / 2,
                       SECONDARY, 2.5)
    b += caption(W / 2, 950,
                 "O código sobe de ambiente em ambiente. Prod pede mais cuidado.")
    export(b, f"{OUT}/08-quatro-ambientes", defs=glow_def("g1"))


# ---------------------------------------------------------------- 09
def p09_blue_green():
    """ATO 2: blue-green — paralelo, testa, troca o tráfego."""
    b = header(KICKER, fig(9))
    b += title(W / 2, 230, "Blue-green: sobe ao lado e troca")
    y0, hc, wc = 380, 360, 520

    b += card(200, y0, wc, hc, "versão antiga")
    b += txt(460, y0 + 180, "ainda no ar", 30, SECONDARY, anchor="middle")
    b += txt(460, y0 + 240, "pronta para voltar", 26, MUTED, anchor="middle")

    b += glow(1460, y0 + hc / 2, 280, "g1")
    b += card(1200, y0, wc, hc, "versão nova", label_fill=ACCENT)
    b += txt(1460, y0 + 180, "sobe em paralelo", 30, SECONDARY,
             anchor="middle")
    b += txt(1460, y0 + 240, "testa · depois troca", 26, MUTED,
             anchor="middle")

    # seta de troca no meio
    b += arrow(760, y0 + 140, 1160, y0 + 140, INK, 3, "troca o tráfego")
    b += arrow(1160, y0 + 240, 760, y0 + 240, SECONDARY, 2.5, "volta fácil",
               dash="8 6")

    b += caption(W / 2, 950,
                 "A antiga fica lá. Se der problema, o tráfego volta sem reescrever.")
    export(b, f"{OUT}/09-blue-green", defs=glow_def("g1"))


# ---------------------------------------------------------------- 10
def p10_canary():
    """ATO 2: canary — libera aos poucos (5% → 100%)."""
    b = header(KICKER, fig(10))
    b += title(W / 2, 230, "Canary: libera para poucos primeiro")

    # escala ordenada de exposição: verde → âmbar → vermelho
    etapas = [("5%", ST_OPEN), ("10%", ST_OPEN), ("50%", ST_GUIDED),
              ("100%", ST_RESTRICTED)]
    wc, hc, gap = 340, 280, 60
    x0 = (W - 4 * wc - 3 * gap) / 2
    y0 = 400
    b += glow(x0 + 3 * (wc + gap) + wc / 2, y0 + hc / 2, 240, "g1")
    for i, (pct, cor) in enumerate(etapas):
        x = x0 + i * (wc + gap)
        b += card(x, y0, wc, hc)
        b += txt(x + wc / 2, y0 + 120, pct, 56, cor,
                 anchor="middle", weight="800")
        b += caps(x + wc / 2, y0 + 200, "do tráfego", 20, SECONDARY,
                  anchor="middle")
        if i < 3:
            b += arrow(x + wc + 6, y0 + hc / 2, x + wc + gap - 6, y0 + hc / 2,
                       SECONDARY, 2.5)
    b += txt(W / 2, 780, "Se quebrar no começo, só poucos perceberam. E você volta rápido.",
             28, SECONDARY, anchor="middle")
    b += caption(W / 2, 950,
                 "Estratégia existe para reduzir o risco de publicar.")
    export(b, f"{OUT}/10-canary", defs=glow_def("g1"))


# ---------------------------------------------------------------- 11
def p11_rollback_e_schema():
    """ATO 3: rollback de código pode piorar se o schema mudou."""
    b = header(KICKER, fig(11))
    b += title(W / 2, 230, "Rollback + schema: voltar pode piorar")

    # fluxo: versão nova → problema → rollback
    b += card(120, 360, 400, 220, "versão nova no ar")
    b += txt(320, 500, "mudou o schema", 26, SECONDARY, anchor="middle")

    b += arrow(540, 470, 640, 470, ST_RESTRICTED, 3)

    b += card(660, 360, 400, 220, "problema detectado")
    b += xmark(860, 500, 22, ST_RESTRICTED, 4)

    b += arrow(1080, 470, 1180, 470, SECONDARY, 3, "rollback")

    b += glow(1480, 470, 240, "g1")
    b += card(1200, 360, 560, 220, "código antigo volta", label_fill=ACCENT)
    b += txt(1480, 500, "não conhece a coluna nova", 24, SECONDARY,
             anchor="middle")

    # aviso inferior (sem segundo amarelo — ACCENT já está no card da direita)
    b += card(220, 640, 1480, 160)
    b += caps(960, 700, "quando o rollback não resolve", 22, SECONDARY,
              anchor="middle")
    b += txt(960, 760,
             "Mexeu em schema ou quebrou API? Avançar e corrigir. Voltar cria segundo incidente.",
             26, SECONDARY, anchor="middle")

    b += caption(W / 2, 950,
                 "Rollback troca versão. Não desfaz mudança de dado.")
    export(b, f"{OUT}/11-rollback-e-schema", defs=glow_def("g1"))


# ---------------------------------------------------------------- 12
def p12_incidente_post_mortem():
    """ATO 3: incidente + quatro perguntas do post-mortem."""
    b = header(KICKER, fig(12))
    b += title(W / 2, 230, "Incidente e post-mortem")

    # incidente (esquerda)
    b += card(140, 360, 700, 420)
    b += caps(490, 430, "incidente", 26, ACCENT, anchor="middle")
    b += glow(490, 560, 220, "g1")
    b += txt(490, 520, "quebra com impacto real", 30, INK, anchor="middle",
             weight="700")
    b += txt(490, 600, "não consegue logar", 26, SECONDARY, anchor="middle")
    b += txt(490, 650, "não consegue comprar", 26, SECONDARY, anchor="middle")
    b += txt(490, 700, "não consegue acessar", 26, SECONDARY, anchor="middle")

    # post-mortem (direita)
    b += card(940, 360, 840, 420)
    b += caps(1360, 430, "post-mortem", 26, SECONDARY, anchor="middle")
    perguntas = [
        "o que aconteceu?",
        "como detectamos?",
        "como resolvemos?",
        "o que vamos mudar?",
    ]
    for i, q in enumerate(perguntas):
        y = 510 + i * 55
        b += circle(1020, y - 8, 10, fill=SURFACE, stroke=INK, sw=2)
        b += txt(1060, y, q, 28, SECONDARY)

    b += caption(W / 2, 950,
                 "Controlou o problema. Depois senta e pergunta para não repetir.")
    export(b, f"{OUT}/12-incidente-post-mortem", defs=glow_def("g1"))


# ---------------------------------------------------------------- 13
def p13_ciclo_completo():
    """ATO 3: o cano completo em uma linha — usuário só vê a ponta."""
    b = header(KICKER, fig(13))
    b += title(W / 2, 230, "O ciclo completo, até o usuário")
    steps = ["código", "commit", "CI", "CD", "ambientes", "no ar"]
    wc, gap = 250, 40
    x0 = (W - 6 * wc - 5 * gap) / 2
    y0 = 420
    b += glow(x0 + 5 * (wc + gap) + wc / 2, y0 + 80, 240, "g1")
    for i, s in enumerate(steps):
        x = x0 + i * (wc + gap)
        destaque = (i == 5)
        b += card(x, y0, wc, 160)
        b += txt(x + wc / 2, y0 + 68, str(i + 1), 28,
                 ACCENT if destaque else MUTED, anchor="middle", weight="800")
        b += txt(x + wc / 2, y0 + 116, s, 24, INK, anchor="middle",
                 weight="600")
        if i < 5:
            b += arrow(x + wc + 4, y0 + 80, x + wc + gap - 4, y0 + 80,
                       SECONDARY, 2.5)
    b += txt(W / 2, 700,
             "Lint, testes e build moram dentro do CI. Blue-green e canary, no deploy.",
             26, SECONDARY, anchor="middle")
    b += txt(W / 2, 760,
             "O usuário só enxerga a última ponta. E percebe se algo mudou.",
             26, SECONDARY, anchor="middle")
    b += caption(W / 2, 950,
                 "Se deu ruim: rollback (quando seguro), entender, corrigir, de novo.")
    export(b, f"{OUT}/13-ciclo-completo", defs=glow_def("g1"))


# ---------------------------------------------------------------- 14
def p14_mapa_da_temporada():
    """Fechamento: mapa da temporada revisitado — ep07 fecha o cano."""
    b = header(KICKER, fig(14))
    b += title(W / 2, 230, "O mapa da temporada, fechado")

    layers = [
        ("02", "front-end e estado", "navegador · HTML · CSS · JS"),
        ("03", "request, response, API", "a ponte navegador ↔ servidor"),
        ("04", "banco de dados", "memória de longo prazo"),
        ("05", "auth e sessão", "quem é você · o que pode"),
        ("06", "git e versionamento", "fotos no tempo · rede de segurança"),
        ("07", "build, CI/CD, deploy", "o cano que leva ao ar"),
    ]
    # duas colunas de 3
    wc, hc, gapx, gapy = 800, 140, 60, 28
    x0 = (W - 2 * wc - gapx) / 2
    y0 = 340
    for i, (ep, nome, desc) in enumerate(layers):
        col = i % 2
        row = i // 2
        x = x0 + col * (wc + gapx)
        y = y0 + row * (hc + gapy)
        destaque = (ep == "07")
        if destaque:
            b += glow(x + wc / 2, y + hc / 2, 200, "g1")
        b += card(x, y, wc, hc)
        b += caps(x + 40, y + 55, f"ep {ep}", 20,
                  ACCENT if destaque else MUTED)
        b += txt(x + 200, y + 58, nome, 28, INK if not destaque else ACCENT,
                 weight="700")
        b += txt(x + 200, y + 105, desc, 24, SECONDARY)

    b += caption(W / 2, 950,
                 "Quando a IA sugerir mudança: em qual camada isso mora?")
    export(b, f"{OUT}/14-mapa-da-temporada", defs=glow_def("g1"))


if __name__ == "__main__":
    p01_fonte_vs_buildado()
    p02_o_que_o_build_faz()
    p03_tres_motivos_build_quebrado()
    p04_cano_neutro()
    p05_ci_o_portao()
    p06_tres_verificacoes()
    p07_delivery_vs_deployment()
    p08_quatro_ambientes()
    p09_blue_green()
    p10_canary()
    p11_rollback_e_schema()
    p12_incidente_post_mortem()
    p13_ciclo_completo()
    p14_mapa_da_temporada()
