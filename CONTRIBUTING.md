# Como contribuir

Obrigado por querer fortalecer este repositório.

## O que é este repositório

Kit de apoio dos vídeos sobre vibe coding: conceito, roteiro, mapa, glossário, SEO, shorts, pranchas e **exemplos didáticos**. Não é um produto, nem um curso de ferramenta específica.

## Como contribuir

1. Abra uma **issue** descrevendo a ideia ou a correção.
2. Espere alinhamento (escopo e abordagem).
3. Abra um **PR pequeno**, a partir de `main`, com uma mudança por assunto.

Issues e PRs de qualquer pessoa são bem-vindos.

## O que é aceito

- Correção factual ou de clareza no material
- Typos e melhorias de glossário
- Novos exemplos no padrão de `episodes/*/exemplos/`
- Ajustes que reforcem "o que quebra se isso faltar"

## O que não é aceito

- Tutorial de ferramenta ou plataforma específica
- Nomes de empresas ou produtos reais no material público
- Secrets reais (mesmo "só de teste" se forem chaves válidas)
- Rewrite grande de roteiro sem issue prévia alinhada

## Como adicionar um exemplo

1. Crie arquivos em `episodes/NN-slug/exemplos/`.
2. Nomeie `exemplo-N-slug.md` e, se ajudar, `exemplo-N-slug.<ext>`.
3. Título humano no markdown: `Exemplo N - Título`.
4. Inclua: o que ilustra, o trecho, o que observar, o que quebra se faltar.
5. Atualize `exemplos/README.md` do episódio.
6. Linguagem mista por camada (JS, SQL, YAML, env, etc.).
7. Sem emoji; identidade anônima; segredos só com valores fake (`chave_exemplo_nao_usar`).

## Regras editoriais

- PT-BR
- Sem emoji
- Identidade anônima no material de publicação
- Conceito só entra se responde "o que quebra se isso faltar"

## Merge

Somente o mantenedor (`guifav`) faz merge em `main`.

- Se o autor do PR for o mantenedor, ele pode mergear **sem reviewer**.
- PRs de outras pessoas: o mantenedor revisa e mergeia.
