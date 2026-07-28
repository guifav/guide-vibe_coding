# Glossario minimo (aparece na descrição do YouTube)

Só os termos que aparecem no roteiro. Um por linha, tradução direta.

---

## Memória e persistencia

- **Estado da página (state)** - memória do front enquanto a aba esta aberta; morre ao fechar
- **Memória não confiável do servidor** - o processo até guarda em memória, mas pode reiniciar, rodar em varias cópias, e não compartilha estado entre elas
- **Dado persistente** - dado que sobrevive entre requests, sessoes, reinicios, e aparece igual para qualquer cópia do servidor
- **Banco de dados** - lugar separado, com dados estruturados, que o servidor consulta

## Tipos de banco

- **Relacional** - tabelas com linhas, colunas e relacoes entre elas
- **Documento** - registros soltos em formato de texto estruturado, sem tabela rigida
- **Chave-valor** - dicionario gigante: entra chave, sai valor
- **SQL** - linguagem usada para escrever queries em bancos relacionais

## Como o servidor fala com o banco

- **Query** - pergunta estruturada que o servidor faz ao banco
- **Select** - tipo de query que busca dados (ler)
- **Resultado (result set)** - o que o banco devolve depois de uma query

## Estrutura do dado

- **Schema** - a estrutura dos dados; em bancos relacionais são tabelas e colunas; em bancos de documentos e um formato esperado de campos e tipos
- **Tabela** - estrutura de linhas e colunas no banco relacional
- **Coluna** - campo individual dentro de uma tabela (ex: nome, email)
- **Tipo** - o formato aceito na coluna (texto, número, data, booleano)

## Quando a estrutura muda

- **Migracao** - instrucoes que atualizam o schema de uma versao para outra
- **Schema v1 / v2** - estados da estrutura antes e depois de uma migracao

## Riscos comuns

- **Duplicado** - mesmo dado gravado duas vezes; checar antes de gravar não resolve sob concorrência
- **Inconsistente** - dado certo num lugar, errado em outro
- **Perdido** - servidor disse que gravou mas o dado não chegou ao banco
- **Concorrência** - dois usuarios editam o mesmo dado ao mesmo tempo e um sobrescreve o outro
- **Idempotente** - operação desenhada para, se repetida, não gerar efeito extra; protege contra duplicidade
- **Restrição de unicidade** - regra no banco que impede gravar dois registros com o mesmo valor num campo (ex: email)

---

## Pergunta-chave para usar com IA

Quando a IA sugerir uma mudança que toca dados, pergunte:

"Essa mudança mora no front ou no banco?"

E em seguida:

"Precisa de query? Mexe no schema? Tem migracao?"

As opcoes de camada são:
- Front (estado da página, memória local)
- Servidor (lógica, request)
- Banco (dado persistente, schema, migracao)

A resposta diz o tamanho do risco. Se ela mexer no schema sem gerar migracao, pergunte antes de subir.
