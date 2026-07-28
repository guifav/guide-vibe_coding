# Contribuições, exemplos e merge do mantenedor — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publicar `CONTRIBUTING.md`, exemplos híbridos em cada episódio, `CODEOWNERS`, e ruleset no GitHub para que só `guifav` mergeie `main` (sem reviewer quando ele for o autor do PR).

**Architecture:** Exemplos moram em `episodes/NN-*/exemplos/` (markdown + arquivo de código opcional). Documentação de contribuição na raiz. Proteção via ruleset + CODEOWNERS; required approvals = 0; merge restrito a `guifav`.

**Tech Stack:** Markdown, snippets JS/SQL/YAML/env, GitHub Rulesets API (`gh api`), CODEOWNERS.

## Global Constraints

- PT-BR; sem emoji
- Identidade anônima: zero nomes de produtos/empresas reais
- Segredos só fake: `chave_exemplo_nao_usar`
- Exemplos curtos (didáticos), não apps executáveis
- Nada vai para `main` sem PR; só `guifav` mergeia
- Spec canônica: `docs/superpowers/specs/2026-07-28-contribuicoes-exemplos-merge-design.md`

## File map

| Path | Responsibility |
|---|---|
| `CONTRIBUTING.md` | Guia de contribuições |
| `README.md` | Link Contribuições + `exemplos/` na estrutura; texto do Gui |
| `.github/CODEOWNERS` | `* @guifav` |
| `episodes/*/exemplos/**` | Exemplos por episódio |
| `episodes/*/README.md` | Citar pasta `exemplos/` |
| GitHub ruleset `main` | Require PR; restrict merge a guifav; approvals 0 |

---

### Task 1: Branch, CONTRIBUTING, README, CODEOWNERS

**Files:**
- Create: `CONTRIBUTING.md`
- Create: `.github/CODEOWNERS`
- Modify: `README.md`
- Modify: (later tasks touch episode READMEs)

**Interfaces:**
- Produces: link `./CONTRIBUTING.md`; estrutura cita `exemplos/`

- [ ] **Step 1: Criar branch de implementação**

Se PR #7 (`fix/sem-temporadas-sequencia-unica`) ainda estiver aberto e incluir só o fix de temporadas + a spec, criar:

```bash
git checkout fix/sem-temporadas-sequencia-unica
git pull
git checkout -b feat/contribuicoes-exemplos-merge
```

Se #7 já estiver mergeado em `main`:

```bash
git checkout main && git pull
git checkout -b feat/contribuicoes-exemplos-merge
```

- [ ] **Step 2: Escrever `CONTRIBUTING.md`**

Criar o arquivo com este conteúdo completo:

```markdown
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
```

- [ ] **Step 3: Criar `.github/CODEOWNERS`**

```
* @guifav
```

- [ ] **Step 4: Atualizar `README.md`**

Aplicar (preservar princípios; incorporar tom do Gui):

1. Intro: material dos vídeos do Guilherme Favaron sobre vibe coding; ênfase em compreensão real, não aprovação por confiança cega.
2. Em **Estrutura de cada episódio**, adicionar após `05-shorts-cortes.md`:

```markdown
- `exemplos/` - trechos ilustrativos (markdown + código quando fizer sentido)
```

3. Manter **Princípios**.
4. Adicionar no fim:

```markdown
## Contribuições

Caso queira sugerir conteúdo para fortalecer este repositório, siga o guia em [`CONTRIBUTING.md`](./CONTRIBUTING.md).
```

- [ ] **Step 5: Verificar**

```bash
test -f CONTRIBUTING.md && test -f .github/CODEOWNERS
rg -n "CONTRIBUTING|exemplos/" README.md
```

Expected: arquivos existem; README cita ambos.

- [ ] **Step 6: Commit**

```bash
git add CONTRIBUTING.md .github/CODEOWNERS README.md
git commit -m "$(cat <<'EOF'
docs: CONTRIBUTING, CODEOWNERS e exemplos na estrutura do README

EOF
)"
```

---

### Task 2: Exemplos episódios 01–02

**Files:**
- Create: `episodes/01-deploy-do-zero-ao-ar/exemplos/**`
- Create: `episodes/02-front-end-e-estado/exemplos/**`
- Modify: `episodes/01-deploy-do-zero-ao-ar/README.md`
- Modify: `episodes/02-front-end-e-estado/README.md`

