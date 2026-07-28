# Glossario minimo (aparece na descricao do YouTube)

So os termos que aparecem no roteiro. Um por linha, traducao direta.

---

## A rede de seguranca basica

- **Git** - sistema de versionamento; tira fotos do codigo no tempo
- **Commit** - o ato de tirar uma foto do codigo em um momento especifico
- **Mensagem do commit** - o que mudou, escrito em uma frase
- **Imutavel** - depois de tirada, a foto nao muda; fica ruim, tira outra
- **Repo (repositorio)** - onde as fotos do codigo ficam guardadas (ex: GitHub)
- **GitHub** - plataforma de repo na nuvem (tem tambem GitLab, Bitbucket)

## Trabalhando em paralelo

- **Branch** - linha paralela para mexer sem estragar a original
- **Main** - a linha principal, a versao oficial do projeto (antigamente: master)
- **Master** - nome antigo da main, ainda aparece em projetos velhos
- **Merge** - juntar a branch de volta na linha principal
- **Conflito** - quando duas pessoas mexem no mesmo lugar; o git nao decide sozinho
- **Diff** - a diferenca entre duas versões, linha por linha

## O fluxo profissional

- **Push** - mandar a branch do computador para o repo na nuvem
- **Pull request (PR)** - pedido formal de merge, com revisao antes
- **Review** - o ato de alguem olhar o codigo do PR antes de aprovar
- **Fluxo completo** - branch nova, commit, push, PR, review, merge

## Por que o deploy usa o repo

- **Linha do tempo unica** - a main do repo e o ponto de verdade do projeto
- **Colaborativo** - varias pessoas em branches diferentes convergem no repo
- **Deploy** - pega a main do repo, nao o codigo do seu computador

---

## Pergunta-chave para usar com IA

Quando a IA sugerir uma mudanca no codigo, pergunte:

"Essa mudanca vai entrar por PR ou direto na main?"

Se for direto na main, em projeto serio, pergunte por que.

As opcoes do fluxo sao:
- Branch nova a partir da main
- Commits na branch
- Push para o repo
- Pull request com diff
- Review de alguem
- Merge na main

A resposta diz se a mudanca vai passar pela rede de seguranca ou se vai entrar pela porta dos fundos.
