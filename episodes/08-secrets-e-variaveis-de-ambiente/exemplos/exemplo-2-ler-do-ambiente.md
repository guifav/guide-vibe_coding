# Exemplo 2 - Ler do ambiente

## O que ilustra

O ATO 2 do episódio 08: o código **pergunta pelo nome** (`CHAVE_PAGAMENTO`); o **ambiente** entrega o valor. Fechadura no código, chave no ambiente — os dois não viajam juntos no repo.

## Trecho / arquivo

Ver [`exemplo-2-ler-do-ambiente.js`](./exemplo-2-ler-do-ambiente.js):

```javascript
const chave = process.env.CHAVE_PAGAMENTO;
if (!chave) {
  throw new Error("faltou CHAVE_PAGAMENTO no ambiente");
}
```

- **`process.env.CHAVE_PAGAMENTO`** — leitura pelo nome; valor vem de `.env` local ou config do servidor.
- **`throw` se faltar** — falha cedo e clara; melhor que rodar com chave vazia e falhar no pagamento.
- **Sem literal no fonte** — quem lê o repo vê só o nome, nunca o segredo.

## O que observar

- Mesmo padrão em dev (arquivo `.env`) e prod (painel de variáveis do ambiente).
- Erro explícito na subida evita deploy "verde" que quebra na primeira transação.
- IA costuma colar a chave inline para "funcionar logo" — trocar por `process.env` antes do commit.
- Nome da variável documentado no `.env.example` alinha time e deploy.

## O que quebra se faltar

| Ausência | Consequência |
|---|---|
| Leitura via ambiente | Chave hardcoded no JS; repo vira vazamento público. |
| Checagem se variável existe | App sobe; falha só quando usuário tenta pagar. |
| Variável configurada em prod | Funciona local; produção retorna erro genérico ou 500. |
| Nome estável entre ambientes | Script de deploy usa nome diferente; segredo "some" no ar. |