- [ ] **Step 1: Ep01 — criar exemplos**

`episodes/01-deploy-do-zero-ao-ar/exemplos/README.md`:

```markdown
# Exemplos — Deploy do Zero ao Ar

| Arquivo | O que ilustra |
|---|---|
| [exemplo-1-mapa.md](./exemplo-1-mapa.md) | Camadas do mapa (visão geral) |
| [exemplo-2-caminho-ao-ar.md](./exemplo-2-caminho-ao-ar.md) | Do commit ao ar |
| [exemplo-3-manifesto-minimo.md](./exemplo-3-manifesto-minimo.md) + `.json` | Extra: manifesto mínimo de um app |
```

`exemplo-1-mapa.md` — texto com o mapa em ASCII (código / navegador / servidor / API / banco / auth / build-CI-CD / domínio), bullets "o que observar", "o que quebra se faltar camada".

`exemplo-2-caminho-ao-ar.md` — sequência `commit → repo → build → CI → deploy → domínio`.

`exemplo-3-manifesto-minimo.md` + `exemplo-3-manifesto-minimo.json`:

```json
{
  "name": "app-exemplo",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "build": "echo build-exemplo",
    "start": "echo start-exemplo"
  }
}
```

Explicar: o manifesto nomeia o projeto e os scripts que o cano de build/deploy costuma chamar — sem amarrar a ferramenta real.

- [ ] **Step 2: Ep02 — criar exemplos**

`exemplo-1-pagina.html` — HTML mínimo com título + botão + parágrafo.

`exemplo-1-pagina.md` — estrutura / aparência / comportamento.

`exemplo-2-estado.js`:

```javascript
let contagem = 0;

function incrementar() {
  contagem = contagem + 1;
  // a tela precisa ser atualizada a partir do estado
  document.getElementById("valor").textContent = String(contagem);
}
```

`exemplo-2-estado.md` — estado como memória da página.

`exemplo-3-tres-estados.js` + `.md` — flags `carregando`, `erro`, `vazio` (extra).

`exemplos/README.md` indexando os três.

- [ ] **Step 3: Atualizar READMEs dos eps 01 e 02**

Na tabela de arquivos de cada README, adicionar linha:

`| \`exemplos/\` | Trechos ilustrativos (markdown + código) |`

- [ ] **Step 4: Verificar**

```bash
ls episodes/01-deploy-do-zero-ao-ar/exemplos/
ls episodes/02-front-end-e-estado/exemplos/
rg -n "produtos? reais|empresa|vercel|github actions|openai" episodes/0{1,2}-*/exemplos/ || true
```

Expected: pastas populadas; sem nomes de produtos (o `|| true` só lista matches — deve imprimir vazio).

- [ ] **Step 5: Commit**

```bash
git add episodes/01-deploy-do-zero-ao-ar episodes/02-front-end-e-estado
git commit -m "$(cat <<'EOF'
docs: exemplos ilustrativos dos episódios 01 e 02

EOF
)"
```

---

### Task 3: Exemplos episódios 03–04

**Files:**
- Create: `episodes/03-request-response-e-api/exemplos/**`
- Create: `episodes/04-banco-de-dados/exemplos/**`
- Modify: READMEs 03 e 04

- [ ] **Step 1: Ep03**

`exemplo-1-request.js`:

```javascript
// GET: pedir dados. POST: enviar dados.
const resposta = await fetch("/api/pedidos/42", { method: "GET" });
const corpo = await resposta.json();
```

`exemplo-2-contrato.json`:

```json
{
  "pedido": {
    "id": 42,
    "status": "aberto",
    "total": 19.9
  },
  "status_http_exemplo": 200
}
```

`exemplo-3-fronteira.js` — front chama API; comentário explícito: front não monta SQL.

+ markdowns e README do diretório.

- [ ] **Step 2: Ep04**

`exemplo-1-schema.sql`:

```sql
CREATE TABLE pedidos (
  id INTEGER PRIMARY KEY,
  status TEXT NOT NULL,
  total REAL NOT NULL,
  criado_em TEXT NOT NULL
);
```

`exemplo-2-query.sql`:

