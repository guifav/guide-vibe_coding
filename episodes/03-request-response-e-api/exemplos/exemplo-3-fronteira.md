# Exemplo 3 - Fronteira (extra)

## O que ilustra

O ATO 3 do episódio 03: o front **não deveria saber nada do banco**. Só conversa com a API. Essa separação de camadas é o que mantém o sistema são — quando a IA mistura as camadas, o problema começa.

## Trecho / arquivo

Ver [`exemplo-3-fronteira.js`](./exemplo-3-fronteira.js):

```javascript
// O front conversa só com a API — nunca monta SQL nem acessa o banco diretamente.
async function carregarPedido(id) {
  const resposta = await fetch("/api/pedidos/" + id);
  if (!resposta.ok) {
    throw new Error("Pedido não encontrado");
  }
  return resposta.json();
}
```

- **`fetch("/api/pedidos/...")`** — front fala só com a API, não com o banco.
- **`resposta.ok`** — checa status antes de parsear; fronteira respeitada também na resposta.
- **Sem SQL no front** — query, schema e migração ficam no servidor (tema do episódio 04).

## O que observar

- O front conhece URLs e contratos JSON; o servidor conhece banco e regras de negócio.
- Misturar camadas (SQL no navegador, credencial de banco no front) expõe dados e quebra deploy.
- A IA às vezes gera `SELECT ...` dentro do componente — anti-padrão clássico.
- Trocar o banco no servidor não deveria exigir mudar o front, se a API mantiver o contrato.

## O que quebra se faltar

| Ausência | Consequência |
|---|---|
| Fronteira front/API | Lógica de banco vaza para o navegador; difícil testar e trocar camadas. |
| API como única porta | Front acoplado ao schema do banco; mudança de coluna quebra a tela. |
| Checagem de `resposta.ok` | Erro 404/500 vira JSON inválido ou exceção obscura. |
| Contrato estável na API | Servidor muda formato sem avisar; front quebra em produção. |
