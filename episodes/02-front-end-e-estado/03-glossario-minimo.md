# Glossario minimo (aparece na descrição do YouTube)

Só os termos que aparecem no roteiro. Um por linha, tradução direta.

---

## O navegador e a estrutura

- **HTML** - o que aparece na tela (texto, botao, imagem)
- **CSS** - como aparece (cor, tamanho, posição)
- **JavaScript** - o que acontece (clicou, mudou, calculou)
- **DOM (Document Object Model)** - a árvore de elementos que o navegador cria a partir do HTML
- **No (node)** - cada elemento da árvore do DOM (um botao, um div, um texto)
- **Renderizar (render)** - o ato do navegador pintar os pixels na tela a partir do DOM

## Estado e o ciclo

- **Estado (state)** - a memória da página enquanto ela esta aberta
- **Variável** - caixinha com nome para guardar um valor que pode mudar
- **Componente** - um pedaco reutilizavel da tela (botao, lista, formulario)
- **Hook** - forma organizada de guardar o estado de um componente
- **Store (estado global)** - lugar central onde estado compartilhado entre componentes mora
- **Evento** - aviso de que o usuario fez algo (clicou, digitou, arrastou)
- **Re-render** - o navegador repintar a parte da tela que mudou
- **Reatividade** - a tela se atualizar sozinha quando o estado muda

## Os estados que a IA esquece

- **Loading** - o dado ainda não chegou; precisa mostrar que esta carregando
- **Empty** - o dado chegou, mas a lista esta vazia
- **Error** - a chamada deu erro; o dado não vai chegar
- **Partial** - o dado chegou pela metade
- **Stale** - o dado chegou, mas já esta desatualizado
- **Caminho feliz** - o caso em que tudo da certo (o único que a IA costuma tratar)

## Ferramentas

- **DevTools** - ferramenta de desenvolvedor embutida no navegador (F12)
- **Aba Elements** - onde ve a árvore do DOM
- **Aba Network** - onde ve os arquivos e pedidos chegando

---

## Pergunta-chave para usar com IA

Quando algo quebra na tela, pergunte em tres partes:

1. O evento esta disparando?
2. O estado esta mudando?
3. A tela esta re-renderizando?

E quando a IA gerar uma tela que mostra dados, cobre os cinco:

"Tratou loading, empty, error, partial e stale?"

A resposta diz o quanto da vida real aquela tela cobre.
