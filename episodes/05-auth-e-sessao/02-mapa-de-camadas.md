# Mapa de camadas (para mostrar na tela / base do thumbnail)

Este e o diagrama que Gui desenha ou mostra durante o vídeo. Simples, sem ferramentas, só o fluxo de auth e o que cada conceito responde.

## O mapa (versao texto)

```
  Você ABRE O SITE (visitante anônimo, sem nome)
                |
                v
  +-----------------------------------+
  |  Autenticação                     |  <- "quem e você?"
  |  - login (email + senha)          |
  |  - senha vira hash, comparada     |
  |  - se bate: você passa a existir  |
  +-----------------------------------+
                |
                v
  +-----------------------------------+
  |  SERVIDOR CRIA A Memória          |  <- como ele lembra de você
  |  - SESSAO: memória no servidor    |
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
  |  Autorização                      |  <- "o que você pode fazer?"
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
  |  - roubado: alguém se passa por vc|
  +-----------------------------------+
```

## As duas perguntas (versao para fixar)

```
  Autenticação               Autorização
  "quem e você?"             "o que você pode fazer?"
       |                          |
       v                          v
  login + senha              papel ou recurso
  token / sessao             permitido ou negado
```

Essas duas perguntas são o coração do vídeo. Tudo o mais (sessao, token, cookie, RBAC) e detalhe de como cada uma e respondida.

## Onde a memória mora (sessao vs token)

```
  SESSAO                          TOKEN
  memória no SERVIDOR             memória no CLIENTE
       |                              |
       v                              v
  servidor guarda sessao         servidor não guarda nada
  devolve session ID             devolve o cracha (token)
  navegador leva cookie         navegador leva token
       |                              |
       v                              v
  servidor consulta a memória   servidor le o token direto
```

## Como usar no vídeo

- Desenhar o fluxo principal na tela no início do ATO 1, sem explicar tudo.
- Voltar ao mapa no final de cada ato, destacando as partes que já foram cobertas.
- No ATO 3, destacar bem as duas perguntas (autenticação vs autorização) lado a lado.
- No fim do vídeo, o mapa completo esta desenhado e o espectador ve o ciclo: visitante -> login -> sessao/token -> autorização -> logoff.

## Versao para thumbnail

Texto curto sobre o diagrama:
- Título sobre a imagem: "Quem e você? O que pode fazer?"
- Duas portas lado a lado: "LOGIN" e "ACESSO"
- Um cracha grande no centro, com seta apontando para um servidor
- Sem palavras densas; só "login", "token", "permissao".
