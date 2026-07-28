#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pranchas do episódio 04 - Banco de Dados.
Uma prancha por passagem visual do roteiro (seções "Mostrar").
Design system: Midnight Grid (ver midnight_kit.py).
"""

from midnight_kit import (W, H, INK, SECONDARY, MUTED, BORDER, ACCENT,
                          SURFACE, ELEVATED, ST_OPEN, ST_GUIDED, ST_RESTRICTED,
                          export, header, title, caption, txt, caps, line,
                          rrect, circle, path, glow, glow_def, arrow, card,
                          chip, xmark, check, dim_bracket_v)

OUT = "../../episodes/04-banco-de-dados/pranchas"
KICKER = "EP 04 · Banco de dados"
N = 11


def fig(n):
    return f"prancha {n:02d}/{N}"


# ---------------------------------------------------------------- 01
def p01_caminho_do_dado():
    """Abertura: o mapa de camadas, do clique ao banco."""
    b = header(KICKER, fig(1))
    b += title(W / 2, 230, "O caminho do dado: do clique ao banco")
    wc, hc, gap = 400, 300, 240
    x0, y0 = 120, 430
    b += caps(x0 + wc / 2, y0 - 44, "usuário clica ou digita", 20, SECONDARY,
              anchor="middle")
    # navegador
    b += card(x0, y0, wc, hc, "navegador · front")
    b += txt(x0 + wc / 2, y0 + 168, "estado da página", 25, SECONDARY,
             anchor="middle")
    b += txt(x0 + wc / 2, y0 + 206, "morre ao fechar", 25, SECONDARY,
             anchor="middle")
    # servidor
    x1 = x0 + wc + gap
    b += card(x1, y0, wc, hc, "servidor")
    b += txt(x1 + wc / 2, y0 + 168, "memória não confiável", 25, SECONDARY,
             anchor="middle")
    b += txt(x1 + wc / 2, y0 + 206, "pode reiniciar", 25, SECONDARY,
             anchor="middle")
    # banco
    x2 = x1 + wc + gap
    b += glow(x2 + wc / 2, y0 + hc / 2, 320, "g1")
    b += card(x2, y0, wc, hc, "banco de dados", label_fill=ACCENT)
    b += txt(x2 + wc / 2, y0 + 168, "dado persistente", 25, SECONDARY,
             anchor="middle")
    b += txt(x2 + wc / 2, y0 + 206, "sobrevive a tudo", 25, SECONDARY,
             anchor="middle")
    b += arrow(x0 + wc + 12, y0 + hc / 2, x1 - 12, y0 + hc / 2, INK, 3,
               "request")
    b += arrow(x1 + wc + 12, y0 + hc / 2, x2 - 12, y0 + hc / 2, INK, 3,
               "query")
    b += caption(W / 2, 950,
                 "Ao fim do episódio, você sabe o que quebra em cada pedaço.")
    export(b, f"{OUT}/01-caminho-do-dado", defs=glow_def("g1"))


# ---------------------------------------------------------------- 02
def p02_memoria_nao_confiavel():
    """ATO 1: três situações em que a memória do servidor falha."""
    b = header(KICKER, fig(2))
    b += title(W / 2, 230, "A memória do servidor não é confiável")
    cards = [("o processo reiniciou", "a memória foi junto", "o dado sumiu"),
             ("duas cópias no ar", "cada uma com a sua memória",
              "nada é compartilhado"),
             ("usuário na cópia B", "a cópia A não vê",
              "memórias separadas")]
    wc, hc, gap = 520, 380, 60
    x0 = (W - 3 * wc - 2 * gap) / 2
    y0 = 350
    for i, (label, l1, l2) in enumerate(cards):
        x = x0 + i * (wc + gap)
        b += card(x, y0, wc, hc, label)
        b += xmark(x + wc / 2, y0 + 150, 26, ST_RESTRICTED, 4.5)
        b += txt(x + wc / 2, y0 + 258, l1, 26, SECONDARY, anchor="middle")
        b += txt(x + wc / 2, y0 + 300, l2, 26, SECONDARY, anchor="middle")
    b += glow(W / 2, 850, 300, "g1")
    b += caps(W / 2, 858, "dado importante não pode morar aqui", 24, ACCENT,
              anchor="middle")
    b += caption(W / 2, 960,
                 "Ela dura enquanto o processo está no ar e ninguém mexeu.")
    export(b, f"{OUT}/02-memoria-nao-confiavel", defs=glow_def("g1"))


# ---------------------------------------------------------------- 03
def p03_o_que_morre_o_que_dura():
    """ATO 1: memória da página (morre) vs banco (dura)."""
    b = header(KICKER, fig(3))
    b += title(W / 2, 230, "O que morre e o que dura")
    wc, hc, gap = 720, 420, 120
    x0 = (W - 2 * wc - gap) / 2
    y0 = 350
    # memória da página
    b += card(x0, y0, wc, hc, "memória da página")
    itens = ["a cor do botão clicado", "o texto ainda não enviado",
             "o filtro aberto na tela"]
    for i, s in enumerate(itens):
        y = y0 + 150 + i * 66
        b += circle(x0 + 70, y - 9, 6, fill=MUTED, stroke="none", sw=0)
        b += txt(x0 + 106, y, s, 27, SECONDARY)
    b += caps(x0 + wc / 2, y0 + hc - 36, "morre ao fechar a aba", 19, MUTED,
              anchor="middle")
    # banco de dados
    x1 = x0 + wc + gap
    b += glow(x1 + wc / 2, y0 + hc / 2, 340, "g1")
    b += card(x1, y0, wc, hc, "banco de dados", label_fill=ACCENT)
    itens2 = ["usuários e contas", "pedidos e produtos",
              "mensagens e configurações"]
    for i, s in enumerate(itens2):
        y = y0 + 150 + i * 66
        b += circle(x1 + 70, y - 9, 6, fill=INK, stroke="none", sw=0)
        b += txt(x1 + 106, y, s, 27, SECONDARY)
    b += caps(x1 + wc / 2, y0 + hc - 36, "dura entre sessões e reinícios", 19,
              SECONDARY, anchor="middle")
    b += caption(W / 2, 950,
                 "Persistente: sobrevive ao request, à sessão e ao reinício.")
    export(b, f"{OUT}/03-o-que-morre-o-que-dura", defs=glow_def("g1"))


# ---------------------------------------------------------------- 04
def p04_dois_caminhos():
    """ATO 1: caminho A (só no front) vs caminho B (atravessa o servidor)."""
    b = header(KICKER, fig(4))
    b += title(W / 2, 230, "Dois caminhos depois do clique")
    wc, hc, gap = 280, 110, 62
    x0 = 110

    # caminho A: fica no front
    b += caps(x0, 400, "caminho A · fica no front", 24, SECONDARY)
    y1 = 430
    stepsA = ["clica", "variável no front", "tela atualiza", "fecha a aba"]
    for i, s in enumerate(stepsA):
        x = x0 + i * (wc + gap)
        b += card(x, y1, wc, hc)
        b += txt(x + wc / 2, y1 + 64, s, 24, INK, anchor="middle", weight="600")
        b += arrow(x + wc + 8, y1 + hc / 2, x + wc + gap - 8, y1 + hc / 2,
                   SECONDARY, 2.5)
    xr = x0 + 4 * (wc + gap) + 60
    b += xmark(xr, y1 + hc / 2 - 12, 22, ST_RESTRICTED, 4.5)
    b += caps(xr, y1 + hc / 2 + 52, "perdeu", 20, ST_RESTRICTED,
              anchor="middle")

    # caminho B: atravessa o servidor
    b += caps(x0, 680, "caminho B · atravessa o servidor", 24, ACCENT)
    y2 = 710
    stepsB = ["clica", "request ao servidor", "grava no banco"]
    for i, s in enumerate(stepsB):
        x = x0 + i * (wc + gap)
        if i == 2:
            b += glow(x + wc / 2, y2 + hc / 2, 240, "g1")
        b += card(x, y2, wc, hc)
        b += txt(x + wc / 2, y2 + 64, s, 24, INK, anchor="middle", weight="600")
        b += arrow(x + wc + 8, y2 + hc / 2, x + wc + gap - 8, y2 + hc / 2,
                   SECONDARY, 2.5)
    xr2 = x0 + 3 * (wc + gap) + 60
    b += check(xr2, y2 + hc / 2 - 12, 22, ST_OPEN, 4.5)
    b += caps(xr2, y2 + hc / 2 + 52, "dura", 20, ST_OPEN, anchor="middle")

    b += caption(W / 2, 950, "“Salvei.” Salvou onde: no front ou no banco?")
    export(b, f"{OUT}/04-dois-caminhos", defs=glow_def("g1"))


# ---------------------------------------------------------------- 05
def p05_tres_familias():
    """ATO 2: as três famílias de banco no conceito."""
    b = header(KICKER, fig(5))
    b += title(W / 2, 230, "As três famílias de banco")
    wc, hc, gap = 480, 440, 80
    x0 = (W - 3 * wc - 2 * gap) / 2
    y0 = 330
    b += glow(x0 + wc / 2, y0 + hc / 2, 300, "g1")

    # relacional: tabela
    x = x0
    b += card(x, y0, wc, hc)
    tx, ty, tw, th = x + 140, y0 + 70, 200, 130
    b += rrect(tx, ty, tw, th, 8, fill=ELEVATED, stroke=SECONDARY, sw=2)
    for i in (1, 2):
        b += line(tx, ty + i * th / 3, tx + tw, ty + i * th / 3, SECONDARY,
                  1.5, opacity=0.7)
        b += line(tx + i * tw / 3, ty, tx + i * tw / 3, ty + th, SECONDARY,
                  1.5, opacity=0.7)
    b += txt(x + wc / 2, y0 + 300, "relacional", 40, ACCENT, anchor="middle",
             weight="800", spacing=-1.0)
    b += txt(x + wc / 2, y0 + 356, "tabelas: linhas e colunas", 24, SECONDARY,
             anchor="middle")

    # documento: página com linhas
    x = x0 + wc + gap
    b += card(x, y0, wc, hc)
    dx, dy, dw, dh = x + 170, y0 + 60, 140, 150
    b += rrect(dx, dy, dw, dh, 8, fill=ELEVATED, stroke=SECONDARY, sw=2)
    for i in range(4):
        w_line = dw - 44 if i < 3 else dw - 90
        b += line(dx + 22, dy + 34 + i * 30, dx + 22 + w_line,
                  dy + 34 + i * 30, SECONDARY, 2, opacity=0.7)
    b += txt(x + wc / 2, y0 + 300, "documento", 40, INK, anchor="middle",
             weight="800", spacing=-1.0)
    b += txt(x + wc / 2, y0 + 356, "blocos soltos · JSON", 24, SECONDARY,
             anchor="middle")

    # chave-valor: pares
    x = x0 + 2 * (wc + gap)
    b += card(x, y0, wc, hc)
    for i, yy in enumerate((y0 + 90, y0 + 160)):
        b += rrect(x + 100, yy - 22, 110, 44, 9999, fill=ELEVATED,
                   stroke=SECONDARY, sw=1.5)
        b += caps(x + 155, yy + 6, "chave", 15, SECONDARY, anchor="middle")
        b += arrow(x + 222, yy, x + 268, yy, SECONDARY, 2)
        b += rrect(x + 280, yy - 22, 110, 44, 9999, fill=ELEVATED,
                   stroke=SECONDARY, sw=1.5)
        b += caps(x + 335, yy + 6, "valor", 15, SECONDARY, anchor="middle")
    b += txt(x + wc / 2, y0 + 300, "chave-valor", 40, INK, anchor="middle",
             weight="800", spacing=-1.0)
    b += txt(x + wc / 2, y0 + 356, "dicionário: direto e rápido", 24,
             SECONDARY, anchor="middle")

    b += caption(W / 2, 950,
                 "Três famílias bastam para entender o que a IA sugere.")
    export(b, f"{OUT}/05-tres-familias", defs=glow_def("g1"))


# ---------------------------------------------------------------- 06
def p06_query():
    """ATO 2: query é a pergunta, resultado é a resposta."""
    b = header(KICKER, fig(6))
    b += title(W / 2, 230, "Query: a pergunta que o servidor faz")
    y0 = 400
    b += card(240, y0, 480, 320, "servidor")
    b += txt(480, y0 + 175, "“quantos cadastros", 27, SECONDARY,
             anchor="middle")
    b += txt(480, y0 + 213, "temos hoje?”", 27, SECONDARY, anchor="middle")
    # banco como cilindro
    b += glow(1440, y0 + 160, 300, "g1")
    cx, cy = 1440, y0 + 160
    b += path(f"M{cx-190} {cy-120} a 190 46 0 0 0 380 0 l 0 240 "
              f"a 190 46 0 0 1 -380 0 Z", stroke=BORDER, w=2, fill=SURFACE)
    b += path(f"M{cx-190} {cy-120} a 190 46 0 0 0 380 0", stroke=ACCENT, w=2.5)
    b += caps(cx, cy + 20, "banco de dados", 22, ACCENT, anchor="middle")
    b += txt(cx, cy + 66, "responde só o que", 23, SECONDARY, anchor="middle")
    b += txt(cx, cy + 100, "foi perguntado", 23, SECONDARY, anchor="middle")
    b += arrow(740, y0 + 110, 1200, y0 + 110, INK, 3, "query · a pergunta")
    b += arrow(1200, y0 + 250, 740, y0 + 250, SECONDARY, 3,
               "resultado · a resposta")
    b += caption(W / 2, 950,
                 "Query errada, resposta errada. O banco não adivinha.")
    export(b, f"{OUT}/06-query", defs=glow_def("g1"))


# ---------------------------------------------------------------- 07
def p07_schema():
    """ATO 2: schema em tabela relacional e em documento."""
    b = header(KICKER, fig(7))
    b += title(W / 2, 230, "Schema: o contrato do dado")
    wc, hc, gap = 760, 440, 120
    x0 = (W - 2 * wc - gap) / 2
    y0 = 340

    # relacional: tabela com colunas e tipos
    b += glow(x0 + wc / 2, y0 + hc / 2, 340, "g1")
    b += card(x0, y0, wc, hc, "banco relacional · tabela", label_fill=ACCENT)
    cols = [("nome", "texto"), ("email", "texto"),
            ("nascimento", "data"), ("ativo", "sim · não")]
    tx, ty = x0 + 60, y0 + 110
    cw = (wc - 120) / 4
    for i, (nome, tipo) in enumerate(cols):
        cxc = tx + i * cw + cw / 2
        b += caps(cxc, ty + 40, nome, 16, INK, anchor="middle")
        b += txt(cxc, ty + 82, tipo, 21, SECONDARY, anchor="middle")
        if i > 0:
            b += line(tx + i * cw, ty + 10, tx + i * cw, ty + 250, BORDER, 1.5)
    b += line(tx, ty + 106, tx + wc - 120, ty + 106, SECONDARY, 2)
    for row in (1, 2):
        yy = ty + 106 + row * 72
        b += line(tx, yy, tx + wc - 120, yy, BORDER, 1.5)
        for i in range(4):
            b += line(tx + i * cw + 34, yy - 34, tx + (i + 1) * cw - 34,
                      yy - 34, MUTED, 2, opacity=0.5)

    # documento: formato esperado
    x1 = x0 + wc + gap
    b += card(x1, y0, wc, hc, "banco de documentos")
    linhas = [("{", 0), ("nome: texto,", 44), ("email: texto,", 44),
              ("nascimento: data,", 44), ("ativo: sim ou não", 44), ("}", 0)]
    for i, (s, indent) in enumerate(linhas):
        b += txt(x1 + 130 + indent, y0 + 130 + i * 44, s, 26, SECONDARY)
    b += caps(x1 + wc / 2, y0 + hc - 36, "formato esperado", 19, MUTED,
              anchor="middle")
    b += caption(W / 2, 950,
                 "O schema diz o que pode entrar. Isso protege o dado.")
    export(b, f"{OUT}/07-schema", defs=glow_def("g1"))


# ---------------------------------------------------------------- 08
def p08_quatro_riscos():
    """ATO 3: os quatro riscos mais comuns."""
    b = header(KICKER, fig(8))
    b += title(W / 2, 230, "Quatro riscos que o banco traz")
    riscos = [("duplicado", "o mesmo dado", "gravado duas vezes"),
              ("inconsistente", "certo num lugar,", "velho no outro"),
              ("perdido", "a tela diz salvo,", "o banco não recebeu"),
              ("concorrência", "dois editam juntos,", "um apaga o outro")]
    wc, hc, gap = 380, 340, 60
    x0 = (W - 4 * wc - 3 * gap) / 2
    y0 = 340
    for i, (nome, l1, l2) in enumerate(riscos):
        x = x0 + i * (wc + gap)
        b += card(x, y0, wc, hc)
        b += xmark(x + wc / 2, y0 + 84, 20, ST_RESTRICTED, 4)
        b += txt(x + wc / 2, y0 + 172, nome, 34, INK, anchor="middle",
                 weight="800", spacing=-0.8)
        b += txt(x + wc / 2, y0 + 232, l1, 23, SECONDARY, anchor="middle")
        b += txt(x + wc / 2, y0 + 268, l2, 23, SECONDARY, anchor="middle")
    b += glow(W / 2, 830, 300, "g1")
    b += caps(W / 2, 800, "o banco fala · o código precisa escutar", 24,
              ACCENT, anchor="middle")
    b += txt(W / 2, 860, "O erro vem com aviso. O silêncio nasce quando a "
             "aplicação ignora o aviso.", 27, SECONDARY, anchor="middle")
    b += caption(W / 2, 960,
                 "Validar a entrada, confirmar a gravação, tratar concorrência.")
    export(b, f"{OUT}/08-quatro-riscos", defs=glow_def("g1"))


# ---------------------------------------------------------------- 09
def p09_front_nao_e_banco():
    """ATO 3: KPI guardado no navegador vs no banco."""
    b = header(KICKER, fig(9))
    b += title(W / 2, 230, "O painel de KPI não mora no navegador")
    y0, hc = 380, 420
    # só no navegador
    b += card(200, y0, 600, hc, "kpi só no navegador")
    itens = [("limpou o navegador: perdeu", 160),
             ("outro computador: não vê", 240),
             ("outra pessoa: não acessa", 320)]
    for s, dy in itens:
        b += xmark(300, y0 + dy - 8, 14, ST_RESTRICTED, 3.5)
        b += txt(340, y0 + dy, s, 27, SECONDARY)
    # atravessa o servidor
    b += glow(1420, y0 + hc / 2, 320, "g1")
    b += card(1120, y0, 600, hc, "servidor · banco", label_fill=ACCENT)
    itens2 = [("dura entre sessões", 160),
              ("visível de qualquer lugar", 240),
              ("compartilhado com o time", 320)]
    for s, dy in itens2:
        b += check(1220, y0 + dy - 8, 14, ST_OPEN, 3.5)
        b += txt(1260, y0 + dy, s, 27, SECONDARY)
    b += arrow(830, y0 + hc / 2, 1090, y0 + hc / 2, INK, 3, "atravessa")
    b += caption(W / 2, 950,
                 "Dado de todos, que dura ou decide negócio: mora no banco.")
    export(b, f"{OUT}/09-front-nao-e-banco", defs=glow_def("g1"))


# ---------------------------------------------------------------- 10
def p10_migracao():
    """ATO 3: migração leva o schema de v1 para v2."""
    b = header(KICKER, fig(10))
    b += title(W / 2, 230, "Migração: quando a estrutura muda")
    y0, hc = 380, 300
    b += card(280, y0, 460, hc, "schema v1")
    b += txt(510, y0 + 160, "usuários:", 27, SECONDARY, anchor="middle")
    b += txt(510, y0 + 204, "nome · email", 30, INK, anchor="middle",
             weight="600")
    b += glow(960, y0 + hc / 2, 260, "g1")
    b += arrow(760, y0 + hc / 2, 1160, y0 + hc / 2, INK, 3, "migração",
               label_fill=ACCENT)
    b += card(1180, y0, 460, hc, "schema v2")
    b += txt(1410, y0 + 160, "usuários:", 27, SECONDARY, anchor="middle")
    b += txt(1410, y0 + 204, "nome · email · telefone", 30, INK,
             anchor="middle", weight="600")
    b += xmark(560, 812, 16, ST_RESTRICTED, 4)
    b += txt(600, 822, "código novo esperando v2 com o banco em v1: "
             "quebra na primeira gravação", 27, SECONDARY)
    b += caption(W / 2, 950,
                 "Mexeu na estrutura? Pergunte: tem migração? quem vai rodar?")
    export(b, f"{OUT}/10-migracao", defs=glow_def("g1"))


# ---------------------------------------------------------------- 11
def p11_tres_protecoes():
    """Fechamento: as três proteções que importam na prática."""
    b = header(KICKER, fig(11))
    b += title(W / 2, 230, "As três proteções que importam")
    itens = [("validar a entrada", "antes de gravar: o dado chega limpo ao banco"),
             ("confirmar a gravação",
              "não assumir que salvou só porque o servidor respondeu"),
             ("migrar com segurança",
              "mudar a estrutura sem quebrar o que já existe")]
    sx = 340
    y0, hc, gap = 350, 150, 32
    b += glow(sx, y0 + (3 * hc + 2 * gap) / 2, 300, "g1")
    b += line(sx, y0, sx, y0 + 3 * hc + 2 * gap, ACCENT, 3)
    for i, (nome, desc) in enumerate(itens):
        y = y0 + i * (hc + gap)
        yc = y + hc / 2
        b += card(sx + 100, y, 1150, hc)
        b += circle(sx, yc, 27, fill="#000000", stroke=ACCENT, sw=3)
        b += txt(sx, yc + 11, str(i + 1), 30, ACCENT, anchor="middle",
                 weight="800")
        b += txt(sx + 160, yc - 12, nome, 34, INK, weight="700", spacing=-0.8)
        b += txt(sx + 160, yc + 36, desc, 24, SECONDARY)
    b += caption(W / 2, 950,
                 "Valide, confirme, migre. É disciplina, não burocracia.")
    export(b, f"{OUT}/11-tres-protecoes", defs=glow_def("g1"))


if __name__ == "__main__":
    p01_caminho_do_dado()
    p02_memoria_nao_confiavel()
    p03_o_que_morre_o_que_dura()
    p04_dois_caminhos()
    p05_tres_familias()
    p06_query()
    p07_schema()
    p08_quatro_riscos()
    p09_front_nao_e_banco()
    p10_migracao()
    p11_tres_protecoes()
