#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pranchas do episódio 06 - Git e Versionamento.
Uma prancha por passagem visual do roteiro (seções "Mostrar").
Design system: Midnight Grid (ver midnight_kit.py).
"""

from midnight_kit import (W, H, INK, SECONDARY, MUTED, BORDER, ACCENT,
                          SURFACE, ELEVATED, ST_OPEN, ST_GUIDED, ST_RESTRICTED,
                          export, header, title, caption, txt, caps, line,
                          rrect, circle, path, glow, glow_def, arrow, card,
                          chip, xmark, check, dim_bracket_v)

OUT = "../../episodes/06-git-e-versionamento/pranchas"
KICKER = "EP 06 · Git e versionamento"
N = 12


def fig(n):
    return f"prancha {n:02d}/{N}"


# ---------------------------------------------------------------- 01
def p01_caos_manual():
    """ATO 1: antes do git, o versionamento manual e caótico."""
    b = header(KICKER, fig(1))
    b += title(W / 2, 230, "Antes do git: versionar na mão")
    # pasta com arquivos nomeados caoticamente
    b += rrect(170, 316, 240, 44, 10, fill=ELEVATED, stroke=BORDER, sw=2)
    b += caps(290, 345, "projeto", 18, SECONDARY, anchor="middle")
    b += card(170, 360, 780, 480)
    arquivos = ["app.js", "app_v2.js", "app_final.js",
                "app_final_agora_vai.js", "app_velho_nao_apagar.js"]
    b += glow(560, 672, 240, "g1")
    for i, nome in enumerate(arquivos):
        y = 448 + i * 76
        destaque = (i == 3)
        b += rrect(230, y - 34, 30, 40, 6, fill=SURFACE,
                   stroke=ACCENT if destaque else BORDER, sw=2)
        b += txt(292, y, nome, 32 if destaque else 29,
                 ACCENT if destaque else SECONDARY,
                 weight="700" if destaque else "400")
    # as perguntas sem resposta
    b += caps(1090, 420, "quatro perguntas sem resposta", 22, SECONDARY)
    perguntas = ["o que mudou entre as versões?", "quem mudou?",
                 "quando quebrou?", "por que mudou?"]
    for i, q in enumerate(perguntas):
        y = 510 + i * 82
        b += xmark(1115, y - 9, 13, ST_RESTRICTED, 3.5)
        b += txt(1158, y, q, 29, SECONDARY)
    b += caption(W / 2, 950,
                 "Funciona para um arquivo. Para um projeto inteiro, vira caos.")
    export(b, f"{OUT}/01-o-caos-manual", defs=glow_def("g1"))


# ---------------------------------------------------------------- 02
def p02_commit_a_foto():
    """ATO 1: o commit como foto polaroid — mensagem, autor, data, id, imutável."""
    b = header(KICKER, fig(2))
    b += title(W / 2, 230, "Commit: a foto do código")
    # polaroid
    b += glow(560, 590, 320, "g1")
    b += rrect(280, 340, 560, 500, 14, fill=ELEVATED, stroke=BORDER, sw=2)
    b += rrect(320, 380, 480, 330, 10, fill=SURFACE, stroke=BORDER, sw=2)
    # linhas de código dentro da foto
    larguras = [300, 380, 220, 340, 260, 400, 180]
    for i, lw in enumerate(larguras):
        y = 425 + i * 40
        b += rrect(360, y, lw, 10, 5, fill=MUTED, stroke="none", sw=0,
                   opacity=0.55)
    b += txt(560, 782, "“adiciona tela de login”", 27, SECONDARY,
             anchor="middle", italic=True)
    # metadados da foto
    b += caps(980, 400, "toda foto registra", 22, SECONDARY)
    meta = [("mensagem", "o que mudou, escrito por você"),
            ("autor", "quem tirou a foto"),
            ("data", "quando a foto foi tirada"),
            ("identificador", "o número de série, único")]
    for i, (k, v) in enumerate(meta):
        y = 478 + i * 76
        b += caps(980, y, k, 22, INK)
        b += txt(1310, y, v, 27, SECONDARY)
    b += line(980, 792, 1790, 792, BORDER, 2)
    b += chip(1090, 858, "imutável", ACCENT)
    b += txt(1230, 866, "depois de tirada, a foto não muda", 26, SECONDARY)
    b += caption(W / 2, 968,
                 "Ficou ruim? Tira uma foto nova. A antiga continua no álbum.")
    export(b, f"{OUT}/02-commit-a-foto", defs=glow_def("g1"))


# ---------------------------------------------------------------- 03
def p03_repo_o_album():
    """ATO 1: o repo como álbum — cópia local e cópia remota."""
    b = header(KICKER, fig(3))
    b += title(W / 2, 230, "Repo: o álbum onde as fotos moram")
    y0, hc, wc = 400, 360, 640
    # repo local
    b += card(160, y0, wc, hc, "repo local · no seu computador")
    b += line(260, y0 + 180, 700, y0 + 180, BORDER, 2)
    for x in (300, 430, 560, 690):
        b += circle(x, y0 + 180, 17, fill=SURFACE, stroke=INK, sw=3)
    b += txt(480, y0 + 280, "todos os commits, em ordem", 24, SECONDARY,
             anchor="middle")
    # repo remoto
    b += glow(1440, y0 + 180, 320, "g1")
    b += card(1120, y0, wc, hc, "repo remoto · na nuvem", label_fill=ACCENT)
    b += line(1220, y0 + 180, 1660, y0 + 180, BORDER, 2)
    for x in (1260, 1390, 1520, 1650):
        b += circle(x, y0 + 180, 17, fill=SURFACE, stroke=INK, sw=3)
    b += txt(1440, y0 + 280, "a cópia que o time inteiro acessa", 24,
             SECONDARY, anchor="middle")
    b += arrow(820, y0 + 180, 1100, y0 + 180, INK, 3, "o código viaja")
    b += txt(W / 2, 855,
             "A mesma linha do tempo, em dois lugares: sua máquina e um servidor.",
             28, SECONDARY, anchor="middle")
    b += caption(W / 2, 960,
                 "A plataforma muda de nome; o conceito é um só.")
    export(b, f"{OUT}/03-repo-o-album", defs=glow_def("g1"))


# ---------------------------------------------------------------- 04
def p04_rede_basica():
    """ATO 1: só commit + repo já são a rede de segurança básica."""
    b = header(KICKER, fig(4))
    b += title(W / 2, 230, "Só com isso, a rede de segurança básica")
    cols = [("Quebrou algo?", "volta para a foto anterior"),
            ("O que mudou?", "compara duas fotos"),
            ("Quem fez isso?", "olha o autor e a data")]
    wc, hc, gap = 480, 340, 80
    x0 = (W - 3 * wc - 2 * gap) / 2
    y0 = 360
    b += glow(x0 + wc / 2, y0 + hc / 2, 300, "g1")
    for i, (pergunta, resposta) in enumerate(cols):
        x = x0 + i * (wc + gap)
        b += card(x, y0, wc, hc)
        b += txt(x + wc / 2, y0 + 140, pergunta, 40,
                 ACCENT if i == 0 else INK, anchor="middle", weight="800",
                 spacing=-1.0)
        b += txt(x + wc / 2, y0 + 225, resposta, 27, SECONDARY,
                 anchor="middle")
    b += txt(W / 2, 820, "Isso já resolve 80% do problema.", 30, SECONDARY,
             anchor="middle")
    b += caption(W / 2, 950,
                 "Falta uma coisa: testar algo arriscado sem estragar a linha principal.")
    export(b, f"{OUT}/04-rede-de-seguranca-basica", defs=glow_def("g1"))


# ---------------------------------------------------------------- 05
def p05_branch_o_ramal():
    """ATO 2: main no centro, vários ramais nomeados saindo dela."""
    b = header(KICKER, fig(5))
    b += title(W / 2, 230, "Branch: um ramal para cada trabalho")
    yM = 600
    b += glow(420, yM, 260, "g1")
    # main em destaque (o acento da prancha)
    b += arrow(200, yM, 1730, yM, ACCENT, 4)
    for x in (320, 560, 800, 1040, 1280, 1520):
        b += circle(x, yM, 14, fill=SURFACE, stroke=ACCENT, sw=3)
    b += caps(200, yM + 74, "main · a versão oficial · o que o deploy usa",
              20, ACCENT)
    # ramal 1 (para cima)
    b += path(f"M440 {yM} C 480 {yM-100}, 500 {yM-170}, 560 {yM-170} "
              f"L 900 {yM-170}", stroke=SECONDARY, w=3)
    for x in (660, 800):
        b += circle(x, yM - 170, 12, fill=SURFACE, stroke=SECONDARY, sw=3)
    b += caps(730, yM - 210, "feature-login", 19, SECONDARY, anchor="middle")
    # ramal 2 (mais alto)
    b += path(f"M860 {yM} C 900 {yM-140}, 920 {yM-270}, 980 {yM-270} "
              f"L 1320 {yM-270}", stroke=SECONDARY, w=3)
    for x in (1080, 1220):
        b += circle(x, yM - 270, 12, fill=SURFACE, stroke=SECONDARY, sw=3)
    b += caps(1150, yM - 310, "fix-bug-123", 19, SECONDARY, anchor="middle")
    # ramal 3 (para baixo)
    b += path(f"M1100 {yM} C 1140 {yM+90}, 1160 {yM+160}, 1220 {yM+160} "
              f"L 1560 {yM+160}", stroke=SECONDARY, w=3)
    for x in (1320, 1460):
        b += circle(x, yM + 160, 12, fill=SURFACE, stroke=SECONDARY, sw=3)
    b += caps(1390, yM + 215, "experimento-novo-layout", 19, SECONDARY,
              anchor="middle")
    b += caption(W / 2, 950,
                 "A main fica intocada enquanto cada ramal experimenta.")
    export(b, f"{OUT}/05-branch-o-ramal", defs=glow_def("g1"))


# ---------------------------------------------------------------- 06
def p06_merge_confluencia():
    """ATO 2: merge como confluência de rios."""
    b = header(KICKER, fig(6))
    b += title(W / 2, 230, "Merge: a confluência dos rios")
    yM = 620
    # main antes do merge
    b += line(220, yM, 1120, yM, INK, 3)
    for x in (340, 540, 740):
        b += circle(x, yM, 14, fill=SURFACE, stroke=INK, sw=3)
    b += caps(300, yM + 70, "main", 20, SECONDARY)
    # branch que entrega as mudanças
    b += path(f"M420 {yM} C 470 {yM-100}, 500 {yM-180}, 560 {yM-180} "
              f"L 900 {yM-180} C 990 {yM-180}, 1040 {yM-60}, 1120 {yM}",
              stroke=SECONDARY, w=3)
    for x in (640, 800):
        b += circle(x, yM - 180, 12, fill=SURFACE, stroke=SECONDARY, sw=3)
    b += caps(720, yM - 225, "branch", 20, SECONDARY, anchor="middle")
    # o ponto de merge (o acento)
    b += glow(1120, yM, 280, "g1")
    b += circle(1120, yM, 20, fill=ELEVATED, stroke=ACCENT, sw=4)
    b += caps(1120, yM + 76, "merge", 24, ACCENT, anchor="middle")
    # main depois do merge: um rio só, mais forte
    b += arrow(1140, yM, 1720, yM, INK, 5)
    b += circle(1420, yM, 16, fill=SURFACE, stroke=INK, sw=3)
    b += caps(1440, yM - 60, "main com tudo da branch", 20, SECONDARY,
              anchor="middle")
    b += txt(W / 2, 850,
             "Depois do merge, a main tem tudo que estava na branch.",
             28, SECONDARY, anchor="middle")
    b += caption(W / 2, 955, "Dois rios se encontram e viram um só.")
    export(b, f"{OUT}/06-merge-a-confluencia", defs=glow_def("g1"))


# ---------------------------------------------------------------- 07
def p07_conflito():
    """ATO 2: conflito — marcadores no arquivo e resolução manual."""
    b = header(KICKER, fig(7))
    b += title(W / 2, 230, "Conflito: o git não decide sozinho")
    # o arquivo marcado
    b += glow(590, 590, 320, "g1")
    b += card(150, 330, 880, 520)
    b += caps(590, 384, "um arquivo · duas mudanças no mesmo lugar", 19,
              SECONDARY, anchor="middle")
    linhas = [("função de login:", SECONDARY, "400"),
              ("<<<<<<< sua versão", ST_RESTRICTED, "700"),
              ("botão azul, texto “Entrar”", INK, "400"),
              ("=======", ST_RESTRICTED, "700"),
              ("botão verde, texto “Acessar”", INK, "400"),
              (">>>>>>> versão do colega", ST_RESTRICTED, "700")]
    for i, (s, cor, peso) in enumerate(linhas):
        b += txt(220, 452 + i * 52, s, 28, cor, weight=peso)
    b += txt(220, 792, "o git parou aqui e marcou o arquivo", 24, MUTED,
             italic=True)
    # como resolver
    b += caps(1120, 420, "resolver é manual", 22, ACCENT)
    b += check(1145, 502, 16, ST_OPEN, 4)
    b += txt(1192, 512, "abrir, ler as duas versões,", 28, SECONDARY)
    b += txt(1192, 550, "decidir e apagar as marcas", 28, SECONDARY)
    b += xmark(1145, 646, 16, ST_RESTRICTED, 4)
    b += txt(1192, 656, "aceitar “resolvido” da IA", 28, SECONDARY)
    b += txt(1192, 694, "sem olhar o arquivo", 28, SECONDARY)
    b += txt(1120, 792, "Conflito mal resolvido é bug silencioso.", 26,
             MUTED, italic=True)
    b += caption(W / 2, 950, "Conflito bem resolvido é coisa de humano.")
    export(b, f"{OUT}/07-conflito", defs=glow_def("g1"))


# ---------------------------------------------------------------- 08
def p08_pull_request():
    """ATO 3: o PR como sala de revisão — diff, arquivos, comentários."""
    b = header(KICKER, fig(8))
    b += title(W / 2, 230, "Pull request: a sala de revisão")
    # a janela do PR
    b += card(260, 320, 1400, 540)
    b += txt(320, 398, "Adicionar tela de login", 34, INK, weight="700")
    b += glow(1480, 388, 200, "g1")
    b += chip(1480, 388, "pull request", ACCENT)
    b += line(320, 438, 1600, 438, BORDER, 2)
    # coluna do diff
    b += caps(320, 492, "diff · linha por linha", 18, SECONDARY)
    b += txt(320, 552, "−  botão sem verificação de senha", 26, MUTED)
    b += txt(320, 604, "+  verifica a senha antes de entrar", 26, INK)
    b += txt(320, 656, "+  mensagem de erro clara", 26, INK)
    b += caps(320, 744, "3 arquivos modificados · 2 commits", 18, MUTED)
    # coluna dos comentários
    b += rrect(1020, 466, 580, 140, 12, fill=ELEVATED, stroke=BORDER, sw=2)
    b += caps(1050, 504, "comentário do revisor", 16, SECONDARY)
    b += txt(1050, 556, "“por que você fez assim?”", 25, INK, italic=True)
    b += rrect(1020, 636, 580, 140, 12, fill=ELEVATED, stroke=BORDER, sw=2)
    b += caps(1050, 674, "resposta", 16, SECONDARY)
    b += txt(1050, 726, "“a antiga deixava passar senha vazia.”", 25, INK,
             italic=True)
    b += caption(W / 2, 950,
                 "“Tenho uma branch pronta. Olha o que mudei. Posso juntar na main?”")
    export(b, f"{OUT}/08-pull-request", defs=glow_def("g1"))


# ---------------------------------------------------------------- 09
def p09_review_o_portao():
    """ATO 3: review — o portão entre 'eu fiz' e 'está na main'."""
    b = header(KICKER, fig(9))
    b += title(W / 2, 230, "Review: o portão antes da main")
    y0 = 430
    # eu fiz
    b += card(170, y0, 420, 300, "eu fiz")
    b += txt(380, y0 + 140, "branch pronta,", 26, SECONDARY, anchor="middle")
    b += txt(380, y0 + 178, "commits feitos", 26, SECONDARY, anchor="middle")
    # o portão
    b += glow(960, 560, 300, "g1")
    b += rrect(770, 340, 380, 56, 10, fill=ELEVATED, stroke=BORDER, sw=2)
    b += caps(960, 376, "review", 22, ACCENT, anchor="middle")
    b += rrect(800, 396, 26, 360, 6, fill=ELEVATED, stroke=BORDER, sw=2)
    b += rrect(1094, 396, 26, 360, 6, fill=ELEVATED, stroke=BORDER, sw=2)
    acoes = ["lê o diff", "pergunta por quê", "sugere melhoria",
             "aponta riscos"]
    for i, s in enumerate(acoes):
        b += txt(960, 486 + i * 70, s, 23, SECONDARY, anchor="middle")
    # está na main
    b += card(1330, y0, 420, 300, "na main")
    b += check(1440, y0 + 132, 16, ST_OPEN, 4)
    b += txt(1478, y0 + 140, "revisado,", 26, SECONDARY)
    b += txt(1478, y0 + 178, "sem surpresa", 26, SECONDARY)
    # fluxo
    b += arrow(602, 580, 788, 580, INK, 3)
    b += arrow(1132, 580, 1318, 580, INK, 3, "aprovado")
    b += arrow(940, 830, 500, 830, SECONDARY, 2.5,
               "mudanças pedidas · volta e ajusta", dash="10 8")
    b += caption(W / 2, 955,
                 "Entre “eu fiz” e “está na main”, sempre um segundo par de olhos.")
    export(b, f"{OUT}/09-review-o-portao", defs=glow_def("g1"))


# ---------------------------------------------------------------- 10
def p10_fluxo_completo():
    """ATO 3: o fluxo completo — a esteira em seis passos."""
    b = header(KICKER, fig(10))
    b += title(W / 2, 230, "O fluxo completo, sempre nessa ordem")
    steps = [("branch nova", "a partir da main"),
             ("commit", "fotos na branch"),
             ("push", "manda para a nuvem"),
             ("PR", "pedido com diff"),
             ("review", "alguém aprova"),
             ("merge", "entra na main")]
    wc, gap = 262, 36
    x0 = (W - 6 * wc - 5 * gap) / 2
    y0 = 430
    b += glow(x0 + 5 * (wc + gap) + wc / 2, y0 + 100, 240, "g1")
    for i, (nome, sub) in enumerate(steps):
        x = x0 + i * (wc + gap)
        b += card(x, y0, wc, 200)
        b += txt(x + wc / 2, y0 + 66, str(i + 1), 30,
                 ACCENT if i == 5 else MUTED, anchor="middle", weight="800")
        b += txt(x + wc / 2, y0 + 118, nome, 26, INK, anchor="middle",
                 weight="700")
        b += txt(x + wc / 2, y0 + 158, sub, 19, SECONDARY, anchor="middle")
        if i < 5:
            b += arrow(x + wc + 5, y0 + 100, x + wc + gap - 5, y0 + 100,
                       SECONDARY, 2.5)
    b += txt(W / 2, 770,
             "Dez pessoas, dez branches — todas convergem na main pelo mesmo portão.",
             28, SECONDARY, anchor="middle")
    b += caption(W / 2, 950,
                 "Esse é o coração do trabalho profissional com código.")
    export(b, f"{OUT}/10-fluxo-completo", defs=glow_def("g1"))


# ---------------------------------------------------------------- 11
def p11_deploy_usa_o_repo():
    """ATO 3: o deploy pega a main do repo, nunca a sua máquina."""
    b = header(KICKER, fig(11))
    b += title(W / 2, 230, "O deploy usa o repo, não seu computador")
    # seu computador
    b += card(150, 380, 470, 340, "seu computador")
    itens = ["só você vê", "desliga, dorme", "o time não alcança"]
    for i, s in enumerate(itens):
        y = 508 + i * 70
        b += xmark(230, y - 8, 13, ST_RESTRICTED, 3.5)
        b += txt(268, y, s, 27, SECONDARY)
    # o repo, ponto de verdade
    b += glow(1005, 550, 300, "g1")
    b += card(770, 360, 470, 380, "repo · main", label_fill=ACCENT)
    b += line(870, 560, 1140, 560, BORDER, 2)
    for x in (880, 1005, 1130):
        b += circle(x, 560, 16, fill=SURFACE, stroke=INK, sw=3)
    b += caps(1005, 668, "ponto de verdade", 20, SECONDARY, anchor="middle")
    # no ar
    b += card(1400, 430, 370, 240, "no ar")
    b += txt(1585, 548, "o site que", 26, SECONDARY, anchor="middle")
    b += txt(1585, 586, "todos usam", 26, SECONDARY, anchor="middle")
    # caminhos
    b += arrow(622, 550, 750, 550, INK, 3, "push")
    b += arrow(1260, 550, 1380, 550, INK, 3, "deploy")
    # o caminho que não existe
    b += path("M 385 722 C 385 852, 1585 852, 1585 672", stroke=MUTED, w=2.5,
              dash="10 8")
    b += xmark(985, 815, 18, ST_RESTRICTED, 4)
    b += caps(985, 890, "o deploy nunca olha aqui", 18, MUTED,
              anchor="middle")
    b += caption(W / 2, 962,
                 "Sem push, seu código não existe para o resto do mundo.")
    export(b, f"{OUT}/11-deploy-usa-o-repo", defs=glow_def("g1"))


# ---------------------------------------------------------------- 12
def p12_a_rede_inteira():
    """Encerramento: o mapa completo — a rede de segurança inteira."""
    b = header(KICKER, fig(12))
    b += title(W / 2, 230, "A rede de segurança inteira")
    yM = 640
    # main
    b += line(180, yM, 1450, yM, INK, 3)
    for x in (300, 460, 1400):
        b += circle(x, yM, 13, fill=SURFACE, stroke=INK, sw=3)
    b += caps(240, yM + 64, "main", 18, SECONDARY)
    # branch com commits
    b += path(f"M560 {yM} C 610 {yM-90}, 640 {yM-170}, 700 {yM-170} "
              f"L 1060 {yM-170}", stroke=SECONDARY, w=3)
    for x in (800, 960):
        b += circle(x, yM - 170, 11, fill=SURFACE, stroke=SECONDARY, sw=3)
    b += caps(700, yM - 205, "branch", 16, SECONDARY)
    # push para o repo remoto
    b += arrow(880, yM - 200, 880, yM - 300, SECONDARY, 2.5)
    b += caps(908, yM - 250, "push", 16, SECONDARY)
    b += chip(880, yM - 336, "repo remoto", SECONDARY)
    # o portão de PR e review
    b += glow(1150, yM - 170, 260, "g1")
    b += rrect(1060, yM - 226, 180, 112, 12, fill=ELEVATED, stroke=BORDER,
               sw=2)
    b += caps(1150, yM - 182, "pr · review", 16, ACCENT, anchor="middle")
    # a branch entra na main
    b += path(f"M1240 {yM-170} C 1300 {yM-170}, 1320 {yM}, 1380 {yM}",
              stroke=SECONDARY, w=3)
    b += caps(1400, yM + 64, "merge", 18, SECONDARY, anchor="middle")
    # a main segue para o deploy
    b += arrow(1450, yM, 1700, yM, INK, 3)
    b += caps(1620, yM + 64, "para o deploy", 16, SECONDARY, anchor="middle")
    b += txt(W / 2, 850,
             "commit é a foto · branch é o ramal · PR e review são o portão · merge é a confluência",
             26, SECONDARY, anchor="middle")
    b += caption(W / 2, 955,
                 "Código novo chega na main de forma controlada, revisada, sem surpresa.")
    export(b, f"{OUT}/12-a-rede-inteira", defs=glow_def("g1"))


if __name__ == "__main__":
    p01_caos_manual()
    p02_commit_a_foto()
    p03_repo_o_album()
    p04_rede_basica()
    p05_branch_o_ramal()
    p06_merge_confluencia()
    p07_conflito()
    p08_pull_request()
    p09_review_o_portao()
    p10_fluxo_completo()
    p11_deploy_usa_o_repo()
    p12_a_rede_inteira()
