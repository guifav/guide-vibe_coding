# Shorts e cortes

Cada corte isola um conceito, com gancho para o video completo.

---

## Short 1 — Sessao vs token: onde a memoria mora?

**Gancho (0-3s):** "Sessao e token resolvem o mesmo problema. Mas a memoria mora em lugares diferentes."

**Corpo:** HTTP nao tem memoria, cada request e um estranho. Sessao e a memoria no servidor: ele guarda, te da um session ID, voce leva no cookie. Token e o cracha no cliente: carrega dentro quem e voce, o servidor nao guarda nada. Analogia: sessao e guarda-volumes, token e cracha no pescoco.

**CTA:** "No video completo eu conto todas as camadas de auth, do login ao logoff. Link na descricao."

---

## Short 2 — Autenticacao vs autorizacao: a diferenca crucial

**Gancho:** "Autenticacao e autorizacao nao sao a mesma coisa. Confundir as duas e onde os problemas comecam."

**Corpo:** autenticacao responde "quem e voce?" (login, senha, token de identidade). Autorizacao responde "o que voce pode fazer?" (papel, recurso, permissao). Voce pode estar autenticado e nao autorizado a apagar a conta de outro usuario. As duas juntas formam o que chamamos de auth.

**CTA:** "A historia completa de como auth funciona ta no canal."

---

## Short 3 — Por que a IA sempre quer simplificar auth (e por que e perigoso)

**Gancho:** "Se a IA sugerir remover ou comentar uma verificacao de auth, pare. Pergunte antes."

**Corpo:** auth e a camada que mais sofre com sugestoes de simplificacao. A IA fala "vamos desativar esse middleware", "vou comentar essa verificacao de permissao". Cada remocao abre o servidor para o mundo. O que era protegido vira publico. Regra: se a IA sugerir mexer em auth, pergunte "o que para de ser verificado se eu remover isso?".

**CTA:** "Quer entender o mapa inteiro de auth? Video completo no canal."

---

## Short 4 — Token roubado: o que acontece quando seu cracha cai na mao errada

**Gancho:** "Se alguem roubar seu token, essa pessoa se passa por voce. E o servidor nao percebe."

**Corpo:** token e um cracha. Se e interceptado, quem tem o cracha e obedecido como se fosse voce. Por isso token tem expiracao (prazo de validade). Por isso logoff existe (para invalidar o cracha). Auth nao e so o login, e um ciclo: login no comeco, logoff e expiracao no fim.

**CTA:** "O ciclo completo de auth ta no video principal."
