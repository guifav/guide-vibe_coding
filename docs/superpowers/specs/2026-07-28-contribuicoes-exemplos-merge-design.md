# Design: CONTRIBUTING, proteção de merge e exemplos por episódio

Data: 2026-07-28  
Repo: `guifav/guide-vibe_coding`  
Status: aguardando review do Gui

## Objetivo

1. Documentar como contribuir (`CONTRIBUTING.md` + link no README).
2. Configurar o GitHub para que **somente `guifav` possa fazer merge em `main`**, mantendo issues e PRs abertos a qualquer pessoa.
3. Criar pasta `exemplos/` em cada episódio, no formato híbrido (markdown + arquivo de código quando ajudar), ilustrando o conteúdo do episódio e permitindo extras ilustrativos.

## Fora de escopo

- CI obrigatória / status checks.
- Issue/PR templates.
- Reescrever roteiros ou pranchas.
- Exemplos executáveis como app completo (não há servidor, deps instaláveis nem monorepo de demos).

---

## 1. Exemplos por episódio

### Localização

```
episodes/NN-slug/
  exemplos/
    README.md
    exemplo-1-titulo.md
    exemplo-1-titulo.<ext>    # opcional, quando o código isolado ajudar
    exemplo-2-titulo.md
    ...
```

### Convenções

- Arquivo: `exemplo-N-slug` em kebab-case.
- Título no markdown: `Exemplo N - Título` (ex.: `Exemplo 1 - API`).
- Linguagem do código **mista por camada**: JS no front/API, SQL no banco, YAML no CI, `.env.example` em secrets, etc.
- Identidade anônima: zero nomes de produtos/empresas reais.
- Segredos: só valores obviamente falsos (`chave_exemplo_nao_usar`).
- Sem emoji.

### Conteúdo mínimo de cada `.md`

1. O que ilustra (1–2 frases, amarrado ao ato/roteiro).
2. Trecho ou referência ao arquivo de código.
3. O que observar (2–4 bullets).
4. O que quebra se isso faltar.

### Inventário inicial

Cada episódio cobre o núcleo do vídeo; 1 extra ilustrativo é permitido.

| Ep | Exemplos (títulos humanos) | Extensões típicas |
|---|---|---|
| 01 | Exemplo 1 - Mapa; Exemplo 2 - Caminho ao ar; Exemplo 3 - Manifesto mínimo (extra) | `.md`, `.json` |
| 02 | Exemplo 1 - Pagina; Exemplo 2 - Estado; Exemplo 3 - Tres estados (extra) | `.html`, `.js` |
| 03 | Exemplo 1 - Request; Exemplo 2 - Contrato; Exemplo 3 - Fronteira (extra) | `.js`, `.json` |
| 04 | Exemplo 1 - Schema; Exemplo 2 - Query; Exemplo 3 - Migracao (extra) | `.sql` |
| 05 | Exemplo 1 - Login; Exemplo 2 - Permissao; Exemplo 3 - Auth vs authz (extra) | `.js` |
| 06 | Exemplo 1 - Commits; Exemplo 2 - Branch; Exemplo 3 - PR (extra) | `.md`, texto |
| 07 | Exemplo 1 - Pipeline; Exemplo 2 - Build; Exemplo 3 - Rollback e schema (extra) | `.yml`, `.js`/`.sh` |
| 08 | Exemplo 1 - Env; Exemplo 2 - Ler do ambiente; Exemplo 3 - Rotacao (extra) | `.env.example`, `.js`, `.gitignore` sample |

O `exemplos/README.md` de cada episódio lista os arquivos com uma linha de descrição cada.

### Atualização da estrutura do episódio

No README raiz e nos READMEs de episódio (onde listar estrutura), incluir:

- `exemplos/` - trechos ilustrativos do episódio (markdown + código quando fizer sentido)

---

## 2. CONTRIBUTING e README

### `CONTRIBUTING.md` (raiz)

Seções:

1. **O que é este repositório** — kit dos vídeos + exemplos didáticos; não é produto nem curso de ferramenta.
2. **Como contribuir** — abrir issue → alinhar → PR pequeno.
3. **Aceito** — correção factual, clareza, typos, glossário, novos exemplos no padrão.
4. **Não aceito** — tutorial de ferramenta específica; nomes de produtos reais; secrets reais; rewrite grande de roteiro sem issue prévia.
5. **Como adicionar um exemplo** — seguir a seção 1; atualizar `exemplos/README.md` do episódio.
6. **Regras editoriais** — PT-BR; sem emoji; identidade anônima; “o que quebra se isso faltar”.
7. **Fluxo de PR** — branch a partir de `main`; descrição do porquê; um assunto por PR.
8. **Merge** — somente o mantenedor (`guifav`) mergeia em `main`. Issues e PRs de qualquer pessoa são bem-vindos. Se o autor do PR for o mantenedor, ele pode mergear **sem reviewer**.

### README raiz

- Incorporar ajustes de texto do Gui (crédito / tom), se ainda estiverem só no editor.
- Seção **Contribuições** apontando para [`CONTRIBUTING.md`](./CONTRIBUTING.md).
- Em **Estrutura de cada episódio**, citar `exemplos/`.
- Manter a seção **Princípios** (não substituir por Contribuições).

---

## 3. Proteção do GitHub

### Política

| Quem | Issues | Abrir PR | Merge em `main` |
|---|---|---|---|
| Qualquer pessoa | sim | sim | não |
| `guifav` (mantenedor), autor do PR | — | sim | sim, **sem reviewer obrigatório** |
| `guifav`, PR de outra pessoa | — | — | sim (após review dele, por processo; sem gate duro de N approvals) |

### Implementação

1. Arquivo `.github/CODEOWNERS` com:

   ```
   * @guifav
   ```

2. **Ruleset** (ou branch protection) em `main`:
   - Require a pull request before merging.
   - Restrict who can push/merge matching branches → só `guifav`.
   - Required approvals: **0** (para o mantenedor autor do PR poder mergear sem reviewer).
   - Sem required status checks neste momento.
   - Bypass do ruleset: não necessário se approvals = 0 e restrict merge = guifav.

3. Issues permanecem habilitadas; forks/PRs externos aceitos.

### Efeito

- Contribuidores externos: abrem PR; só `guifav` mergeia.
- PRs do próprio `guifav`: merge direto após o PR (sem depender de segundo reviewer).

---

## Critérios de pronto

- [ ] `CONTRIBUTING.md` na raiz e link no README.
- [ ] `exemplos/` nos 8 episódios com README + inventário acima.
- [ ] `.github/CODEOWNERS` commitado.
- [ ] Ruleset/protection aplicada em `main` via API/`gh`.
- [ ] Zero menções a produtos reais e zero secrets reais nos exemplos.
- [ ] Trabalho em branch + PR (não commit direto em `main`).

## Notas de implementação

- Continuar na branch atual de trabalho ou abrir branch dedicada a partir de `main`/`fix/sem-temporadas-*` conforme o estado do PR #7; preferir um PR focado neste design se #7 já estiver só sobre “sem temporadas”.
- Exemplos são didáticos e curtos (dezenas de linhas), não apps.
