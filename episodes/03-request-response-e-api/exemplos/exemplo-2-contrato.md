# Exemplo 2 - Contrato

## O que ilustra

O ATO 2 do episódio 03: o servidor **devolve** algo. O formato é JSON (texto organizado). O **contrato** define o que você pede versus o que recebe. O **status code** diz honestamente o que aconteceu.

## Trecho / arquivo

Ver [`exemplo-2-contrato.json`](./exemplo-2-contrato.json):

```json
{
  "pedido": {
    "id": 42,
    "status": "aberto",
    "total": 19.9
  },
  "status_http_exemplo": 200
}
```

- **`pedido`** — objeto com os campos que o front espera receber.
- **`id`, `status`, `total`** — campos do contrato; mudar nome ou tipo quebra o front.
- **`status_http_exemplo`: 200** — lembrete didático: 200 significa "deu certo"; 404 = não achei; 500 = quebrou no servidor.

## O que observar

- JSON é texto legível, mas o front depende da **forma** exata dos campos.
- Status code e corpo vêm juntos — um 200 com corpo vazio é diferente de um 404 com mensagem de erro.
- A IA costuma inventar campos que a API real não devolve; o contrato real manda.
- O front deve tratar cada status de forma diferente (sucesso, não encontrado, erro).

## O que quebra se faltar

| Ausência | Consequência |
|---|---|
| Contrato acordado | Front lê `pedido.total` mas a API devolve `valor` — tela mostra `undefined`. |
| Status code honesto | Erro vira 200 com corpo vazio; front acha que deu certo. |
| Campos obrigatórios | Front quebra ao acessar propriedade que não veio. |
| Tratamento de erro no front | 404 ou 500 viram tela branca ou mensagem genérica. |
