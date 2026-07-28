let carregando = true;
let erro = null;
let dados = null;

function renderizar() {
  const area = document.getElementById("conteudo");
  if (!area) return;

  if (carregando) {
    area.textContent = "Carregando...";
    return;
  }

  if (erro) {
    area.textContent = "Erro: " + erro;
    return;
  }

  if (!dados || dados.length === 0) {
    area.textContent = "Nenhum item encontrado.";
    return;
  }

  area.textContent = "Itens: " + dados.join(", ");
}

function simularSucesso(lista) {
  carregando = false;
  erro = null;
  dados = lista;
  renderizar();
}

function simularErro(mensagem) {
  carregando = false;
  erro = mensagem;
  dados = null;
  renderizar();
}

// estado inicial: ainda carregando
renderizar();
