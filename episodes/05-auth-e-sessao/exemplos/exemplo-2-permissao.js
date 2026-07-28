// Autorização: depois de saber quem é, decide o que pode.
const usuario = {
  id: 7,
  papel: "user",
  pode(acao) {
    const permissoes = {
      admin: ["editar_pedido", "apagar_pedido"],
      user: ["ver_pedido"],
    };
    return (permissoes[this.papel] || []).includes(acao);
  },
};

function editarPedido(usuario, pedidoId) {
  if (!usuario.pode("editar_pedido")) {
    return { status_http: 403, mensagem: "Sem permissão para editar pedidos" };
  }

  return { status_http: 200, pedidoId, resultado: "editado" };
}
