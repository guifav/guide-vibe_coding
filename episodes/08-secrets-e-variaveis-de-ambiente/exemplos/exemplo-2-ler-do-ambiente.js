// Código pede pelo nome; quem responde é o ambiente (nunca hardcode no fonte).
const chave = process.env.CHAVE_PAGAMENTO;
if (!chave) {
  throw new Error("faltou CHAVE_PAGAMENTO no ambiente");
}
