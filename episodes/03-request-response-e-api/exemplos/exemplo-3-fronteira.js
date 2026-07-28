// O front conversa só com a API — nunca monta SQL nem acessa o banco diretamente.
async function carregarPedido(id) {
  const resposta = await fetch("/api/pedidos/" + id);
  if (!resposta.ok) {
    throw new Error("Pedido não encontrado");
  }
  return resposta.json();
}
