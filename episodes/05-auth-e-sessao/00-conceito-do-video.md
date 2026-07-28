# Conceito do vídeo - Auth e Sessao

## Tese

A maioria das pessoas que programa com IA hoje não enxerga a diferença entre "quem e você" e "o que você pode fazer". Para a IA, auth e uma palavra que aparece no código. Para quem decide, falta o mapa de como o servidor descobre identidade e enforce limites.

Este vídeo conta a história de um login, do visitante anônimo ate o logoff, em ordem cronologica. Não e curso de cada protocolo de seguranca. E a narrativa de uma jornada: você chega como estranho, o servidor te reconhece, te da um cracha, e a partir dai cada pedido seu carrega esse cracha ate ele expirar ou ser revogado.

O objetivo não e ensinar a implementar auth. E fazer o espectador enxergar as duas perguntas que toda camada de auth responde: "quem e você?" e "você pode fazer isso?". Quando ele enxerga, ele para de aceitar quando a IA sugere "simplificar" auth e comeca a perguntar "que pergunta essa mudança para de responder?".

## Por que esse formato funciona

- Linear: o espectador acompanha do início ao fim sem se perder, porque cada conceito surge da necessidade do passo anterior.
- Arquitetural: o mapa mental que fica e o de fluxo de identidade (visitante -> login -> sessao -> token -> permissao -> logoff), não uma lista de bibliotecas.
- Superficial de proposito: cada conceito e apresentado com uma analogia e uma consequencia. Aprofundar fica para vídeos futuros da série.

## Público

- Vibe coders que usam Cursor / Claude / Copilot e não sabem o que e um token
- Pessoas de produto / negocio que dialogam com devs e querem entender o contexto
- Iniciantes em desenvolvimento web que já ouviram "auth", "sessao", "JWT" mas não sabem a diferença

## Tom

Direto, sem jargao desnecessario. Cada termo técnico que aparece e imediatamente traduzido em uma frase. Didático, não academico. Gui falando para camera ou com tela mostrando um diagrama simples.

## Estrutura em 3 atos

**ATO 1 - O problema e o login (sem auth, qualquer um ve tudo)**
O mundo sem auth: qualquer pessoa pede qualquer coisa e o servidor obedece. Por que isso não funciona. O que muda quando você faz login: de visitante para conhecido. O servidor agora tem um nome para você.

**ATO 2 - Como o servidor lembra de você (sessao e token)**
HTTP não tem memória. Cada request e um estranho batendo na porta. Sessao e como o servidor cria uma memória entre requests. Token e o cracha que o servidor te da depois do login, e que cada request carrega para o servidor saber quem bateu.

**ATO 3 - Quem pode o que (autenticação vs autorização, permissoes, perigos)**
A diferença crucial: autenticação responde "quem e você?", autorização responde "o que você pode fazer?". Permissoes por papel (admin, user, guest) e por recurso (esse item e seu?). Por que remover ou mexer em auth e sempre perigoso, especialmente quando a IA sugere "simplificar". O que pode dar errado: logoff, expiracao, token roubado. Fecha com a ponte para o episodio 06: antes de mexer nisso com seguranca, precisamos de uma rede de protecao.

## O que Não entra neste vídeo

- Implementacao de JWT passo a passo, assinatura, chaves publicas/privadas
- OAuth, OpenID Connect, SSO, provedores de identidade (Google, GitHub login)
- Criptografia de senha (hash, bcrypt, salt) em profundidade
- Ataques especificos (CSRF, XSS, SQL injection focado em auth)
- Comparacao de bibliotecas (Auth0, Firebase Auth, NextAuth, Supabase Auth)
- MFA, 2FA, biometria

Esses viram vídeos da série, um por tema. Este vídeo e o mapa conceitual.
