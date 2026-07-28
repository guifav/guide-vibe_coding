# Conceito do vídeo - Deploy do Zero ao Ar

## Tese

A maioria das pessoas que programa com IA hoje não enxerga o que acontece entre o código que ela escreve e o site que abre no navegador. Para a IA, tudo e "texto que vira site". Para quem decide, falta o mapa.

Este vídeo conta duas histórias que andam juntas, mas que precisam ser nomeadas como duas, distintas uma da outra. A primeira e o fluxo de publicação: como o código chega ao ar (código -> git -> build -> deploy). A segunda e o fluxo de uso: o que acontece quando alguém acessa a URL pronta (navegador -> domínio -> servidor -> API -> banco -> resposta -> navegador). O fluxo de publicação e a linha principal do vídeo. O fluxo de uso e a volta final de ~90 segundos, no encerramento.

A narrativa tem duas jornadas: você publica código para que ele viva em um servidor, e depois alguém acessa e dispara o ciclo de uso. Em cada passo uma camada nova aparece com um trabalho especifico.

O objetivo e fazer o espectador enxergar as camadas e saber distinguir em qual das duas jornadas uma mudança se encaixa. Quando ele enxerga, ele para de aceitar a IA cegamente e comeca a perguntar "essa mudança mora em qual camada? e afeta a publicação ou o uso?".

## Por que esse formato funciona

- Duas jornadas nomeadas: o espectador distingue o fluxo de publicação (como o código chega ao ar) do fluxo de uso (o que acontece quando alguém acessa). São caminhos distintos, percorridos em momentos distintos do vídeo.
- Arquitetural: o mapa mental que fica e o de camadas (front / servidor / banco / deploy), um mapa de camadas.
- Superficial de proposito: cada camada e apresentada com uma analogia e uma consequencia. Aprofundar fica para vídeos futuros da série.

## Público

- Vibe coders que usam Cursor / Claude / Copilot e não sabem o que e um servidor
- Pessoas de produto / negocio que dialogam com devs e querem entender o contexto
- Iniciantes em desenvolvimento web

## Tom

Direto, sem jargao desnecessario. Cada termo técnico que aparece e imediatamente traduzido em uma frase. Didático, acessível. Gui falando para camera ou com tela mostrando um diagrama simples.

## Estrutura em 3 atos

**ATO 1 - No seu computador (código + git)**
Onde tudo comeca. O que e código, o que e uma página, e por que existe versionamento (git). Estado e variáveis não entram aqui: são o tema do ep02. O ATO 1 só sinaliza que a página tem memória própria e deixa o gancho. Sem isso, o passo seguinte não faz sentido.

**ATO 2 - As camadas do servidor (servidor + API + banco + auth)**
O computador de casa não e um bom lugar para servir um site. Precisa de um servidor. O servidor recebe pedidos (API), guarda dados que não somem (banco), e sabe quem e quem e o que pode fazer (auth, separando autenticação de autorização). Cada camada aparece porque a história precisa dela.

**ATO 3 - Indo ao ar (build + CI/CD + deploy + domínio)**
Código pronto no repo vira algo vivo. Em muitos projetos há build; em projetos simples pode ir direto. CI/CD valida antes de publicar, deploy coloca na nuvem, e o domínio e o endereço que o usuario digita. O DNS costuma continuar apontando para o mesmo serviço; mudar DNS e exceção.

**ENCERRAMENTO - A volta final: o fluxo de uso (~90s)**
Com o deploy pronto, percorre-se a segunda jornada: o que acontece quando alguém acessa a URL. Navegador -> domínio -> servidor -> API -> banco -> resposta -> renderiza. Esse e o fluxo de uso, distinto do fluxo de publicação percorrido nos atos anteriores.

## O que Não entra neste vídeo

- Estado e variáveis em profundidade (tema do ep02; aqui só gancho)
- Detalhes de framework especifico (React internals, Next.js App Router, etc)
- Containers, Kubernetes, infraestrutura de nuvem avancada
- Performance / SEO / analytics
- Seguranca profunda (alem do conceito de auth)
- Comparacao exaustiva de bancos / servidores

Esses viram vídeos da série, um por tema. Este vídeo e o mapa.
