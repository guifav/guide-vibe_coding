# Exemplo 2 - Query

## O que ilustra

O ATO 2 do episódio 04: como o servidor **pergunta** algo ao banco. A query é a frase que pede dados — filtra, seleciona colunas e devolve só o que a aplicação precisa.

## Trecho / arquivo

Ver [`exemplo-2-query.sql`](./exemplo-2-query.sql):

```sql
SELECT id, status, total
FROM pedidos
WHERE status = 'aberto';
```

- **`SELECT id, status, total`** — quais colunas trazer de volta (não traz `criado_em`).
- **`FROM pedidos`** — de qual tabela ler.
- **`WHERE status = 'aberto'`** — filtro: só pedidos abertos.

## O que observar

- Query roda no **servidor**, não no navegador — reforça a fronteira do episódio 03.
- Selecionar só colunas necessárias evita vazar dados e reduz tráfego.
- `WHERE` define o recorte; sem filtro, a query traz tudo — perigoso em tabelas grandes.
- O resultado da query vira JSON na API; o contrato da API deve refletir o que a query devolve.

## O que quebra se faltar

| Ausência | Consequência |
|---|---|
| Query correta | Servidor devolve dados errados, vazios ou de outra tabela. |
| Filtro (`WHERE`) | Lista traz pedidos fechados junto; regra de negócio violada. |
| Colunas alinhadas ao contrato da API | Front espera `total`, query não seleciona — campo some na resposta. |
| Query no lugar certo (servidor) | SQL no front expõe estrutura interna e credenciais. |
