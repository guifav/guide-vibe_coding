# Conceito do vídeo - Git e Versionamento

## Tese

A maioria das pessoas que programa com IA hoje não tem rede de seguranca. Ela escreve, a IA escreve, e quando algo quebra ninguém sabe como voltar. O maximo que existe e uma pasta cheia de arquivos com nomes como "versao_final_v2_agora_vai.txt".

Este vídeo conta a história do versionamento: por que ele existe, como funciona, e por que o deploy (o topico do episodio 01) nunca usa o código do seu computador e sim o código que esta guardado no repo, na nuvem.

O objetivo não e ensinar a decorar comandos git. E fazer o espectador enxergar a rede de seguranca por tras de qualquer projeto serio: fotos no tempo, linhas paralelas, e um pedido formal antes de qualquer mudança chegar na versao principal. Quando ele enxerga isso, ele entende por que "jogar direto na main" e sinal de amadorismo e por que um PR existe.

## Por que esse formato funciona

- Linear: o espectador acompanha do início ao fim sem se perder, porque cada conceito surge da necessidade do passo anterior. O commit nasce do problema de voltar no tempo. A branch nasce do medo de estragar o original. O PR nasce do risco de juntar sem revisar.
- Arquitetural: o mapa mental que fica e o de uma linha do tempo com ramais, não uma lista de comandos. O espectador sai sabendo desenhar o fluxo, não digitar git.
- Superficial de proposito: cada conceito e apresentado com uma analogia e uma consequencia. Aprofundar comandos especificos fica para vídeos futuros da série.

## Público

- Vibe coders que usam Cursor / Claude / Copilot e nunca usaram git de proposito
- Pessoas que já ouviram falar de GitHub mas não sabem o que e um PR ou um conflito
- Iniciantes em desenvolvimento web que querem entender por que o deploy passa pelo repo

## Tom

Direto, sem jargao desnecessario. Cada termo técnico que aparece e imediatamente traduzido em uma frase. Didático, não academico. Gui falando para camera ou com tela mostrando um diagrama simples de linha do tempo.

## Estrutura em 3 atos

**ATO 1 - O problema e a foto (commit + repo)**
Onde tudo comeca. O problema de voltar no tempo sem rede de seguranca. O commit como foto do código. A anatomia de cada foto (mensagem, autor, data, imutavel). E o repository, o lugar onde as fotos ficam guardadas, com o GitHub como o repo na nuvem.

**ATO 2 - Trabalhando em paralelo (branch + merge + conflito)**
Ninguém quer estragar o original enquanto testa algo. A branch e a linha paralela. A main e a principal. O merge junta de volta. E o conflito, quando duas pessoas mexem no mesmo arquivo e a máquina não decide sozinha.

**ATO 3 - O fluxo profissional (PR + review + por que o deploy usa o repo)**
Código novo não entra direto na principal. O pull request e o pedido formal de merge, com revisão. O fluxo completo: branch nova, commit, push, PR, review, merge. E por que o deploy usa o repo e não o seu computador: linha do tempo única, colaborativa. Fecha com a ponte para o episodio 07.

## O que Não entra neste vídeo

- Comandos git especificos (git rebase, git cherry-pick, git stash, reflog)
- Comparacao GitHub vs GitLab vs Bitbucket
- Configuração de hooks, pre-commit, CI dentro do git
- Git internals (objetos, trees, blobs)
- Estratégias de branching avancadas (gitflow, trunk-based)
- Resolução detalhada de conflito ferramenta por ferramenta

Esses viram vídeos da série, um por tema. Este vídeo e o mapa mental da rede de seguranca.
