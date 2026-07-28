# Glossario minimo (aparece na descricao do YouTube)

So os termos que aparecem no roteiro. Um por linha, traducao direta.

---

## Memoria e persistencia

- **Estado da pagina (state)** - memoria do front enquanto a aba esta aberta; morre ao fechar
- **Memoria volatil do servidor** - servidor esquece entre requests por natureza
- **Dado persistente** - dado que sobrevive entre requests, sessoes e reinicios
- **Banco de dados** - lugar separado, com dados estruturados, que o servidor consulta

## Tipos de banco

- **Relacional** - tabelas com linhas, colunas e relacoes entre elas (ex: Postgres, MySQL)
- **Documento** - registros soltos em formato de texto estruturado, sem tabela rigida (ex: MongoDB)
- **Chave-valor** - dicionario gigante: entra chave, sai valor (ex: Redis, DynamoDB)
- **SQL** - linguagem usada para escrever queries em bancos relacionais

## Como o servidor fala com o banco

- **Query** - pergunta estruturada que o servidor faz ao banco
- **Select** - tipo de query que busca dados (ler)
- **Insert / Update / Delete** - queries que gravam ou alteram dados (escrever)
- **Resultado (result set)** - o que o banco devolve depois de uma query

## Estrutura do dado

- **Schema** - definicao do que cada coluna significa; o contrato do banco
- **Tabela** - estrutura de linhas e colunas no banco relacional
- **Coluna** - campo individual dentro de uma tabela (ex: nome, email)
- **Tipo** - o formato aceito na coluna (texto, numero, data, booleano)

## Quando a estrutura muda

- **Migracao** - instrucoes que atualizam o schema de uma versao para outra
- **Schema v1 / v2** - estados da estrutura antes e depois de uma migracao

## Riscos comuns

- **Duplicado** - mesmo dado gravado duas vezes por falta de checagem
- **Inconsistente** - dado certo num lugar, errado em outro
- **Perdido** - servidor disse que gravou mas o dado nao chegou ao banco
- **Concorrencia** - dois usuarios editam o mesmo dado ao mesmo tempo e um sobrescreve o outro

---

## Pergunta-chave para usar com IA

Quando a IA sugerir uma mudanca que toca dados, pergunte:

"Essa mudanca mora no front ou no banco?"

E em seguida:

"Precisa de query? Mexe no schema? Tem migracao?"

As opcoes de camada sao:
- Front (estado da pagina, memoria local)
- Servidor (logica, request)
- Banco (dado persistente, schema, migracao)

A resposta diz o tamanho do risco. Se ela mexer no schema sem gerar migracao, pergunte antes de subir.
