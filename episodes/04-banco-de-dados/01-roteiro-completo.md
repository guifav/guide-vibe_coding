# Roteiro completo - Banco de Dados

**Duracao alvo:** 15-20 min
**Formato:** Gui falando para camera, alternando com diagrama simples na tela
**Regra pedagogica:** cada termo tecnico e traduzido em 1 frase antes de continuar. Nenhum termo fica sem traducao.

---

## ABERTURA (0:00-0:45)

### Na camera

"Voce abre um site, adiciona um produto no carrinho, fecha a aba. Volta no dia seguinte. O carrinho ainda esta la. Como o servidor lembrou?"

"A resposta nao e magia. E banco de dados. Mas a maioria das pessoas que programa com IA hoje nao distingue entre 'a pagina lembrou' e 'o dado sobreviveu'. Para a IA, tudo e variavel."

"Neste video vou contar por que o banco existe, o que ele guarda de verdade, e o que quebra quando voce ou a IA ignoram ele. Sem SQL, sem comparacao de motores. So o mapa."

### Mostrar

Diagrama do mapa (arquivo 02) com as camadas em cor clara. So mostrar, sem explicar. Dizer: "esse mapa vai ganhando vida aos poucos. No fim voce vai enxergar o banco inteiro."

---

## ATO 1 - A necessidade (0:45-6:00)

### Cena 1 - O servidor esquece (0:45-2:00)

### Falar

"No episodio anterior a gente viu que o servidor recebe um pedido, processa e devolve uma resposta. Mas tem um detalhe que muita gente esquece: depois que ele responde, ele esquece."

"O servidor, por natureza, e amnesico. Cada request e uma conversa isolada. Quando termina, o servidor nao lembra de voce."

"Isso nao e defeito. E assim que ele funciona para conseguir atender milhares de pedidos ao mesmo tempo sem explodir de informacao."

### Mostrar

Dois retangulos lado a lado: "REQUEST 1" e "REQUEST 2". Uma setinha entre eles com a palavra "esquece".

### Falar

"Mas obvio que alguns dados precisam sobreviver. Se voce criou conta, o servidor precisa lembrar no dia seguinte. Se fez um pedido, a loja precisa guardar. Se a IA disse que salvou, mas o servidor esquece, o dado sumiu."

"E para isso que existe o banco de dados."

### Cena 2 - O que precisa durar (2:00-3:30)

### Falar

"Nem tudo precisa durar. A cor do botao que voce clicou nao. O texto que voce digitou num campo e ainda nao enviou nao. Isso e memoria da pagina."

"O que precisa durar sao os dados que pertencem ao sistema, nao a sessao atual: usuarios, pedidos, produtos, mensagens, configuracoes."

### Mostrar

Uma tabela simples com duas colunas: "memoria da pagina (morre)" e "memoria do servidor (dura)". Exemplos lado a lado.

### Falar

"Termo que vai aparecer: dado persistente. Persistente quer dizer que sobrevive entre requests, entre sessoes, entre reinicios. O banco e onde mora o dado persistente."

### Cena 3 - Dado estruturado vs memoria da pagina (3:30-6:00)

### Falar

"Tem uma confusao muito comum em quem programa com IA. A pagina tem estado, lembra? Aquilo do episodio 01, a memoria enquanto a aba esta aberta."

"Pessoa clica, muda uma variavel no front, a tela atualiza. Ela acha que salvou. Mas se fechar a aba, perdeu. Estado da pagina nao e banco."

### Mostrar

Dois caminhos lado a lado. Caminho A: clica -> variavel muda no front -> tela atualiza -> fecha aba -> some. Caminho B: clica -> front manda request para o servidor -> servidor grava no banco -> dura para sempre.

### Falar

"A regra e simples: dado que importa para o negocio tem que atravessar o servidor e chegar no banco. Dado que so importa para a sessao atual pode ficar no front."

"Quando a IA te disser 'salvei', pergunte: salvei onde? No front ou no banco? Se ela nao fez o dado atravessar o servidor, ela nao salvou de verdade."

### Fechamento do ATO 1

Mostrar o mapa de camadas com as partes do ATO 1 destacadas: memoria volatil do servidor, dado persistente, front vs banco. Dizer: "agora que a gente sabe por que o banco existe, vamos entender como ele funciona por dentro."

