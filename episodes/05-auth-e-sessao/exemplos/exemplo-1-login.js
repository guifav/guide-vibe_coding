// Login: credenciais entram, token de sessão sai.
function fazerLogin(email, senha) {
  if (!email || !senha) {
    return { ok: false, erro: "Credenciais incompletas" };
  }

  // Em produção: comparar hash da senha, nunca a senha em texto.
  const token = "tok_exemplo_nao_usar_abc123"; // crachá fake — só ilustração

  return {
    ok: true,
    token, // cada request seguinte carrega esse crachá
    usuario: { id: 7, email },
  };
}
