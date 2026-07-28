# Shorts e cortes

Cada corte isola uma ideia do episodio, com gancho para o vídeo completo.

---

## Short 1 - Por que o servidor não guarda seu dado?

**Gancho (0-3s):** "O servidor até pode lembrar de você. Mas essa memória não e confiável."

**Corpo:** o processo do servidor pode guardar coisas em memória, mas pode reiniciar a qualquer momento, rodar em varias cópias, e uma cópia não vê o que a outra guardou. Para dados que precisam durar e aparecer em outros dispositivos (conta, pedido, configuração), existe o banco de dados. Sem banco, dado some no primeiro reinício.

**CTA:** "No vídeo completo eu conto como o banco funciona por dentro. Link na descrição."

---

## Short 2 - Front não e banco (o erro classico)

**Gancho:** "A IA disse que salvou. Mas ela mentiu. Salvou no front."

**Corpo:** estado da página morre quando fecha a aba. Dado de negocio (KPI, catalogo, comercio) precisa atravessar o servidor e chegar no banco. Salvar no navegador e perder no próximo computador. Regra: se e de todos ou precisa durar, vai para o banco.

**CTA:** "Quer entender a diferença? Vídeo completo no canal."

---

## Short 3 - Query: a pergunta do servidor ao banco

**Gancho:** "O servidor não abre o banco como um arquivo. Ele pergunta."

**Corpo:** query e a pergunta estruturada. Pode buscar, gravar, alterar, contar. O banco responde sem saber se você perguntou certo. Query errada costuma gerar erro, mas se a aplicação ignora ou trata mal, o problema fica em silêncio.

**CTA:** "A anatomia do banco ta no vídeo principal. Link na bio."

---

## Short 4 - Migracao: o que a IA ignora

**Gancho:** "A IA adicionou uma coluna no código. Esqueceu da migracao. Seu app vai quebrar."

**Corpo:** schema e a estrutura do banco. Quando muda, nasce a migracao: instrucoes que atualizam o banco de uma versao para outra. Sem migracao, o código novo espera uma estrutura que o banco ainda não tem. O banco avisa que a coluna não existe; o problema e quando a aplicação ignora o erro.

**CTA:** "Esse e o erro mais comum com IA. Vídeo completo no canal."
