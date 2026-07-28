# Exemplo 1 - Env

## O que ilustra

O ATO 2 do episódio 08: o **.env** guarda valores reais só na sua máquina; o **.env.example** (ou `.env.example` no repo) lista **nomes** sem segredos. O `.gitignore` impede que o arquivo com valores reais entre no commit.

## Trecho / arquivo

Ver [`exemplo-1-env.env.example`](./exemplo-1-env.env.example):

```
CHAVE_PAGAMENTO=chave_exemplo_nao_usar
URL_BANCO=postgres://usuario:senha_exemplo@localhost:5432/app
```

Ver [`exemplo-1-env.gitignore-sample`](./exemplo-1-env.gitignore-sample):

```
.env
```

- **`CHAVE_PAGAMENTO`** — nome que o código usa; valor real mora no `.env` local ou no painel de produção.
- **`chave_exemplo_nao_usar`** — placeholder óbvio; nunca é chave de verdade.
- **`.env` no gitignore** — linha que evita commit acidental do arquivo com segredos.

## O que observar

- Example no repo: documenta quais variáveis existem; clone novo sabe o que configurar.
- `.env` local nunca sobe — cada desenvolvedor e cada ambiente têm valores próprios.
- Commit imutável (ep06): se `.env` entrou no histórico, apagar o arquivo não apaga a foto.
- Mesmos nomes em dev e prod; só mudam os valores (chave de teste vs chave real).

## O que quebra se faltar

| Ausência | Consequência |
|---|---|
| `.env` no `.gitignore` | Um `git add .` publica senhas no repo. |
| `.env.example` no repo | Novo dev não sabe quais variáveis configurar; app falha silenciosamente. |
| Placeholders falsos no example | Alguém copia example achando que é valor real e sobe produção quebrada. |
| Valores reais só fora do git | Segredo no código-fonte; qualquer fork expõe o negócio. |
