# Mapa de camadas (para mostrar na tela / base do thumbnail)

Este e o diagrama que Gui desenha ou mostra durante o video. Simples, sem ferramentas, so camadas e o fluxo.

## O mapa (versao texto)

```
  USUARIO CLICA OU DIGITA
                |
                v
  +-------------------------------+
  |  NAVEGADOR (front)            |  <- estado da pagina (morre ao fechar)
  |  - variaveis locais           |
  |  - memoria de sessao          |
  +-------------------------------+
                |
                | request com dado
                v
  +-------------------------------+
  |  SERVIDOR (amnesico)          |  <- esquece entre requests
  |  - recebe o pedido            |
  |  - decide o que fazer         |
  +-------------------------------+
                |
                | query
                v
  +-------------------------------+
  |  BANCO DE DADOS (persistente) |  <- onde o dado sobrevive
  |  - SCHEMA (estrutura)         |
  |  - QUERY (pergunta/resultado) |
  |  - MIGRACAO (quando muda)     |
  +-------------------------------+
                |
                | resultado
                v
  SERVIDOR RESPONDE E O DADO DURA
```

## O caminho do dado (do clique a durar para sempre)

```
  1. USUARIO CLICA no front
       (estado da pagina muda, ainda nao salvou)
                |
  2. FRONT manda REQUEST para o servidor
       (dado atravessa a fronteira)
                |
  3. SERVIDOR recebe e valida
       (decide se grava, busca ou ignora)
                |
  4. SERVIDOR faz QUERY no banco
       (pergunta estruturada)
                |
  5. BANCO grava segundo o SCHEMA
       (coluna certa, tipo certo)
                |
  6. DADO DURA entre requests, sessoes, reinicios
```

## Quando a estrutura muda (migracao)

```
  SCHEMA v1 (antigo)
       tabela usuarios: nome, email
                |
        [ MIGRACAO ]
                |
  SCHEMA v2 (novo)
       tabela usuarios: nome, email, telefone

  SE o codigo novo espera v2 mas o banco ainda ta em v1 -> ERRO
  SE ninguem rodou a migracao -> codigo quebra em silencio
```

## Tipos de banco (no conceito)

```
  RELACIONAL          DOCUMENTO           CHAVE-VALOR
  +----------+        +----------+        +----------+
  | tabela   |        | doc JSON |        | chave    |
  | linhas   |        | solto    |        | valor    |
  | colunas  |        | sem rigi |        | dicionar |
  | relacoes |        | flexivel |        | rapido   |
  +----------+        +----------+        +----------+
   Postgres            MongoDB             Redis
   MySQL               CouchDB             DynamoDB
```

## Como usar no video

- Desenhar o mapa principal no inicio do ATO 1, sem explicar tudo.
- Voltar ao mapa no final de cada ato, destacando as partes cobertas.
- Mostrar o bloco de migracao quando entrar no ATO 3.
- No fim, o mapa completo mostra o dado nascendo no front e durando no banco.

## Versao para thumbnail

Texto curto sobre o diagrama:
- Titulo sobre a imagem: "Onde o dado SOBREVIVE entre requests?"
- Setas: clique -> front -> servidor -> banco
- Destacar a palavra "persistente" ao lado do banco
- Sem palavras densas; so "front", "servidor", "banco", "persistente".
