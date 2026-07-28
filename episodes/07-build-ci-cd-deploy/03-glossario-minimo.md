# Glossario minimo (aparece na descrição do YouTube)

Só os termos que aparecem no roteiro. Um por linha, tradução direta. Este glossario fecha a temporada: ao final dele, listamos também os termos dos episodios anteriores, para ter o glossario completo da série.

---

## Build

- **Build** - transformação do código em algo servivel (cozinha do restaurante)
- **Compile** - traduzir código de uma linguagem para outra que a máquina executa (possibilidade, nem todo build faz)
- **Minify** - remover espacos, comentarios e encurtar nomes para o arquivo ficar menor (possibilidade)
- **Tree-shake** - remover código importado mas não usado (sacode a árvore, folhas mortas caem) (possibilidade)
- **Bundle** - juntar varios arquivos em um só, ou em poucos, para menos viagens na rede (possibilidade)
- **Sintaxe** - a gramatica do código; abriu parentese tem que fechar
- **Tipo (type)** - categoria de um valor (número, texto, data); operações invalidas para o tipo quebram
- **Dependencia** - pedaco de código de outra pessoa que o seu precisa para funcionar

## CI/CD

- **CI (Continuous Integration)** - cano que roda sozinho toda vez que código entra no repo
- **Continuous Delivery** - prepara uma versao publicável e para; exige humano apertar o botao de publicar
- **Continuous Deployment** - depois do CI verde, publica em produção automaticamente, sem decisão humana
- **CD** - nome genérico para o cano que continua depois do CI; pode ser Delivery ou Deployment
- **Lint** - verificador de estilo do código (indentacao, nomes, padrao do time)
- **Teste** - pedaco de código que verifica se outro pedaco faz o que deveria
- **Pipeline** - outro nome para o cano; a sequência de etapas automatizadas
- **CI verde / CI vermelho** - passou em todas as etapas / falhou em alguma

## Ambientes

- **Ambiente** - servidor (ou conjunto) com um proposito especifico no ciclo
- **Local** - seu computador; só você ve
- **Dev** - servidor compartilhado de teste; quebra a vontade
- **Staging** - ensaio; copia o mais proxima possivel do real
- **Prod (produção)** - o ar; o servidor que o usuario acessa

## Deploy

- **Deploy** - ato de colocar a nova versao no servidor em prod
- **Rollback** - desfazer o deploy; colocar de volta a versao anterior
- **Rollback seguro** - só vale quando banco, API e versao anterior continuam compatíveis
- **Blue-green** - sobe nova em paralelo, testa, troca o trafego de uma vez
- **Canary** - libera a nova para poucos usuarios primeiro, aumenta gradativamente

## Quando algo da errado

- **Incidente** - quebra em prod com impacto real no usuario
- **Post-mortem** - conversa estruturada depois do incidente resolvido; foco em entender
- **Zero downtime** - deploy em que nenhum usuario percebe a troca

---

## O ciclo completo (uma linha)

**commit** -> **push** -> **CI** (lint, testes, build) -> **CD** -> **ambiente** (dev/staging/prod) -> **deploy** -> **usuario percebe**

---

## Pergunta-chave para usar com IA

Quando a IA sugerir um deploy ou uma mudança que vai ao ar, pergunte duas coisas:

1. "Se isso der errado em prod, conseguimos voltar rápido? Tem rollback? Qual estratégia de deploy?"

2. "Essa mudança mexe em schema de banco ou quebra compatibilidade de API? Se sim, rollback de código não resolve."

As duas respostas juntas dizem o tamanho do risco.

---

## Glossario da temporada completa (referencia rápida)

Termos dos episodios anteriores, para consulta.

- **HTML / CSS / JavaScript** - o que aparece / como aparece / o que acontece (ep02)
- **Estado (state)** - memória da página enquanto esta aberta (ep02)
- **Variável** - nome para guardar um valor que pode mudar (ep02)
- **Servidor** - outro computador, sempre ligado, responde a pedidos (ep03)
- **Request / Response** - pedido que vai / resposta que volta (ep03)
- **API** - balcao de atendimento do servidor; contrato de pedido/resposta (ep03)
- **Endpoint** - uma porta especifica da API (ep03)
- **JSON** - texto organizado para dados trafegarem (ep03)
- **Banco de dados** - memória de longo prazo do servidor (ep04)
- **Auth (autenticação)** - camada que responde "quem e você?" (ep05)
- **Token** - cracha que o servidor da depois do login (ep05)
- **Sessao** - periodo em que o servidor te mantem logado (ep05)
- **Git** - sistema de versionamento; tira fotos do código no tempo (ep06)
- **Commit** - o ato de tirar uma foto no git (ep06)
- **Branch** - linha paralela para testar sem estragar o original (ep06)
- **Merge** - juntar a branch de volta na linha principal (ep06)
- **Repo (repositorio)** - onde as fotos do código ficam guardadas (ep06)
- **Domínio** - o nome que o usuario digita (ep01)
- **DNS** - lista telefonica que traduz o domínio no endereço do servidor (ep01)
