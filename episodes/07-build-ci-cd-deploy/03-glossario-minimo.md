# Glossário mínimo (aparece na descrição do YouTube)

Só os termos que aparecem no roteiro. Um por linha, tradução direta. Este glossário fecha a temporada: ao final dele, listamos também os termos dos episódios anteriores, para ter o glossário completo da série.

---

## Build

- **Build** - transformação do código em algo servível (cozinha do restaurante)
- **Compile** - traduzir código de uma linguagem para outra que a máquina executa (possibilidade, nem todo build faz)
- **Minify** - remover espaços, comentários e encurtar nomes para o arquivo ficar menor (possibilidade)
- **Tree-shake** - remover código importado mas não usado (sacode a árvore, folhas mortas caem) (possibilidade)
- **Bundle** - juntar vários arquivos em um só, ou em poucos, para menos viagens na rede (possibilidade)
- **Sintaxe** - a gramática do código; abriu parêntese tem que fechar
- **Tipo (type)** - categoria de um valor (número, texto, data); operações inválidas para o tipo quebram
- **Dependência** - pedaço de código de outra pessoa que o seu precisa para funcionar

## CI/CD

- **CI (Continuous Integration)** - cano que roda sozinho toda vez que código entra no repo
- **Continuous Delivery** - prepara uma versão publicável e para; exige humano apertar o botão de publicar
- **Continuous Deployment** - depois do CI verde, publica em produção automaticamente, sem decisão humana
- **CD** - nome genérico para o cano que continua depois do CI; pode ser Delivery ou Deployment
- **Lint** - verificador de estilo do código (indentação, nomes, padrão do time)
- **Teste** - pedaço de código que verifica se outro pedaço faz o que deveria
- **Pipeline** - outro nome para o cano; a sequência de etapas automatizadas
- **CI verde / CI vermelho** - passou em todas as etapas / falhou em alguma

## Ambientes

- **Ambiente** - um lugar onde o código roda, com um propósito específico no ciclo
- **Local** - seu computador; só você vê
- **Dev** - servidor compartilhado de teste; quebra à vontade
- **Staging** - ensaio; cópia o mais próxima possível do real
- **Prod (produção)** - o ar; o servidor que o usuário acessa

## Deploy

- **Deploy** - ato de colocar a nova versão no servidor em prod
- **Rollback** - desfazer o deploy; colocar de volta a versão anterior
- **Rollback seguro** - só vale quando banco, API e versão anterior continuam compatíveis
- **Blue-green** - sobe nova em paralelo, testa, troca o tráfego de uma vez
- **Canary** - libera a nova para poucos usuários primeiro, aumenta gradativamente

## Quando algo dá errado

- **Incidente** - quebra em prod com impacto real no usuário
- **Post-mortem** - conversa estruturada depois do incidente resolvido; foco em entender
- **Zero downtime** - deploy em que nenhum usuário percebe a troca

---

## O ciclo completo (uma linha)

**commit** -> **push** -> **CI** (lint, testes, build) -> **CD** -> **ambiente** (dev/staging/prod) -> **deploy** -> **usuário percebe**

---

## Pergunta-chave para usar com IA

Quando a IA sugerir um deploy ou uma mudança que vai ao ar, pergunte duas coisas:

1. "Se isso der errado em prod, conseguimos voltar rápido? Tem rollback? Qual estratégia de deploy?"

2. "Essa mudança mexe em schema de banco ou quebra compatibilidade de API? Se sim, rollback de código não resolve."

As duas respostas juntas dizem o tamanho do risco.

---

## Glossário da temporada completa (referência rápida)

Termos dos episódios anteriores, para consulta.

- **HTML / CSS / JavaScript** - o que aparece / como aparece / o que acontece (ep02)
- **Estado (state)** - memória da página enquanto está aberta (ep02)
- **Variável** - nome para guardar um valor que pode mudar (ep02)
- **Servidor** - outro computador, sempre ligado, responde a pedidos (ep01)
- **Request / Response** - pedido que vai / resposta que volta (ep03)
- **API** - balcão de atendimento do servidor; contrato de pedido/resposta (ep03)
- **Endpoint** - uma porta específica da API (ep03)
- **JSON** - texto organizado para dados trafegarem (ep03)
- **Banco de dados** - memória de longo prazo do servidor (ep04)
- **Auth (autenticação)** - camada que responde "quem é você?" (ep05)
- **Token** - crachá que o servidor dá depois do login (ep05)
- **Sessão** - período em que o servidor te mantém logado (ep05)
- **Git** - sistema de versionamento; tira fotos do código no tempo (ep06)
- **Commit** - o ato de tirar uma foto no git (ep06)
- **Branch** - linha paralela para testar sem estragar o original (ep06)
- **Merge** - juntar a branch de volta na linha principal (ep06)
- **Repo (repositório)** - onde as fotos do código ficam guardadas (ep06)
- **Domínio** - o nome que o usuário digita (ep01)
- **DNS** - lista telefônica que traduz o domínio no endereço do servidor (ep01)
