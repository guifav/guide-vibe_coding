# Roteiro completo - Banco de Dados

**Duracao alvo:** 15-20 min
**Formato:** Gui falando para camera, alternando com diagrama simples na tela
**Regra pedagogica:** cada termo técnico e traduzido em 1 frase antes de continuar. Nenhum termo fica sem tradução.

---

## ABERTURA (0:00-0:45)

### Na camera

"Você abre um site, adiciona um produto no carrinho, fecha a aba. Volta no dia seguinte. O carrinho ainda esta la. Como o servidor lembrou?"

"A resposta não e magia. E banco de dados. Mas a maioria das pessoas que programa com IA hoje não distingue entre 'a página lembrou' e 'o dado sobreviveu'. Para a IA, tudo e variável."

"Neste vídeo vou contar por que o banco existe, o que ele guarda de verdade, e o que quebra quando você ou a IA ignoram ele. Sem SQL, sem comparacao de motores. Só o mapa."

### Mostrar

Diagrama do mapa (arquivo 02) com as camadas em cor clara. Só mostrar, sem explicar. Dizer: "esse mapa vai ganhando vida aos poucos. No fim você vai enxergar o banco inteiro."

---

## ATO 1 - A necessidade (0:45-6:00)

### Cena 1 - O servidor esquece (0:45-2:00)

### Falar

"No episodio anterior a gente viu que o servidor recebe um pedido, processa e devolve uma resposta. Mas tem um detalhe que muita gente esquece: depois que ele responde, ele esquece."

"O servidor, por natureza, e amnesico. Cada request e uma conversa isolada. Quando termina, o servidor não lembra de você."

"Isso não e defeito. E assim que ele funciona para conseguir atender milhares de pedidos ao mesmo tempo sem explodir de informação."

### Mostrar

Dois retangulos lado a lado: "REQUEST 1" e "REQUEST 2". Uma setinha entre eles com a palavra "esquece".

### Falar

"Mas óbvio que alguns dados precisam sobreviver. Se você criou conta, o servidor precisa lembrar no dia seguinte. Se fez um pedido, a loja precisa guardar. Se a IA disse que salvou, mas o servidor esquece, o dado sumiu."

"E para isso que existe o banco de dados."

### Cena 2 - O que precisa durar (2:00-3:30)

### Falar

"Nem tudo precisa durar. A cor do botao que você clicou não. O texto que você digitou num campo e ainda não enviou não. Isso e memória da página."

"O que precisa durar são os dados que pertencem ao sistema, não a sessao atual: usuarios, pedidos, produtos, mensagens, configurações."

### Mostrar

Uma tabela simples com duas colunas: "memória da página (morre)" e "memória do servidor (dura)". Exemplos lado a lado.

### Falar

"Termo que vai aparecer: dado persistente. Persistente quer dizer que sobrevive entre requests, entre sessoes, entre reinicios. O banco e onde mora o dado persistente."

### Cena 3 - Dado estruturado vs memória da página (3:30-6:00)

### Falar

"Tem uma confusão muito comum em quem programa com IA. A página tem estado, lembra? Aquilo do episodio 01, a memória enquanto a aba esta aberta."

"Pessoa clica, muda uma variável no front, a tela atualiza. Ela acha que salvou. Mas se fechar a aba, perdeu. Estado da página não e banco."

### Mostrar

Dois caminhos lado a lado. Caminho A: clica -> variável muda no front -> tela atualiza -> fecha aba -> some. Caminho B: clica -> front manda request para o servidor -> servidor grava no banco -> dura para sempre.

### Falar

"A regra e simples: dado que importa para o negocio tem que atravessar o servidor e chegar no banco. Dado que só importa para a sessao atual pode ficar no front."

"Quando a IA te disser 'salvei', pergunte: salvei onde? No front ou no banco? Se ela não fez o dado atravessar o servidor, ela não salvou de verdade."

### Fechamento do ATO 1

Mostrar o mapa de camadas com as partes do ATO 1 destacadas: memória volatil do servidor, dado persistente, front vs banco. Dizer: "agora que a gente sabe por que o banco existe, vamos entender como ele funciona por dentro."

---

## ATO 2 - Como funciona (6:00-12:00)

