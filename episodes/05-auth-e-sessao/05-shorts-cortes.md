# Shorts e cortes

Cada corte isola um conceito, com gancho para o vídeo completo.

---

## Short 1 - Sessao vs token: onde a memória mora?

**Gancho (0-3s):** "Sessao e token resolvem o mesmo problema. Mas a memória mora em lugares diferentes."

**Corpo:** HTTP não tem memória, cada request e um estranho. Sessao e a memória no servidor: ele guarda, te da um session ID, você leva no cookie. Token e o cracha no cliente: carrega dentro quem e você, o servidor não guarda nada. Analogia: sessao e guarda-volumes, token e cracha no pescoco.

**CTA:** "No vídeo completo eu conto todas as camadas de auth, do login ao logoff. Link na descrição."

---

## Short 2 - Autenticação vs autorização: a diferença crucial

**Gancho:** "Autenticação e autorização não são a mesma coisa. Confundir as duas e onde os problemas comecam."

**Corpo:** autenticação responde "quem e você?" (login, senha, token de identidade). Autorização responde "o que você pode fazer?" (papel, recurso, permissao). Você pode estar autenticado e não autorizado a apagar a conta de outro usuario. As duas juntas formam o que chamamos de auth.

**CTA:** "A história completa de como auth funciona ta no canal."

---

## Short 3 - Por que a IA sempre quer simplificar auth (e por que e perigoso)

**Gancho:** "Se a IA sugerir remover ou comentar uma verificação de auth, pare. Pergunte antes."

**Corpo:** auth e a camada que mais sofre com sugestoes de simplificação. A IA fala "vamos desativar esse middleware", "vou comentar essa verificação de permissao". Cada remoção abre o servidor para o mundo. O que era protegido vira público. Regra: se a IA sugerir mexer em auth, pergunte "o que para de ser verificado se eu remover isso?".

**CTA:** "Quer entender o mapa inteiro de auth? Vídeo completo no canal."

---

## Short 4 - Token roubado: o que acontece quando seu cracha cai na mao errada

**Gancho:** "Se alguém roubar seu token, essa pessoa se passa por você. E o servidor não percebe."

**Corpo:** token e um cracha. Se e interceptado, quem tem o cracha e obedecido como se fosse você. Por isso token tem expiracao (prazo de validade). Por isso logoff existe (para invalidar o cracha). Auth não e só o login, e um ciclo: login no começo, logoff e expiracao no fim.

**CTA:** "O ciclo completo de auth ta no vídeo principal."
