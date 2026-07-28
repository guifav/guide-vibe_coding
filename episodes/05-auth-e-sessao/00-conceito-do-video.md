# Conceito do vídeo - Auth e Sessão

## Tese

A maioria das pessoas que programa com IA hoje não enxerga a diferença entre "quem é você" e "o que você pode fazer". Para a IA, auth é uma palavra que aparece no código. Para quem decide, falta o mapa de como o servidor descobre identidade e enforce limites.

Este vídeo conta a história de um login, do visitante anônimo até o logoff, em ordem cronológica. Não é curso de cada protocolo de segurança. É a narrativa de uma jornada: você chega como estranho, o servidor te reconhece, te dá um crachá, e a partir daí cada pedido seu carrega esse crachá até ele expirar ou ser revogado.

O objetivo é fazer o espectador enxergar as duas perguntas que toda camada de auth responde: "quem é você?" e "você pode fazer isso?". Quando ele enxerga, ele para de aceitar quando a IA sugere "simplificar" auth e começa a perguntar "que pergunta essa mudança para de responder?".

## Por que esse formato funciona

- Linear: o espectador acompanha o vídeo inteiro sem se perder, porque cada conceito surge da necessidade do passo anterior.
- Arquitetural: o mapa mental que fica é o de fluxo de identidade (visitante -> login -> sessão -> token -> permissão -> logoff), não uma lista de bibliotecas.
- Superficial de propósito: cada conceito é apresentado com uma analogia e uma consequência. Aprofundar fica para vídeos futuros da série.

## Público

- Vibe coders que usam Cursor / Claude / Copilot e não sabem o que é um token
- Pessoas de produto / negócio que dialogam com devs e querem entender o contexto
- Iniciantes em desenvolvimento web que já ouviram "auth", "sessão", "JWT" mas não sabem a diferença

## Tom

Direto, sem jargão desnecessário. Cada termo técnico que aparece é imediatamente traduzido em uma frase. Didático. Gui falando para câmera ou com tela mostrando um diagrama simples.

## Estrutura em 3 atos

**ATO 1 - O problema e o login (sem auth, qualquer um vê tudo)**
O mundo sem auth: qualquer pessoa pede qualquer coisa e o servidor obedece. Por que isso não funciona. O que muda quando você faz login: você vira conhecido. O servidor agora tem um nome para você.

**ATO 2 - Como o servidor lembra de você (sessão e token)**
HTTP não tem memória. Cada request é um estranho batendo na porta. Sessão é como o servidor cria uma memória entre requests. Token é o crachá que o servidor te dá depois do login, e que cada request carrega para o servidor saber quem bateu.

**ATO 3 - Quem pode o que (autenticação vs autorização, permissões, perigos)**
A diferença crucial: autenticação responde "quem é você?", autorização responde "o que você pode fazer?". Permissões por papel (admin, user, guest) e por recurso (esse item é seu?). Por que remover ou mexer em auth é sempre perigoso, especialmente quando a IA sugere "simplificar". O que pode dar errado: logoff, expiração, token roubado. Fecha com a ponte para o episódio 06: antes de mexer nisso com segurança, precisamos de uma rede de proteção.

## O que Não entra neste vídeo

- Implementação de JWT passo a passo, assinatura, chaves públicas/privadas
- OAuth, OpenID Connect, SSO, provedores de identidade (Google, GitHub login)
- Criptografia de senha (hash, bcrypt, salt) em profundidade
- Ataques específicos (CSRF, XSS, SQL injection focado em auth)
- Comparação de bibliotecas (Auth0, Firebase Auth, NextAuth, Supabase Auth)
- MFA, 2FA, biometria

Esses viram vídeos da série, um por tema. Este vídeo é o mapa conceitual.
