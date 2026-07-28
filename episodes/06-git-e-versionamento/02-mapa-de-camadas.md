# Mapa de camadas (para mostrar na tela / base do thumbnail)

Este e o diagrama que Gui desenha ou mostra durante o video. Simples, sem ferramentas, so a linha do tempo com ramais e o fluxo.

## O mapa (versao texto)

```
  A LINHA DO TEMPO DO CODIGO
  (cada ponto = 1 commit, foto imutavel)

  ----*--------*--------*--------*----> MAIN (linha principal)
                                  |
                                  | merge (a branch entra aqui)
                                  |
                            ------*----> BRANCH (linha paralela)
                            |     |
                            *-----*    commits da feature
                            |
                          criada a partir da main
```

## O fluxo profissional completo

O fluxo que conecta o seu computador à main do repo:

```
  1. BRANCH NOVA (a partir da main)
       (linha paralela, nome descritivo)
                |
  2. COMMIT (na branch)
       (fotos com mensagem, autor, data)
                |
  3. PUSH (branch vai para a nuvem)
       (sai do seu computador, entra no repo)
                |
  4. PULL REQUEST (PR)
       (pedido formal de merge, com diff)
                |
  5. REVIEW
       (alguem olha, comenta, aprova)
                |
  6. MERGE
       (branch entra na main)
                |
  7. MAIN ATUALIZADA
       (linha do tempo unica, ponto de verdade do deploy)
```

## O que pode dar errado no meio

```
  CONFLITO: duas branches mexem no mesmo lugar
            o git não decide sozinho
            marcadores <<<<<<< ======= >>>>>>>
            resolução manual, humana

  PUSH ESQUECIDO: código só no computador
                  para o resto do mundo, não existe
                  o deploy não vê

  MERGE DIRETO NA MAIN: sem PR, sem review
                        sinal de amadorismo em projeto serio
                        código sem segundo par de olhos
```

## Como usar no video

- Desenhar a linha do tempo no inicio do ATO 1, com pontos (commits) e nada mais.
- No ATO 2, adicionar as branches saindo da main e os pontos de merge voltando.
- No ATO 3, adicionar o fluxo completo (branch -> commit -> push -> PR -> review -> merge) como uma esteira horizontal.
- No fim do video, o diagrama completo mostra a rede de seguranca inteira.

## Versao para thumbnail

Texto curto sobre o diagrama:
- Titulo sobre a imagem: "Por que NINGUEM joga direto na MAIN?"
- Linha principal em destaque (main), com branches coloridas saindo dela
- Portao de PR no meio, com seta de "merge"
- Sem palavras densas; so "branch", "PR", "merge", "main".
