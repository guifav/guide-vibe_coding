#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pranchas do episódio 05 - Auth e Sessão.
Uma prancha por passagem visual do roteiro (seções "Mostrar").
Design system: Midnight Grid (ver midnight_kit.py).
"""

from midnight_kit import (W, H, INK, SECONDARY, MUTED, BORDER, ACCENT,
                          SURFACE, ELEVATED, ST_OPEN, ST_GUIDED, ST_RESTRICTED,
                          export, header, title, caption, txt, caps, line,
                          rrect, circle, path, glow, glow_def, arrow, card,
                          chip, xmark, check)

OUT = "../../episodes/05-auth-e-sessao/pranchas"
KICKER = "EP 05 · Auth e sessão"
N = 12


def fig(n):
    return f"prancha {n:02d}/{N}"


# ---------------------------------------------------------------- 01
def p01_mundo_sem_auth():
    """ATO 1: servidor sem auth — qualquer um pede, tudo responde."""
    b = header(KICKER, fig(1))
    b += title(W / 2, 230, "Mundo sem auth: todo mundo é admin")
    y0, hc = 360, 400
    # visitantes anônimos
    b += card(140, y0, 520, hc, "visitantes anônimos")
    pedidos = [("lista de usuários", 140), ("perfil de outra pessoa", 220),
               ("apagar dado alheio", 300)]
    for s, dy in pedidos:
        b += circle(210, y0 + dy - 8, 10, fill=MUTED, stroke=MUTED, sw=1)
        b += txt(250, y0 + dy, s, 26, SECONDARY)
    # setas
    b += arrow(680, y0 + hc / 2, 900, y0 + hc / 2, INK, 3, "request")
    # servidor sem filtro
    b += glow(1360, y0 + hc / 2, 320, "g1")
    b += card(920, y0, 860, hc, "servidor · sem auth", label_fill=ACCENT)
    b += txt(1350, y0 + 160, "responde igual para todos", 30, INK,
             anchor="middle", weight="700")
    b += txt(1350, y0 + 230, "sem filtro · sem discriminação", 26, SECONDARY,
             anchor="middle")
    b += txt(1350, y0 + 290, "privacidade zero · alteração livre", 26,
             SECONDARY, anchor="middle")
    b += caption(W / 2, 950,
                 "Sem camada de controle, quem chega primeiro manda.")
    export(b, f"{OUT}/01-mundo-sem-auth", defs=glow_def("g1"))


# ---------------------------------------------------------------- 02
def p02_login():
    """ATO 1: login transforma visitante em usuário."""
    b = header(KICKER, fig(2))
    b += title(W / 2, 230, "Login: de visitante a alguém específico")
    wc, hc, gap = 620, 380, 200
    x0 = (W - 2 * wc - gap) / 2
    y0 = 360
    b += card(x0, y0, wc, hc, "antes · visitante")
    b += txt(x0 + wc / 2, y0 + 170, "sem nome", 40, MUTED, anchor="middle",
             weight="700")
    b += txt(x0 + wc / 2, y0 + 240, "estranho para o servidor", 26, SECONDARY,
             anchor="middle")
    b += glow(x0 + wc + gap + wc / 2, y0 + hc / 2, 300, "g1")
    x1 = x0 + wc + gap
    b += card(x1, y0, wc, hc, "depois · usuário", label_fill=ACCENT)
    b += txt(x1 + wc / 2, y0 + 170, "tem um nome", 40, INK, anchor="middle",
             weight="700")
    b += txt(x1 + wc / 2, y0 + 240, "histórico · permissões · dados seus", 26,
             SECONDARY, anchor="middle")
    b += arrow(x0 + wc + 16, y0 + hc / 2, x1 - 16, y0 + hc / 2, INK, 3,
               "login")
    b += caption(W / 2, 950,
                 "Login é se identificar e provar quem você é.")
    export(b, f"{OUT}/02-login", defs=glow_def("g1"))


# ---------------------------------------------------------------- 03
def p03_senha_e_hash():
    """ATO 1: senha digitada vira hash e é comparada."""
    b = header(KICKER, fig(3))
    b += title(W / 2, 230, "Senha vira hash — e o servidor compara")
    steps = [
        ("senha digitada", "o que você digita"),
        ("hash", "embaralhamento sem volta"),
        ("hash guardado", "o que o servidor tem"),
        ("bate?", "login ok ou negado"),
    ]
    wc, gap = 360, 70
    x0 = (W - 4 * wc - 3 * gap) / 2
    y0 = 400
    b += glow(x0 + 1.5 * (wc + gap) + wc / 2, y0 + 120, 280, "g1")
    for i, (nome, desc) in enumerate(steps):
        x = x0 + i * (wc + gap)
        accent = (i == 1)
        b += card(x, y0, wc, 280, nome,
                  label_fill=ACCENT if accent else SECONDARY)
        b += txt(x + wc / 2, y0 + 170, desc, 24, SECONDARY, anchor="middle")
        if i < 3:
            b += arrow(x + wc + 8, y0 + 140, x + wc + gap - 8, y0 + 140,
                       SECONDARY, 2.5)
    b += txt(W / 2, 800, "O servidor não guarda a senha. Guarda o hash dela.",
             28, SECONDARY, anchor="middle")
    b += caption(W / 2, 950,
                 "Hash é embaralhamento que não tem volta.")
    export(b, f"{OUT}/03-senha-e-hash", defs=glow_def("g1"))


# ---------------------------------------------------------------- 04
def p04_http_sem_memoria():
    """ATO 2: HTTP trata cada request como o primeiro."""
    b = header(KICKER, fig(4))
    b += title(W / 2, 230, "HTTP não tem memória")
    y0 = 380
    # request 1
    b += card(160, y0, 480, 220, "request 1")
    b += txt(400, y0 + 140, "“eu fiz login”", 28, SECONDARY, anchor="middle")
    # request 2
    b += card(160, y0 + 280, 480, 220, "request 2")
    b += txt(400, y0 + 420, "outro pedido", 28, SECONDARY, anchor="middle")
    # servidor
    b += glow(1400, y0 + 260, 320, "g1")
    b += card(920, y0, 840, 500, "servidor", label_fill=ACCENT)
    b += txt(1340, y0 + 180, "“quem é você?”", 40, INK, anchor="middle",
             weight="800")
    b += txt(1340, y0 + 280, "responde e esquece", 28, SECONDARY,
             anchor="middle")
    b += txt(1340, y0 + 340, "próximo request: estranho de novo", 28,
             SECONDARY, anchor="middle")
    b += arrow(660, y0 + 110, 900, y0 + 110, INK, 2.5)
    b += arrow(660, y0 + 390, 900, y0 + 390, INK, 2.5)
    b += caption(W / 2, 950,
                 "Cada request é tratado como se fosse o primeiro.")
    export(b, f"{OUT}/04-http-sem-memoria", defs=glow_def("g1"))


# ---------------------------------------------------------------- 05
def p05_sessao():
    """ATO 2: sessão = guarda-volumes; cookie leva o bilhete."""
    b = header(KICKER, fig(5))
    b += title(W / 2, 230, "Sessão: o guarda-volumes do servidor")
    y0 = 380
    # navegador
    b += card(120, y0, 480, 420, "navegador")
    b += txt(360, y0 + 160, "guarda só o bilhete", 26, SECONDARY,
             anchor="middle")
    b += chip(360, y0 + 260, "session ID · cookie", SECONDARY, 18)
    b += txt(360, y0 + 350, "leva em cada request", 24, MUTED,
             anchor="middle")
    # setas
    b += arrow(620, y0 + 140, 820, y0 + 140, INK, 3, "login")
    b += arrow(820, y0 + 340, 620, y0 + 340, SECONDARY, 3, "cookie")
    # servidor
    b += glow(1360, y0 + 210, 300, "g1")
    b += card(840, y0, 940, 420, "servidor · memória da sessão",
              label_fill=ACCENT)
    b += txt(1310, y0 + 160, "guarda a identidade", 28, INK, anchor="middle",
             weight="700")
    b += txt(1310, y0 + 220, "ID · nome · permissões", 26, SECONDARY,
             anchor="middle")
    b += txt(1310, y0 + 300, "consulta o bilhete → sabe quem é", 26,
             SECONDARY, anchor="middle")
    b += caption(W / 2, 960,
                 "A memória mora no servidor. O navegador só carrega o ID.")
    export(b, f"{OUT}/05-sessao", defs=glow_def("g1"))


# ---------------------------------------------------------------- 06
def p06_token():
    """ATO 2: token = crachá assinado que o cliente carrega."""
    b = header(KICKER, fig(6))
    b += title(W / 2, 230, "Token: o crachá que você carrega")
    y0 = 380
    # servidor gera
    b += card(120, y0, 520, 420, "servidor")
    b += txt(380, y0 + 160, "gera o crachá", 28, SECONDARY, anchor="middle")
    b += txt(380, y0 + 220, "assinatura só dele", 26, SECONDARY,
             anchor="middle")
    b += txt(380, y0 + 300, "não guarda sessão", 26, MUTED, anchor="middle")
    b += arrow(660, y0 + 210, 860, y0 + 210, INK, 3)
    # crachá no centro
    b += glow(1060, y0 + 210, 260, "g1")
    b += card(880, y0 + 40, 360, 340, None, elevated=True)
    b += caps(1060, y0 + 110, "token", 28, ACCENT, anchor="middle")
    b += txt(1060, y0 + 200, "quem você é", 26, INK, anchor="middle",
             weight="700")
    b += txt(1060, y0 + 260, "dentro do crachá", 24, SECONDARY,
             anchor="middle")
    b += arrow(1260, y0 + 210, 1460, y0 + 210, INK, 3)
    # navegador
    b += card(1480, y0, 320, 420, "navegador")
    b += txt(1640, y0 + 200, "guarda e envia", 26, SECONDARY, anchor="middle")
    b += txt(1640, y0 + 260, "em cada request", 26, SECONDARY, anchor="middle")
    b += caption(W / 2, 960,
                 "Ler, qualquer um lê. Forjar a assinatura, não.")
    export(b, f"{OUT}/06-token", defs=glow_def("g1"))


# ---------------------------------------------------------------- 07
def p07_sessao_vs_token():
    """ATO 2: onde a memória mora — sessão vs token."""
    b = header(KICKER, fig(7))
    b += title(W / 2, 230, "Sessão vs token: onde a memória mora")
    wc, hc, gap = 720, 420, 120
    x0 = (W - 2 * wc - gap) / 2
    y0 = 350
    b += glow(x0 + wc / 2, y0 + hc / 2, 300, "g1")
    # sessão
    b += card(x0, y0, wc, hc, "sessão", label_fill=ACCENT)
    linhas_s = [("memória no servidor", 140),
                ("navegador leva o bilhete", 210),
                ("dá para invalidar na hora", 280),
                ("simples de controlar", 350)]
    for s, dy in linhas_s:
        b += txt(x0 + wc / 2, y0 + dy, s, 28, SECONDARY, anchor="middle")
    # token
    x1 = x0 + wc + gap
    b += card(x1, y0, wc, hc, "token")
    linhas_t = [("memória no cliente", 140),
                ("crachá carrega a identidade", 210),
                ("bom com vários servidores", 280),
                ("servidor só precisa ler", 350)]
    for s, dy in linhas_t:
        b += txt(x1 + wc / 2, y0 + dy, s, 28, SECONDARY, anchor="middle")
    b += caption(W / 2, 950,
                 "Os dois resolvem o mesmo problema: lembrar entre requests.")
    export(b, f"{OUT}/07-sessao-vs-token", defs=glow_def("g1"))


# ---------------------------------------------------------------- 08
def p08_autenticacao_vs_autorizacao():
    """ATO 3: as duas perguntas de auth."""
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
    b += txt(x0 + wc / 2, y0 + 260, "login · senha · token · sessão", 26,
             SECONDARY, anchor="middle")
    x1 = x0 + wc + gap
    b += card(x1, y0, wc, hc)
    b += caps(x1 + wc / 2, y0 + 70, "autorização", 24, SECONDARY,
              anchor="middle")
    b += txt(x1 + wc / 2, y0 + 180, "O que você pode?", 44, INK,
             anchor="middle", weight="800")
    b += txt(x1 + wc / 2, y0 + 260, "papel · recurso · permitido ou negado", 26,
             SECONDARY, anchor="middle")
    b += arrow(x0 + wc + 14, y0 + hc / 2, x1 - 14, y0 + hc / 2, INK, 3)
    b += caption(W / 2, 950,
                 "Autenticado não é autorizado a tudo.")
    export(b, f"{OUT}/08-autenticacao-vs-autorizacao", defs=glow_def("g1"))


# ---------------------------------------------------------------- 09
def p09_permissoes_por_papel():
    """ATO 3: RBAC — admin / user / guest com escala ordenada."""
    b = header(KICKER, fig(9))
    b += title(W / 2, 230, "Permissão por papel")
    # cabeçalhos de ação
    acoes = ["ver", "editar", "apagar", "gerenciar"]
    papeis = [
        ("admin", ST_OPEN, [True, True, True, True]),
        ("user", ST_GUIDED, [True, True, False, False]),
        ("guest", ST_RESTRICTED, [True, False, False, False]),
    ]
    # tabela
    col_w = 220
    row_h = 110
    x_label = 280
    x0 = 520
    y0 = 360
    b += glow(W / 2, 620, 340, "g1")
    for j, a in enumerate(acoes):
        b += caps(x0 + j * col_w + col_w / 2, y0, a, 22, SECONDARY,
                  anchor="middle")
    for i, (papel, cor, perms) in enumerate(papeis):
        y = y0 + 50 + i * row_h
        b += chip(x_label, y + 40, papel, cor, 20)
        for j, ok in enumerate(perms):
            cx = x0 + j * col_w + col_w / 2
            cy = y + 40
            if ok:
                b += check(cx, cy, 18, ST_OPEN, 4)
            else:
                b += xmark(cx, cy, 16, ST_RESTRICTED, 3.5)
    b += txt(W / 2, 820, "Papel é um grupo com um conjunto de permissões.",
             28, SECONDARY, anchor="middle")
    b += caption(W / 2, 950,
                 "Admin pode tudo. User o que é dele. Guest só o público.")
    export(b, f"{OUT}/09-permissoes-por-papel", defs=glow_def("g1"))


# ---------------------------------------------------------------- 10
def p10_permissao_por_recurso():
    """ATO 3: ownership — esse item é seu?"""
    b = header(KICKER, fig(10))
    b += title(W / 2, 230, "Permissão por recurso: esse item é seu?")
    y0 = 370
    # user A
    b += card(140, y0, 560, 400, "usuário A")
    b += rrect(220, y0 + 120, 400, 100, 12, fill=ELEVATED, stroke=ACCENT, sw=2)
    b += txt(420, y0 + 180, "comentário de A", 26, INK, anchor="middle",
             weight="600")
    b += check(280, y0 + 300, 18, ST_OPEN, 4)
    b += txt(320, y0 + 308, "pode editar o próprio", 24, SECONDARY)
    # user B
    b += card(1220, y0, 560, 400, "usuário B")
    b += rrect(1300, y0 + 120, 400, 100, 12, fill=ELEVATED, stroke=BORDER, sw=2)
    b += txt(1500, y0 + 180, "comentário de B", 26, INK, anchor="middle",
             weight="600")
    b += check(1360, y0 + 300, 18, ST_OPEN, 4)
    b += txt(1400, y0 + 308, "pode editar o próprio", 24, SECONDARY)
    # tentativa cruzada
    b += glow(960, y0 + 200, 220, "g1")
    b += arrow(720, y0 + 170, 1200, y0 + 170, ST_RESTRICTED, 3)
    b += xmark(960, y0 + 170, 28, ST_RESTRICTED, 5)
    b += caps(960, y0 + 250, "esse item não é seu", 22, ST_RESTRICTED,
              anchor="middle")
    b += caption(W / 2, 950,
                 "Mesmo papel, recurso alheio: bloqueado.")
    export(b, f"{OUT}/10-permissao-por-recurso", defs=glow_def("g1"))


# ---------------------------------------------------------------- 11
def p11_remover_auth_perigoso():
    """ATO 3: remover verificação de auth abre o servidor."""
    b = header(KICKER, fig(11))
    b += title(W / 2, 230, "Remover auth é abrir o servidor")
    y0 = 370
    # antes
    b += card(160, y0, 700, 420, "antes · protegido")
    b += check(280, y0 + 160, 20, ST_OPEN, 4)
    b += txt(330, y0 + 168, "verifica quem é", 28, SECONDARY)
    b += check(280, y0 + 240, 20, ST_OPEN, 4)
    b += txt(330, y0 + 248, "verifica o que pode", 28, SECONDARY)
    b += check(280, y0 + 320, 20, ST_OPEN, 4)
    b += txt(330, y0 + 328, "bloqueia o que não deve", 28, SECONDARY)
    # depois
    b += glow(1420, y0 + 210, 300, "g1")
    b += card(1060, y0, 700, 420, "depois · aberto", label_fill=ST_RESTRICTED)
    b += xmark(1180, y0 + 160, 18, ST_RESTRICTED, 4)
    b += txt(1230, y0 + 168, "verificação comentada", 28, SECONDARY)
    b += xmark(1180, y0 + 240, 18, ST_RESTRICTED, 4)
    b += txt(1230, y0 + 248, "protegido vira público", 28, SECONDARY)
    b += xmark(1180, y0 + 320, 18, ST_RESTRICTED, 4)
    b += txt(1230, y0 + 328, "qualquer um manda", 28, SECONDARY)
    b += arrow(880, y0 + 210, 1040, y0 + 210, ST_RESTRICTED, 3, "remove")
    b += caption(W / 2, 960,
                 "Pergunte: o que para de ser verificado se eu remover isso?")
    export(b, f"{OUT}/11-remover-auth-perigoso", defs=glow_def("g1"))


# ---------------------------------------------------------------- 12
def p12_logoff_expiracao_roubo():
    """ATO 3: o fim do crachá — logoff, expiração, roubo."""
    b = header(KICKER, fig(12))
    b += title(W / 2, 230, "Logoff, expiração e crachá roubado")
    cards = [
        ("logoff", "crachá destruído", "sessão apagada · token invalidado"),
        ("expiração", "prazo de validade", "sem prazo = risco eterno"),
        ("roubo", "alguém se passa por você", "servidor obedece o crachá"),
    ]
    wc, hc, gap = 520, 400, 60
    x0 = (W - 3 * wc - 2 * gap) / 2
    y0 = 350
    for i, (nome, l1, l2) in enumerate(cards):
        x = x0 + i * (wc + gap)
        if i == 0:
            b += glow(x + wc / 2, y0 + hc / 2, 260, "g1")
        b += card(x, y0, wc, hc, nome,
                  label_fill=ACCENT if i == 0 else SECONDARY)
        if i == 2:
            b += xmark(x + wc / 2, y0 + 160, 28, ST_RESTRICTED, 5)
        else:
            b += circle(x + wc / 2, y0 + 160, 28, fill=SURFACE,
                        stroke=ACCENT if i == 0 else MUTED, sw=3)
            if i == 1:
                b += line(x + wc / 2 - 22, y0 + 160, x + wc / 2 + 22, y0 + 160,
                          MUTED, 3)
        b += txt(x + wc / 2, y0 + 250, l1, 28, INK, anchor="middle",
                 weight="700")
        b += txt(x + wc / 2, y0 + 310, l2, 24, SECONDARY, anchor="middle")
    b += caption(W / 2, 950,
                 "Auth é um ciclo: login é o começo, logoff e expiração são o fim.")
    export(b, f"{OUT}/12-logoff-expiracao-roubo", defs=glow_def("g1"))


if __name__ == "__main__":
    p01_mundo_sem_auth()
    p02_login()
    p03_senha_e_hash()
    p04_http_sem_memoria()
    p05_sessao()
    p06_token()
    p07_sessao_vs_token()
    p08_autenticacao_vs_autorizacao()
    p09_permissoes_por_papel()
    p10_permissao_por_recurso()
    p11_remover_auth_perigoso()
    p12_logoff_expiracao_roubo()
