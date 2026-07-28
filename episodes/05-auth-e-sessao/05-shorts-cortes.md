# Shorts e cortes

Cada corte isola um conceito, com gancho para o vídeo completo.

---

## Short 1 - Sessão vs token: onde a memória mora?

**Gancho (0-3s):** "Sessão e token resolvem o mesmo problema. Mas a memória mora em lugares diferentes."

**Corpo:** HTTP não tem memória, cada request é um estranho. Sessão é a memória no servidor: ele guarda, te dá um session ID, você leva no cookie. Token é o crachá no cliente: carrega dentro quem é você, o servidor não guarda nada. Analogia: sessão é guarda-volumes, token é crachá no pescoço.

**CTA:** "No vídeo completo eu conto todas as camadas de auth, até o logoff. Link na descrição."

---

## Short 2 - Autenticação vs autorização: a diferença crucial

**Gancho:** "Autenticação e autorização não são a mesma coisa. Confundir as duas é onde os problemas começam."

**Corpo:** autenticação responde "quem é você?" (login, senha, token de identidade). Autorização responde "o que você pode fazer?" (papel, recurso, permissão). Você pode estar autenticado e não autorizado a apagar a conta de outro usuário. As duas juntas formam o que chamamos de auth.

**CTA:** "A história completa de como auth funciona tá no canal."

---

## Short 3 - Por que a IA sempre quer simplificar auth (e por que é perigoso)

**Gancho:** "Se a IA sugerir remover ou comentar uma verificação de auth, pare. Pergunte antes."

**Corpo:** auth é a camada que mais sofre com sugestões de simplificação. A IA fala "vamos desativar esse middleware", "vou comentar essa verificação de permissão". Cada remoção abre o servidor para o mundo. O que era protegido vira público. Regra: se a IA sugerir mexer em auth, pergunte "o que para de ser verificado se eu remover isso?".

**CTA:** "Quer entender o mapa inteiro de auth? Vídeo completo no canal."

---

## Short 4 - Token roubado: o que acontece quando seu crachá cai na mão errada

**Gancho:** "Se alguém roubar seu token, essa pessoa se passa por você. E o servidor não percebe."

**Corpo:** token é um crachá. Se é interceptado, quem tem o crachá é obedecido como se fosse você. Por isso token tem expiração (prazo de validade). Por isso logoff existe (para invalidar o crachá). Auth é um ciclo: login no começo, logoff e expiração no fim.

**CTA:** "O ciclo completo de auth tá no vídeo principal."
