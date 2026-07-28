# Glossario minimo (aparece na descricao do YouTube)

So os termos que aparecem no roteiro. Um por linha, traducao direta.

---

## Identidade

- **Visitante (guest)** — quem chega ao site sem se identificar
- **Usuario (user)** — quem fez login e tem um nome para o servidor
- **Login** — o ato de se identificar e provar quem e voce
- **Senha** — a prova de que voce e quem diz ser
- **Hash** — embaralhamento sem volta; o servidor guarda o hash da senha, nunca a senha

## Memoria entre requests

- **Sessao** — a memoria que mora no servidor; ele guarda e te da um identificador
- **Session ID** — identificador da sessao; viaja entre navegador e servidor via cookie
- **Cookie** — pedaco de texto que o navegador guarda e envia a cada request
- **Token** — cracha que o servidor da depois do login; carrega dentro quem e voce
- **JWT (JSON Web Token)** — um formato especifico de token, muito comum

## As duas perguntas

- **Autenticacao** — responde "quem e voce?" (login, senha, token de identidade)
- **Autorizacao** — responde "o que voce pode fazer?" (vem depois da autenticacao)

## Permissoes

- **Papel (role)** — grupo com um conjunto de permissoes (admin, user, guest)
- **RBAC (Role-Based Access Control)** — nome tecnico para permissao por papel
- **Permissao por recurso** — pergunta "esse item e seu?" em vez de "qual seu papel?"
- **Admin** — papel que pode tudo: ver, editar, apagar, gerenciar
- **403 (Forbidden)** — codigo HTTP que significa "voce esta autenticado, mas nao autorizado"

## O ciclo

- **Logoff (logout)** — o ato de encerrar a sessao ou invalidar o token
- **Expiracao** — prazo de validade do token ou sessao; sem ela, vale para sempre
- **Token roubado** — se alguem intercepta seu token, se passa por voce

---

## Pergunta-chave para usar com IA

Quando a IA sugerir uma mudanca em codigo de auth, pergunte:

"Que pergunta essa verificacao responde: quem e voce, ou o que voce pode fazer?"

As opcoes sao:
- Autenticacao (identidade, login, token valido)
- Autorizacao (papel, recurso, permissao)

A resposta diz o tamanho do risco de remover ou simplificar aquela linha.
