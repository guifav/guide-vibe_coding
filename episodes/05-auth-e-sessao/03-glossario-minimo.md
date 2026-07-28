# Glossário mínimo (aparece na descrição do YouTube)

Só os termos que aparecem no roteiro. Um por linha, tradução direta.

---

## Identidade

- **Visitante (guest)** - quem chega ao site sem se identificar
- **Usuário (user)** - quem fez login e tem um nome para o servidor
- **Login** - o ato de se identificar e provar quem é você
- **Senha** - a prova de que você é quem diz ser
- **Hash** - embaralhamento sem volta; o servidor guarda o hash da senha, nunca a senha

## Memória entre requests

- **Sessão** - a memória que mora no servidor; ele guarda e te dá um identificador
- **Session ID** - identificador da sessão; viaja entre navegador e servidor via cookie
- **Cookie** - pedaço de texto que o navegador guarda e envia a cada request
- **Token** - crachá que o servidor dá depois do login; carrega dentro quem é você
- **Assinatura** - o carimbo do token; só o servidor sabe gerar, e por isso ninguém forja
- **JWT (JSON Web Token)** - um formato específico de token, muito comum

## As duas perguntas

- **Autenticação** - responde "quem é você?" (login, senha, token de identidade)
- **Autorização** - responde "o que você pode fazer?" (vem depois da autenticação)

## Permissões

- **Papel (role)** - grupo com um conjunto de permissões (admin, user, guest)
- **RBAC (Role-Based Access Control)** - nome técnico para permissão por papel
- **Permissão por recurso** - pergunta "esse item é seu?" em vez de "qual seu papel?"
- **Admin** - papel que pode tudo: ver, editar, apagar, gerenciar
- **403 (Forbidden)** - código HTTP do "não pode": o servidor nega esse acesso (o 401 é o "não sei quem você é", falta login)
- **Middleware** - código que roda antes de cada request; no auth, o porteiro que verifica o crachá

## O ciclo

- **Logoff (logout)** - o ato de encerrar a sessão ou invalidar o token
- **Expiração** - prazo de validade do token ou sessão; sem ela, vale para sempre
- **Token roubado** - se alguém intercepta seu token, se passa por você

---

## Pergunta-chave para usar com IA

Quando a IA sugerir uma mudança em código de auth, pergunte:

"Que pergunta essa verificação responde: quem é você, ou o que você pode fazer?"

As opções são:
- Autenticação (identidade, login, token válido)
- Autorização (papel, recurso, permissão)

A resposta diz o tamanho do risco de remover ou simplificar aquela linha.
