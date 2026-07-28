#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pranchas do episódio 08 - Secrets e variáveis de ambiente.
Uma prancha por passagem visual do roteiro (seções "Mostrar").
Design system: Midnight Grid (ver midnight_kit.py).

Valores de chave nas pranchas são SEMPRE obviamente falsos
(chave_exemplo_nao_usar). Nunca valor plausível.
"""

from midnight_kit import (W, H, INK, SECONDARY, MUTED, BORDER, ACCENT,
                          SURFACE, ELEVATED, ST_OPEN, ST_GUIDED, ST_RESTRICTED,
                          export, header, title, caption, txt, caps, line,
                          rrect, circle, path, glow, glow_def, arrow, card,
                          chip, xmark, check)

OUT = "../../episodes/08-secrets-e-variaveis-de-ambiente/pranchas"
KICKER = "EP 08 · Secrets e variáveis de ambiente"
N = 12

# Placeholder único e obviamente falso — nunca valor plausível
FAKE = "chave_exemplo_nao_usar"


def fig(n):
    return f"prancha {n:02d}/{N}"


# ---------------------------------------------------------------- 01
def p01_chave_no_codigo():
    """Abertura: chave colada no código, com X vermelho."""
    b = header(KICKER, fig(1))
    b += title(W / 2, 230, "A chave colada no código")
    b += glow(W / 2, 560, 380, "g1")

    # bloco de "código"
    wc, hc = 1100, 280
    x0 = (W - wc) / 2
    y0 = 400
    b += rrect(x0, y0, wc, hc, 16, fill=SURFACE, stroke=BORDER, sw=2)
    b += caps(x0 + 48, y0 + 56, "trecho do código", 20, MUTED)
    b += txt(x0 + 48, y0 + 150, 'chave = "' + FAKE + '"', 36, INK,
             weight="600")
    b += txt(x0 + 48, y0 + 220, "valor escrito direto no arquivo", 24,
             SECONDARY)

    # X vermelho sobre o bloco
    b += xmark(x0 + wc - 90, y0 + hc / 2, 42, ST_RESTRICTED, 7)

    b += caption(W / 2, 950,
                 "No fim do vídeo, você sabe por que isso está errado.")
    export(b, f"{OUT}/01-chave-no-codigo", defs=glow_def("g1"))


# ---------------------------------------------------------------- 02
def p02_o_que_e_segredo():
    """ATO 1: três exemplos do que conta como segredo."""
    b = header(KICKER, fig(2))
    b += title(W / 2, 230, "Segredo: acesso em seu nome")
    cols = [
        ("chave de API", "senha que um serviço", "dá para o seu sistema"),
        ("senha do banco", "abre a memória", "de longo prazo"),
        ("token de acesso", "prova temporária", "de que você é você"),
    ]
    wc, hc, gap = 520, 400, 60
    x0 = (W - 3 * wc - 2 * gap) / 2
    y0 = 340
    b += glow(x0 + wc / 2, y0 + hc / 2, 300, "g1")
    for i, (nome, l1, l2) in enumerate(cols):
        x = x0 + i * (wc + gap)
        b += card(x, y0, wc, hc)
        b += caps(x + wc / 2, y0 + 70, "segredo", 20,
                  ACCENT if i == 0 else MUTED, anchor="middle")
        b += txt(x + wc / 2, y0 + 170, nome, 34, INK, anchor="middle",
                 weight="700")
        b += txt(x + wc / 2, y0 + 250, l1, 24, SECONDARY, anchor="middle")
        b += txt(x + wc / 2, y0 + 290, l2, 24, SECONDARY, anchor="middle")
        b += txt(x + wc / 2, y0 + 360, FAKE, 20, MUTED, anchor="middle")
    b += caption(W / 2, 950,
                 "Quem tem a chave, usa o serviço em seu nome.")
    export(b, f"{OUT}/02-o-que-e-segredo", defs=glow_def("g1"))


# ---------------------------------------------------------------- 03
def p03_fechadura_e_chave():
    """ATO 1: código = fechadura, segredo = chave."""
    b = header(KICKER, fig(3))
    b += title(W / 2, 230, "Código é fechadura. Segredo é chave.")
    wc, hc, gap = 700, 420, 120
    x0 = (W - 2 * wc - gap) / 2
    y0 = 340

    # fechadura / código
    b += glow(x0 + wc / 2, y0 + hc / 2, 300, "g1")
    b += card(x0, y0, wc, hc, "código · a fechadura", label_fill=ACCENT)
    b += txt(x0 + wc / 2, y0 + 180, "todo mundo pode ver", 30, INK,
             anchor="middle", weight="600")
    b += txt(x0 + wc / 2, y0 + 250, "vai para o repo", 26, SECONDARY,
             anchor="middle")
    b += txt(x0 + wc / 2, y0 + 300, "diz O QUE fazer", 26, SECONDARY,
             anchor="middle")
    b += chip(x0 + wc / 2, y0 + 370, "visível", SECONDARY, 18)

    # chave / segredo
    x1 = x0 + wc + gap
    b += card(x1, y0, wc, hc, "segredo · a chave")
    b += txt(x1 + wc / 2, y0 + 180, "só o dono carrega", 30, INK,
             anchor="middle", weight="600")
    b += txt(x1 + wc / 2, y0 + 250, "nunca no repo", 26, SECONDARY,
             anchor="middle")
    b += txt(x1 + wc / 2, y0 + 300, "diz COM QUAL chave", 26, SECONDARY,
             anchor="middle")
    b += chip(x1 + wc / 2, y0 + 370, "protegido", SECONDARY, 18)

    b += caption(W / 2, 950,
                 "Os dois nunca viajam juntos.")
    export(b, f"{OUT}/03-fechadura-e-chave", defs=glow_def("g1"))


# ---------------------------------------------------------------- 04
def p04_fluxo_do_vazamento():
    """ATO 1: commit imutável → repo → robôs."""
    b = header(KICKER, fig(4))
    b += title(W / 2, 230, "Commitou = vazou")
    steps = [
        ("1", "chave no código"),
        ("2", "commit · foto"),
        ("3", "repo público"),
        ("4", "robôs acham"),
    ]
    wc, gap = 360, 50
    x0 = (W - 4 * wc - 3 * gap) / 2
    y0 = 380
    b += glow(x0 + 3 * (wc + gap) + wc / 2, y0 + 90, 260, "g1")
    for i, (num, label) in enumerate(steps):
        x = x0 + i * (wc + gap)
        b += card(x, y0, wc, 180)
        b += txt(x + wc / 2, y0 + 70, num, 36,
                 ACCENT if i == 0 else MUTED, anchor="middle", weight="800")
        b += txt(x + wc / 2, y0 + 130, label, 26, INK, anchor="middle",
                 weight="600")
        if i < 3:
            b += arrow(x + wc + 6, y0 + 90, x + wc + gap - 6, y0 + 90,
                       SECONDARY, 2.5)

    # alerta: apagar não resolve
    b += rrect(280, 640, 1360, 160, 16, fill=ELEVATED, stroke=BORDER, sw=2)
    b += xmark(360, 720, 22, ST_RESTRICTED, 4)
    b += txt(420, 710, "Apaguei o arquivo depois", 28, INK, weight="600")
    b += txt(420, 760, "A foto antiga continua no álbum. Não resolve.", 26,
             SECONDARY)

    b += caption(W / 2, 950,
                 "Commit é foto imutável. A chave entra para sempre.")
    export(b, f"{OUT}/04-fluxo-do-vazamento", defs=glow_def("g1"))


# ---------------------------------------------------------------- 05
def p05_quatro_ambientes():
    """ATO 2: mesmo código, quatro ambientes, valores diferentes."""
    b = header(KICKER, fig(5))
    b += title(W / 2, 230, "Mesmo código. Valores diferentes.")
    envs = [
        ("local", "chave de teste", False),
        ("dev", "chave de teste", False),
        ("staging", "chave de teste", False),
        ("prod", "chave real", True),
    ]
    wc, hc, gap = 400, 380, 40
    x0 = (W - 4 * wc - 3 * gap) / 2
    y0 = 340
    b += glow(x0 + 3 * (wc + gap) + wc / 2, y0 + hc / 2, 280, "g1")
    for i, (nome, valor, is_prod) in enumerate(envs):
        x = x0 + i * (wc + gap)
        b += card(x, y0, wc, hc, nome,
                  label_fill=ACCENT if is_prod else SECONDARY)
        b += rrect(x + 40, y0 + 100, wc - 80, 90, 12, fill=ELEVATED,
                   stroke=BORDER, sw=1.5)
        b += txt(x + wc / 2, y0 + 155, "mesmo código", 24, INK,
                 anchor="middle", weight="600")
        b += txt(x + wc / 2, y0 + 260, valor, 24, INK if is_prod else SECONDARY,
                 anchor="middle", weight="600")
        b += txt(x + wc / 2, y0 + 320, "CHAVE_PAGAMENTO", 20, MUTED,
                 anchor="middle")
    b += caption(W / 2, 950,
                 "O que muda entre ambientes não é o código. São os valores.")
    export(b, f"{OUT}/05-quatro-ambientes", defs=glow_def("g1"))


# ---------------------------------------------------------------- 06
def p06_variavel_de_ambiente():
    """ATO 2: o código pede pelo nome; o ambiente devolve o valor."""
    b = header(KICKER, fig(6))
    b += title(W / 2, 230, "O código pede pelo nome")

    # código à esquerda (foco amarelo + glow)
    wc, hc = 560, 400
    x0, y0 = 160, 350
    b += glow(x0 + wc / 2, y0 + hc / 2, 300, "g1")
    b += card(x0, y0, wc, hc, "código")
    b += txt(x0 + wc / 2, y0 + 150, "me dá", 28, SECONDARY, anchor="middle")
    b += txt(x0 + wc / 2, y0 + 220, "CHAVE_PAGAMENTO", 34, ACCENT,
             anchor="middle", weight="700")
    b += txt(x0 + wc / 2, y0 + 300, "só o NOME", 24, MUTED, anchor="middle")

    # dois ambientes à direita
    x1, we, he = 900, 860, 180
    b += card(x1, 350, we, he, "ambiente · dev")
    b += txt(x1 + 40, 470, "CHAVE_PAGAMENTO", 22, MUTED)
    b += txt(x1 + we - 40, 470, "chave_teste_nao_usar", 24, SECONDARY,
             anchor="end", weight="600")

    b += card(x1, 570, we, he, "ambiente · prod")
    b += txt(x1 + 40, 690, "CHAVE_PAGAMENTO", 22, MUTED)
    b += txt(x1 + we - 40, 690, FAKE, 24, SECONDARY, anchor="end",
             weight="600")

    b += arrow(x0 + wc + 12, y0 + 120, x1 - 12, 440, INK, 2.5)
    b += arrow(x0 + wc + 12, y0 + 280, x1 - 12, 660, SECONDARY, 2.5)

    b += caps(W / 2, 820, "mesmo nome · valor diferente", 22, SECONDARY,
              anchor="middle")
    b += caption(W / 2, 950,
                 "No código, só o nome. O valor, nunca.")
    export(b, f"{OUT}/06-variavel-de-ambiente", defs=glow_def("g1"))


# ---------------------------------------------------------------- 07
def p07_env_gitignore():
    """ATO 2: .env vs .env.example vs .gitignore."""
    b = header(KICKER, fig(7))
    b += title(W / 2, 230, ".env, .env.example e .gitignore")

    wc, hc, gap = 520, 420, 50
    x0 = (W - 3 * wc - 2 * gap) / 2
    y0 = 340

    # .env — nunca no repo
    b += card(x0, y0, wc, hc, ".env")
    b += txt(x0 + wc / 2, y0 + 130, "valores de verdade", 26, INK,
             anchor="middle", weight="600")
    b += txt(x0 + wc / 2, y0 + 190, "CHAVE = " + FAKE, 22, MUTED,
             anchor="middle")
    b += chip(x0 + wc / 2, y0 + 280, "fica na máquina", SECONDARY, 18)
    b += xmark(x0 + wc / 2, y0 + 360, 20, ST_RESTRICTED, 4)
    b += txt(x0 + wc / 2, y0 + 400, "nunca no repo", 22, ST_RESTRICTED,
             anchor="middle")

    # .env.example — vai para o repo
    x1 = x0 + wc + gap
    b += glow(x1 + wc / 2, y0 + hc / 2, 280, "g1")
    b += card(x1, y0, wc, hc, ".env.example", label_fill=ACCENT)
    b += txt(x1 + wc / 2, y0 + 130, "só os NOMES", 26, INK,
             anchor="middle", weight="600")
    b += txt(x1 + wc / 2, y0 + 190, "CHAVE = ", 22, MUTED, anchor="middle")
    b += chip(x1 + wc / 2, y0 + 280, "mapa sem chave", SECONDARY, 18)
    b += check(x1 + wc / 2, y0 + 360, 20, ST_OPEN, 4)
    b += txt(x1 + wc / 2, y0 + 400, "vai para o repo", 22, ST_OPEN,
             anchor="middle")

    # .gitignore
    x2 = x1 + wc + gap
    b += card(x2, y0, wc, hc, ".gitignore")
    b += txt(x2 + wc / 2, y0 + 130, "lista do que o git", 26, INK,
             anchor="middle", weight="600")
    b += txt(x2 + wc / 2, y0 + 170, "deve ignorar", 26, INK,
             anchor="middle", weight="600")
    b += rrect(x2 + 60, y0 + 230, wc - 120, 70, 12, fill=ELEVATED,
               stroke=BORDER, sw=1.5)
    b += txt(x2 + wc / 2, y0 + 275, ".env", 28, INK, anchor="middle",
             weight="700")
    b += txt(x2 + wc / 2, y0 + 360, "protege o .env", 22, SECONDARY,
             anchor="middle")

    b += caption(W / 2, 950,
                 "O mapa vai para o repo. A chave fica fora.")
    export(b, f"{OUT}/07-env-gitignore", defs=glow_def("g1"))


# ---------------------------------------------------------------- 08
def p08_producao_painel():
    """ATO 2: em prod, o painel da plataforma injeta as variáveis."""
    b = header(KICKER, fig(8))
    b += title(W / 2, 230, "Em produção: o painel da plataforma")

    y0 = 380
    # código viaja
    b += card(140, y0, 420, 320, "código")
    b += txt(350, y0 + 160, "sem valores", 28, INK, anchor="middle",
             weight="600")
    b += txt(350, y0 + 220, "só os nomes", 24, SECONDARY, anchor="middle")

    b += arrow(580, y0 + 100, 780, y0 + 100, INK, 3, "deploy")

    # servidor
    b += glow(1100, y0 + 160, 300, "g1")
    b += card(800, y0, 480, 320, "servidor rodando", label_fill=ACCENT)
    b += txt(1040, y0 + 160, "código + valores", 28, INK, anchor="middle",
             weight="600")
    b += txt(1040, y0 + 220, "se encontram aqui", 24, SECONDARY,
             anchor="middle")

    # painel
    b += card(1400, y0, 380, 320, "painel")
    b += txt(1590, y0 + 140, "NOME = valor", 24, SECONDARY, anchor="middle")
    b += txt(1590, y0 + 200, "cadastrado", 24, SECONDARY, anchor="middle")
    b += txt(1590, y0 + 260, "uma a uma", 24, MUTED, anchor="middle")

    b += arrow(1400, y0 + 160, 1300, y0 + 160, SECONDARY, 2.5,
               "injeta")

    b += caption(W / 2, 950,
                 "O deploy leva o código. A configuração já está esperando.")
    export(b, f"{OUT}/08-producao-painel", defs=glow_def("g1"))


# ---------------------------------------------------------------- 09
def p09_tres_armadilhas():
    """ATO 3: as três armadilhas clássicas da IA."""
    b = header(KICKER, fig(9))
    b += title(W / 2, 230, "Três armadilhas da IA")
    traps = [
        ("chave no código", "está no código", "ou no ambiente?"),
        (".env no repo", ".env está no", ".gitignore?"),
        ("segredo no log", "aparece em log", "ou mensagem?"),
    ]
    wc, hc, gap = 520, 400, 60
    x0 = (W - 3 * wc - 2 * gap) / 2
    y0 = 340
    b += glow(W / 2, y0 + hc / 2, 320, "g1")
    for i, (titulo, q1, q2) in enumerate(traps):
        x = x0 + i * (wc + gap)
        b += card(x, y0, wc, hc)
        b += txt(x + wc / 2, y0 + 70, str(i + 1), 36,
                 ACCENT if i == 0 else MUTED, anchor="middle", weight="800")
        b += txt(x + wc / 2, y0 + 150, titulo, 30, INK, anchor="middle",
                 weight="700")
        b += caps(x + wc / 2, y0 + 240, "pergunta-crivo", 18, MUTED,
                  anchor="middle")
        b += txt(x + wc / 2, y0 + 300, q1, 24, SECONDARY, anchor="middle")
        b += txt(x + wc / 2, y0 + 340, q2, 24, SECONDARY, anchor="middle")
    b += caption(W / 2, 950,
                 "Antes de commitar, procure string longa suspeita no diff.")
    export(b, f"{OUT}/09-tres-armadilhas", defs=glow_def("g1"))


# ---------------------------------------------------------------- 10
def p10_como_pedir_certo():
    """ATO 3: os três prompts prontos que resolvem quase tudo."""
    b = header(KICKER, fig(10))
    b += title(W / 2, 230, "Três pedidos que resolvem quase tudo")
    b += caps(W / 2, 310, "prompts prontos para copiar", 22, ACCENT,
              anchor="middle")

    prompts = [
        ("1", "“use variável de ambiente, não escreva o valor no código”",
         "ela sabe fazer, só precisa do comando"),
        ("2", "“crie o .env.example e garanta que o .env está no .gitignore”",
         "uma frase, e a estrutura fica certa"),
        ("3", "“nunca cole a chave real no chat: use placeholder”",
         "preencha o valor você mesmo, direto no .env"),
    ]
    y0, hc, vgap = 370, 150, 36
    b += glow(W / 2, y0 + hc / 2, 300, "g1")
    for i, (num, prompt, nota) in enumerate(prompts):
        y = y0 + i * (hc + vgap)
        b += card(210, y, 1500, hc)
        b += txt(300, y + 92, num, 52, SECONDARY, anchor="middle",
                 weight="800")
        b += txt(380, y + 72, prompt, 29, INK, weight="600")
        b += txt(380, y + 116, nota, 22, SECONDARY)

    b += caption(W / 2, 990, "A IA faz certo se você pedir certo.")
    export(b, f"{OUT}/10-como-pedir-certo", defs=glow_def("g1"))


# ---------------------------------------------------------------- 11
def p11_protocolo_emergencia():
    """ATO 3: revogar → trocar → verificar."""
    b = header(KICKER, fig(11))
    b += title(W / 2, 230, "Vazou? Protocolo de emergência")
    steps = [
        ("1", "revogar", "cancela a chave", "no painel do serviço"),
        ("2", "trocar", "chave nova no", ".env e no painel"),
        ("3", "verificar", "uso estranho?", "cobrança?"),
    ]
    wc, hc, gap = 480, 360, 70
    x0 = (W - 3 * wc - 2 * gap) / 2
    y0 = 340
    b += glow(x0 + wc / 2, y0 + hc / 2, 280, "g1")
    for i, (num, titulo, l1, l2) in enumerate(steps):
        x = x0 + i * (wc + gap)
        b += card(x, y0, wc, hc)
        b += txt(x + wc / 2, y0 + 80, num, 44,
                 ACCENT if i == 0 else MUTED, anchor="middle", weight="800")
        b += caps(x + wc / 2, y0 + 160, titulo, 24, INK, anchor="middle")
        b += txt(x + wc / 2, y0 + 240, l1, 24, SECONDARY, anchor="middle")
        b += txt(x + wc / 2, y0 + 285, l2, 24, SECONDARY, anchor="middle")
        if i < 2:
            b += arrow(x + wc + 8, y0 + hc / 2, x + wc + gap - 8,
                       y0 + hc / 2, SECONDARY, 2.5)

    b += txt(W / 2, 780,
             "Apagar o commit não desfaz o vazamento.", 26, ST_RESTRICTED,
             anchor="middle", weight="600")
    b += caption(W / 2, 950,
                 "Rotacionar não é uma das opções. É a única.")
    export(b, f"{OUT}/11-protocolo-emergencia", defs=glow_def("g1"))


# ---------------------------------------------------------------- 12
def p12_regra_de_ouro():
    """Encerramento: regra de ouro + mapa código vs ambiente."""
    b = header(KICKER, fig(12))
    b += title(W / 2, 230, "No código, só o nome. O valor, nunca.")

    wc, hc, gap = 720, 380, 100
    x0 = (W - 2 * wc - gap) / 2
    y0 = 340

    b += glow(x0 + wc / 2, y0 + hc / 2, 300, "g1")
    b += card(x0, y0, wc, hc, "código · a fechadura", label_fill=ACCENT)
    b += txt(x0 + wc / 2, y0 + 140, "pede pelo NOME", 32, INK,
             anchor="middle", weight="700")
    b += txt(x0 + wc / 2, y0 + 210, "CHAVE_PAGAMENTO", 28, SECONDARY,
             anchor="middle")
    b += txt(x0 + wc / 2, y0 + 280, "todo mundo pode ver", 24, MUTED,
             anchor="middle")
    b += txt(x0 + wc / 2, y0 + 330, "vai para o repo", 24, MUTED,
             anchor="middle")

    x1 = x0 + wc + gap
    b += card(x1, y0, wc, hc, "ambiente · o quadro de chaves")
    b += txt(x1 + wc / 2, y0 + 140, "guarda o VALOR", 32, INK,
             anchor="middle", weight="700")
    b += txt(x1 + wc / 2, y0 + 210, FAKE, 24, SECONDARY, anchor="middle")
    b += txt(x1 + wc / 2, y0 + 280, "só o dono acessa", 24, MUTED,
             anchor="middle")
    b += txt(x1 + wc / 2, y0 + 330, "nunca vai para o repo", 24, MUTED,
             anchor="middle")

    b += arrow(x0 + wc + 12, y0 + hc / 2, x1 - 12, y0 + hc / 2, INK, 3,
               "pede")

    b += caption(W / 2, 950,
                 "Os dois nunca viajam juntos.")
    export(b, f"{OUT}/12-regra-de-ouro", defs=glow_def("g1"))


if __name__ == "__main__":
    p01_chave_no_codigo()
    p02_o_que_e_segredo()
    p03_fechadura_e_chave()
    p04_fluxo_do_vazamento()
    p05_quatro_ambientes()
    p06_variavel_de_ambiente()
    p07_env_gitignore()
    p08_producao_painel()
    p09_tres_armadilhas()
    p10_como_pedir_certo()
    p11_protocolo_emergencia()
    p12_regra_de_ouro()
