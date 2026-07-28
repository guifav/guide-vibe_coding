# Mapa de camadas (para mostrar na tela / base do thumbnail)

Este é o diagrama que Gui desenha ou mostra durante o vídeo. Simples, sem ferramentas, só camadas e o fluxo.

## O mapa (versão texto)

```
  USUÁRIO CLICA OU DIGITA
                |
                v
  +-------------------------------+
  |  NAVEGADOR (front)            |  <- estado da página (morre ao fechar)
  |  - variáveis locais           |
  |  - memória enquanto a aba vive|
  +-------------------------------+
                |
                | request com dado
                v
  +-------------------------------+
  |  SERVIDOR (memória não      |  <- memória não confiável:
  |   confiável)                |     pode reiniciar, rodar em
  |  - recebe o pedido          |     várias cópias, não
  |  - decide o que fazer       |     compartilha entre elas
  +-------------------------------+
                |
                | query
                v
  +-------------------------------+
  |  BANCO DE DADOS (persistente) |  <- onde o dado sobrevive
  |  - SCHEMA (estrutura)         |
  |  - QUERY (pergunta/resultado) |
  |  - MIGRAÇÃO (quando muda)     |
  +-------------------------------+
                |
                | resultado
                v
  SERVIDOR RESPONDE E O DADO DURA
```

## O caminho do dado (do clique a durar para sempre)

```
  1. USUÁRIO CLICA no front
       (estado da página muda, ainda não salvou)
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
  6. DADO DURA entre requests, sessões, reinícios
```

## Quando a estrutura muda (migração)

```
  SCHEMA v1 (antigo)
       tabela usuarios: nome, email
                |
        [ MIGRAÇÃO ]
                |
  SCHEMA v2 (novo)
       tabela usuarios: nome, email, telefone

  SE o código novo espera v2 mas o banco ainda tá em v1 -> ERRO
  SE ninguém rodou a migração -> o banco reclama que a coluna não existe
  SE a aplicação ignorar o erro -> o dado some sem aviso ao usuário
```

## Tipos de banco (no conceito)

```
  RELACIONAL          DOCUMENTO           CHAVE-VALOR
  +----------+        +----------+        +----------+
  | tabela   |        | doc JSON |        | chave    |
  | linhas   |        | solto    |        | valor    |
  | colunas  |        | sem rigi |        | dicionar |
  | relações |        | flexível |        | rápido   |
  +----------+        +----------+        +----------+
   banco relacional            banco de documentos             banco chave-valor
```

## Como usar no vídeo

- Desenhar o mapa principal no início do ATO 1, sem explicar tudo.
- Voltar ao mapa no final de cada ato, destacando as partes cobertas.
- Mostrar o bloco de migração quando entrar no ATO 3.
- No fim, o mapa completo mostra o dado nascendo no front e durando no banco.

## Versão para thumbnail

Texto curto sobre o diagrama:
- Título sobre a imagem: "Onde o dado SOBREVIVE entre requests?"
- Setas: clique -> front -> servidor -> banco
- Destacar a palavra "persistente" ao lado do banco
- Sem palavras densas; só "front", "servidor", "banco", "persistente".
