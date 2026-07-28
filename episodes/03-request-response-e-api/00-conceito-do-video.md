# Conceito do vídeo - Request, Response e API

## Tese

Tudo que acontece na web é uma conversa entre duas partes: o navegador pede, o servidor responde. Parece simples. Mas a maioria das pessoas que programa com IA hoje não enxerga essa conversa. Para a IA, tudo é "chama a API e pronto". Para quem decide, falta entender o que está sendo pedido, o que está sendo devolvido, e por que às vezes a IA inventa um contrato que não existe.

Este vídeo conta a história de um pedido, até a resposta chegar e virar tela. É a narrativa de um diálogo: cada conceito surge da necessidade do passo anterior.

O objetivo é fazer o espectador enxergar a conversa. Quando ele enxerga, ele para de aceitar "a IA disse que a API devolve isso" e começa a perguntar: "qual é o contrato real? Qual status code voltou? O front deveria saber disso?".

## Por que esse formato funciona

- Linear: o espectador acompanha um pedido até o fim, porque cada conceito surge da necessidade do passo anterior.
- Arquitetural: o mapa mental que fica é o de diálogo (pede / responde / contrato / status), não uma lista de códigos HTTP memorizada.
- Superficial de propósito: cada conceito é apresentado com uma analogia e uma consequência. Aprofundar fica para vídeos futuros.

## Público

- Vibe coders que usam Cursor / Claude / Copilot e não sabem o que é um request
- Pessoas que viram a IA "chamar API" e não entendem o que isso significa
- Iniciantes em desenvolvimento web que já viram o episódio 01 (o mapa)

## Tom

Direto, sem jargão desnecessário. Cada termo técnico que aparece é imediatamente traduzido em uma frase. Didático, não acadêmico. Gui falando para câmera ou com tela mostrando um diagrama simples.

## Estrutura em 3 atos

**ATO 1 - O pedido (request, método, endpoint)**
O navegador pede algo ao servidor. O pedido tem um método (GET para pedir, POST para enviar) e bate numa porta específica (endpoint). Cada URL é uma porta diferente no balcão do servidor.

**ATO 2 - A resposta (JSON, contrato, status codes)**
O servidor devolve algo. O formato da resposta é JSON (texto organizado). O contrato define o que eu peço vs o que recebo. E o status code diz, honestamente, o que aconteceu: 200 (ok), 404 (não achei), 401/403 (não pode), 500 (quebrou). Sem status code honesto, o front fica perdido.

**ATO 3 - A fronteira (front não sabe do banco)**
O front não deveria saber nada do banco. Só conversa com a API. Essa separação é o que mantém o sistema são. Quando a IA mistura as camadas, é aí que o problema começa. Fecha com a ponte para o episódio 04: de onde o servidor tira os dados que devolve?

## O que Não entra neste vídeo

- Detalhes de protocolo HTTP (versões, headers avançados, CORS profundo)
- PUT, PATCH, DELETE e outros métodos além de GET e POST
- Autenticação profunda (token, JWT, sessão) - fica para episódio próprio
- REST vs GraphQL vs RPC - comparação de estilos de API
- Documentação de API (Swagger, OpenAPI) - ferramenta
- Webhooks, Server-Sent Events, WebSocket - outros modelos de conversa

Esses viram vídeos da série, um por tema. Este vídeo é o diálogo básico.
