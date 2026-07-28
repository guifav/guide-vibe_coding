# Exemplo 2 - Permissão

## O que ilustra

O ATO 3 do episódio 05: **autorização** — depois de saber quem é o usuário, o servidor decide **o que ele pode fazer**. Um `user` comum não edita pedido de outro; tentativa honesta devolve **403 Forbidden**.

## Trecho / arquivo

Ver [`exemplo-2-permissao.js`](./exemplo-2-permissao.js):

```javascript
function editarPedido(usuario, pedidoId) {
  if (!usuario.pode("editar_pedido")) {
    return { status_http: 403, mensagem: "Sem permissão para editar pedidos" };
  }

  return { status_http: 200, pedidoId, resultado: "editado" };
}
```

- **`usuario.pode("editar_pedido")`** — checagem de permissão por papel antes da ação.
- **`403`** — "sei quem você é, mas não pode fazer isso" (diferente de 401, que é "não sei quem você é").
- **`papel: "user"`** — papel define o conjunto de ações permitidas (admin vs user vs guest).

## O que observar

- Autenticação vem antes; autorização vem depois — ordem importa.
- 403 é resposta honesta: identidade válida, ação negada.
- Permissão por papel (`admin`, `user`) é o padrão mais comum no dia a dia.
- Remover a linha do `if (!usuario.pode(...))` é o tipo de "simplificação" que a IA sugere e que abre buraco.

## O que quebra se faltar

| Ausência | Consequência |
|---|---|
| Checagem `pode("editar_pedido")` | Qualquer usuário logado edita qualquer pedido. |
| Distinção 401 vs 403 | Front trata "falta login" igual a "sem permissão"; UX confusa. |
| Papel atribuído ao usuário | Todos viram admin implicitamente ou ninguém faz nada. |
| Verificação no servidor | Só esconder botão no front; API ainda aceita o pedido malicioso. |