### Cena 1 - Tipos de banco no conceito (6:00-8:30)

### Falar

"Existem varios tipos de banco, mas você não precisa saber todos. Vou te dar tres para ter o mapa mental."

### Mostrar

Tres retangulos lado a lado, cada um com um icone simples: tabela (relacional), documento (JSON), chave-valor.

### Falar

"Primeiro: relacional. O banco relacional guarda dados em tabelas, com linhas e colunas, igual uma planilha. As tabelas se relacionam: uma tabela de pedidos aponta para uma tabela de clientes. E o tipo mais comum."

"Segundo: documento. O banco de documentos guarda dados em blocos de texto estruturado, parecido com JSON. Cada registro e um documento solto, sem tabela rigida. Bom quando o formato muda muito."

"Terceiro: chave-valor. O banco chave-valor funciona como um dicionario gigante: você da uma chave, ele devolve um valor. Simples, rápido, sem estrutura complexa."

### Traduzir

- Relacional: tabelas com linhas, colunas e relacoes entre elas
- Documento: registros soltos em formato de texto estruturado, sem tabela rigida
- Chave-valor: dicionario gigante, entra chave sai valor

### Falar

"O importante agora não e escolher. E saber que existem familias diferentes, e que quando a IA fala em 'banco relacional', 'banco relacional', 'banco de documentos', 'banco chave-valor', ela esta falando de um desses tres grupos."

### Cena 2 - Query: como o servidor pede algo ao banco (8:30-10:00)

### Falar

"O servidor não acessa o banco diretamente como se fosse um arquivo. Ele faz uma pergunta. Essa pergunta se chama query."

"Query e o pedido estruturado que o servidor faz ao banco. Pode ser 'me da todos os usuarios', 'me da o pedido número 42', 'quantos cadastros temos hoje?'."

### Mostrar

Diagrama: servidor -> seta com "query" -> banco -> seta com "resultado" -> servidor.

### Falar

"No banco relacional a query costuma ser escrita numa linguagem chamada SQL. Mas o detalhe não importa agora. O que importa: query e a pergunta, resultado e a resposta."

"Quando a IA fala em 'query', 'select', 'buscar', 'filtrar', ela esta falando de uma pergunta ao banco. Se ela montar a query errada, o banco responde errado sem reclamar. Ele não sabe o que você quis dizer."

### Cena 3 - Schema: a estrutura dos dados (10:00-12:00)

### Falar

"O banco não guarda qualquer coisa de qualquer jeito. Ele tem estrutura. Essa estrutura se chama schema."

"Schema e a definicao do que cada coluna significa. Na tabela de usuarios, por exemplo: coluna nome e texto, coluna email e texto, coluna data de nascimento e data, coluna ativo e verdadeiro ou falso."

### Mostrar

Uma tabela desenhada com cabecalhos: nome | email | nascimento | ativo. Cada coluna com o tipo ao lado.

### Falar

"O schema e o contrato do banco. Ele diz o que pode entrar e o que não pode. Se você tentar gravar uma data numa coluna de texto, o banco reclama."

"Isso e bom. Protege o dado. Mas também e onde mora o perigo com IA. Vamos ver no próximo ato."

### Fechamento do ATO 2

Mostrar o mapa com tipos, query e schema destacados. Dizer: "essa e a anatomia do banco. Agora vamos ver o que da errado."

---

## ATO 3 - O que da errado (12:00-18:00)

### Cena 1 - Dado duplicado, inconsistente, perdido (12:00-13:30)

### Falar

"Banco resolve muita coisa, mas introduz riscos novos. Vou listar os quatro mais comuns."

"Primeiro: duplicado. O mesmo usuario gravado duas vezes. O mesmo pedido registrado em duplicata. Acontece quando o servidor grava sem checar se já existe."

"Segundo: inconsistente. O cliente mudou o email num lugar, mas o outro lugar ainda tem o antigo. Dado certo aqui, errado ali. O banco ficou descoordenado."

"Terceiro: perdido. O servidor disse que gravou mas o banco não confirmou. Ou a conexão caiu no meio da gravacao. Resultado: usuario acha que salvou, mas o dado não chegou."

