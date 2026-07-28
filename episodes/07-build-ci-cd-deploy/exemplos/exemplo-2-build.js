// Build: transforma fonte em artefato publicável ou devolve motivo da falha.
function buildar(fonte) {
  if (!fonte || fonte.trim() === "") {
    return { ok: false, motivo: "Fonte vazia — nada para transformar" };
  }

  if (fonte.includes("import inexistente")) {
    return { ok: false, motivo: "Dependência faltando no import" };
  }

  return {
    ok: true,
    artefato: {
      nome: "app-compilado.js",
      tamanho_bytes: fonte.length * 2,
      gerado_em: "2026-07-28T12:00:00Z",
    },
  };
}
