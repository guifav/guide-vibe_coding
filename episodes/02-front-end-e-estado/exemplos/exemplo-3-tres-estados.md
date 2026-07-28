# Exemplo 3 - Três estados (extra)

## O que ilustra

O ATO 3 do episódio 02: além do "caminho feliz", toda página real precisa tratar **carregando**, **erro** e **vazio**. A IA costuma entregar só a lista cheia; estes flags evitam tela em branco ou mensagem genérica.

## Trecho / arquivo

Ver [`exemplo-3-tres-estados.js`](./exemplo-3-tres-estados.js):

```javascript
let carregando = true;
let erro = null;
let dados = null;

function renderizar() {
  if (carregando) { /* ... */ return; }
  if (erro) { /* ... */ return; }
  if (!dados || dados.length === 0) { /* vazio */ return; }
  /* caminho feliz: mostrar dados */
}
```

Três flags de estado:

- **`carregando`** — pedido ainda não terminou; usuário precisa de feedback.
- **`erro`** — algo falhou; mensagem clara beats tela branca.
- **`dados` vazio** — sucesso, mas sem itens; diferente de erro e de loading.

## O que observar

- A ordem dos `if` importa: checar loading antes de erro evita flash de mensagem errada.
- `erro` e `dados` mutuamente exclusivos após a resposta — limpar um ao setar o outro.
- "Vazio" não é erro: a chamada funcionou, só não há registros.
- Funções `simularSucesso` e `simularErro` existem para testar os caminhos sem servidor real.

## O que quebra se faltar

| Estado não tratado | Consequência |
|---|---|
| Carregando | Usuário vê lista vazia ou layout quebrado enquanto espera. |
| Erro | Falha de rede vira tela branca ou dados antigos sem aviso. |
| Vazio | Usuário acha que o app quebrou quando a lista legitimately está vazia. |
| Qualquer um dos três | IA entrega demo que "funciona no caminho feliz" e quebra em produção real. |
