# Exemplo 3 - Auth vs authz (extra)

## O que ilustra

O ATO 3 do episódio 05: as **duas perguntas** que toda camada de auth responde. **Autenticação** = quem é você; **autorização** = o que você pode fazer. Confundir as duas é erro clássico — e a IA costuma misturar.

## Trecho / arquivo

| Pergunta | Nome técnico | Exemplo no fluxo |
|---|---|---|
| Quem é você? | **Autenticação** | Login com email/senha; token válido no pedido |
| O que você pode fazer? | **Autorização** | `usuario.pode("editar_pedido")` antes de editar |

Sequência correta:

1. Pedido chega **sem token** → 401 (não autenticado).
2. Pedido chega **com token válido**, mas papel `user` tenta apagar tudo → 403 (autenticado, não autorizado).
3. Pedido chega **com token válido** e papel `admin` → ação permitida.

Analogia do episódio: autenticação é mostrar crachá na portaria; autorização é a sala específica que o crachá abre.

## O que observar

- Token válido não significa "pode tudo" — só prova identidade.
- Middleware de auth costuma responder a primeira pergunta; regra de negócio responde a segunda.
- Remover checagem de login afeta autenticação; remover `pode(...)` afeta autorização — riscos diferentes.
- Pergunta-chave do episódio para a IA: "Que pergunta essa linha responde?"

## O que quebra se faltar

| Ausência | Consequência |
|---|---|
| Autenticação | Estranhos entram como se fossem usuários; dados vazam. |
| Autorização | Usuários logados fazem qualquer ação; um `user` vira admin de fato. |
| Ordem correta (auth antes de authz) | Checa permissão de quem ainda não se identificou — lógica invertida. |
| Respostas HTTP distintas (401 vs 403) | Front e logs não distinguem "falta login" de "sem permissão". |
