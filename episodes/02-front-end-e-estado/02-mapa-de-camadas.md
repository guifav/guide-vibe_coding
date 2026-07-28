# Mapa de camadas (para mostrar na tela / base do thumbnail)

Este e o diagrama que Gui desenha ou mostra durante o video. Simples, sem ferramentas, so o ciclo do front-end e os estados que a IA esquece.

## O mapa principal: o ciclo do front-end (versao texto)

```
  USUARIO ABRE O SITE NO NAVEGADOR
                |
                v
  +-------------------------------------------+
  |  NAVEGADOR BAIXA OS ARQUIVOS              |
  |  - HTML  (estrutura)                      |
  |  - CSS   (aparencia)                      |
  |  - JS    (comportamento)                  |
  +-------------------------------------------+
                |
                v
  +-------------------------------------------+
  |  NAVEGADOR MONTA O DOM                    |
  |  (arvore de elementos, viva na memoria)   |
  +-------------------------------------------+
                |
                v
  +-------------------------------------------+
  |  RENDER: o navegador pinta os pixels      |
  |  O usuario VE a pagina na tela            |
  +-------------------------------------------+
                |
                v
  === A PARTIR DAQUI, O CICLO SE REPETE ===

  USUARIO INTERAGE (clica, digita, arrasta)
                |
                v
  +-------------------------------------------+
  |  EVENTO dispara                           |
  |  (o navegador percebe a acao)             |
  +-------------------------------------------+
                |
                v
  +-------------------------------------------+
  |  ESTADO muda                              |
  |  (variavel / hook / store atualiza valor) |
  +-------------------------------------------+
                |
                v
  +-------------------------------------------+
  |  RE-RENDER: a tela atualiza               |
  |  (o navegador re-pinta a parte que mudou) |
  +-------------------------------------------+
                |
                v
  VOLTA PARA O TOPO: proxima interacao
```

## Os estados que a IA esquece

Mostrar depois do ATO 3, como checklist visual:

```
  TODA TELA QUE MOSTRA DADOS TEM 5 MOMENTOS:

  +------------+    +------------+
  |  LOADING   |    |   EMPTY    |
  |  carregou? |    |  veio nada |
  |  ainda nao |    |            |
  +------------+    +------------+

  +------------+    +------------+
  |   ERROR    |    |  PARTIAL   |
  |  deu ruim  |    |  veio pela |
  |            |    |  metade    |
  +------------+    +------------+

  +------------+
  |   STALE    |
  |  veio, mas |
  |  ja velho  |
  +------------+
```

## Onde o estado mora (categorias, sem framework)

```
  +-----------------------+
  |  VARIAVEL LOCAL       |  <- some quando a tela fecha
  |  (ex: contador)       |
  +-----------------------+
  +-----------------------+
  |  HOOK / ESTADO DE     |  <- vive enquanto o componente existe
  |  COMPONENTE           |
  |  (ex: lista aberta)   |
  +-----------------------+
  +-----------------------+
  |  STORE / ESTADO       |  <- compartilhado entre componentes
  |  GLOBAL               |
  |  (ex: usuario logado) |
  +-----------------------+
  +-----------------------+
  |  SERVIDOR (ep. 03)    |  <- sobrevive entre sessoes
  |  (ex: perfil salvo)   |
  +-----------------------+
```

## Como usar no video

- Mostrar o ciclo principal no inicio do ATO 2, sem explicar tudo. Dizer: "esse ciclo se repete toda vez que voce interage com a pagina".
- Voltar ao ciclo no ATO 3, agora destacando os 5 estados que a IA esquece.
- Mostrar "onde o estado mora" no momento em que falar de variavel, hook e store.

## Versao para thumbnail

Texto curto sobre o diagrama:
- Titulo sobre a imagem: "Por que a tela MUDA sem recarregar?"
- Setas formando um ciclo: evento -> estado -> re-render -> evento
- Sem palavras densas; so "estado", "evento", "tela".
