# Exemplo 2 - Estado

## O que ilustra

O ATO 2 do episódio 02: a página tem **memória** enquanto está aberta. A variável `contagem` guarda o valor; quando o usuário clica, o estado muda e a tela precisa refletir isso — o ciclo evento → estado → re-render.

## Trecho / arquivo

Ver [`exemplo-2-estado.js`](./exemplo-2-estado.js):

```javascript
let contagem = 0;

function incrementar() {
  contagem = contagem + 1;
  document.getElementById("valor").textContent = String(contagem);
}
```

- **`contagem`** — estado: memória da página enquanto a aba está aberta.
- **`incrementar`** — handler do evento: lê estado, calcula novo valor, escreve no DOM.
- A linha que atualiza `textContent` é o **re-render manual** — em frameworks, isso costuma ser automático.

## O que observar

- Mudar só a variável **sem** atualizar o DOM deixa a tela desatualizada — o número na memória e o número na tela divergem.
- Estado vive na memória do navegador; recarregar a página zera `contagem` (volta a 0).
- O ciclo se repete: clique → estado muda → DOM atualiza → usuário vê o novo valor.
- Em apps maiores, o estado mora em variável, hook ou store — a lógica do ciclo é a mesma.

## O que quebra se faltar

| Ausência | Consequência |
|---|---|
| Variável de estado | Cada clique não acumula; tela sempre mostra o mesmo. |
| Atualização do DOM após mudar estado | Memória correta, tela errada — bug clássico de "funciona no console". |
| Função ligada ao evento | Botão não dispara mudança; contador congelado. |
| Persistência (fora deste exemplo) | Fechar aba apaga tudo — tema do episódio 03 (estado no servidor). |
