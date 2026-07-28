# Shorts e cortes

Cada corte isola um conceito, com gancho para o vídeo completo.

---

## Short 1 - DOM: o que o navegador monta quando abre um site

**Gancho (0-3s):** "Você abre um site. O navegador não mostra o código. Ele monta uma árvore. Chama DOM."

**Corpo:** o navegador baixa tres tipos de arquivo. HTML vira estrutura, CSS vira aparencia, JavaScript vira comportamento. O navegador le esses arquivos e cria o DOM, uma árvore de elementos viva na memória. Cada botao, texto e imagem que você ve na tela e um no nessa árvore. Renderizar e pintar os pixels a partir dessa árvore.

**CTA:** "No vídeo completo eu mostro o ciclo inteiro do front-end. Link na descrição."

---

## Short 2 - Estado: por que a tela muda sem recarregar

**Gancho:** "Você clica num botao e a tela muda. Sem recarregar. Como?"

**Corpo:** a página tem memória. Chama estado. Estado e a diferença entre uma página morta e uma página viva. Onde mora? Variável local para coisas simples. Estado de componente (que alguns frameworks chamam de hook). Store para estado compartilhado entre componentes. Quando o estado muda, o código atualiza o DOM e o navegador repinta a parte que depende dele.

**CTA:** "O ciclo completo (evento, estado, re-render) ta no vídeo principal."

---

## Short 3 - O ciclo: evento, estado, re-render

**Gancho:** "Toda vez que você interage com a página, o mesmo ciclo acontece. Tres passos."

**Corpo:** primeiro, evento. Você clica, digita, arrasta. O navegador dispara um aviso. Segundo, estado muda. O código atualiza o valor guardado. Terceiro, re-render. O código atualiza o DOM e o navegador repinta a tela. Isso se repete toda vez. Evento, estado, re-render. Isso e reatividade: a tela se atualizar sozinha quando o estado muda.

**CTA:** "Quer entender o front-end sem jargao? Vídeo completo no canal."

---

## Short 4 - Os 5 estados que a IA esquece

**Gancho:** "A IA faz sua tela funcionar no caminho feliz. E esquece cinco coisas."

**Corpo:** toda tela que mostra dados tem cinco momentos. Loading: o dado ainda não chegou. Empty: chegou, mas a lista esta vazia. Error: a chamada deu erro, o dado não vem. Partial: chegou pela metade. Stale: chegou, mas já esta desatualizado. A IA trata só o caso em que tudo da certo. Os outros ela esquece. Por isso sua tela quebra quando algo da errado.

**CTA:** "A checklist completa ta no vídeo principal. Link na descrição."
