# Conceito do vídeo - Banco de Dados

## Tese

A maioria das pessoas que programa com IA hoje não distingue entre "a página lembrou" e "o dado sobreviveu". Para a IA, tudo é variável. Mas existe uma diferença gigantesca entre a memória da página (que morre quando fecha) e o dado persistente (que sobrevive em uma camada separada, normalmente um banco).

Este vídeo conta por que o banco de dados existe, o que ele guarda de verdade, e o que quebra quando se ignora ele. A narrativa é linear: começa na memória não confiável do servidor, descobre que dados precisam sobreviver, encontra os tipos de banco, aprende a perguntar (query), define a estrutura (schema), e alerta para o que dá errado quando a estrutura muda (migração).

O objetivo é fazer o espectador enxergar o banco como uma camada com responsabilidades claras. Quando ele enxerga, ele para de aceitar que a IA "crie tabelas" sem contexto e começa a perguntar "essa mudança toca o schema? precisa de migração?".

## Por que esse formato funciona

- Linear: cada conceito surge da necessidade do anterior. O espectador nunca é atropelado por jargão solto.
- Arquitetural: o mapa mental que fica é o de camadas (estado da página / memória não confiável do servidor / banco / schema / migração), não uma lista de ferramentas.
- Superficial de propósito: cada conceito entra com uma analogia e uma consequência. Aprofundamento fica para vídeos futuros.
- Practico para IA: o vídeo termina com as perguntas certas para fazer quando a IA sugerir mexer no banco.

## Público

- Vibe coders que usam Cursor / Claude / Copilot e não sabem o que é uma query
- Pessoas de produto / negócio que dialogam com devs e já ouviram "migração" sem entender
- Iniciantes que já viram o episódio 01 e querem aprofundar a camada de banco

## Tom

Direto, sem jargão desnecessário. Cada termo técnico que aparece é imediatamente traduzido em uma frase. Didático, não acadêmico. Gui falando para câmera ou com tela mostrando um diagrama simples.

## Estrutura em 3 atos

**ATO 1 - A necessidade (por que existe banco)**
O servidor até pode lembrar em memória, mas essa lembrança não é confiável nem compartilhada. Para dados que precisam sobreviver a reinícios e aparecer em outros dispositivos, usamos uma camada persistente, normalmente um banco de dados.

**ATO 2 - Como funciona (tipos, query, schema)**
Tipos de banco no conceito (relacional, documento, key-value). Como o servidor pede algo ao banco (query). A estrutura dos dados (schema). Cada peça aparece porque a história precisa dela.

**ATO 3 - O que dá errado (riscos e migração)**
Dado duplicado, inconsistente, perdido, concorrência. Por que salvar KPI ou comércio no navegador é perigoso. Quando a estrutura muda, nasce a migração. A IA às vezes ignora isso; quando algo dá errado, o banco costuma avisar, mas a aplicação pode ignorar o aviso.

## O que Não entra neste vídeo

- SQL profundo, sintaxe de queries específicas
- Comparação exaustiva de bancos (Postgres vs MySQL vs MongoDB)
- Otimização, índices, particionamento, performance
- Backup, replicação, alta disponibilidade
- Modelagem de dados detalhada (normalização, entidades-relacionamentos)

Esses viram vídeos da série, um por tema. Este vídeo é o mapa da camada de banco.