```sql
SELECT id, status, total
FROM pedidos
WHERE status = 'aberto';
```

`exemplo-3-migracao.sql` — extra: adicionar coluna com default seguro vs alteração destrutiva comentada como anti-padrão.

+ markdowns e README.

- [ ] **Step 3: Atualizar READMEs 03–04 + commit**

```bash
git add episodes/03-request-response-e-api episodes/04-banco-de-dados
git commit -m "$(cat <<'EOF'
docs: exemplos ilustrativos dos episódios 03 e 04

EOF
)"
```

---

### Task 4: Exemplos episódios 05–06

**Files:**
- Create: `episodes/05-auth-e-sessao/exemplos/**`
- Create: `episodes/06-git-e-versionamento/exemplos/**`
- Modify: READMEs 05 e 06

- [ ] **Step 1: Ep05**

`exemplo-1-login.js` — recebe credenciais, devolve token fake em comentário/estrutura (sem JWT de lib real nomeada se puder evitar; pode dizer "token" genérico).

`exemplo-2-permissao.js` — `if (!usuario.pode("editar_pedido")) return 403`.

`exemplo-3-auth-vs-authz.md` — autenticação = quem é; autorização = o que pode (extra, pode ser só md).

- [ ] **Step 2: Ep06**

`exemplo-1-commits.md` — linha do tempo de 3 commits descritos.

`exemplo-2-branch.md` — `main` + branch `corrige-total` + merge.

`exemplo-3-pr.md` — template mínimo de descrição de PR (o quê/por quê/como testar), sem citar plataforma.

- [ ] **Step 3: READMEs + commit**

```bash
git add episodes/05-auth-e-sessao episodes/06-git-e-versionamento
git commit -m "$(cat <<'EOF'
docs: exemplos ilustrativos dos episódios 05 e 06

EOF
)"
```

---

### Task 5: Exemplos episódios 07–08

**Files:**
- Create: `episodes/07-build-ci-cd-deploy/exemplos/**`
- Create: `episodes/08-secrets-e-variaveis-de-ambiente/exemplos/**`
- Modify: READMEs 07 e 08

- [ ] **Step 1: Ep07**

`exemplo-1-pipeline.yml`:

```yaml
# Cano genérico: cada etapa verde ou vermelho
etapas:
  - nome: lint
  - nome: testes
  - nome: build
  - nome: publicar  # só se as anteriores passaram
```

`exemplo-2-build.js` — função `buildar(fonte)` que devolve `{ ok: false, motivo }` ou artefato.

`exemplo-3-rollback-e-schema.md` — quando rollback de código não desfaz migração.

- [ ] **Step 2: Ep08**

`exemplo-1-env.env.example`:

```
CHAVE_PAGAMENTO=chave_exemplo_nao_usar
URL_BANCO=postgres://usuario:senha_exemplo@localhost:5432/app
```

`exemplo-1-env.gitignore-sample`:

```
.env
```

`exemplo-1-env.md` — .env local, nunca no repo; example só com nomes.

`exemplo-2-ler-do-ambiente.js`:

```javascript
const chave = process.env.CHAVE_PAGAMENTO;
if (!chave) {
  throw new Error("faltou CHAVE_PAGAMENTO no ambiente");
}
```

`exemplo-3-rotacao.md` — vazou → revoga → troca → verifica (apagar arquivo não basta).

- [ ] **Step 3: READMEs + varredura global**

```bash
rg -n "temporada|Vercel|GitHub Actions|OpenAI|AWS|Stripe" episodes/*/exemplos/ || true
rg -n "sk-|ghp_|AKIA" episodes/*/exemplos/ || true
```

Expected: sem matches.

- [ ] **Step 4: Commit**

```bash
git add episodes/07-build-ci-cd-deploy episodes/08-secrets-e-variaveis-de-ambiente
git commit -m "$(cat <<'EOF'
docs: exemplos ilustrativos dos episódios 07 e 08

EOF
)"
```

---

### Task 6: Ruleset no GitHub + PR

**Files:**
- Remote: ruleset em `guifav/guide-vibe_coding`
- Push da branch + PR

**Interfaces:**
- Consome: `.github/CODEOWNERS` já no repo
- Produz: ruleset ativo em `main`

- [ ] **Step 1: Criar ruleset via API**

