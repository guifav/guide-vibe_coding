# Conceito do video — Git e Versionamento

## Tese

A maioria das pessoas que programa com IA hoje nao tem rede de seguranca. Ela escreve, a IA escreve, e quando algo quebra ninguem sabe como voltar. O maximo que existe e uma pasta cheia de arquivos com nomes como "versao_final_v2_agora_vai.txt".

Este video conta a historia do versionamento: por que ele existe, como funciona, e por que o deploy (o topico do episodio 01) nunca usa o codigo do seu computador e sim o codigo que esta guardado no repo, na nuvem.

O objetivo nao e ensinar a decorar comandos git. E fazer o espectador enxergar a rede de seguranca por tras de qualquer projeto serio: fotos no tempo, linhas paralelas, e um pedido formal antes de qualquer mudanca chegar na versao principal. Quando ele enxerga isso, ele entende por que "jogar direto na main" e sinal de amadorismo e por que um PR existe.

## Por que esse formato funciona

- Linear: o espectador acompanha do inicio ao fim sem se perder, porque cada conceito surge da necessidade do passo anterior. O commit nasce do problema de voltar no tempo. A branch nasce do medo de estragar o original. O PR nasce do risco de juntar sem revisar.
- Arquitetural: o mapa mental que fica e o de uma linha do tempo com ramais, nao uma lista de comandos. O espectador sai sabendo desenhar o fluxo, nao digitar git.
- Superficial de proposito: cada conceito e apresentado com uma analogia e uma consequencia. Aprofundar comandos especificos fica para videos futuros da serie.

## Publico

- Vibe coders que usam Cursor / Claude / Copilot e nunca usaram git de proposito
- Pessoas que ja ouviram falar de GitHub mas nao sabem o que e um PR ou um conflito
- Iniciantes em desenvolvimento web que querem entender por que o deploy passa pelo repo

## Tom

Direto, sem jargao desnecessario. Cada termo tecnico que aparece e imediatamente traduzido em uma frase. Didatico, nao academico. Gui falando para camera ou com tela mostrando um diagrama simples de linha do tempo.

## Estrutura em 3 atos

**ATO 1 — O problema e a foto (commit + repo)**
Onde tudo comeca. O problema de voltar no tempo sem rede de seguranca. O commit como foto do codigo. A anatomia de cada foto (mensagem, autor, data, imutavel). E o repository, o lugar onde as fotos ficam guardadas, com o GitHub como o repo na nuvem.

**ATO 2 — Trabalhando em paralelo (branch + merge + conflito)**
Ninguem quer estragar o original enquanto testa algo. A branch e a linha paralela. A main e a principal. O merge junta de volta. E o conflito, quando duas pessoas mexem no mesmo arquivo e a maquina nao decide sozinha.

**ATO 3 — O fluxo profissional (PR + review + por que o deploy usa o repo)**
Codigo novo nao entra direto na principal. O pull request e o pedido formal de merge, com revisao. O fluxo completo: branch nova, commit, push, PR, review, merge. E por que o deploy usa o repo e nao o seu computador: linha do tempo unica, colaborativa. Fecha com a ponte para o episodio 07.

## O que NAO entra neste video

- Comandos git especificos (git rebase, git cherry-pick, git stash, reflog)
- Comparacao GitHub vs GitLab vs Bitbucket
- Configuracao de hooks, pre-commit, CI dentro do git
- Git internals (objetos, trees, blobs)
- Estrategias de branching avancadas (gitflow, trunk-based)
- Resolucao detalhada de conflito ferramenta por ferramenta

Esses viram videos da serie, um por tema. Este video e o mapa mental da rede de seguranca.
