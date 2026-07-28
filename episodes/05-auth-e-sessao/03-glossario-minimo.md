# Glossario minimo (aparece na descrição do YouTube)

Só os termos que aparecem no roteiro. Um por linha, tradução direta.

---

## Identidade

- **Visitante (guest)** - quem chega ao site sem se identificar
- **Usuario (user)** - quem fez login e tem um nome para o servidor
- **Login** - o ato de se identificar e provar quem e você
- **Senha** - a prova de que você e quem diz ser
- **Hash** - embaralhamento sem volta; o servidor guarda o hash da senha, nunca a senha

## Memória entre requests

- **Sessao** - a memória que mora no servidor; ele guarda e te da um identificador
- **Session ID** - identificador da sessao; viaja entre navegador e servidor via cookie
- **Cookie** - pedaco de texto que o navegador guarda e envia a cada request
- **Token** - cracha que o servidor da depois do login; carrega dentro quem e você
- **Assinatura** - o carimbo do token; só o servidor sabe gerar, e por isso ninguém forja
- **JWT (JSON Web Token)** - um formato especifico de token, muito comum

## As duas perguntas

- **Autenticação** - responde "quem e você?" (login, senha, token de identidade)
- **Autorização** - responde "o que você pode fazer?" (vem depois da autenticação)

## Permissoes

- **Papel (role)** - grupo com um conjunto de permissoes (admin, user, guest)
- **RBAC (Role-Based Access Control)** - nome técnico para permissao por papel
- **Permissao por recurso** - pergunta "esse item e seu?" em vez de "qual seu papel?"
- **Admin** - papel que pode tudo: ver, editar, apagar, gerenciar
- **403 (Forbidden)** - código HTTP do "não pode": o servidor nega esse acesso (o 401 e o "não sei quem você e", falta login)
- **Middleware** - código que roda antes de cada request; no auth, o porteiro que verifica o cracha

## O ciclo

- **Logoff (logout)** - o ato de encerrar a sessao ou invalidar o token
- **Expiracao** - prazo de validade do token ou sessao; sem ela, vale para sempre
- **Token roubado** - se alguém intercepta seu token, se passa por você

---

## Pergunta-chave para usar com IA

Quando a IA sugerir uma mudança em código de auth, pergunte:

"Que pergunta essa verificação responde: quem e você, ou o que você pode fazer?"

As opcoes são:
- Autenticação (identidade, login, token valido)
- Autorização (papel, recurso, permissao)

A resposta diz o tamanho do risco de remover ou simplificar aquela linha.