```bash
gh api repos/guifav/guide-vibe_coding/rulesets \
  --method POST \
  --input - <<'EOF'
{
  "name": "main-maintainer-merge-only",
  "target": "branch",
  "enforcement": "active",
  "conditions": {
    "ref_name": {
      "include": ["refs/heads/main"],
      "exclude": []
    }
  },
  "rules": [
    {
      "type": "pull_request",
      "parameters": {
        "required_approving_review_count": 0,
        "dismiss_stale_reviews_on_push": false,
        "require_code_owner_review": false,
        "require_last_push_approval": false,
        "required_review_thread_resolution": false
      }
    },
    {
      "type": "restrict_dismissals",
      "parameters": {
        "restrict_dismissals": false
      }
    }
  ],
  "bypass_actors": []
}
EOF
```

Se a API recusar `restrict_dismissals` ou pedir outro shape, ajustar. Em seguida garantir restrição de quem pode mergear:

```bash
# Preferência: rule "pull_request" (já exige PR) +
# settings: só guifav com permissão de write/admin (já é dono).
# Se disponível no plano da conta, adicionar rule:
# { "type": "branch_name_pattern" } não serve.
# Usar branch protection clássica se ruleset não expuser "restrict pushes":
gh api repos/guifav/guide-vibe_coding/branches/main/protection \
  --method PUT \
  -H "Accept: application/vnd.github+json" \
  --input - <<'EOF'
{
  "required_status_checks": null,
  "enforce_admins": false,
  "required_pull_request_reviews": {
    "dismiss_stale_reviews": false,
    "require_code_owner_reviews": false,
    "required_approving_review_count": 0
  },
  "restrictions": {
    "users": ["guifav"],
    "teams": [],
    "apps": []
  },
  "allow_force_pushes": false,
  "allow_deletions": false
}
EOF
```

Nota: em repos pessoais, `restrictions` às vezes exige GitHub Pro/Team. Se a API retornar 403/422 explicando plano, documentar no PR e aplicar o máximo disponível (require PR + CODEOWNERS); o CONTRIBUTING já declara a política social.

- [ ] **Step 2: Verificar proteção**

```bash
gh api repos/guifav/guide-vibe_coding/branches/main/protection --jq '{restrictions:.restrictions.users, reviews:.required_pull_request_reviews}' 
# ou
gh api repos/guifav/guide-vibe_coding/rulesets --jq '.[].name'
```

- [ ] **Step 3: Push e abrir PR**

```bash
git push -u origin HEAD
gh pr create --title "feat: CONTRIBUTING, exemplos por episódio e merge só do mantenedor" --body "$(cat <<'EOF'
## Summary
- Guia `CONTRIBUTING.md` + link no README
- Pasta `exemplos/` nos 8 episódios (markdown + código híbrido)
- `.github/CODEOWNERS` (`@guifav`)
- Proteção de `main`: exige PR; só mantenedor mergeia; autor mantenedor mergeia sem reviewer

## Spec
- `docs/superpowers/specs/2026-07-28-contribuicoes-exemplos-merge-design.md`

## Test plan
- [ ] Abrir `CONTRIBUTING.md` e o link do README
- [ ] Abrir um `exemplos/README.md` por episódio
- [ ] `rg -i 'vercel|openai|stripe|sk-|ghp_' episodes/*/exemplos/` vazio
- [ ] Tentar merge em `main` sem PR (deve falhar) / confirmar restrictions

EOF
)"
```

Se a branch ainda empilhar o fix de temporadas, mencionar no body que o PR inclui (ou depende de) #7.

- [ ] **Step 4: Commit de follow-up só se a API exigir arquivo extra**

Só se precisar versionar algo (ex.: doc de limitações do plano). Caso contrário, encerrar.

---

## Spec coverage (self-review)

| Spec | Task |
|---|---|
| Exemplos híbridos + inventário | 2–5 |
| CONTRIBUTING + README | 1 |
| CODEOWNERS | 1 |
| Ruleset/protection + autor merge sem reviewer | 6 |
| Identidade anônima / secrets fake | Global + verify steps |
| PR, não push em main | 1 + 6 |

## Placeholder scan

Nenhum TBD/TODO restante no plano. Fallback da API de restrictions documentado se o plano GitHub bloquear.
