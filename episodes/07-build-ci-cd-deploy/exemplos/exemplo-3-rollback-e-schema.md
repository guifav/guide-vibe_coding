# Exemplo 3 - Rollback e schema (extra)

## O que ilustra

O ATO 3 do episódio 07: **rollback** nem sempre desfaz tudo. Se o deploy alterou o **schema** do banco (nova coluna, tabela renomeada), voltar só o código pode deixar app e banco incompatíveis — o incidente piora.

## Trecho / arquivo

Cenário ilustrativo (deploy com migração + rollback parcial):

```
Deploy v2 (segunda-feira)
  ├── Código: passa a ler coluna "observacao" em pedidos
  └── Migração: ALTER TABLE pedidos ADD COLUMN observacao TEXT

Incidente (terça-feira)
  └── Rollback de código para v1 (sem a coluna no código)

Estado após rollback só de código:
  ├── App v1: não conhece "observacao"
  └── Banco: coluna "observacao" ainda existe (migração não foi revertida)

Risco: queries da v1 ignoram a coluna (ok), mas v2 parcial ou jobs
       antigos podem falhar; re-deploy da v2 assume schema já migrado.
```

- **Rollback de código** — troca o binário/artefato por versão anterior.
- **Migração de schema** — mudança persistente no banco; não some ao reverter código.
- **Compatibilidade** — app e schema precisam combinar; um sem o outro gera erro em cascata.

## O que observar

- Rollback rápido salva quando só o código estava errado.
- Se a migração já rodou em produção, reverter código exige plano para o banco também.
- Ordem comum segura: migração compatível com versão antiga e nova, ou feature flag.
- Post-mortem pergunta: "o rollback resolveu ou só trocou um erro por outro?".

## O que quebra se faltar

| Ausência | Consequência |
|---|---|
| Plano de rollback com schema | Voltar código deixa app lendo colunas que não existem (ou o contrário). |
| Migração reversível ou compatível | Única saída é downtime ou conserto manual no banco. |
| Teste em staging com migração | Surpresa só aparece em produção no primeiro deploy grande. |
| Registro do que o deploy alterou | Time não sabe se rollback parcial basta ou se precisa reverter SQL. |
