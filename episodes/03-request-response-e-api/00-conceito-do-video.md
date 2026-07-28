# Conceito do video - Request, Response e API

## Tese

Tudo que acontece na web e uma conversa entre duas partes: o navegador pede, o servidor responde. Parece simples. Mas a maioria das pessoas que programa com IA hoje nao enxerga essa conversa. Para a IA, tudo e "chama a API e pronto". Para quem decide, falta entender o que esta sendo pedido, o que esta sendo devolvido, e por que as vezes a IA inventa um contrato que nao existe.

Este video conta a historia de um pedido. Do momento em que o navegador dispara um request ate o momento em que a resposta chega e vira tela. Nao e curso de HTTP. E a narrativa de um dialogo: cada conceito surge da necessidade do passo anterior.

O objetivo nao e ensinar protocolo. E fazer o espectador enxergar a conversa. Quando ele enxerga, ele para de aceitar "a IA disse que a API devolve isso" e comeca a perguntar: "qual e o contrato real? Qual status code voltou? O front deveria saber disso?".

## Por que esse formato funciona

- Linear: o espectador acompanha um pedido do inicio ao fim, porque cada conceito surge da necessidade do passo anterior.
- Arquitetural: o mapa mental que fica e o de dialogo (pede / responde / contrato / status), nao uma lista de codigos HTTP memorizada.
- Superficial de proposito: cada conceito e apresentado com uma analogia e uma consequencia. Aprofundar fica para videos futuros.

## Publico

- Vibe coders que usam Cursor / Claude / Copilot e nao sabem o que e um request
- Pessoas que viram a IA "chamar API" e nao entendem o que isso significa
- Iniciantes em desenvolvimento web que ja viram o episodio 01 (o mapa)

## Tom

Direto, sem jargao desnecessario. Cada termo tecnico que aparece e imediatamente traduzido em uma frase. Didatico, nao academico. Gui falando para camera ou com tela mostrando um diagrama simples.

## Estrutura em 3 atos

**ATO 1 - O pedido (request, metodo, endpoint)**
O navegador pede algo ao servidor. O pedido tem um metodo (GET para pedir, POST para enviar) e bate numa porta especifica (endpoint). Cada URL e uma porta diferente no balcao do servidor.

**ATO 2 - A resposta (JSON, contrato, status codes)**
O servidor devolve algo. O formato da resposta e JSON (texto organizado). O contrato define o que eu peco vs o que recebo. E o status code diz, honestamente, o que aconteceu: 200 (ok), 404 (nao achei), 401/403 (nao pode), 500 (quebrou). Sem status code honesto, o front fica perdido.

**ATO 3 - A fronteira (front nao sabe do banco)**
O front nao deveria saber nada do banco. So conversa com a API. Essa separacao e o que mantem o sistema sao. Quando a IA mistura as camadas, e ai que o problema comeca. Fecha com a ponte para o episodio 04: de onde o servidor tira os dados que devolve?

## O que NAO entra neste video

- Detalhes de protocolo HTTP (versoes, headers avancados, CORS profundo)
- PUT, PATCH, DELETE e outros metodos alem de GET e POST
- Autenticacao profunda (token, JWT, sessao) - fica para episodio proprio
- REST vs GraphQL vs RPC - comparacao de estilos de API
- Documentacao de API (Swagger, OpenAPI) - ferramenta, nao conceito
- Webhooks, Server-Sent Events, WebSocket - outros modelos de conversa

Esses viram videos da serie, um por tema. Este video e o dialogo basico.
