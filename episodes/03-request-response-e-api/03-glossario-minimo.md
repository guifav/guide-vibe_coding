# Glossario minimo (aparece na descricao do YouTube)

So os termos que aparecem no roteiro. Um por linha, traducao direta.

---

## O pedido

- **Request** — o pedido que o navegador manda para o servidor
- **HTTP** — o idioma da conversa entre navegador e servidor
- **Metodo** — o tipo do pedido (o que voce quer fazer)
- **GET** — pedir; o navegador diz "me da isso"
- **POST** — enviar; o navegador diz "aqui estao dados, faz algo"
- **Endpoint** — uma porta especifica no balcao do servidor (cada URL e uma porta)
- **URL** — o endereco que diz qual porta bater

## A resposta

- **Response** — a resposta que o servidor devolve para o navegador
- **JSON** — formato de texto organizado para dados trafegarem (chaves e listas)
- **Contrato** — o combinado entre front e servidor: o que eu peco vs o que recebo
- **Status code** — codigo honesto que diz o que aconteceu com o pedido
- **200 (OK)** — deu certo, aqui esta a resposta
- **404 (Not Found)** — nao achei o que voce pediu
- **401 (Unauthorized)** — voce nao esta logado, nao sei quem voce e
- **403 (Forbidden)** — sei quem voce e, mas voce nao pode acessar isso
- **500 (Internal Server Error)** — quebrou no servidor, nao foi culpa sua
- **Crash silencioso** — servidor quebra mas devolve algo vazio; front nao sabe o que houve

## A fronteira

- **Front-end** — o lado do navegador; mostra a tela, manda request, le response
- **API** — o balcao do servidor; atende o pedido, processa, devolve JSON
- **Banco de dados** — o almoxarifado; memoria de longo prazo que o servidor consulta
- **Camadas** — separacao de responsabilidades: front mostra, API atende, banco guarda

---

## Perguntas-chave para usar com IA

Quando a IA sugerir algo envolvendo API, faca tres perguntas:

1. "Qual e o contrato real dessa API?" (o que ela devolve de verdade?)
2. "Qual status code eu devo tratar?" (404, 401, 500 sao coisas diferentes)
3. "Isso mora em qual camada?" (front, API, ou banco?)

Se a IA nao souber responder, ela esta chutando.
