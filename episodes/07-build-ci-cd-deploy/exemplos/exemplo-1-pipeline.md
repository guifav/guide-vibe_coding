# Exemplo 1 - Pipeline

## O que ilustra

O ATO 2 do episódio 07: o **CI** como portão automático. Toda vez que código entra no repo, o cano roda em sequência — lint, testes, build, publicar. Cada etapa fica verde ou vermelha; vermelho bloqueia o resto.

## Trecho / arquivo

Ver [`exemplo-1-pipeline.yml`](./exemplo-1-pipeline.yml):

```yaml
# Cano genérico: cada etapa verde ou vermelho
etapas:
  - nome: lint
  - nome: testes
  - nome: build
  - nome: publicar  # só se as anteriores passaram
```

- **`lint`** — checa estilo e erros óbvios antes de rodar testes caros.
- **`testes`** — confirma que o comportamento esperado ainda funciona.
- **`build`** — transforma a fonte em artefato publicável (ATO 1 do episódio).
- **`publicar`** — só roda se tudo acima passou; é a porta para o CD.

## O que observar

- Ordem importa: publicar sem testes verdes leva bug para produção.
- Vermelho em qualquer etapa para o cano — não é "só aviso", é bloqueio.
- CI não replica produção por completo; verde no cano não garante zero surpresa no ar.
- O YAML aqui é genérico; a ideia vale em qualquer automação de pipeline.

## O que quebra se faltar

| Ausência | Consequência |
|---|---|
| Etapa de testes | Bug chega ao build ou à produção sem barreira. |
| Bloqueio em vermelho | Time ignora falha e publica mesmo assim. |
| Build antes de publicar | Servidor recebe fonte crua ou pacote incompleto. |
| Cano visível no repo | Cada pessoa roda passos diferentes no computador local. |
