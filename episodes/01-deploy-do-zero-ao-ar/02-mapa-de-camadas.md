# Mapa de camadas (para mostrar na tela / base do thumbnail)

Este e o diagrama que Gui desenha ou mostra durante o vídeo. Simples, sem ferramentas, só camadas e o fluxo.

## O mapa (versao texto)

```
  Você DIGITA UM Endereço NO NAVEGADOR
                |
                v
  +-------------------------------+
  |  Domínio (ex: meuapp.com)     |  <- o endereço que o mundo encontra
  +-------------------------------+
                |
                v
  +-------------------------------+
  |  SERVIDOR (sempre ligado)     |  <- outro computador, respondendo
  |  - recebe o pedido (REQUEST)  |
  |  - chama a API (lógica)       |
  |  - consulta o BANCO (dados)   |
  |  - verifica AUTH (quem e você)|
  |  - devolve a RESPOSTA (JSON)  |
  +-------------------------------+
                |
                v
  +-------------------------------+
  |  NAVEGADOR (renderiza)        |  <- transforma a resposta em tela
  |  - FRONT-END (HTML/CSS/JS)    |
  |  - ESTADO da página           |
  +-------------------------------+
                |
                v
  Você VE A Página NA TELA
```

## O caminho de volta (deploy, contado na ordem inversa)

O deploy e a história de colocar esse servidor no ar:

```
  1. Código no seu computador
       (HTML, CSS, JS, estado, variáveis)
                |
  2. GIT / REPO
       (versionamento, commit, branch)
                |
  3. BUILD
       (transforma o código em algo servivel)
                |
  4. CI/CD
       (testa antes de publicar, automatizado)
                |
  5. DEPLOY
       (sobe para a nuvem / servidor)
                |
  6. Domínio aponta para o servidor
       (DNS, URL)
                |
  7. NO AR: alguém acessa e o ciclo acima acontece
```

## Como usar no vídeo

- Desenhar esse mapa na tela (ou em um slide simples) no início do ATO 1, sem explicar tudo.
- Voltar ao mapa no final de cada ato, destacando as camadas que já foram cobertas.
- No fim do vídeo, o mapa completo esta desenhado e o espectador ve a jornada inteira.

## Versao para thumbnail

Texto curto sobre o diagrama:
- Título sobre a imagem: "O que acontece entre o Código e o SITE?"
- Setas: computador -> nuvem -> tela
- Sem palavras densas; só "código", "servidor", "ar".
