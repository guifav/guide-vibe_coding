# Mapa de camadas (para mostrar na tela / base do thumbnail)

Este é o diagrama que Gui desenha ou mostra durante o vídeo. O foco deste episódio é o cano build/CI/CD/deploy, mas no fechamento voltamos ao mapa inteiro das camadas.

## O cano (versão texto)

```
  SEU COMPUTADOR
  +-----------------------+
  | Código FONTE          |
  | (o que você escreve)  |
  +-----------------------+
              |
              v  (commit + push)
  +-----------------------+
  | REPO (nuvem)          |  <- plataforma de repositório remoto
  +-----------------------+
              |
              v  (dispara o cano)
  ==================================================
  CANO CI/CD  (roda sozinho, toda vez que entra código)
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
  | BUILD                 |  verde/vermelho (transformação)
  | traduz sintaxe /     |
  | reduz tamanho /      |
  | remove e junta       |
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
  | blue-green / canary   |
  +-----------------------+
              |
              v
  +-----------------------+
  | NO AR                 |  <- usuário acessa e percebe
  +-----------------------+
```

## Quando o cano quebra

```
  commit -> [lint]   VERDE
         -> [testes] VERMELHO  <-- PARA AQUI
         -> [build]  (não roda)
         -> [deploy] (não roda)

  Resultado: código bloqueado, alguém conserta.
```

## Os ambientes

```
  LOCAL (seu PC)     -> só você vê
       |
       v
  DEV (compartilhado) -> time joga código junto, quebra à vontade
       |
       v
  STAGING (ensaio)    -> cópia do real, ensaia o deploy
       |
       v
  PROD (o ar)         -> usuário acessa, não se mexe sem cuidado
```

## Estratégias de deploy

```
  BLUE-GREEN
    [blue: antiga]  [green: nova]
       tráfego ----->  (paralelo, testa, depois troca)
    (volta fácil se der problema)

  CANARY
    [nova] recebe 5% -> 10% -> 50% -> 100%
    (se quebrar, poucos perceberam)
```

## Quando rollback NÃO resolve (atenção)

```
  Rollback do código só é seguro quando banco, API e
  versão anterior continuam compatíveis.

  Se o deploy mudou SCHEMA do banco:
    código novo gravou dado na coluna nova
    rollback p/ código antigo -> não conhece a coluna
    pode quebrar ou ignorar dado -> segundo incidente

  Se o deploy quebrou COMPATIBILIDADE de API:
    outros sistemas já se adaptaram à resposta nova
    rollback p/ versão antiga -> idioma que ninguém espera

  Nesses casos: avançar, não voltar.
  Corrigir à frente e fazer novo deploy.
```

## Mapa das camadas revisitado (mostrar no fechamento)

```
  EPISÓDIO 01: o mapa inteiro (visão geral)
       |
       +-- 02: FRONT-END E ESTADO      (navegador, HTML/CSS/JS, estado)
       |
       +-- 03: REQUEST, RESPONSE, API  (ponte navegador <-> servidor)
       |
       +-- 04: BANCO DE DADOS          (memória de longo prazo)
       |
       +-- 05: AUTH E SESSÃO           (quem é você, o que pode)
       |
       +-- 06: GIT E VERSIONAMENTO     (rede de segurança, voltar no tempo)
       |
       +-- 07: BUILD, CI/CD, DEPLOY    (o cano que leva ao ar) <-- você está aqui
       |
       (a sequência continua: 08 secrets e variáveis de ambiente)
```

## Como usar no vídeo

- Mostrar o cano no início do ATO 1, só a estrutura, sem explicar cada etapa.
- Voltar ao cano no fim de cada cena do ATO 2, destacando a etapa que acabou de ser explicada.
- Mostrar os ambientes e as estratégias como blocos separados, visuais, dentro do ATO 2.
- No ATO 3, mostrar o cano completo em uma linha só, depois transicionar para o mapa das camadas revisitado.
- O mapa das camadas é o fechamento visual: cada camada listada com o episódio que a explicou; no encerramento, ponte para o ep08.

## Versão para thumbnail

Texto curto sobre o diagrama:
- Título sobre a imagem: "O que acontece DEPOIS do commit?"
- Setas: commit -> cano -> ar
- Destacar as palavras "build", "CI/CD", "deploy" como as três portas
- Sem ferramentas específicas, só conceitos