"Quarto: concorrência. Dois usuarios editando o mesmo dado ao mesmo tempo. Um sobrescreve o outro sem saber. Isso e classico em sistemas reais."

### Mostrar

Quatro icones simples com as palavras: duplicado, inconsistente, perdido, concorrência.

### Falar

"Nenhum desses erros da tela azul. Eles acontecem em silêncio. Por isso o banco precisa de disciplina: checar antes de gravar, confirmar a gravacao, tratar concorrência."

### Cena 2 - Por que o front não e banco (13:30-15:00)

### Falar

"Tem um erro que vejo bastante em quem programa com IA: guardar dado de negocio no navegador."

"Pessoa cria um painel de KPI (indicador de desempenho do negocio) e salva os números no front, numa variável, num armazenamento local do navegador. Acha que resolveu. Mas: se a pessoa limpar o navegador, perdeu. Se abrir em outro computador, não ve. Se outra pessoa precisar ver, não tem como."

### Mostrar

Duas situacoes lado a lado. Esquerda: navegador com dados locais e um X vermelho (limpou, perdeu). Direita: servidor com banco e um check verde (acessivel de qualquer lugar).

### Falar

"Regra prática: dado que e de todos, ou que precisa durar, ou que alimenta decisão de negocio, não pode morar só no navegador. Tem que atravessar o servidor e chegar no banco."

"Isso vale para KPI, para itens de catalogo, para configurações de comercio, para qualquer coisa que não seja preference pessoal de sessao."

### Cena 3 - Migracao: quando a estrutura muda (15:00-17:00)

### Falar

"Lembra do schema? A estrutura do banco. Pois e: essa estrutura muda. Você adiciona uma coluna, remove outra, muda um tipo. Quando isso acontece, nasce a migracao."

"Migracao e o conjunto de instrucoes que atualiza o schema do banco de uma versao para outra. Sem migracao, o código novo espera uma estrutura que o banco ainda não tem. E quebra."

### Mostrar

Linha do tempo: schema v1 -> migracao -> schema v2. código novo espera schema v2. Se o banco ainda ta em v1, da erro.

### Falar

"Aqui e onde a IA mais engana. Ela sugere adicionar uma coluna no código, criar uma nova tabela, mudar um campo. Mas ela as vezes ignora a migracao. Ela escreve o código como se o banco já estivesse atualizado."

"Resultado: você sobe o código, e na hora de gravar o dado, o banco reclama que a coluna não existe. Ou pior, ele não reclama e o dado some."

"Quando a IA sugerir mexer na estrutura de dados, pergunte sempre: isso precisa de migracao? Ela já gerou? Quem vai rodar?"

### Cena 4 - Ponte para o próximo episodio (17:00-18:00)

### Falar

"O banco guarda os dados de todos. Os usuarios, os pedidos, as configurações. Mas se os dados são de todos, como saber quem pode ver o quê?"

"O cliente pode ver seus proprios pedidos, mas não os dos outros. O administrador pode ver tudo. O visitante sem login não deveria ver nada privado."

"E para resolver isso que existe a proxima camada: autenticação e autorização. Quem e você, e o que você pode fazer. Isso e o tema do próximo episodio."

### Fechamento do ATO 3

Mostrar o mapa completo: memória volatil, dado persistente, tipos de banco, query, schema, migracao, riscos.

---

## ENCERRAMENTO (18:00-19:30)

### Na camera

"Para programar com IA sem ser enganado, você não precisa saber SQL nem escolher o banco perfeito. Precisa saber que o banco existe, o que ele guarda, e o que quebra quando se ignora a estrutura."

"Quando a IA sugerir uma mudança que toca dados, pergunte: isso mora no front ou no banco? Precisa de query? Mexe no schema? Tem migracao?"

"Se você não souber responder, pergunte para ela mesma: 'essa mudança toca o banco? tem migracao?'. A resposta te da o contexto do risco."

"Na descrição tem o glossario com todos os termos que apareceram. Repo público [link] para consultar depois."

"O próximo episodio vai ser sobre autenticação e autorização: se os dados são de todos, como saber quem pode ver o que?"

### Call to action

- Inscreva-se para a série
- Comente qual parte do banco você quer aprofundar
- Repo com o glossario: [link]
