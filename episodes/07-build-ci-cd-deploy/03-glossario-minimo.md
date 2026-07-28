# Glossario minimo (aparece na descricao do YouTube)

So os termos que aparecem no roteiro. Um por linha, traducao direta. Este glossario fecha a temporada: ao final dele, listamos tambem os termos dos episodios anteriores, para ter o glossario completo da serie.

---

## Build

- **Build** - transformacao do codigo em algo servivel (cozinha do restaurante)
- **Compile** - traduzir codigo de uma linguagem para outra que a maquina executa
- **Minify** - remover espacos, comentarios e encurtar nomes para o arquivo ficar menor
- **Tree-shake** - remover codigo importado mas nao usado (sacode a arvore, folhas mortas caem)
- **Bundle** - juntar varios arquivos em um so, ou em poucos, para menos viagens na rede
- **Sintaxe** - a gramatica do codigo; abriu parentese tem que fechar
- **Tipo (type)** - categoria de um valor (numero, texto, data); operacoes invalidas para o tipo quebram
- **Dependencia** - pedaco de codigo de outra pessoa que o seu precisa para funcionar

## CI/CD

- **CI (Continuous Integration)** - cano que roda sozinho toda vez que codigo entra no repo
- **CD (Continuous Deployment/Delivery)** - continuacao do cano que publica depois do CI verde
- **Lint** - verificador de estilo do codigo (indentacao, nomes, padrao do time)
- **Teste** - pedaco de codigo que verifica se outro pedaco faz o que deveria
- **Pipeline** - outro nome para o cano; a sequencia de etapas automatizadas
- **CI verde / CI vermelho** - passou em todas as etapas / falhou em alguma

## Ambientes

- **Ambiente** - servidor (ou conjunto) com um proposito especifico no ciclo
- **Local** - seu computador; so voce ve
- **Dev** - servidor compartilhado de teste; quebra a vontade
- **Staging** - ensaio; copia o mais proxima possivel do real
- **Prod (producao)** - o ar; o servidor que o usuario acessa

## Deploy

- **Deploy** - ato de colocar a nova versao no servidor em prod
- **Rollback** - desfazer o deploy; colocar de volta a versao anterior
- **Tudo-de-uma-vez (all-at-once)** - derruba a antiga, sobe a nova; pode ter pausa
- **Blue-green** - sobe nova em paralelo, testa, troca o trafego de uma vez
- **Canary** - libera a nova para poucos usuarios primeiro, aumenta gradativamente

## Quando algo da errado

- **Incidente** - quebra em prod com impacto real no usuario
- **Post-mortem** - conversa estruturada depois do incidente resolvido; entender, nao culpar
- **Zero downtime** - deploy em que nenhum usuario percebe a troca

---

## O ciclo completo (uma linha)

**commit** -> **push** -> **CI** (lint, testes, build) -> **CD** -> **ambiente** (dev/staging/prod) -> **deploy** -> **usuario percebe**

---

## Pergunta-chave para usar com IA

Quando a IA sugerir um deploy ou uma mudanca que vai ao ar, pergunte:

"Se isso der errado em prod, conseguimos voltar rapido? Tem rollback? Qual estrategia de deploy?"

A resposta diz o tamanho do risco.

---

## Glossario da temporada completa (referencia rapida)

Termos dos episodios anteriores, para consulta.

- **HTML / CSS / JavaScript** - o que aparece / como aparece / o que acontece (ep02)
- **Estado (state)** - memoria da pagina enquanto esta aberta (ep02)
- **Variavel** - nome para guardar um valor que pode mudar (ep02)
- **Servidor** - outro computador, sempre ligado, responde a pedidos (ep03)
- **Request / Response** - pedido que vai / resposta que volta (ep03)
- **API** - balcao de atendimento do servidor; contrato de pedido/resposta (ep03)
- **Endpoint** - uma porta especifica da API (ep03)
- **JSON** - texto organizado para dados trafegarem (ep03)
- **Banco de dados** - memoria de longo prazo do servidor (ep04)
- **Auth (autenticacao)** - camada que responde "quem e voce?" (ep05)
- **Token** - cracha que o servidor da depois do login (ep05)
- **Sessao** - periodo em que o servidor te mantem logado (ep05)
- **Git** - sistema de versionamento; tira fotos do codigo no tempo (ep06)
- **Commit** - o ato de tirar uma foto no git (ep06)
- **Branch** - linha paralela para testar sem estragar o original (ep06)
- **Merge** - juntar a branch de volta na linha principal (ep06)
- **Repo (repositorio)** - onde as fotos do codigo ficam guardadas (ep06)
- **Dominio** - o nome que o usuario digita (ep01)
- **DNS** - lista telefonica que traduz o dominio no endereco do servidor (ep01)
