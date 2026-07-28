# Exemplo 3 - PR (extra)

## O que ilustra

O ATO 3 do episódio 06: o **pedido formal de merge** com revisão. Antes de juntar `corrige-total` na `main`, alguém lê o diff, entende o porquê e confirma que dá para testar.

## Trecho / arquivo

Template mínimo de descrição (sem citar plataforma):

```markdown
## O quê
Corrige cálculo de total quando desconto é zero.

## Por quê
Pedidos com desconto 0 exibiam total R$ NaN na tela de confirmação.

## Como testar
1. Criar pedido com subtotal R$ 50,00 e desconto 0.
2. Abrir tela de confirmação.
3. Verificar que total mostra R$ 50,00 (não NaN).

## Escopo
- Altera: calcula-total.js
- Branch: corrige-total → main
```

- **O quê** — resumo em uma frase do que o merge traz.
- **Por quê** — motivo de negócio ou bug; não basta "porque sim".
- **Como testar** — passos que o revisor (ou você daqui a três meses) consegue repetir.
- **Escopo** — arquivos e branch envolvidos; limita surpresas no diff.

## O que observar

- PR é portão: código novo não entra direto na main em projeto sério.
- Descrição boa acelera review; descrição vazia vira "confia no diff".
- O diff mostra linha por linha o que muda — a descrição explica o contexto.
- Depois do merge, a main vira fonte para deploy (ponte para episódio 07).

## O que quebra se faltar

| Ausência | Consequência |
|---|---|
| PR antes do merge | Mudanças entram sem olhar; bug ou regressão na main. |
| Seção "por quê" | Revisor não sabe se a mudança é necessária ou acidental. |
| Passos de teste | Ninguém valida; bug volta na produção. |
| Review de outra pessoa (quando possível) | Olhar único perde caso óbvio; rede de segurança mais fraca. |
