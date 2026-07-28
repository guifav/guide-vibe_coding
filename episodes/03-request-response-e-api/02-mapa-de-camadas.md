# Mapa do dialogo (para mostrar na tela / base do thumbnail)

Este e o diagrama que Gui desenha ou mostra durante o vídeo. Simples, sem ferramentas, só o fluxo do request e response.

## O dialogo (versao texto)

```
  NAVEGADOR (front-end)
       |
       |  REQUEST
       |  - metodo: GET (pedir) ou POST (enviar)
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
  |  (navegador)     |     |  (balcao)        |     |  (almoxarifado)  |
  |                  |     |                  |     |                  |
  |  - manda request |---->|  - atende        |---->|  - guarda dados  |
  |  - le response   |<----|  - processa      |<----|  - devolve dado  |
  |                  |     |  - devolve JSON  |     |                  |
  +------------------+     +------------------+     +------------------+
        |                         |                         |
        |  Não SABE DO BANCO       |  SABE DO BANCO          |
        |  só conversa com a API   |  não sabe do front      |
        +-------------------------+-------------------------+
```

O front nunca fala direto com o banco. A seta do front para na API.

## A conversa completa (um pedido, do início ao fim)

```
  1. USUARIO clica ou digita URL
                |
  2. NAVEGADOR monta REQUEST
     - metodo: GET ou POST
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
     - le o JSON
     - confere o status code
     - renderiza na tela (ou mostra erro)
```

## Como usar no vídeo

- Desenhar o dialogo (navegador -> servidor -> navegador) no início do ATO 1, sem explicar tudo.
- Voltar ao mapa no final de cada ato, destacando o que já foi coberto.
- No ATO 3, mostrar a fronteira: tres blocos separados (front, API, banco) com a seta do front parando na API.

## Versao para thumbnail

Texto curto sobre o diagrama:
- Título sobre a imagem: "O que acontece quando você CLICA?" ou "Request e Response: a conversa invisivel"
- Setas: navegador -> servidor -> navegador
- Destacar: "GET / POST", "JSON", "200 ou 404?"
- Sem palavras densas; só o fluxo do pedido e da resposta.
