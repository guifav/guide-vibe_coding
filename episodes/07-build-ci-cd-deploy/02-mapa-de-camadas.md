# Mapa de camadas (para mostrar na tela / base do thumbnail)

Este e o diagrama que Gui desenha ou mostra durante o video. O foco deste episodio e o cano build/CI/CD/deploy, mas no fechamento voltamos ao mapa inteiro da temporada.

## O cano (versao texto)

```
  SEU COMPUTADOR
  +-----------------------+
  | CODIGO FONTE          |
  | (o que voce escreve)  |
  +-----------------------+
              |
              v  (commit + push)
  +-----------------------+
  | REPO (nuvem)          |  <- GitHub, GitLab, etc
  +-----------------------+
              |
              v  (dispara o cano)
  ==================================================
  CANO CI/CD  (roda sozinho, toda vez que entra codigo)
  ==================================================
              |
              v
  +-----------------------+
  | LINT                  |  verde/vermelho (estilo)
  +-----------------------+
              |
              v
  +-----------------------+
  | TESTES                |  verde/vermelho (comportamento)
  +-----------------------+
              |
              v
  +-----------------------+
  | BUILD                 |  verde/vermelho (transformacao)
  | compile / minify /    |
  | tree-shake / bundle   |
  +-----------------------+
              |
              v  (CI verde = segue; vermelho = PARA)
  ==================================================
              |
              v
  +-----------------------+
  | CD (publica)          |
  +-----------------------+
              |
              v
  +-----------------------+
  | AMBIENTES             |
  | dev -> staging -> prod|
  +-----------------------+
              |
              v
  +-----------------------+
  | DEPLOY em prod        |
  | tudo-de-uma-vez /     |
  | blue-green / canary   |
  +-----------------------+
              |
              v
  +-----------------------+
  | NO AR                 |  <- usuario acessa e percebe
  +-----------------------+
```

## Quando o cano quebra

```
  commit -> [lint]   VERDE
         -> [testes] VERMELHO  <-- PARA AQUI
         -> [build]  (nao roda)
         -> [deploy] (nao roda)

  Resultado: codigo bloqueado, alguem conserta.
```

## Os ambientes

```
  LOCAL (seu PC)     -> so voce ve
       |
       v
  DEV (compartilhado) -> time joga codigo junto, quebra a vontade
       |
       v
  STAGING (ensaio)    -> copia do real, ensaia o deploy
       |
       v
  PROD (o ar)         -> usuario acessa, nao se mexe sem cuidado
```

## Estrategias de deploy

```
  TUDO-DE-UMA-VEZ
    [antiga] some -> [nova] entra
    (pode ter pausa perceptivel)

  BLUE-GREEN
    [blue: antiga]  [green: nova]
       trafego ----->  (paralelo, testa, depois troca)
    (volta facil se der problema)

  CANARY
    [nova] recebe 5% -> 10% -> 50% -> 100%
    (se quebrar, poucos perceberam)
```

## Mapa da temporada revisitado (mostrar no fechamento)

```
  EPISODIO 01: o mapa inteiro (visao geral)
       |
       +-- 02: FRONT-END E ESTADO      (navegador, HTML/CSS/JS, estado)
       |
       +-- 03: REQUEST, RESPONSE, API  (ponte navegador <-> servidor)
       |
       +-- 04: BANCO DE DADOS          (memoria de longo prazo)
       |
       +-- 05: AUTH E SESSAO           (quem e voce, o que pode)
       |
       +-- 06: GIT E VERSIONAMENTO     (rede de seguranca, voltar no tempo)
       |
       +-- 07: BUILD, CI/CD, DEPLOY    (o cano que leva ao ar) <-- voce esta aqui
```

## Como usar no video

- Mostrar o cano no inicio do ATO 1, so a estrutura, sem explicar cada etapa.
- Voltar ao cano no fim de cada cena do ATO 2, destacando a etapa que acabou de ser explicada.
- Mostrar os ambientes e as estrategias como blocos separados, visuais, dentro do ATO 2.
- No ATO 3, mostrar o cano completo em uma linha so, depois transicionar para o mapa da temporada revisitado.
- O mapa da temporada e o fechamento visual: cada camada listada com o episódio que a explicou.

## Versao para thumbnail

Texto curto sobre o diagrama:
- Titulo sobre a imagem: "O que acontece DEPOIS do commit?"
- Setas: commit -> cano -> ar
- Destacar as palavras "build", "CI/CD", "deploy" como as tres portas
- Sem ferramentas especificas, so conceitos
