# Conceito do vídeo - Deploy do Zero ao Ar

## Tese

A maioria das pessoas que programa com IA hoje não enxerga o que acontece entre o código que ela escreve e o site que abre no navegador. Para a IA, tudo e "texto que vira site". Para quem decide, falta o mapa.

Este vídeo conta a história de um deploy, do zero ao ar, em ordem cronologica. Não e curso de cada tecnologia. E a narrativa de uma jornada: você escreve código, ele vira algo que o mundo acessa, e em cada passo da jornada uma camada nova aparece com um trabalho especifico.

O objetivo não e ensinar a programar. E fazer o espectador enxergar as camadas. Quando ele enxerga, ele para de aceitar a IA cegamente e comeca a perguntar "essa mudança mora em qual camada?".

## Por que esse formato funciona

- Linear: o espectador acompanha do início ao fim sem se perder, porque cada conceito surge da necessidade do passo anterior.
- Arquitetural: o mapa mental que fica e o de camadas (front / servidor / banco / deploy), não uma lista de ferramentas.
- Superficial de proposito: cada camada e apresentada com uma analogia e uma consequencia. Aprofundar fica para vídeos futuros da série.

## Público

- Vibe coders que usam Cursor / Claude / Copilot e não sabem o que e um servidor
- Pessoas de produto / negocio que dialogam com devs e querem entender o contexto
- Iniciantes em desenvolvimento web

## Tom

Direto, sem jargao desnecessario. Cada termo técnico que aparece e imediatamente traduzido em uma frase. Didático, não academico. Gui falando para camera ou com tela mostrando um diagrama simples.

## Estrutura em 3 atos

**ATO 1 - No seu computador (código + estado + git)**
Onde tudo comeca. O que e código, o que e uma página, o que muda sem recarregar (estado), e por que existe versionamento (git). Sem isso, o passo seguinte não faz sentido.

**ATO 2 - Saindo do seu computador (servidor + API + banco + auth)**
O computador de casa não e acessivel pelo mundo. Precisa de um servidor. O servidor recebe pedidos (API), guarda dados que não somem (banco), e sabe quem e quem (auth). Cada camada aparece porque a história precisa dela.

**ATO 3 - Indo ao ar (build + CI/CD + deploy + domínio)**
Código pronto no repo vira algo vivo. Build transforma, CI/CD valida antes de publicar, deploy coloca na nuvem, e o domínio e o endereço que o usuario digita. Fecha com o ciclo completo: o que acontece quando alguém acessa a URL.

## O que Não entra neste vídeo

- Detalhes de framework especifico (React internals, Next.js App Router, etc)
- Containers, Kubernetes, infraestrutura de nuvem avancada
- Performance / SEO / analytics
- Seguranca profunda (alem do conceito de auth)
- Comparacao exaustiva de bancos / servidores

Esses viram vídeos da série, um por tema. Este vídeo e o mapa.
