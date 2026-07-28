# Mapa de camadas (para mostrar na tela / base do thumbnail)

Este é o diagrama que Gui desenha ou mostra durante o vídeo. Simples, sem ferramentas, só o fluxo de auth e o que cada conceito responde.

## O mapa (versão texto)

```
  Você ABRE O SITE (visitante anônimo, sem nome)
                |
                v
  +-----------------------------------+
  |  Autenticação                     |  <- "quem é você?"
  |  - login (email + senha)          |
  |  - senha vira hash, comparada     |
  |  - se bate: você passa a existir  |
  +-----------------------------------+
                |
                v
  +-----------------------------------+
  |  SERVIDOR CRIA A Memória          |  <- como ele lembra de você
  |  - SESSÃO: memória no servidor    |
  |    (devolve session ID no cookie) |
  |  - TOKEN: crachá no cliente       |
  |    (carrega identidade dentro)    |
  +-----------------------------------+
                |
                v
  +-----------------------------------+
  |  CADA REQUEST CARREGA O CRACHÁ    |  <- cookie ou token
  |  - servidor lê                    |
  |  - descobre quem é                |
  |  - passa para a próxima pergunta  |
  +-----------------------------------+
                |
                v
  +-----------------------------------+
  |  Autorização                      |  <- "o que você pode fazer?"
  |  - por PAPEL (admin/user/guest)   |
  |  - por RECURSO (esse item é seu?) |
  |  - se permitido: executa          |
  |  - se negado: bloqueia (403)      |
  +-----------------------------------+
                |
                v
  +-----------------------------------+
  |  LOGOFF / EXPIRAÇÃO               |  <- o fim do crachá
  |  - logoff: crachá destruído       |
  |  - expiração: prazo de validade   |
  |  - roubado: alguém se passa por vc|
  +-----------------------------------+
```

## As duas perguntas (versão para fixar)

```
  Autenticação               Autorização
  "quem é você?"             "o que você pode fazer?"
       |                          |
       v                          v
  login + senha              papel ou recurso
  token / sessão             permitido ou negado
```

Essas duas perguntas são o coração do vídeo. Tudo o mais (sessão, token, cookie, RBAC) é detalhe de como cada uma é respondida.

## Onde a memória mora (sessão vs token)

```
  SESSÃO                          TOKEN
  memória no SERVIDOR             memória no CLIENTE
       |                              |
       v                              v
  servidor guarda sessão         servidor não guarda nada
  devolve session ID             devolve o crachá (token)
  navegador leva cookie         navegador leva token
       |                              |
       v                              v
  servidor consulta a memória   servidor lê o token direto
```

## Como usar no vídeo

- Desenhar o fluxo principal na tela no início do ATO 1, sem explicar tudo.
- Voltar ao mapa no final de cada ato, destacando as partes que já foram cobertas.
- No ATO 3, destacar bem as duas perguntas (autenticação vs autorização) lado a lado.
- No fim do vídeo, o mapa completo está desenhado e o espectador vê o ciclo: visitante -> login -> sessão/token -> autorização -> logoff.

## Versão para thumbnail

Texto curto sobre o diagrama:
- Título sobre a imagem: "Quem é você? O que pode fazer?"
- Duas portas lado a lado: "LOGIN" e "ACESSO"
- Um crachá grande no centro, com seta apontando para um servidor
- Sem palavras densas; só "login", "token", "permissão".
