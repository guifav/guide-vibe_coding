# Guide - Vibe Coding (ia-aplicada)

Material de apoio dos vídeos do Guilherme Favaron sobre **vibe coding**: programar com IA com compreensão real do que está acontecendo, não aprovação do trabalho que a IA realiza por confiança.

Cada vídeo é uma pasta em `episodes/` com o kit completo: conceito, roteiro, mapa visual, glossário, títulos/thumbnail/SEO e cortes para Shorts.

## A sequência

Oito episódios, na ordem. O episódio 01 desenha o mapa inteiro e nomeia duas jornadas: o fluxo de publicação (do código ao ar) e o fluxo de uso (do navegador ao banco). Os episódios 02 a 05 fazem o zoom nas camadas do fluxo de uso; os episódios 06 e 07 voltam ao fluxo de publicação (a rede de segurança e o caminho até o ar). O episódio 08 continua a sequência: com o mapa desenhado, ensina a operar sem se machucar (secrets e variáveis de ambiente). Cada um é autocontido, mas a ordem faz sentido se assistir na sequência.


| #   | Episódio                        | Camada                | Pasta                                                                                   |
| --- | ------------------------------- | --------------------- | --------------------------------------------------------------------------------------- |
| 01  | Deploy do Zero ao Ar            | Mapa completo         | [01-deploy-do-zero-ao-ar/](./episodes/01-deploy-do-zero-ao-ar/)                       |
| 02  | Front-end e Estado              | Navegador             | [02-front-end-e-estado/](./episodes/02-front-end-e-estado/)                           |
| 03  | Request, Response e API         | Navegador ↔ Servidor  | [03-request-response-e-api/](./episodes/03-request-response-e-api/)                   |
| 04  | Banco de Dados                  | Servidor ↔ Dados      | [04-banco-de-dados/](./episodes/04-banco-de-dados/)                                   |
| 05  | Auth e Sessão                   | Quem é você           | [05-auth-e-sessao/](./episodes/05-auth-e-sessao/)                                     |
| 06  | Git e Versionamento             | Rede de segurança     | [06-git-e-versionamento/](./episodes/06-git-e-versionamento/)                         |
| 07  | Build, CI/CD e Deploy           | Indo ao ar (profundo) | [07-build-ci-cd-deploy/](./episodes/07-build-ci-cd-deploy/)                           |
| 08  | Secrets e Variáveis de Ambiente | Onde as chaves moram  | [08-secrets-e-variaveis-de-ambiente/](./episodes/08-secrets-e-variaveis-de-ambiente/) |




## Estrutura de cada episódio

- `README.md` - índice e visão geral
- `00-conceito-do-video.md` - tese, público, estrutura
- `01-roteiro-completo.md` - roteiro falado com timestamps
- `02-mapa-de-camadas.md` - diagrama visual
- `03-glossario-minimo.md` - termos que aparecem, 1 linha cada
- `04-titulos-thumbnail-seo.md` - títulos, thumbnail, tags
- `05-shorts-cortes.md` - cortes curtos para Shorts/Reels
- `exemplos/` - trechos ilustrativos (markdown + código quando fizer sentido)
- `pranchas/` - slides SVG + PNG (1920×1080) no design system Midnight Grid, uma por passagem visual do roteiro
- `apresentacao.pdf` - as pranchas consolidadas em PDF (1 página = 1 prancha), pronto para projetar

Geradores em `[tools/pranchas/](./tools/pranchas/)`: `python3 gerar_epNN.py` regenera as pranchas; `python3 gerar_pdfs.py` regenera os PDFs.

## Princípios

- Narrativa didática, sem jargão desnecessário
- Cada termo técnico é traduzido em 1 frase antes de continuar
- Conceito só entra se responde "o que quebra se isso faltar"
- Sem afirmações absolutas: descrever configurações comuns, não regras universais
- Identidade anônima: zero menções a empresas ou produtos reais no material de publicação (roteiro, glossário, mapa, títulos, shorts e pranchas); os `00-conceito` são documentos de planejamento
- Saída replicável: glossário mínimo por episódio; o ep07 consolida o glossário das camadas do mapa; a série segue no ep08

## Contribuições

Caso queira sugerir conteúdo para fortalecer este repositório, siga o guia em [`CONTRIBUTING.md`](./CONTRIBUTING.md).
