# Roteiro completo - Banco de Dados

**Duração alvo:** 15-20 min
**Formato:** Gui falando para câmera, alternando com diagrama simples na tela
**Regra pedagógica:** cada termo técnico é traduzido em 1 frase antes de continuar. Nenhum termo fica sem tradução.

---

## ABERTURA (0:00-0:45)

### Na câmera

"Você cria uma conta num site, fecha a aba, desliga o computador. Volta no dia seguinte. A conta ainda está lá. Ou então você confirma um pedido, abre em outro celular, e ele aparece. Como o servidor lembrou?"

"A resposta é banco de dados. Mas a maioria das pessoas que programa com IA hoje não distingue entre 'a página lembrou' e 'o dado sobreviveu'. Para a IA, tudo é variável."

"Neste vídeo vou contar por que o banco existe, o que ele guarda de verdade, e o que quebra quando você ou a IA ignoram ele. Sem SQL, sem comparação de motores. Só o mapa."

### Mostrar

Diagrama do mapa (arquivo 02) com as camadas em cor clara. Só mostrar, sem explicar. Dizer: "no fim do vídeo, esse mapa vai estar todo preenchido, e você vai saber o que quebra em cada pedaço dele."

---

## ATO 1 - A necessidade (0:45-6:00)

### Cena 1 - O servidor não confia na própria memória (0:45-2:00)

### Falar

"No episódio anterior a gente viu que o servidor recebe um pedido, processa e devolve uma resposta. Mas tem um detalhe importante sobre o que ele lembra."

"O servidor até pode guardar coisas em memória, igual um programa qualquer. Mas essa memória não é confiável. O processo pode reiniciar a qualquer momento. Pode rodar em várias cópias ao mesmo tempo, cada uma com a sua memória separada. E um usuário atendido por uma cópia não é visto pelas outras."

"Por isso dizemos que a memória do servidor não serve para guardar dado importante. Ela dura enquanto o processo tá no ar e ninguém mexeu."

### Mostrar

Três situações lado a lado, cada uma com um X: servidor reiniciou (memória sumiu), duas cópias do servidor rodando (memórias diferentes), usuário atendido pela cópia B não aparece na cópia A.

### Falar

"Mas óbvio que alguns dados precisam sobreviver. Se você criou conta, o servidor precisa lembrar no dia seguinte, mesmo depois de reiniciar. Se fez um pedido, a loja precisa guardar. Se a IA disse que salvou mas só ficou na memória do processo, o dado sumiu no primeiro reinício."

"É para isso que existe o banco de dados."

### Cena 2 - O que precisa durar (2:00-3:30)

### Falar

"Nem tudo precisa durar. A cor do botão que você clicou não. O texto que você digitou num campo e ainda não enviou não. Isso é memória da página."

"O que precisa durar são os dados que pertencem ao sistema, não à sessão atual: usuários, pedidos, produtos, mensagens, configurações."

### Mostrar

Uma tabela simples com duas colunas: "memória da página (morre)" e "banco (dura)". Exemplos lado a lado.

### Falar

"Termo que vai aparecer: dado persistente. Persistente quer dizer que sobrevive entre requests, entre sessões, entre reinícios, e que aparece igual para qualquer cópia do servidor. O banco é onde mora o dado persistente."

### Cena 3 - Dado estruturado vs memória da página (3:30-6:00)

### Falar

"Tem uma confusão muito comum em quem programa com IA. A página tem estado, lembra? Aquilo do episódio 02, a memória enquanto a aba está aberta."

"Pessoa clica, muda uma variável no front, a tela atualiza. Ela acha que salvou. Mas se fechar a aba, perdeu. Estado da página não é banco."

### Mostrar

Dois caminhos lado a lado. Caminho A: clica -> variável muda no front -> tela atualiza -> fecha aba -> some. Caminho B: clica -> front manda request para o servidor -> servidor grava no banco -> dura para sempre.

### Falar

"A regra é simples: dado que importa para o negócio tem que atravessar o servidor e chegar no banco. Dado que só importa para a sessão atual pode ficar no front."

"Quando a IA te disser 'salvei', pergunte: salvei onde? No front ou no banco? Se ela não fez o dado atravessar o servidor, ela não salvou de verdade."

### Fechamento do ATO 1

Mostrar o mapa de camadas com as partes do ATO 1 destacadas: memória não confiável do servidor, dado persistente, front vs banco. Dizer: "agora que a gente sabe por que o banco existe, vamos entender como ele funciona por dentro."

---

