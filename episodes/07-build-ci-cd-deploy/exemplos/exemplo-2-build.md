# Exemplo 2 - Build

## O que ilustra

O ATO 1 do episódio 07: o **build** transforma o que você escreveu em algo que o ambiente consegue servir. Pode dar certo (artefato) ou errado (`ok: false` com `motivo`) — dependência faltando, fonte vazia, sintaxe inválida.

## Trecho / arquivo

Ver [`exemplo-2-build.js`](./exemplo-2-build.js):

```javascript
function buildar(fonte) {
  if (!fonte || fonte.trim() === "") {
    return { ok: false, motivo: "Fonte vazia — nada para transformar" };
  }

  if (fonte.includes("import inexistente")) {
    return { ok: false, motivo: "Dependência faltando no import" };
  }

  return {
    ok: true,
    artefato: {
      nome: "app-compilado.js",
      tamanho_bytes: fonte.length * 2,
      gerado_em: "2026-07-28T12:00:00Z",
    },
  };
}
```

- **`fonte`** — código ou arquivos que você editou no editor.
- **`ok: false, motivo`** — build quebrou; o motivo aponta onde olhar (dependência, sintaxe, tipo).
- **`artefato`** — pacote pronto para o deploy; não é mais o fonte solto.

## O que observar

- Build local verde não substitui build no cano — ambientes podem diferir.
- "Build failed" no CI quase sempre é problema de transformação, não de deploy.
- Artefato é o que vai ao ar; editar fonte sem rebuild deixa produção desatualizada.
- Motivo explícito economiza horas de "funcionava na minha máquina".

## O que quebra se faltar

| Ausência | Consequência |
|---|---|
| Etapa de build no cano | Código quebrado ou incompleto chega ao ambiente. |
| Tratamento de erro (`motivo`) | Log genérico; ninguém sabe se foi dependência ou sintaxe. |
| Artefato versionado/publicado | Deploy pega pasta errada ou commit antigo sem rebuild. |
| Build reproduzível | "Passou aqui" não passa no CI; time perde confiança no cano. |
