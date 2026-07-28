# Exemplo 1 - Página

## O que ilustra

O ATO 1 do episódio 02: o que o navegador monta quando abre um site. HTML vira estrutura, CSS vira aparência, JavaScript vira comportamento — três papéis distintos no mesmo arquivo ou em arquivos separados.

## Trecho / arquivo

Ver [`exemplo-1-pagina.html`](./exemplo-1-pagina.html):

```html
<h1>Contador simples</h1>
<p id="valor">0</p>
<button type="button" onclick="incrementar()">Somar</button>
```

- **HTML** — título, parágrafo com id `valor`, botão que chama `incrementar()`.
- **CSS** (no `<style>`) — fonte e espaçamento; define aparência sem mudar a estrutura.
- **JavaScript** (via `<script>`) — comportamento: reage ao clique (detalhado no Exemplo 2).

## O que observar

- Cada camada tem um trabalho: estrutura ≠ aparência ≠ comportamento.
- O `id="valor"` liga HTML ao JavaScript — sem esse gancho, o script não sabe onde escrever.
- O botão dispara um **evento** (clique); o JS escuta e reage.
- Abrir o HTML no navegador já monta o DOM — não precisa de servidor para este exemplo.

## O que quebra se faltar

| Ausência | Consequência |
|---|---|
| HTML (estrutura) | Nada aparece na tela; navegador não tem o que montar. |
| CSS | Página funciona, mas ilegível ou sem hierarquia visual. |
| JavaScript (quando a tela precisa reagir) | Botão clica e nada muda; interatividade morta. |
| `id` no elemento alvo | Script roda, mas não encontra onde atualizar o texto. |
