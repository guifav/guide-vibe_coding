# Exemplo 2 - Branch

## O que ilustra

O ATO 2 do episódio 06: **branch** como linha paralela. A `main` continua estável enquanto `corrige-total` experimenta a correção; o **merge** junta de volta quando estiver pronto.

## Trecho / arquivo

```
main:           ●───●───●─────────────────●  (merge)
                     \                   /
corrige-total:        ●───●───●───●───/
                      ↑           ↑
                   branch      commits da correção
                   criada      na linha paralela
```

Passos narrados:

1. **`main`** em `e4f5g6h` — versão oficial com bug no total.
2. **`git branch corrige-total`** — abre ramal paralelo a partir da main.
3. Dois commits em `corrige-total` — testa correção sem tocar na principal.
4. **`merge corrige-total → main`** — junta a correção; main avança com o fix.

- **`main`** — linha principal, versão oficial do projeto.
- **`corrige-total`** — branch descartável ou efêmera; nome descreve o objetivo.
- **Merge** — ponto onde as linhas convergem; main passa a incluir a correção.

## O que observar

- Branch existe porque ninguém quer estragar o original enquanto testa.
- Commits na branch não alteram a main até o merge — rede de segurança em ação.
- Nome da branch (`corrige-total`) ajuda quem revisa a entender o propósito.
- Se a correção falhar, descarta-se a branch; a main nunca foi arriscada.

## O que quebra se faltar

| Ausência | Consequência |
|---|---|
| Branch separada | Correção experimental quebra a versão oficial no meio do trabalho. |
| Merge consciente | Código pronto fica preso na branch; main nunca recebe o fix. |
| Main protegida | "Versão oficial" vira amontoado de testes incompletos. |
| Commits na branch (não só arquivos soltos) | Sem histórico do que mudou na correção; difícil revisar. |
