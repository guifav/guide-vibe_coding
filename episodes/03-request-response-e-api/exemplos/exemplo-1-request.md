# Exemplo 1 - Request

## O que ilustra

O ATO 1 do episódio 03: o navegador **pede** algo ao servidor. O pedido tem um **método** (GET para ler, POST para enviar) e bate num **endpoint** — uma URL específica no servidor.

## Trecho / arquivo

Ver [`exemplo-1-request.js`](./exemplo-1-request.js):

```javascript
// GET: pedir dados. POST: enviar dados.
const resposta = await fetch("/api/pedidos/42", { method: "GET" });
const corpo = await resposta.json();
```

- **`fetch`** — função do navegador que envia o pedido.
- **`/api/pedidos/42`** — endpoint: a "porta" onde o servidor atende pedidos de pedido nº 42.
- **`method: "GET"`** — estou pedindo dados, não enviando.
- **`resposta.json()`** — transforma o corpo da resposta em objeto JavaScript.

## O que observar

- GET e POST são os dois métodos mais comuns no dia a dia; cada um tem um papel.
- A URL identifica **o quê** você quer; o método identifica **o que fazer** com isso.
- `await` espera a resposta chegar — a conversa não é instantânea.
- O endpoint `/api/pedidos/42` é convenção; o servidor define quais portas existem.

## O que quebra se faltar

| Ausência | Consequência |
|---|---|
| Método correto | Servidor recusa ou interpreta errado (ex.: GET onde deveria ser POST). |
| Endpoint válido | 404 — o servidor não sabe o que entregar nessa URL. |
| `await` / tratamento da resposta | Código segue antes da resposta chegar; tela mostra `undefined`. |
| URL coerente com o contrato | Front pede em um lugar; servidor responde em outro — bug silencioso. |
