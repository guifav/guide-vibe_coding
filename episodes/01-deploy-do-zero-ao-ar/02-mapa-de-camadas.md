# Mapa de camadas (para mostrar na tela / base do thumbnail)

Este e o diagrama que Gui desenha ou mostra durante o video. Simples, sem ferramentas, so camadas e o fluxo.

## O mapa (versao texto)

```
  VOCE DIGITA UM ENDERECO NO NAVEGADOR
                |
                v
  +-------------------------------+
  |  DOMINIO (ex: meuapp.com)     |  <- o endereco que o mundo encontra
  +-------------------------------+
                |
                v
  +-------------------------------+
  |  SERVIDOR (sempre ligado)     |  <- outro computador, respondendo
  |  - recebe o pedido (REQUEST)  |
  |  - chama a API (logica)       |
  |  - consulta o BANCO (dados)   |
  |  - verifica AUTH (quem e voce)|
  |  - devolve a RESPOSTA (JSON)  |
  +-------------------------------+
                |
                v
  +-------------------------------+
  |  NAVEGADOR (renderiza)        |  <- transforma a resposta em tela
  |  - FRONT-END (HTML/CSS/JS)    |
  |  - ESTADO da pagina           |
  +-------------------------------+
                |
                v
  VOCE VE A PAGINA NA TELA
```

## O caminho de volta (deploy, contado na ordem inversa)

O deploy e a historia de colocar esse servidor no ar:

```
  1. CODIGO no seu computador
       (HTML, CSS, JS, estado, variaveis)
                |
  2. GIT / REPO
       (versionamento, commit, branch)
                |
  3. BUILD
       (transforma o codigo em algo servivel)
                |
  4. CI/CD
       (testa antes de publicar, automatizado)
                |
  5. DEPLOY
       (sobe para a nuvem / servidor)
                |
  6. DOMINIO aponta para o servidor
       (DNS, URL)
                |
  7. NO AR: alguem acessa e o ciclo acima acontece
```

## Como usar no video

- Desenhar esse mapa na tela (ou em um slide simples) no inicio do ATO 1, sem explicar tudo.
- Voltar ao mapa no final de cada ato, destacando as camadas que ja foram cobertas.
- No fim do video, o mapa completo esta desenhado e o espectador ve a jornada inteira.

## Versao para thumbnail

Texto curto sobre o diagrama:
- Titulo sobre a imagem: "O que acontece entre o CODIGO e o SITE?"
- Setas: computador -> nuvem -> tela
- Sem palavras densas; so "codigo", "servidor", "ar".
