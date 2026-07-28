# Exemplo 1 - Schema

## O que ilustra

O ATO 2 do episódio 04: a **estrutura** dos dados no banco. O schema define quais colunas existem, seus tipos e o que é obrigatório — a "planta" da gaveta onde os dados ficam guardados.

## Trecho / arquivo

Ver [`exemplo-1-schema.sql`](./exemplo-1-schema.sql):

```sql
CREATE TABLE pedidos (
  id INTEGER PRIMARY KEY,
  status TEXT NOT NULL,
  total REAL NOT NULL,
  criado_em TEXT NOT NULL
);
```

- **`CREATE TABLE pedidos`** — cria a tabela que guarda pedidos.
- **`id INTEGER PRIMARY KEY`** — identificador único de cada linha.
- **`status TEXT NOT NULL`** — texto obrigatório; linha sem status é rejeitada.
- **`total REAL NOT NULL`** — valor numérico obrigatório.
- **`criado_em TEXT NOT NULL`** — data/hora guardada como texto (formato definido pela aplicação).

## O que observar

- Schema é contrato persistente: diferente do JSON da API, ele sobrevive reinícios.
- `NOT NULL` impede linhas incompletas — o banco recusa inserção inválida.
- Tipos (`INTEGER`, `TEXT`, `REAL`) limitam o que cabe em cada coluna.
- Mudar schema depois exige **migração** (Exemplo 3), não basta editar o arquivo e reiniciar.

## O que quebra se faltar

| Ausência | Consequência |
|---|---|
| Tabela / schema definido | Dados ficam só em memória; somem ao reiniciar o servidor. |
| `PRIMARY KEY` em `id` | Duplicatas ou impossibilidade de referenciar um pedido específico. |
| `NOT NULL` onde importa | Linhas incompletas entram no banco; relatórios e totais ficam errados. |
| Tipos coerentes | Texto onde deveria ser número quebra cálculos e ordenação. |