## ATO 2 - Como funciona (6:00-12:00)

### Cena 1 - Tipos de banco no conceito (6:00-6:45)

### Falar

"Existem vários tipos de banco, mas você não precisa saber todos para programar com IA. O mapa mental cabe em três famílias: tabelas com linhas e colunas (relacional), blocos de texto estruturado soltos como JSON (documento), e um dicionário gigante de chave e valor. Isso é o bastante para entender o que a IA está sugerindo."

### Mostrar

Três retângulos lado a lado, cada um com um ícone simples: tabela (relacional), documento (JSON), chave-valor. Sem nomes de produto.

### Falar

"O importante aqui é saber que existem famílias diferentes, e que quando a IA fala em 'banco relacional', 'banco de documentos', 'banco chave-valor', ela está falando de um desses três grupos."

### Cena 2 - Query: como o servidor pede algo ao banco (6:45-8:15)

### Falar

"O servidor não acessa o banco diretamente como se fosse um arquivo. Ele faz uma pergunta. Essa pergunta se chama query."

"Query é o pedido estruturado que o servidor faz ao banco. Pode ser 'me dá todos os usuários', 'me dá o pedido número 42', 'quantos cadastros temos hoje?'."

### Mostrar

Diagrama: servidor -> seta com "query" -> banco -> seta com "resultado" -> servidor.

### Falar

"No banco relacional a query costuma ser escrita numa linguagem chamada SQL. Mas o detalhe não importa agora. O que importa: query é a pergunta, resultado é a resposta. E query não é só leitura: também grava, altera e apaga. A query de leitura é o select."

"Quando a IA fala em 'query', 'select', 'buscar', 'filtrar', ela está falando de uma pergunta ao banco. Query inválida, o banco reclama na hora. Mas query válida perguntando a coisa errada, o banco responde errado sem reclamar. Ele não sabe o que você quis dizer."

### Cena 3 - Schema: a estrutura dos dados (8:15-12:00)

### Falar

"O banco não guarda qualquer coisa de qualquer jeito. Ele tem estrutura. Essa estrutura se chama schema."

"Schema é a estrutura dos dados. Em bancos relacionais, o schema são tabelas e colunas: na tabela de usuários, por exemplo, coluna nome é texto, coluna email é texto, coluna data de nascimento é data, coluna ativo é verdadeiro ou falso."

"Em bancos de documentos, o schema é um formato esperado: o documento deveria ter esses campos, com esses tipos. A ideia é a mesma: existe uma estrutura esperada para o dado entrar."

### Mostrar

Duas representações lado a lado: à esquerda uma tabela (relacional) com cabeçalhos nome | email | nascimento | ativo e o tipo ao lado de cada coluna; à direita um documento JSON (documento) com os mesmos campos indicados como formato esperado.

### Falar

"O schema é o contrato do banco. Ele diz o que pode entrar e o que não pode. No relacional, se você tentar gravar uma data numa coluna de texto, o banco reclama. No de documentos, a verificação pode ser mais flexível, mas o princípio se mantém: existe um formato esperado."

"Isso é bom. Protege o dado. Mas também é onde mora o perigo com IA. Vamos ver no próximo ato."

### Fechamento do ATO 2

Mostrar o mapa com tipos, query e schema destacados. Dizer: "essa é a anatomia do banco. Agora vamos ver o que dá errado."

---

## ATO 3 - O que dá errado (12:00-18:00)

### Cena 1 - Dado duplicado, inconsistente, perdido (12:00-13:30)

### Falar

"Banco resolve muita coisa, mas introduz riscos novos. Vou listar os quatro mais comuns."

"Primeiro: duplicado. O mesmo usuário gravado duas vezes. O mesmo pedido registrado em duplicata. Acontece quando o servidor grava sem uma proteção real. Atenção: só checar se já existe antes de gravar não resolve. Se dois pedidos chegarem ao mesmo tempo, os dois checam, os dois não encontram, e os dois gravam. A proteção de verdade vem de uma restrição de unicidade no banco ou de uma operação desenhada para não repetir (idempotente)."

"Segundo: inconsistente. O cliente mudou o email num lugar, mas o outro lugar ainda tem o antigo. Dado certo aqui, errado ali. O banco ficou descoordenado."

"Terceiro: perdido. O servidor disse que gravou mas o banco não confirmou. Ou a conexão caiu no meio da gravação. Resultado: usuário acha que salvou, mas o dado não chegou."

"Quarto: concorrência. Dois usuários editando o mesmo dado ao mesmo tempo. Um sobrescreve o outro sem saber. Isso é clássico em sistemas reais."

