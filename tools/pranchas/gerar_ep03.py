#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pranchas do episódio 03 - Request, Response e API.
Uma prancha por passagem visual do roteiro (seções "Mostrar").
Design system: Midnight Grid (ver midnight_kit.py).
"""

from midnight_kit import (W, H, INK, SECONDARY, MUTED, BORDER, ACCENT,
                          SURFACE, ELEVATED, ST_OPEN, ST_GUIDED, ST_RESTRICTED,
                          export, header, title, caption, txt, caps, line,
                          rrect, circle, path, glow, glow_def, arrow, card,
                          chip, xmark, check, dim_bracket_v)

OUT = "../../episodes/03-request-response-e-api/pranchas"
KICKER = "EP 03 · Request, response e API"
N = 13


def fig(n):
    return f"prancha {n:02d}/{N}"


# ---------------------------------------------------------------- 01
def p01_request_response():
    """Abertura: o diálogo navegador-servidor, só mostrar."""
    b = header(KICKER, fig(1))
    b += title(W / 2, 230, "Entre o clique e a tela, uma conversa")
    y0, hc, wc = 400, 360, 480
    b += card(180, y0, wc, hc, "navegador")
    b += glow(1500, y0 + hc / 2, 300, "g1")
    b += card(1260, y0, wc, hc, "servidor", label_fill=ACCENT)
    b += txt(420, y0 + 185, "pede", 44, INK, anchor="middle", weight="800")
    b += txt(420, y0 + 245, "clique, URL, formulário", 24, SECONDARY,
             anchor="middle")
    b += txt(1500, y0 + 185, "responde", 44, INK, anchor="middle", weight="800")
    b += txt(1500, y0 + 245, "processa e devolve", 24, SECONDARY,
             anchor="middle")
    b += arrow(700, y0 + 110, 1220, y0 + 110, INK, 3, "request · o pedido")
    b += arrow(1220, y0 + 260, 700, y0 + 260, SECONDARY, 3,
               "response · a resposta")
    b += caption(W / 2, 950,
                 "O navegador pede. O servidor responde. Sempre nessa ordem.")
    export(b, f"{OUT}/01-request-response", defs=glow_def("g1"))


# ---------------------------------------------------------------- 02
def p02_get_vs_post():
    """ATO 1: os dois métodos que cobrem 90% da web."""
    b = header(KICKER, fig(2))
    b += title(W / 2, 230, "GET pede. POST envia.")
    wc, hc, gap = 720, 440, 120
    x0, y0 = 180, 340
    b += glow(x0 + wc / 2, y0 + hc / 2, 320, "g1")
    # GET
    b += card(x0, y0, wc, hc)
    b += caps(x0 + wc / 2, y0 + 64, "GET · pedir", 26, ACCENT, anchor="middle")
    b += txt(x0 + wc / 2, y0 + 190, "“me dá isso”", 44, INK, anchor="middle",
             weight="800")
    b += txt(x0 + wc / 2, y0 + 300, "abrir a página, ver a lista,", 26,
             SECONDARY, anchor="middle")
    b += txt(x0 + wc / 2, y0 + 340, "carregar o produto", 26, SECONDARY,
             anchor="middle")
    b += txt(x0 + wc / 2, y0 + 396, "não muda nada no servidor", 24, MUTED,
             anchor="middle")
    # POST
    x1 = x0 + wc + gap
    b += card(x1, y0, wc, hc)
    b += caps(x1 + wc / 2, y0 + 64, "POST · enviar", 26, SECONDARY,
              anchor="middle")
    b += txt(x1 + wc / 2, y0 + 165, "“aqui estão dados,", 44, INK,
             anchor="middle", weight="800")
    b += txt(x1 + wc / 2, y0 + 222, "faz algo com isso”", 44, INK,
             anchor="middle", weight="800")
    b += txt(x1 + wc / 2, y0 + 300, "criar a conta, enviar o formulário,", 26,
             SECONDARY, anchor="middle")
    b += txt(x1 + wc / 2, y0 + 340, "adicionar ao carrinho", 26, SECONDARY,
             anchor="middle")
    b += txt(x1 + wc / 2, y0 + 396, "manda dados que mudam algo", 24, MUTED,
             anchor="middle")
    b += txt(W / 2, 862, "Existem outros (PUT, PATCH, DELETE), mas esses dois cobrem 90% da web.",
             28, SECONDARY, anchor="middle")
    b += caption(W / 2, 950,
                 "Se a IA diz “fazer um GET”, ela está dizendo o tipo do pedido.")
    export(b, f"{OUT}/02-get-vs-post", defs=glow_def("g1"))


# ---------------------------------------------------------------- 03
def p03_endpoint_portas():
    """ATO 1: endpoints, o servidor com várias portas."""
    b = header(KICKER, fig(3))
    b += title(W / 2, 230, "Endpoint: cada URL é uma porta")
    b += glow(1420, 600, 340, "g1")
    # navegador
    b += card(160, 440, 400, 300, "navegador")
    b += txt(360, 585, "a URL diz", 30, INK, anchor="middle", weight="700")
    b += txt(360, 630, "em qual porta bater", 24, SECONDARY, anchor="middle")
    # servidor com portas
    b += card(1080, 340, 680, 520, "servidor")
    portas = [("/api/produtos", "devolve a lista de produtos", 430),
              ("/api/usuarios", "devolve a lista de usuários", 556),
              ("/api/pedidos", "devolve os pedidos", 682)]
    for url, desc, y in portas:
        b += rrect(1130, y, 400, 96, 12, fill=ELEVATED, stroke=BORDER, sw=2)
        b += txt(1160, y + 42, url, 28, INK, weight="600")
        b += txt(1160, y + 74, desc, 20, SECONDARY)
    b += caps(1420, 826, "endpoints · as portas", 22, ACCENT, anchor="middle")
    # setas do navegador para as portas
    b += arrow(600, 530, 1110, 478, SECONDARY, 2.5)
    b += arrow(600, 590, 1110, 604, SECONDARY, 2.5)
    b += arrow(600, 650, 1110, 730, SECONDARY, 2.5)
    b += caption(W / 2, 950,
                 "Você não pede sanduíche no caixa eletrônico. Cada porta atende um pedido.")
    export(b, f"{OUT}/03-endpoint-portas", defs=glow_def("g1"))


# ---------------------------------------------------------------- 04
def p04_json():
    """ATO 2: JSON, o formato da resposta."""
    b = header(KICKER, fig(4))
    b += title(W / 2, 230, "JSON: a resposta em texto organizado")
    b += glow(600, 590, 320, "g1")
    b += card(280, 350, 640, 470, "response · o que volta")
    linhas = [(360, "{"),
              (420, '"nome": "Produto A",'),
              (420, '"preco": 29.90,'),
              (420, '"estoque": true'),
              (360, "}")]
    y = 480
    for x, s in linhas:
        b += txt(x, y, s, 30, SECONDARY, weight="400")
        y += 52
    # anotações à direita
    b += caps(1080, 430, "texto que o front lê", 24, ACCENT)
    notas = [("chaves { } agrupam os campos", "abrem e fecham um bloco de dados", 530),
             ("aspas marcam textos", "números e verdadeiro/falso vão sem aspas", 650),
             ("cada linha: um nome e um valor", "o front lê isso e monta a tela", 770)]
    for t, d, y in notas:
        b += txt(1080, y, t, 28, INK, weight="600")
        b += txt(1080, y + 40, d, 24, SECONDARY)
    b += caption(W / 2, 950,
                 "Fácil para o computador ler. Fácil para você conferir.")
    export(b, f"{OUT}/04-json", defs=glow_def("g1"))


# ---------------------------------------------------------------- 05
def p05_contrato():
    """ATO 2: o contrato certo vs o contrato quebrado."""
    b = header(KICKER, fig(5))
    b += title(W / 2, 230, "O contrato: o que peço, o que recebo")
    wc, hc, gap = 780, 470, 60
    x0, y0 = 150, 320
    b += glow(x0 + wc / 2, y0 + hc / 2, 320, "g1")
    # certo
    b += card(x0, y0, wc, hc)
    b += caps(x0 + wc / 2, y0 + 52, "contrato certo", 22, ST_OPEN,
              anchor="middle")
    b += txt(x0 + 70, y0 + 140, "front pede: um produto", 27, SECONDARY)
    b += txt(x0 + 70, y0 + 200, "servidor devolve:", 27, SECONDARY)
    b += txt(x0 + 70, y0 + 248, '{ "nome": ..., "preco": ... }', 28, INK,
             weight="600")
    b += txt(x0 + 70, y0 + 312, "front lê nome e preço", 27, SECONDARY)
    b += check(x0 + 92, y0 + 388, 18, ST_OPEN, 4)
    b += txt(x0 + 140, y0 + 398, "funciona", 30, INK, weight="700")
    # quebrado
    x1 = x0 + wc + gap
    b += card(x1, y0, wc, hc)
    b += caps(x1 + wc / 2, y0 + 52, "contrato quebrado", 22, ST_RESTRICTED,
              anchor="middle")
    b += txt(x1 + 70, y0 + 140, "front espera: título", 27, SECONDARY)
    b += txt(x1 + 70, y0 + 200, "servidor devolve:", 27, SECONDARY)
    b += txt(x1 + 70, y0 + 248, '{ "nome": ..., "preco": ... }', 28, INK,
             weight="600")
    b += txt(x1 + 70, y0 + 312, "front procura título, não acha", 27, SECONDARY)
    b += xmark(x1 + 92, y0 + 388, 18, ST_RESTRICTED, 4)
    b += txt(x1 + 140, y0 + 398, "tela em branco", 30, INK, weight="700")
    b += txt(W / 2, 866, "Contrato: o combinado entre front e servidor. O que eu peço, e o que recebo.",
             28, SECONDARY, anchor="middle")
    b += caption(W / 2, 950, "Se um lado muda o combinado, o outro quebra.")
    export(b, f"{OUT}/05-contrato", defs=glow_def("g1"))


# ---------------------------------------------------------------- 06
def p06_contrato_inventado():
    """ATO 2: a IA inventa contrato — campos que ninguém confirmou."""
    b = header(KICKER, fig(6))
    b += title(W / 2, 230, "Quando a IA inventa o contrato")
    y0 = 370
    # o que a IA escreveu
    b += card(180, y0, 560, 340, "o que a IA escreveu")
    b += txt(250, y0 + 128, "o front espera receber:", 25, SECONDARY)
    b += txt(250, y0 + 185, '"título": ...', 30, INK, weight="600")
    b += txt(250, y0 + 232, '"descrição": ...', 30, INK, weight="600")
    b += txt(250, y0 + 296, "campos que ninguém confirmou", 24, MUTED)
    # o que o servidor devolve
    b += card(1180, y0, 560, 340, "o que o servidor devolve")
    b += txt(1250, y0 + 128, "o contrato real:", 25, SECONDARY)
    b += txt(1250, y0 + 185, '"nome": "Produto A"', 30, INK, weight="600")
    b += txt(1250, y0 + 232, '"preco": 29.90', 30, INK, weight="600")
    b += txt(1250, y0 + 296, "nada de título ou descrição", 24, MUTED)
    # o choque no meio
    b += glow(960, y0 + 160, 250, "g1")
    b += line(760, y0 + 150, 900, y0 + 138, MUTED, 2)
    b += line(1160, y0 + 150, 1020, y0 + 138, MUTED, 2)
    b += xmark(960, y0 + 130, 34, ST_RESTRICTED, 5)
    b += caps(960, y0 + 228, "não bate", 22, ST_RESTRICTED, anchor="middle")
    b += caps(W / 2, 812, "a IA chutou os campos", 24, ACCENT, anchor="middle")
    b += txt(W / 2, 866, "O código roda sem acusar erro. E a tela fica vazia.",
             28, SECONDARY, anchor="middle")
    b += caption(W / 2, 950,
                 "Pergunte: “você viu o contrato real, ou está chutando os campos?”")
    export(b, f"{OUT}/06-contrato-inventado", defs=glow_def("g1"))


# ---------------------------------------------------------------- 07
def p07_status_codes():
    """ATO 2: os cinco status codes que cobrem 95% dos casos."""
    b = header(KICKER, fig(7))
    b += title(W / 2, 230, "Cinco status codes cobrem quase tudo")
    b += caps(240, 330, "verde: deu certo · âmbar: problema no pedido · vermelho: quebrou lá dentro",
              18, ACCENT)
    rows = [("200", "ok", "deu certo, aqui está a resposta", ST_OPEN),
            ("404", "not found", "não achei o que você pediu", ST_GUIDED),
            ("401", "unauthorized", "você não está logado: não sei quem você é", ST_GUIDED),
            ("403", "forbidden", "sei quem você é, mas você não pode acessar isso", ST_GUIDED),
            ("500", "server error", "quebrou lá dentro: não foi culpa sua", ST_RESTRICTED)]
    y0, rh, step = 360, 88, 102
    b += glow(960, y0 + rh / 2, 260, "g1")
    for i, (code, nome, desc, color) in enumerate(rows):
        y = y0 + i * step
        b += rrect(240, y, 1440, rh, 12, fill=SURFACE, stroke=BORDER, sw=1.5)
        b += txt(330, y + 58, code, 40, color, weight="800")
        b += caps(470, y + 54, nome, 20, color)
        b += txt(920, y + 56, desc, 27, SECONDARY)
    b += caption(W / 2, 950,
                 "O status code é o servidor sendo honesto sobre o que aconteceu.")
    export(b, f"{OUT}/07-status-codes", defs=glow_def("g1"))


# ---------------------------------------------------------------- 08
def p08_401_vs_403():
    """ATO 2: o par de status mais confundido, em dois painéis."""
    b = header(KICKER, fig(8))
    b += title(W / 2, 230, "401 e 403: portas fechadas diferentes")
    wc, hc, gap = 700, 420, 120
    x0 = (W - 2 * wc - gap) / 2
    y0 = 340
    b += glow(x0 + wc / 2, y0 + hc / 2, 300, "g1")

    b += card(x0, y0, wc, hc)
    b += txt(x0 + wc / 2, y0 + 110, "401", 72, ST_GUIDED, anchor="middle",
             weight="800")
    b += caps(x0 + wc / 2, y0 + 160, "unauthorized", 20, SECONDARY,
              anchor="middle")
    b += txt(x0 + wc / 2, y0 + 250, "“não te conheço”", 36, INK,
             anchor="middle", weight="700")
    b += txt(x0 + wc / 2, y0 + 330, "falta login: quem é você?", 25,
             SECONDARY, anchor="middle")

    x1 = x0 + wc + gap
    b += card(x1, y0, wc, hc)
    b += txt(x1 + wc / 2, y0 + 110, "403", 72, ST_GUIDED, anchor="middle",
             weight="800")
    b += caps(x1 + wc / 2, y0 + 160, "forbidden", 20, SECONDARY,
              anchor="middle")
    b += txt(x1 + wc / 2, y0 + 250, "“te conheço, e não pode”", 36, INK,
             anchor="middle", weight="700")
    b += txt(x1 + wc / 2, y0 + 330, "logado, sem permissão para isso", 25,
             SECONDARY, anchor="middle")

    b += caps(W / 2, 850, "a porta fechou pelo motivo certo?", 22, ACCENT,
              anchor="middle")
    b += caption(W / 2, 950, "401 pede login. 403 pede permissão.")
    export(b, f"{OUT}/08-401-vs-403", defs=glow_def("g1"))


# ---------------------------------------------------------------- 09
def p09_crash_silencioso():
    """ATO 2: crash honesto (500) vs crash silencioso (resposta vazia)."""
    b = header(KICKER, fig(9))
    b += title(W / 2, 230, "Crash honesto, crash silencioso")
    wc, hc, gap = 350, 130, 55
    x0 = (W - 4 * wc - 3 * gap) / 2
    step = wc + gap

    def fluxo(y, cards):
        out = ""
        for i, (main, sub) in enumerate(cards):
            x = x0 + i * step
            out += rrect(x, y, wc, hc, 14, fill=SURFACE, stroke=BORDER, sw=2)
            out += txt(x + wc / 2, y + 58, main, 26, INK, anchor="middle",
                       weight="600")
            out += txt(x + wc / 2, y + 94, sub, 21, SECONDARY, anchor="middle")
            if i < 3:
                out += arrow(x + wc + 7, y + hc / 2, x + step - 7, y + hc / 2,
                             SECONDARY, 2.5)
        return out

    y1, y2 = 400, 660
    b += glow(x0 + 2 * step + wc / 2, y1 + hc / 2, 230, "g1")
    b += caps(x0, y1 - 34, "resposta honesta", 22, ST_OPEN)
    b += check(x0 + 356, y1 - 42, 13, ST_OPEN, 3.5)
    b += fluxo(y1, [("request vai", "o pedido chega"),
                    ("servidor quebra", "algo falhou lá dentro"),
                    ("devolve 500", "assume o erro"),
                    ("front avisa o usuário", "mensagem de erro na tela")])
    b += caps(x0, y2 - 34, "crash silencioso", 22, ST_RESTRICTED)
    b += xmark(x0 + 348, y2 - 42, 13, ST_RESTRICTED, 3.5)
    b += fluxo(y2, [("request vai", "o mesmo pedido"),
                    ("servidor quebra", "a mesma falha"),
                    ("devolve vazio", "finge que deu certo"),
                    ("tela parada", "sem mensagem, sem pista")])
    b += txt(W / 2, 876, "Quando a IA falar em “tratar erro”, pergunte: tratar qual? 404, 401, 500?",
             28, SECONDARY, anchor="middle")
    b += caption(W / 2, 950,
                 "O pior erro não é o 500. É a resposta que não diz nada.")
    export(b, f"{OUT}/09-crash-silencioso", defs=glow_def("g1"))


# ---------------------------------------------------------------- 10
def p10_fronteira():
    """ATO 3: a fronteira — front, API (balcão), banco (almoxarifado)."""
    b = header(KICKER, fig(10))
    b += title(W / 2, 230, "A fronteira: o front não vê o banco")
    y0 = 370
    b += card(150, y0, 430, 300, "front · o cliente")
    b += txt(365, y0 + 155, "manda request", 26, SECONDARY, anchor="middle")
    b += txt(365, y0 + 195, "lê response", 26, SECONDARY, anchor="middle")
    b += glow(950, y0 + 130, 280, "g1")
    b += card(760, y0 - 40, 380, 380, "API · o balcão", label_fill=ACCENT,
              elevated=True)
    b += txt(950, y0 + 140, "atende o pedido", 25, SECONDARY, anchor="middle")
    b += txt(950, y0 + 178, "busca o que precisa", 25, SECONDARY,
             anchor="middle")
    b += txt(950, y0 + 216, "devolve JSON", 25, SECONDARY, anchor="middle")
    b += card(1330, y0, 440, 300, "banco · o almoxarifado")
    b += txt(1550, y0 + 155, "guarda os dados", 26, SECONDARY, anchor="middle")
    b += txt(1550, y0 + 195, "entrega o que a API pede", 26, SECONDARY,
             anchor="middle")
    b += arrow(596, y0 + 100, 744, y0 + 100, INK, 2.5, "request",
               label_size=17)
    b += arrow(744, y0 + 220, 596, y0 + 220, SECONDARY, 2.5, "response",
               label_size=17)
    b += arrow(1156, y0 + 100, 1314, y0 + 100, INK, 2.5, "consulta",
               label_size=17)
    b += arrow(1314, y0 + 220, 1156, y0 + 220, SECONDARY, 2.5, "dado",
               label_size=17)
    # o caminho proibido: front -> banco direto
    b += path(f"M365 {y0 + 300} V 800 H 894", stroke=MUTED, w=2, dash="10,10")
    b += path(f"M1022 800 H 1550 V {y0 + 300}", stroke=MUTED, w=2, dash="10,10")
    b += xmark(958, 800, 20, ST_RESTRICTED, 4)
    b += caps(958, 862, "o front não fala direto com o banco", 20, MUTED,
              anchor="middle")
    b += caption(W / 2, 950, "Você pede no balcão. Não entra no almoxarifado.")
    export(b, f"{OUT}/10-fronteira-front-api-banco", defs=glow_def("g1"))


# ---------------------------------------------------------------- 11
def p11_camadas():
    """ATO 3: camadas — cada uma com um trabalho."""
    b = header(KICKER, fig(11))
    b += title(W / 2, 230, "Camadas: cada uma com um trabalho")
    cols = [("front", "mostra", "telas, botões, interação"),
            ("api", "atende e processa", "recebe, executa, responde"),
            ("banco", "guarda", "dados que sobrevivem")]
    wc, hc, gap = 480, 320, 80
    x0, y0 = 160, 360
    b += glow(x0 + wc + gap + wc / 2, y0 + hc / 2, 300, "g1")
    for i, (nome, verbo, desc) in enumerate(cols):
        x = x0 + i * (wc + gap)
        b += card(x, y0, wc, hc, nome)
        b += txt(x + wc / 2, y0 + 175, verbo, 42, INK, anchor="middle",
                 weight="800")
        b += txt(x + wc / 2, y0 + 245, desc, 24, SECONDARY, anchor="middle")
    b += txt(W / 2, 776, "Separadas, você troca uma sem quebrar a outra. Misturadas, tudo quebra junto.",
             28, SECONDARY, anchor="middle")
    b += caps(W / 2, 852, "pergunte à IA: isso mora em qual camada?", 24,
              ACCENT, anchor="middle")
    b += caption(W / 2, 950,
                 "Cada camada tem um trabalho. A fronteira mantém o sistema são.")
    export(b, f"{OUT}/11-camadas", defs=glow_def("g1"))


# ---------------------------------------------------------------- 12
def p12_tres_armadilhas():
    """ATO 3: as três armadilhas clássicas da IA com API."""
    b = header(KICKER, fig(12))
    b += title(W / 2, 230, "As três armadilhas da IA com API")
    dados = [("inventar contrato",
              ["espera campos que o servidor", "nunca confirmou"],
              ["“Você viu o contrato", "ou chutou?”"]),
             ("ignorar status code",
              ["trata 404, 401 e 500", "como se fossem o mesmo erro"],
              ["“Qual status code", "eu devo tratar?”"]),
             ("misturar camadas",
              ["põe lógica de banco no front,", "ou de front no servidor"],
              ["“Isso mora em", "qual camada?”"])]
    wc, hc, gap = 540, 460, 60
    x0, y0 = 90, 340
    b += glow(x0 + wc / 2, y0 + hc / 2, 320, "g1")
    for i, (nome, desc, pergunta) in enumerate(dados):
        x = x0 + i * (wc + gap)
        cx = x + wc / 2
        b += card(x, y0, wc, hc)
        b += caps(cx, y0 + 56, f"armadilha {i + 1}", 20, MUTED, anchor="middle")
        b += txt(cx, y0 + 130, nome, 34, INK, anchor="middle", weight="800")
        for j, s in enumerate(desc):
            b += txt(cx, y0 + 192 + j * 38, s, 24, SECONDARY, anchor="middle")
        b += line(x + 60, y0 + 288, x + wc - 60, y0 + 288, BORDER, 1.5)
        b += caps(cx, y0 + 336, "pergunte", 18, ACCENT if i == 0 else MUTED,
                  anchor="middle")
        for j, s in enumerate(pergunta):
            b += txt(cx, y0 + 386 + j * 40, s, 27, INK, anchor="middle",
                     italic=True)
    b += caption(W / 2, 950,
                 "Três perguntas, um crivo. Faça-as toda vez que a IA mexer com API.")
    export(b, f"{OUT}/12-tres-armadilhas", defs=glow_def("g1"))


# ---------------------------------------------------------------- 13
def p13_conversa_completa():
    """Encerramento: a conversa inteira, do clique à tela."""
    b = header(KICKER, fig(13))
    b += title(W / 2, 230, "A conversa inteira, do clique à tela")
    steps = [("você clica", "ou digita a URL"),
             ("request parte", "método + endpoint"),
             ("servidor processa", "consulta o banco"),
             ("response volta", "JSON + status code"),
             ("front renderiza", "a tela atualiza")]
    wc, hc, gap = 320, 190, 36
    x0 = (W - 5 * wc - 4 * gap) / 2
    y0 = 430
    b += glow(x0 + 4 * (wc + gap) + wc / 2, y0 + hc / 2, 240, "g1")
    for i, (main, sub) in enumerate(steps):
        x = x0 + i * (wc + gap)
        b += card(x, y0, wc, hc)
        b += txt(x + wc / 2, y0 + 62, str(i + 1), 30,
                 ACCENT if i == 4 else MUTED, anchor="middle", weight="800")
        b += txt(x + wc / 2, y0 + 112, main, 24, INK, anchor="middle",
                 weight="600")
        b += txt(x + wc / 2, y0 + 150, sub, 21, SECONDARY, anchor="middle")
        if i < 4:
            b += arrow(x + wc + 5, y0 + 95, x + wc + gap - 5, y0 + 95,
                       SECONDARY, 2.5)
    b += txt(W / 2, 750, "Esse ciclo é a conversa inteira. E ela acontece a cada clique.",
             28, SECONDARY, anchor="middle")
    b += caption(W / 2, 950,
                 "O front pede. A API atende. O banco guarda. Cada um no seu lugar.")
    export(b, f"{OUT}/13-conversa-completa", defs=glow_def("g1"))


if __name__ == "__main__":
    p01_request_response()
    p02_get_vs_post()
    p03_endpoint_portas()
    p04_json()
    p05_contrato()
    p06_contrato_inventado()
    p07_status_codes()
    p08_401_vs_403()
    p09_crash_silencioso()
    p10_fronteira()
    p11_camadas()
    p12_tres_armadilhas()
    p13_conversa_completa()
