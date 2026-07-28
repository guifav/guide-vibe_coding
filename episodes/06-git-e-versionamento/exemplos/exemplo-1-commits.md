# Exemplo 1 - Commits

## O que ilustra

O ATO 1 do episódio 06: o **commit** como foto do código em um momento. Três fotos na linha do tempo — cada uma imutável, com mensagem que explica o que mudou.

## Trecho / arquivo

Linha do tempo (do mais antigo ao mais recente):

```
[a1b2c3d] feat: adiciona tela de listagem de pedidos
    └── Arquivos: pagina-pedidos.html, estilo.css
    └── Autor: dev-exemplo | Data: 2026-07-10

[e4f5g6h] fix: corrige total quando desconto é zero
    └── Arquivos: calcula-total.js
    └── Autor: dev-exemplo | Data: 2026-07-15

[i7j8k9l] docs: atualiza glossário de status de pedido
    └── Arquivos: glossario.md
    └── Autor: dev-exemplo | Data: 2026-07-20
```

- **`a1b2c3d`** — hash curto do commit; identificador único da foto (valores ilustrativos).
- **Mensagem** — frase que responde "o que mudou?" para quem lê a linha do tempo depois.
- **Imutável** — commit `a1b2c3d` não muda; erro vira novo commit (`e4f5g6h`), não edição da foto antiga.

## O que observar

- Cada commit é um ponto para voltar no tempo — "como estava no dia 15?".
- Mensagem clara economiza horas quando alguém pergunta "por que isso mudou?".
- Commits pequenos e focados são mais fáceis de revisar e reverter.
- As fotos ficam guardadas no **repo** — local ou no repositório remoto na nuvem.

## O que quebra se faltar

| Ausência | Consequência |
|---|---|
| Commits regulares | Impossível voltar; só existe "versão de agora" ou cópias manuais confusas. |
| Mensagem descritiva | Linha do tempo ilegível; ninguém sabe o que cada foto contém. |
| Repo (local ou remoto) | Fotos só no computador de uma pessoa; somem com HD ou troca de máquina. |
| Respeito à imutabilidade | Reescrever histórico quebra referências; time perde o fio da meada. |
