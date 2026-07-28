let contagem = 0;

function incrementar() {
  contagem = contagem + 1;
  // a tela precisa ser atualizada a partir do estado
  document.getElementById("valor").textContent = String(contagem);
}
