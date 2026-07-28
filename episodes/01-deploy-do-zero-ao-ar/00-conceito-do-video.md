# Conceito do vídeo - Deploy do Zero ao Ar

## Tese

A maioria das pessoas que programa com IA hoje não enxerga o que acontece entre o código que ela escreve e o site que abre no navegador. Para a IA, tudo é "texto que vira site". Para quem decide, falta o mapa.

Este vídeo conta duas histórias que andam juntas, mas que precisam ser nomeadas como duas, distintas uma da outra. A primeira é o fluxo de publicação: como o código chega ao ar (código -> git -> build -> deploy). A segunda é o fluxo de uso: o que acontece quando alguém acessa a URL pronta (navegador -> domínio -> servidor -> API -> banco -> resposta -> navegador). O fluxo de publicação é a linha principal do vídeo. O fluxo de uso é a volta final de ~90 segundos, no encerramento.

A narrativa tem duas jornadas: você publica código para que ele viva em um servidor, e depois alguém acessa e dispara o ciclo de uso. Em cada passo uma camada nova aparece com um trabalho específico.

O objetivo é fazer o espectador enxergar as camadas e saber distinguir em qual das duas jornadas uma mudança se encaixa. Quando ele enxerga, ele para de aceitar a IA cegamente e começa a perguntar "essa mudança mora em qual camada? e afeta a publicação ou o uso?".

## Por que esse formato funciona

- Duas jornadas nomeadas: o espectador distingue o fluxo de publicação (como o código chega ao ar) do fluxo de uso (o que acontece quando alguém acessa). São caminhos distintos, percorridos em momentos distintos do vídeo.
- Arquitetural: o mapa mental que fica é o de camadas (front / servidor / banco / deploy), um mapa de camadas.
- Superficial de propósito: cada camada é apresentada com uma analogia e uma consequência. Aprofundar fica para vídeos futuros da série.

## Público

- Vibe coders que usam Cursor / Claude / Copilot e não sabem o que é um servidor
- Pessoas de produto / negócio que dialogam com devs e querem entender o contexto
- Iniciantes em desenvolvimento web

## Tom

Direto, sem jargão desnecessário. Cada termo técnico que aparece é imediatamente traduzido em uma frase. Didático, acessível. Gui falando para câmera ou com tela mostrando um diagrama simples.

## Estrutura em 3 atos

**ATO 1 - No seu computador (código + git)**
Onde tudo começa. O que é código, o que é uma página, e por que existe versionamento (git). Estado e variáveis não entram aqui: são o tema do ep02. O ATO 1 só sinaliza que a página tem memória própria e deixa o gancho. Sem isso, o passo seguinte não faz sentido.

**ATO 2 - As camadas do servidor (servidor + API + banco + auth)**
O computador de casa não é um bom lugar para servir um site. Precisa de um servidor. O servidor recebe pedidos (API), guarda dados que não somem (banco), e sabe quem é quem e o que pode fazer (auth, separando autenticação de autorização). Cada camada aparece porque a história precisa dela.

**ATO 3 - Indo ao ar (build + CI/CD + deploy + domínio)**
Código pronto no repo vira algo vivo. Em muitos projetos há build; em projetos simples pode ir direto. CI/CD valida antes de publicar, deploy coloca na nuvem, e o domínio é o endereço que o usuário digita. O DNS costuma continuar apontando para o mesmo serviço; mudar DNS é exceção.

**ENCERRAMENTO - A volta final: o fluxo de uso (~90s)**
Com o deploy pronto, percorre-se a segunda jornada: o que acontece quando alguém acessa a URL. Navegador -> domínio -> servidor -> API -> banco -> resposta -> renderiza. Esse é o fluxo de uso, distinto do fluxo de publicação percorrido nos atos anteriores.

## O que Não entra neste vídeo

- Estado e variáveis em profundidade (tema do ep02; aqui só gancho)
- Detalhes de framework específico (React internals, Next.js App Router, etc)
- Containers, Kubernetes, infraestrutura de nuvem avançada
- Performance / SEO / analytics
- Segurança profunda (além do conceito de auth)
- Comparação exaustiva de bancos / servidores

Esses viram vídeos da série, um por tema. Este vídeo é o mapa.
