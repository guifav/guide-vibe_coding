# Glossário mínimo (aparece na descrição do YouTube)

Só os termos que aparecem no roteiro. Um por linha, tradução direta.

---

## O navegador e a estrutura

- **HTML** - o que aparece na tela (texto, botão, imagem)
- **CSS** - como aparece (cor, tamanho, posição)
- **JavaScript** - o que acontece (clicou, mudou, calculou)
- **DOM (Document Object Model)** - a árvore de elementos que o navegador cria a partir do HTML
- **Nó (node)** - cada elemento da árvore do DOM (um botão, um div, um texto)
- **Renderizar (render)** - o ato do navegador pintar os pixels na tela a partir do DOM

## Estado e o ciclo

- **Estado (state)** - a memória da página enquanto ela está aberta
- **Variável** - caixinha com nome para guardar um valor que pode mudar
- **Componente** - um pedaço reutilizável da tela (botão, lista, formulário)
- **Hook** - nome que alguns frameworks dão à forma organizada de guardar o estado de um componente
- **Store (estado global)** - lugar central onde estado compartilhado entre componentes mora
- **Evento** - aviso de que o usuário fez algo (clicou, digitou, arrastou)
- **Re-render** - o código (ou o framework) atualizar o DOM quando o estado muda; o navegador repinta o resultado
- **Reatividade** - a tela se atualizar sozinha quando o estado muda (trabalho do framework, não do navegador)
- **Framework** - kit de estrutura pronta (componentes, re-render, convenções) sobre o qual o seu front roda
- **Sessão** - memória que o servidor guarda sobre você entre requests (tema do ep05)

## Os estados que a IA esquece

- **Loading** - o dado ainda não chegou; precisa mostrar que está carregando
- **Empty** - o dado chegou, mas a lista está vazia
- **Error** - a chamada deu erro; o dado não vai chegar
- **Partial** - o dado chegou pela metade
- **Stale** - o dado chegou, mas já está desatualizado
- **Caminho feliz** - o caso em que tudo dá certo (o único que a IA costuma tratar)

## Ferramentas

- **DevTools** - ferramenta de desenvolvedor embutida no navegador (F12)
- **Aba Elements** - onde vê a árvore do DOM
- **Aba Network** - onde vê os arquivos e pedidos chegando

---

## Pergunta-chave para usar com IA

Quando algo quebra na tela, pergunte em três partes:

1. O evento está disparando?
2. O estado está mudando?
3. A tela está re-renderizando?

E quando a IA gerar uma tela que mostra dados, cobre os cinco:

"Tratou loading, empty, error, partial e stale?"

A resposta diz o quanto da vida real aquela tela cobre.
