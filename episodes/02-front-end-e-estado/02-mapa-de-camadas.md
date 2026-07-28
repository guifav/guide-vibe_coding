# Mapa de camadas (para mostrar na tela / base do thumbnail)

Este é o diagrama que Gui desenha ou mostra durante o vídeo. Simples, sem ferramentas, só o ciclo do front-end e os estados que a IA esquece.

## O mapa principal: o ciclo do front-end (versão texto)

```
  USUÁRIO ABRE O SITE NO NAVEGADOR
                |
                v
  +-------------------------------------------+
  |  NAVEGADOR BAIXA OS ARQUIVOS              |
  |  - HTML  (estrutura)                      |
  |  - CSS   (aparência)                      |
  |  - JS    (comportamento)                  |
  +-------------------------------------------+
                |
                v
  +-------------------------------------------+
  |  NAVEGADOR MONTA O DOM                    |
  |  (árvore de elementos, viva na memória)   |
  +-------------------------------------------+
                |
                v
  +-------------------------------------------+
  |  RENDER: o navegador pinta os pixels      |
  |  O usuário VÊ a página na tela            |
  +-------------------------------------------+
                |
                v
  === A PARTIR DAQUI, O CICLO SE REPETE ===

  USUÁRIO INTERAGE (clica, digita, arrasta)
                |
                v
  +-------------------------------------------+
  |  EVENTO dispara                           |
  |  (o navegador percebe a ação)             |
  +-------------------------------------------+
                |
                v
  +-------------------------------------------+
  |  ESTADO muda                              |
  |  (variável / hook / store atualiza valor) |
  +-------------------------------------------+
                |
                v
  +-------------------------------------------+
  |  RE-RENDER: a tela atualiza               |
  |  (o código atualiza o DOM;                |
  |   o navegador repinta o que mudou)        |
  +-------------------------------------------+
                |
                v
  VOLTA PARA O TOPO: próxima interação
```

## Os estados que a IA esquece

Mostrar depois do ATO 3, como checklist visual:

```
  TODA TELA QUE MOSTRA DADOS TEM 5 MOMENTOS:

  +------------+    +------------+
  |  LOADING   |    |   EMPTY    |
  |  carregou? |    |  veio nada |
  |  ainda não |    |            |
  +------------+    +------------+

  +------------+    +------------+
  |   ERROR    |    |  PARTIAL   |
  |  deu ruim  |    |  veio pela |
  |            |    |  metade    |
  +------------+    +------------+

  +------------+
  |   STALE    |
  |  veio, mas |
  |  já velho  |
  +------------+
```

## Onde o estado mora (categorias, sem framework)

```
  +-----------------------+
  |  Variável LOCAL       |  <- some quando a tela fecha
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
  |  (ex: usuário logado) |
  +-----------------------+
  +-----------------------+
  |  SERVIDOR (ep. 03)    |  <- sobrevive entre sessões
  |  (ex: perfil salvo)   |
  +-----------------------+
```

## Como usar no vídeo

- Mostrar o ciclo principal no início do ATO 2, sem explicar tudo. Dizer: "esse ciclo se repete toda vez que você interage com a página".
- Voltar ao ciclo no ATO 3, agora destacando os 5 estados que a IA esquece.
- Mostrar "onde o estado mora" no momento em que falar de variável, hook e store.

## Versão para thumbnail

Texto curto sobre o diagrama:
- Título sobre a imagem: "Por que a tela MUDA sem recarregar?"
- Setas formando um ciclo: evento -> estado -> re-render -> evento
- Sem palavras densas; só "estado", "evento", "tela".
