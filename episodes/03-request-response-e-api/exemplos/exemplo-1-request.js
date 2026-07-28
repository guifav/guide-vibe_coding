// GET: pedir dados. POST: enviar dados.
const resposta = await fetch("/api/pedidos/42", { method: "GET" });
const corpo = await resposta.json();
