# Glossario minimo (aparece na descricao do YouTube)

So os termos que aparecem no roteiro. Um por linha, traducao direta.

---

## O navegador e a estrutura

- **HTML** - o que aparece na tela (texto, botao, imagem)
- **CSS** - como aparece (cor, tamanho, posicao)
- **JavaScript** - o que acontece (clicou, mudou, calculou)
- **DOM (Document Object Model)** - a arvore de elementos que o navegador cria a partir do HTML
- **No (node)** - cada elemento da arvore do DOM (um botao, um div, um texto)
- **Renderizar (render)** - o ato do navegador pintar os pixels na tela a partir do DOM

## Estado e o ciclo

- **Estado (state)** - a memoria da pagina enquanto ela esta aberta
- **Variavel** - caixinha com nome para guardar um valor que pode mudar
- **Componente** - um pedaco reutilizavel da tela (botao, lista, formulario)
- **Hook** - forma organizada de guardar o estado de um componente
- **Store (estado global)** - lugar central onde estado compartilhado entre componentes mora
- **Evento** - aviso de que o usuario fez algo (clicou, digitou, arrastou)
- **Re-render** - o navegador repintar a parte da tela que mudou
- **Reatividade** - a tela se atualizar sozinha quando o estado muda

## Os estados que a IA esquece

- **Loading** - o dado ainda nao chegou; precisa mostrar que esta carregando
- **Empty** - o dado chegou, mas a lista esta vazia
- **Error** - a chamada deu erro; o dado nao vai chegar
- **Partial** - o dado chegou pela metade
- **Stale** - o dado chegou, mas ja esta desatualizado
- **Caminho feliz** - o caso em que tudo da certo (o unico que a IA costuma tratar)

## Ferramentas

- **DevTools** - ferramenta de desenvolvedor embutida no navegador (F12)
- **Aba Elements** - onde ve a arvore do DOM
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
