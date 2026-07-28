# Exemplo 1 - Mapa

## O que ilustra

Visão geral das camadas que aparecem no episódio 01: do código no seu computador até a resposta que chega no navegador de quem acessa. Duas jornadas distintas — publicação e uso — compartilham algumas camadas, mas percorrem caminhos diferentes.

## Trecho / diagrama

```
  JORNADA DE PUBLICAÇÃO (como o código chega ao ar)
  ┌─────────┐    ┌──────┐    ┌───────┐    ┌─────┐    ┌────────┐    ┌─────────┐
  │  código │ -> │ repo │ -> │ build │ -> │ CI  │ -> │ deploy │ -> │ domínio │
  └─────────┘    └──────┘    └───────┘    └─────┘    └────────┘    └─────────┘

  JORNADA DE USO (o que acontece quando alguém acessa a URL)
  ┌───────────┐    ┌─────────┐    ┌─────────┐    ┌─────┐    ┌───────┐    ┌───────────┐
  │ navegador │ -> │ domínio │ -> │ servidor│ -> │ API │ -> │ banco │ -> │ resposta  │
  └───────────┘    └─────────┘    └─────────┘    └─────┘    └───────┘    └───────────┘
                                                                    │
                                                         (auth decide quem pode)
```

Camadas transversais:

- **Código / front-end** — o que você escreve; vira página no navegador.
- **Servidor** — recebe pedidos; não roda no computador de casa em produção.
- **API** — contrato de pedidos e respostas entre front e back.
- **Banco** — dados que sobrevivem ao fechar o navegador.
- **Auth** — autenticação (quem é) e autorização (o que pode fazer).
- **Build / CI / CD** — transforma código em artefato publicável e valida antes de ir ao ar.
- **Domínio** — endereço legível que aponta para onde o deploy mora.

## O que observar

- Publicação e uso são **dois caminhos**: você publica em um momento; alguém acessa em outro.
- Cada camada aparece porque a história precisa dela — não porque "sempre existe".
- Mudança em **build** afeta publicação; mudança em **API** afeta uso (e às vezes os dois).
- Auth cruza servidor e API: sem ela, todo mundo vê ou altera tudo.
- O domínio aparece nas duas jornadas: é o endereço na publicação e a porta de entrada no uso.

## O que quebra se faltar

| Camada ausente | Consequência |
|---|---|
| Repo (versionamento) | Sem histórico; impossível voltar ou publicar de forma repetível. |
| Build (quando o projeto exige) | Código-fonte não vira o que o servidor consegue servir. |
| CI | Erros chegam ao ar sem validação automática. |
| Deploy | Código fica só na máquina local; ninguém de fora acessa. |
| Domínio | Só IP ou URL técnica; usuário não sabe onde entrar. |
| Servidor | Navegador não tem quem atender o pedido. |
| API | Front e back não conversam de forma previsível. |
| Banco | Dados somem ao recarregar ou fechar a aba. |
| Auth | Não há distinção entre visitante, usuário logado e admin. |
