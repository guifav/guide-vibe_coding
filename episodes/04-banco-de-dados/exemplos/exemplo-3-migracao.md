# Exemplo 3 - Migração (extra)

## O que ilustra

O ATO 3 do episódio 04: quando a **estrutura muda**, nasce a migração. Adicionar coluna com default seguro preserva dados existentes; apagar coluna ou tabela sem plano é anti-padrão que a IA costuma sugerir de forma casual.

## Trecho / arquivo

Ver [`exemplo-3-migracao.sql`](./exemplo-3-migracao.sql):

```sql
-- Migração segura: nova coluna com valor padrão para linhas existentes
ALTER TABLE pedidos ADD COLUMN observacao TEXT NOT NULL DEFAULT '';

-- Anti-padrão (NÃO fazer em produção sem plano de rollback):
-- ALTER TABLE pedidos DROP COLUMN total;
-- DROP TABLE pedidos;
```

- **`ADD COLUMN ... DEFAULT ''`** — linhas antigas recebem string vazia; ninguém quebra.
- **`NOT NULL` com default** — novas linhas também precisam do campo, mas o default cobre o vazio inicial.
- **`DROP COLUMN` / `DROP TABLE` comentados** — lembrete do que **não** fazer sem backup e plano.

## O que observar

- Migração é mudança de schema **em produção**, não só editar o arquivo local.
- Default seguro evita que linhas existentes fiquem inválidas ao adicionar coluna obrigatória.
- Remover coluna que o código ainda lê quebra a API na hora — coordenar deploy e migração.
- A IA às vezes propõe `DROP TABLE` para "recomeçar"; em ambiente real isso apaga dados.

## O que quebra se faltar

| Ausência | Consequência |
|---|---|
| Migração ao mudar schema | Código espera coluna que não existe; queries falham em produção. |
| Default ao adicionar `NOT NULL` | Inserção em linhas antigas falha; deploy trava. |
| Plano antes de `DROP` | Dados perdidos sem recuperação; downtime longo. |
| Ordem deploy ↔ migração | App novo lê coluna antes da migração rodar — erro em cascata. |
