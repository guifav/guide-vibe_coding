# Mapa de camadas (para mostrar na tela / base do thumbnail)

Este é o diagrama que Gui desenha ou mostra durante o vídeo. Simples, sem ferramentas, só camadas e o fluxo.

O vídeo percorre duas jornadas distintas. Este mapa mostra as duas, separadas para não confundir.

## Jornada 1: fluxo de publicação (a linha principal do vídeo)

Como o código sai do computador e chega ao ar.

```
  1. Código no seu computador
       (HTML, CSS, JS)
                |
  2. GIT / REPO
       (versionamento, commit, branch)
                |
  3. BUILD (em muitos projetos; em projetos simples pode ir direto)
       (transforma o código em algo servível)
                |
  4. CI/CD
       (testa antes de publicar, automatizado)
                |
  5. DEPLOY
       (sobe para a nuvem / servidor)
                |
  6. Domínio aponta para o servidor
       (DNS, URL; costuma continuar apontando para o mesmo serviço)
                |
  7. NO AR
```

## Jornada 2: fluxo de uso (a volta final, ~90s no encerramento)

O que acontece quando alguém acessa a URL já publicada.

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
  |  - executa a lógica (API)     |
  |  - consulta o BANCO (dados)   |
  |  - verifica AUTH              |
  |    (autenticação: quem é você)|
  |    (autorização: o que pode)  |
  |  - devolve a RESPOSTA         |
  |    (a página, ou um JSON)     |
  +-------------------------------+
                |
                v
  +-------------------------------+
  |  NAVEGADOR (renderiza)        |  <- transforma a resposta em tela
  |  - FRONT-END (HTML/CSS/JS)    |
  +-------------------------------+
                |
                v
  Você VÊ A Página NA TELA
       (a página pode ter estado; isso é o ep02)
```

## Como usar no vídeo

- Desenhar o mapa na tela (ou em um slide simples) no início do ATO 1, mostrando as duas jornadas em cor clara, sem explicar tudo.
- O fluxo de publicação é percorrido nos atos 1, 2 e 3.
- O fluxo de uso é percorrido uma única vez, no encerramento (~90s), como a "volta final".
- Voltar ao mapa no final de cada ato, destacando as camadas que já foram cobertas.
- No fim do vídeo, o mapa completo está desenhado e o espectador vê as duas jornadas inteiras.

## Versão para thumbnail

Texto curto sobre o diagrama:
- Título sobre a imagem: "O que acontece entre o Código e o SITE?"
- Setas: computador -> nuvem -> tela
- Sem palavras densas; só "código", "servidor", "ar".
