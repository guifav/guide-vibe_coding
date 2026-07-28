# Exemplo 1 - Login

## O que ilustra

O ATO 1 do episódio 05: o visitante vira **usuário conhecido**. O login recebe credenciais, valida quem você diz ser e devolve um **token** — o crachá que os próximos pedidos vão carregar.

## Trecho / arquivo

Ver [`exemplo-1-login.js`](./exemplo-1-login.js):

```javascript
function fazerLogin(email, senha) {
  if (!email || !senha) {
    return { ok: false, erro: "Credenciais incompletas" };
  }

  const token = "tok_exemplo_nao_usar_abc123"; // crachá fake — só ilustração

  return {
    ok: true,
    token,
    usuario: { id: 7, email },
  };
}
```

- **`email`, `senha`** — credenciais que provam identidade (ATO 1: "quem é você?").
- **`token`** — crachá genérico; em produção seria assinado pelo servidor, não inventado no front.
- **`usuario`** — dados mínimos de quem acabou de entrar; o servidor agora tem um nome para você.

## O que observar

- Login responde autenticação: transforma estranho em usuário identificado.
- O token viaja nos pedidos seguintes — HTTP sozinho não lembra quem bateu na porta.
- Senha nunca deve voltar na resposta; só o crachá e dados públicos do perfil.
- Valor `tok_exemplo_nao_usar_abc123` é fake; em produção, tokens reais exigem expiração e revogação.

## O que quebra se faltar

| Ausência | Consequência |
|---|---|
| Validação de credenciais | Qualquer email/senha entra; identidade falsa. |
| Token na resposta | Servidor não reconhece pedidos seguintes; usuário "desloga" a cada clique. |
| Hash da senha no servidor | Senha em texto no banco; vazamento expõe contas reais. |
| Tratamento de erro (`ok: false`) | Front acha que login deu certo com corpo vazio ou exceção. |
