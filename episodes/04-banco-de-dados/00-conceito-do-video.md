# Conceito do video - Banco de Dados

## Tese

A maioria das pessoas que programa com IA hoje nao distingue entre "a pagina lembrou" e "o dado sobreviveu". Para a IA, tudo e variavel. Mas existe uma diferenca gigantesca entre a memoria da pagina (que morre quando fecha) e a memoria do servidor (que precisa de um banco para durar).

Este video conta por que o banco de dados existe, o que ele guarda de verdade, e o que quebra quando se ignora ele. A narrativa e linear: comeca na memoria volatil do servidor, descobre que dados precisam sobreviver, encontra os tipos de banco, aprende a perguntar (query), define a estrutura (schema), e alerta para o que da errado quando a estrutura muda (migracao).

O objetivo nao e ensinar SQL nem comparar motores. E fazer o espectador enxergar o banco como uma camada com responsabilidades claras. Quando ele enxerga, ele para de aceitar que a IA "crie tabelas" sem contexto e comeca a perguntar "essa mudanca toca o schema? precisa de migracao?".

## Por que esse formato funciona

- Linear: cada conceito surge da necessidade do anterior. O espectador nunca e atropelado por jargao solto.
- Arquitetural: o mapa mental que fica e o de camadas (estado da pagina / memoria do servidor / banco / schema / migracao), nao uma lista de ferramentas.
- Superficial de proposito: cada conceito entra com uma analogia e uma consequencia. Aprofundamento fica para videos futuros.
- Practico para IA: o video termina com as perguntas certas para fazer quando a IA sugerir mexer no banco.

## Publico

- Vibe coders que usam Cursor / Claude / Copilot e nao sabem o que e uma query
- Pessoas de produto / negocio que dialogam com devs e ja ouviram "migracao" sem entender
- Iniciantes que ja viram o episodio 01 e querem aprofundar a camada de banco

## Tom

Direto, sem jargao desnecessario. Cada termo tecnico que aparece e imediatamente traduzido em uma frase. Didatico, nao academico. Gui falando para camera ou com tela mostrando um diagrama simples.

## Estrutura em 3 atos

**ATO 1 - A necessidade (por que existe banco)**
O servidor esquece tudo entre requests. A memoria da pagina nao persiste. Alguns dados precisam sobreviver. O banco nasce dessa necessidade.

**ATO 2 - Como funciona (tipos, query, schema)**
Tipos de banco no conceito (relacional, documento, key-value). Como o servidor pede algo ao banco (query). A estrutura dos dados (schema). Cada peca aparece porque a historia precisa dela.

**ATO 3 - O que da errado (riscos e migracao)**
Dado duplicado, inconsistente, perdido, concorrencia. Por que salvar KPI ou comercio no navegador e perigoso. Quando a estrutura muda, nasce a migracao. A IA as vezes ignora isso e quebra em silencio.

## O que NAO entra neste video

- SQL profundo, sintaxe de queries especificas
- Comparacao exaustiva de bancos (Postgres vs MySQL vs MongoDB)
- Otimizacao, indices, particionamento, performance
- Backup, replicacao, alta disponibilidade
- Modelagem de dados detalhada (normalizacao, entidades-relacionamentos)

Esses viram videos da serie, um por tema. Este video e o mapa da camada de banco.