---

## ATO 2 - Como funciona (6:00-12:00)

### Cena 1 - Tipos de banco no conceito (6:00-8:30)

### Falar

"Existem varios tipos de banco, mas voce nao precisa saber todos. Vou te dar tres para ter o mapa mental."

### Mostrar

Tres retangulos lado a lado, cada um com um icone simples: tabela (relacional), documento (JSON), chave-valor.

### Falar

"Primeiro: relacional. O banco relacional guarda dados em tabelas, com linhas e colunas, igual uma planilha. As tabelas se relacionam: uma tabela de pedidos aponta para uma tabela de clientes. E o tipo mais comum."

"Segundo: documento. O banco de documentos guarda dados em blocos de texto estruturado, parecido com JSON. Cada registro e um documento solto, sem tabela rigida. Bom quando o formato muda muito."

"Terceiro: chave-valor. O banco chave-valor funciona como um dicionario gigante: voce da uma chave, ele devolve um valor. Simples, rapido, sem estrutura complexa."

### Traduzir

- Relacional: tabelas com linhas, colunas e relacoes entre elas
- Documento: registros soltos em formato de texto estruturado, sem tabela rigida
- Chave-valor: dicionario gigante, entra chave sai valor

### Falar

"O importante agora nao e escolher. E saber que existem familias diferentes, e que quando a IA fala em 'Postgres', 'MySQL', 'MongoDB', 'Redis', ela esta falando de um desses tres grupos."

### Cena 2 - Query: como o servidor pede algo ao banco (8:30-10:00)

### Falar

"O servidor nao acessa o banco diretamente como se fosse um arquivo. Ele faz uma pergunta. Essa pergunta se chama query."

"Query e o pedido estruturado que o servidor faz ao banco. Pode ser 'me da todos os usuarios', 'me da o pedido numero 42', 'quantos cadastros temos hoje?'."

### Mostrar

Diagrama: servidor -> seta com "query" -> banco -> seta com "resultado" -> servidor.

### Falar

"No banco relacional a query costuma ser escrita numa linguagem chamada SQL. Mas o detalhe nao importa agora. O que importa: query e a pergunta, resultado e a resposta."

"Quando a IA fala em 'query', 'select', 'buscar', 'filtrar', ela esta falando de uma pergunta ao banco. Se ela montar a query errada, o banco responde errado sem reclamar. Ele nao sabe o que voce quis dizer."

### Cena 3 - Schema: a estrutura dos dados (10:00-12:00)

### Falar

"O banco nao guarda qualquer coisa de qualquer jeito. Ele tem estrutura. Essa estrutura se chama schema."

"Schema e a definicao do que cada coluna significa. Na tabela de usuarios, por exemplo: coluna nome e texto, coluna email e texto, coluna data de nascimento e data, coluna ativo e verdadeiro ou falso."

### Mostrar

Uma tabela desenhada com cabecalhos: nome | email | nascimento | ativo. Cada coluna com o tipo ao lado.

### Falar

"O schema e o contrato do banco. Ele diz o que pode entrar e o que nao pode. Se voce tentar gravar uma data numa coluna de texto, o banco reclama."

"Isso e bom. Protege o dado. Mas tambem e onde mora o perigo com IA. Vamos ver no proximo ato."

### Fechamento do ATO 2

Mostrar o mapa com tipos, query e schema destacados. Dizer: "essa e a anatomia do banco. Agora vamos ver o que da errado."

---

## ATO 3 - O que da errado (12:00-18:00)

### Cena 1 - Dado duplicado, inconsistente, perdido (12:00-13:30)

### Falar

"Banco resolve muita coisa, mas introduz riscos novos. Vou listar os quatro mais comuns."

"Primeiro: duplicado. O mesmo usuario gravado duas vezes. O mesmo pedido registrado em duplicata. Acontece quando o servidor grava sem checar se ja existe."

"Segundo: inconsistente. O cliente mudou o email num lugar, mas o outro lugar ainda tem o antigo. Dado certo aqui, errado ali. O banco ficou descoordenado."

"Terceiro: perdido. O servidor disse que gravou mas o banco nao confirmou. Ou a conexao caiu no meio da gravacao. Resultado: usuario acha que salvou, mas o dado nao chegou."

