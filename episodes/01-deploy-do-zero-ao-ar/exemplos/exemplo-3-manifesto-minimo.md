# Exemplo 3 - Manifesto mínimo (extra)

## O que ilustra

Um manifesto de projeto — aqui em formato genérico — nomeia o app e declara os **scripts** que o cano de build e deploy costuma chamar. Não amarra a nenhuma ferramenta real; mostra só a ideia de "o pipeline precisa saber como construir e iniciar".

## Trecho / arquivo

Ver [`exemplo-3-manifesto-minimo.json`](./exemplo-3-manifesto-minimo.json):

```json
{
  "name": "app-exemplo",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "build": "echo build-exemplo",
    "start": "echo start-exemplo"
  }
}
```

- **`name`** — identifica o projeto no repo e nos logs do pipeline.
- **`scripts.build`** — comando que CI/deploy invoca para gerar o artefato publicável.
- **`scripts.start`** — comando para subir o processo em ambiente de execução (quando o deploy roda um servidor Node, por exemplo).

## O que observar

- O manifesto não é o app; é a **ficha de instruções** que ferramentas externas leem.
- Sem script `build` declarado, o pipeline não sabe o que executar — ou assume um padrão que pode não existir.
- `private: true` evita publicação acidental em registro de pacotes (conceito ilustrativo).
- Projetos sem build (HTML estático) podem não ter manifesto algum — e tudo bem.

## O que quebra se faltar

| Ausência | Consequência |
|---|---|
| Manifesto (em projetos que dependem dele) | CI não encontra comando de build; deploy falha ou publica versão errada. |
| Script `build` | Artefato nunca é gerado; deploy sobe código-fonte cru ou pasta vazia. |
| Script `start` (quando o runtime exige) | Container ou processo sobe e cai imediatamente; site fora do ar. |
| Campo `name` | Logs e dashboards ficam genéricos; difícil saber qual app falhou. |
