# Glossário mínimo (aparece na descrição do YouTube)

Só os termos que aparecem no roteiro. Um por linha, tradução direta.

---

## A rede de segurança básica

- **Git** - sistema de versionamento; tira fotos do código no tempo
- **Commit** - o ato de tirar uma foto do código em um momento específico
- **Mensagem do commit** - o que mudou, escrito em uma frase
- **Imutável** - depois de tirada, a foto não muda; fica ruim, tira outra
- **Repo (repositório)** - onde as fotos do código ficam guardadas (no seu computador ou na nuvem)
- **Repo remoto** - a cópia do repo hospedada na nuvem, acessível pelo time inteiro

## Trabalhando em paralelo

- **Branch** - linha paralela para mexer sem estragar a original
- **Main** - a linha principal, a versão oficial do projeto (antigamente: master)
- **Master** - nome antigo da main, ainda aparece em projetos velhos
- **Merge** - juntar a branch de volta na linha principal
- **Conflito** - quando duas pessoas mexem no mesmo lugar; o git não decide sozinho
- **Diff** - a diferença entre duas versões, linha por linha

## O fluxo profissional

- **Push** - mandar a branch do computador para o repo na nuvem
- **Pull request (PR)** - pedido formal de merge, com revisão antes
- **Review** - o ato de alguém olhar o código do PR antes de aprovar
- **Fluxo completo** - branch nova, commit, push, PR, review, merge

## Por que o deploy usa o repo

- **Linha do tempo única** - a main do repo é o ponto de verdade do projeto
- **Colaborativo** - várias pessoas em branches diferentes convergem no repo
- **Deploy** - pega a main do repo, não o código do seu computador

---

## Pergunta-chave para usar com IA

Quando a IA sugerir uma mudança no código, pergunte:

"Essa mudança vai entrar por PR ou direto na main?"

Se for direto na main, em projeto sério, pergunte por quê.

As opções do fluxo são:
- Branch nova a partir da main
- Commits na branch
- Push para o repo
- Pull request com diff
- Review de alguém
- Merge na main

A resposta diz se a mudança vai passar pela rede de segurança ou se vai entrar pela porta dos fundos.