"Quarto: concorrencia. Dois usuarios editando o mesmo dado ao mesmo tempo. Um sobrescreve o outro sem saber. Isso e classico em sistemas reais."

### Mostrar

Quatro icones simples com as palavras: duplicado, inconsistente, perdido, concorrencia.

### Falar

"Nenhum desses erros da tela azul. Eles acontecem em silencio. Por isso o banco precisa de disciplina: checar antes de gravar, confirmar a gravacao, tratar concorrencia."

### Cena 2 - Por que o front nao e banco (13:30-15:00)

### Falar

"Tem um erro que vejo bastante em quem programa com IA: guardar dado de negocio no navegador."

"Pessoa cria um painel de KPI e salva os numeros no front, numa variavel, num armazenamento local do navegador. Acha que resolveu. Mas: se a pessoa limpar o navegador, perdeu. Se abrir em outro computador, nao ve. Se outra pessoa precisar ver, nao tem como."

### Mostrar

Duas situacoes lado a lado. Esquerda: navegador com dados locais e um X vermelho (limpou, perdeu). Direita: servidor com banco e um check verde (acessivel de qualquer lugar).

### Falar

"Regra pratica: dado que e de todos, ou que precisa durar, ou que alimenta decisao de negocio, nao pode morar so no navegador. Tem que atravessar o servidor e chegar no banco."

"Isso vale para KPI, para itens de catalogo, para configuracoes de comercio, para qualquer coisa que nao seja preference pessoal de sessao."

### Cena 3 - Migracao: quando a estrutura muda (15:00-17:00)

### Falar

"Lembra do schema? A estrutura do banco. Pois e: essa estrutura muda. Voce adiciona uma coluna, remove outra, muda um tipo. Quando isso acontece, nasce a migracao."

"Migracao e o conjunto de instrucoes que atualiza o schema do banco de uma versao para outra. Sem migracao, o codigo novo espera uma estrutura que o banco ainda nao tem. E quebra."

### Mostrar

Linha do tempo: schema v1 -> migracao -> schema v2. codigo novo espera schema v2. Se o banco ainda ta em v1, da erro.

### Falar

"Aqui e onde a IA mais engana. Ela sugere adicionar uma coluna no codigo, criar uma nova tabela, mudar um campo. Mas ela as vezes ignora a migracao. Ela escreve o codigo como se o banco ja estivesse atualizado."

"Resultado: voce sobe o codigo, e na hora de gravar o dado, o banco reclama que a coluna nao existe. Ou pior, ele nao reclama e o dado some."

"Quando a IA sugerir mexer na estrutura de dados, pergunte sempre: isso precisa de migracao? Ela ja gerou? Quem vai rodar?"

### Cena 4 - Ponte para o proximo episodio (17:00-18:00)

### Falar

"O banco guarda os dados de todos. Os usuarios, os pedidos, as configuracoes. Mas se os dados sao de todos, como saber quem pode ver o quê?"

"O cliente pode ver seus proprios pedidos, mas nao os dos outros. O administrador pode ver tudo. O visitante sem login nao deveria ver nada privado."

"E para resolver isso que existe a proxima camada: autenticacao e autorizacao. Quem e voce, e o que voce pode fazer. Isso e o tema do proximo episodio."

### Fechamento do ATO 3

Mostrar o mapa completo: memoria volatil, dado persistente, tipos de banco, query, schema, migracao, riscos.

---

## ENCERRAMENTO (18:00-19:30)

### Na camera

"Para programar com IA sem ser enganado, voce nao precisa saber SQL nem escolher o banco perfeito. Precisa saber que o banco existe, o que ele guarda, e o que quebra quando se ignora a estrutura."

"Quando a IA sugerir uma mudanca que toca dados, pergunte: isso mora no front ou no banco? Precisa de query? Mexe no schema? Tem migracao?"

"Se voce nao souber responder, pergunte para ela mesma: 'essa mudanca toca o banco? tem migracao?'. A resposta te da o contexto do risco."

"Na descricao tem o glossario com todos os termos que apareceram. Repo publico [link] para consultar depois."

"O proximo episodio vai ser sobre autenticacao e autorizacao: se os dados sao de todos, como saber quem pode ver o que?"

### Call to action

- Inscreva-se para a serie
- Comente qual parte do banco voce quer aprofundar
- Repo com o glossario: [link]
