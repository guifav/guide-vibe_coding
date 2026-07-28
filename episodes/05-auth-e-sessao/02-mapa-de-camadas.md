# Mapa de camadas (para mostrar na tela / base do thumbnail)

Este e o diagrama que Gui desenha ou mostra durante o video. Simples, sem ferramentas, so o fluxo de auth e o que cada conceito responde.

## O mapa (versao texto)

```
  VOCE ABRE O SITE (visitante anonimo, sem nome)
                |
                v
  +-----------------------------------+
  |  AUTENTICACAO                     |  <- "quem e voce?"
  |  - login (email + senha)          |
  |  - senha vira hash, comparada     |
  |  - se bate: voce passa a existir  |
  +-----------------------------------+
                |
                v
  +-----------------------------------+
  |  SERVIDOR CRIA A MEMORIA          |  <- como ele lembra de voce
  |  - SESSAO: memoria no servidor    |
  |    (devolve session ID no cookie) |
  |  - TOKEN: cracha no cliente       |
  |    (carrega identidade dentro)    |
  +-----------------------------------+
                |
                v
  +-----------------------------------+
  |  CADA REQUEST CARREGA O CRACHA    |  <- cookie ou token
  |  - servidor le                    |
  |  - descobre quem e                |
  |  - passa para a proxima pergunta  |
  +-----------------------------------+
                |
                v
  +-----------------------------------+
  |  AUTORIZACAO                      |  <- "o que voce pode fazer?"
  |  - por PAPEL (admin/user/guest)   |
  |  - por RECURSO (esse item e seu?) |
  |  - se permitido: executa          |
  |  - se negado: bloqueia (403)      |
  +-----------------------------------+
                |
                v
  +-----------------------------------+
  |  LOGOFF / EXPIRACAO               |  <- o fim do cracha
  |  - logoff: cracha destruido       |
  |  - expiracao: prazo de validade   |
  |  - roubado: alguem se passa por vc|
  +-----------------------------------+
```

## As duas perguntas (versao para fixar)

```
  AUTENTICACAO               AUTORIZACAO
  "quem e voce?"             "o que voce pode fazer?"
       |                          |
       v                          v
  login + senha              papel ou recurso
  token / sessao             permitido ou negado
```

Essas duas perguntas sao o coracao do video. Tudo o mais (sessao, token, cookie, RBAC) e detalhe de como cada uma e respondida.

## Onde a memoria mora (sessao vs token)

```
  SESSAO                          TOKEN
  memoria no SERVIDOR             memoria no CLIENTE
       |                              |
       v                              v
  servidor guarda sessao         servidor nao guarda nada
  devolve session ID             devolve o cracha (token)
  navegador leva cookie         navegador leva token
       |                              |
       v                              v
  servidor consulta a memoria   servidor le o token direto
```

## Como usar no video

- Desenhar o fluxo principal na tela no inicio do ATO 1, sem explicar tudo.
- Voltar ao mapa no final de cada ato, destacando as partes que ja foram cobertas.
- No ATO 3, destacar bem as duas perguntas (autenticacao vs autorizacao) lado a lado.
- No fim do video, o mapa completo esta desenhado e o espectador ve o ciclo: visitante -> login -> sessao/token -> autorizacao -> logoff.

## Versao para thumbnail

Texto curto sobre o diagrama:
- Titulo sobre a imagem: "Quem e voce? O que pode fazer?"
- Duas portas lado a lado: "LOGIN" e "ACESSO"
- Um cracha grande no centro, com seta apontando para um servidor
- Sem palavras densas; so "login", "token", "permissao".