### Mostrar

Quatro ícones simples com as palavras: duplicado, inconsistente, perdido, concorrência.

### Falar

"Esses erros normalmente geram uma resposta de erro do banco. O problema é que o silêncio aparece quando a aplicação ignora ou trata mal esse erro. O banco fala; o código que não escuta. Por isso o banco precisa de disciplina: validar a entrada, confirmar a gravação, tratar concorrência."

### Cena 2 - Por que o front não é banco (13:30-15:00)

### Falar

"Tem um erro que vejo bastante em quem programa com IA: guardar dado de negócio no navegador."

"Pessoa cria um painel de KPI (indicador de desempenho do negócio) e salva os números no front, numa variável, num armazenamento local do navegador. Acha que resolveu. Mas: se a pessoa limpar o navegador, perdeu. Se abrir em outro computador, não vê. Se outra pessoa precisar ver, não tem como."

### Mostrar

Duas situações lado a lado. Esquerda: navegador com dados locais e um X vermelho (limpou, perdeu). Direita: servidor com banco e um check verde (acessível de qualquer lugar).

### Falar

"Regra prática: dado que é de todos, ou que precisa durar, ou que alimenta decisão de negócio, não pode morar só no navegador. Tem que atravessar o servidor e chegar no banco."

"Isso vale para KPI, para itens de catálogo, para configurações do negócio, para qualquer coisa que não seja preferência pessoal de sessão."

### Cena 3 - Migração: quando a estrutura muda (15:00-17:00)

### Falar

"Lembra do schema? A estrutura do banco. Pois é: essa estrutura muda. Você adiciona uma coluna, remove outra, muda um tipo. Quando isso acontece, nasce a migração."

"Migração é o conjunto de instruções que atualiza o schema do banco de uma versão para outra. Sem migração, o código novo espera uma estrutura que o banco ainda não tem. E quebra."

### Mostrar

Linha do tempo: schema v1 -> migração -> schema v2. código novo espera schema v2. Se o banco ainda tá em v1, dá erro.

### Falar

"Aqui é onde a IA mais engana. Ela sugere adicionar uma coluna no código, criar uma nova tabela, mudar um campo. Mas ela às vezes ignora a migração. Ela escreve o código como se o banco já estivesse atualizado."

"Resultado: você sobe o código, e na hora de gravar o dado, o banco reclama que a coluna não existe. Ou pior: a aplicação ignora o erro que o banco devolveu, e o dado some sem aviso."

"Quando a IA sugerir mexer na estrutura de dados, pergunte sempre: isso precisa de migração? Ela já gerou? Quem vai rodar?"

### Cena 4 - Ponte para o próximo episódio (17:00-18:00)

### Falar

"O banco guarda os dados de todos. Os usuários, os pedidos, as configurações. Mas se os dados são de todos, como saber quem pode ver o quê?"

"O cliente pode ver seus próprios pedidos, mas não os dos outros. O administrador pode ver tudo. O visitante sem login não deveria ver nada privado."

"É para resolver isso que existe a próxima camada: autenticação e autorização. Quem é você, e o que você pode fazer. Isso é o tema do próximo episódio."

### Fechamento do ATO 3

Mostrar o mapa completo: memória não confiável, dado persistente, tipos de banco, query, schema, migração, riscos.

### Falar

"Resumindo as três proteções que importam na prática. Primeira: validar a entrada antes de gravar, para o dado chegar limpo. Segunda: confirmar a gravação, para não assumir que salvou só porque o servidor respondeu. Terceira: migrar com segurança, para mudar a estrutura sem quebrar o que já existe."

---

## ENCERRAMENTO (18:00-19:30)

### Na câmera

"Para programar com IA sem ser enganado, você só precisa saber que o banco existe, o que ele guarda, e o que quebra quando se ignora a estrutura."

"Quando a IA sugerir uma mudança que toca dados, pergunte: isso mora no front ou no banco? Precisa de query? Mexe no schema? Tem migração?"

"Se você não souber responder, pergunte para ela mesma: 'essa mudança toca o banco? tem migração?'. A resposta te dá o contexto do risco."

"Na descrição tem o glossário com todos os termos que apareceram. Repo público [link] para consultar depois."

"O próximo episódio vai ser sobre autenticação e autorização: se os dados são de todos, como saber quem pode ver o quê?"

### Call to action

- Inscreva-se para a série
- Comente qual parte do banco você quer aprofundar
- Repo com o glossário: [link]
