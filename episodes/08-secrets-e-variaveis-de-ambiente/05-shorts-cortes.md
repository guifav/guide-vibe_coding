# Shorts e cortes

Cada corte isola um conceito, com gancho para o vídeo completo.

---

## Short 1 - Você publicou sua senha

**Gancho (0-3s):** "Você colou a chave de API no código e commitou? Você publicou sua senha."

**Corpo:** o repo é compartilhado; se for público, o mundo vê. Existem robôs varrendo repos públicos procurando chaves. Uma chave commitada em repo público é encontrada em minutos. Código é a fechadura, todo mundo pode ver. Segredo é a chave, só o dono carrega.

**CTA:** "No vídeo completo eu mostro onde a chave mora de verdade. Link na descrição."

---

## Short 2 - O git nunca esquece

**Gancho:** "Apagou a chave do código e commitou de novo? Não adiantou nada."

**Corpo:** commit é uma foto imutável. Se a chave entrou num commit, ela está naquela foto para sempre; apagar o arquivo hoje não apaga a foto de ontem. A única saída é rotacionar: revogar a chave antiga no painel do serviço e gerar uma nova. Trocar a fechadura, não esconder a chave copiada.

**CTA:** "O protocolo de emergência completo está no vídeo. Link na descrição."

---

## Short 3 - O que é um .env (em 60 segundos)

**Gancho:** "Todo projeto sério tem um arquivo .env. Você sabe o que ele faz?"

**Corpo:** o código pede o valor pelo nome; quem responde é o ambiente. No local, os valores moram no .env: um par nome-valor por linha. O .env NUNCA vai para o repo: ele fica listado no .gitignore. O que vai para o repo é o .env.example: os nomes, sem os valores.

**CTA:** "Como isso funciona em produção está no vídeo completo."

---

## Short 4 - As 3 perguntas antes de aceitar código da IA

**Gancho:** "A IA conectou um serviço para você? Três perguntas antes de aceitar."

**Corpo:** primeira: essa chave está no código ou no ambiente? Segunda: o .env está no .gitignore? Terceira: algum segredo aparece em log ou mensagem de erro? Se qualquer resposta estiver errada, não commita. E nunca cole a chave real no chat: use placeholder e preencha você mesmo.

**CTA:** "A checklist completa está no vídeo. Link na descrição."
