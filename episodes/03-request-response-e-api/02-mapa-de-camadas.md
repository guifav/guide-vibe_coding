# Mapa do diálogo (para mostrar na tela / base do thumbnail)

Este é o diagrama que Gui desenha ou mostra durante o vídeo. Simples, sem ferramentas, só o fluxo do request e response.

## O diálogo (versão texto)

```
  NAVEGADOR (front-end)
       |
       |  REQUEST
       |  - método: GET (pedir) ou POST (enviar)
       |  - endpoint: /api/produtos (a porta)
       |
       v
  +-------------------------------+
  |  SERVIDOR                     |
  |  - recebe o request           |
  |  - processa (lógica)          |
  |  - consulta o BANCO           |
  |  - monta a RESPOSTA           |
  +-------------------------------+
       |
       |  RESPONSE
       |  - JSON (dados em texto organizado)
       |  - CONTRATO (o que foi combinado)
       |  - STATUS CODE (200, 404, 401, 403, 500)
       |
       v
  NAVEGADOR (renderiza na tela)
```

## A fronteira (o que cada um enxerga)

```
  +------------------+     +------------------+     +------------------+
  |  FRONT-END       |     |  API             |     |  BANCO           |
  |  (navegador)     |     |  (balcão)        |     |  (almoxarifado)  |
  |                  |     |                  |     |                  |
  |  - manda request |---->|  - atende        |---->|  - guarda dados  |
  |  - lê response   |<----|  - processa      |<----|  - devolve dado  |
  |                  |     |  - devolve JSON  |     |                  |
  +------------------+     +------------------+     +------------------+
        |                         |                         |
        |  Não SABE DO BANCO       |  SABE DO BANCO          |
        |  só conversa com a API   |  não sabe do front      |
        +-------------------------+-------------------------+
```

O front nunca fala direto com o banco. A seta do front para na API.

## A conversa completa (um pedido inteiro)

```
  1. USUÁRIO clica ou digita URL
                |
  2. NAVEGADOR monta REQUEST
     - método: GET ou POST
     - endpoint: a URL da porta
                |
  3. SERVIDOR recebe o request
     - identifica o endpoint
     - executa a lógica
     - consulta o BANCO se precisar
                |
  4. SERVIDOR monta RESPONSE
     - JSON com os dados
     - dentro do CONTRATO combinado
     - com STATUS CODE honesto
                |
  5. NAVEGADOR recebe o response
     - lê o JSON
     - confere o status code
     - renderiza na tela (ou mostra erro)
```

## Como usar no vídeo

- Desenhar o diálogo (navegador -> servidor -> navegador) no início do ATO 1, sem explicar tudo.
- Voltar ao mapa no final de cada ato, destacando o que já foi coberto.
- No ATO 3, mostrar a fronteira: três blocos separados (front, API, banco) com a seta do front parando na API.

## Versão para thumbnail

Texto curto sobre o diagrama:
- Título sobre a imagem: "O que acontece quando você CLICA?" ou "Request e Response: a conversa invisível"
- Setas: navegador -> servidor -> navegador
- Destacar: "GET / POST", "JSON", "200 ou 404?"
- Sem palavras densas; só o fluxo do pedido e da resposta.
