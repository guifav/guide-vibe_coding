# Roteiro completo - Request, Response e API

**Duracao alvo:** 15-20 min
**Formato:** Gui falando para camera, alternando com diagrama simples na tela
**Regra pedagogica:** cada termo técnico e traduzido em 1 frase antes de continuar. Nenhum termo fica sem tradução.

---

## ABERTURA (0:00-1:00)

### Na camera

"Você abre um site. Clica num botao. E alguma coisa acontece. Mas o que exatamente viajou entre o seu clique e a resposta que apareceu na tela?"

"No episodio 01 eu contei a história de um deploy, ate ele ir ao ar. No episodio passado, a gente entrou na primeira camada, o navegador. Agora quero abrir uma das camadas mais importantes: o dialogo entre o navegador e o servidor."

"Praticamente tudo que acontece na web e uma conversa de duas partes. O navegador pede. O servidor responde. Neste vídeo eu vou contar essa conversa inteira. E no caminho você vai entender por que a IA as vezes inventa coisas que não existem."

### Mostrar

Diagrama simples (arquivo 02): navegador de um lado, servidor do outro, uma seta indo com "request" e outra voltando com "response". Só mostrar, sem explicar.

---

## ATO 1 - O pedido (1:00-7:00)

### Cena 1 - O que e um request (1:00-3:00)

### Falar

"Quando você digita um endereço ou clica num botao, o navegador manda um pedido para o servidor. Esse pedido se chama request."

"Request e só isso: um pedido. Igual você faz num balcao. Chega, pede algo, espera a resposta."

"Esse pedido viaja por um protocolo chamado HTTP. Não se preocupe com o nome agora. HTTP e só o idioma que navegador e servidor combinaram para conversar. Como um telefone: ambos precisam falar o mesmo idioma para se entender."

### Mostrar

No diagrama, animar a seta do navegador para o servidor com a palavra "REQUEST".

### Traduzir

- Request: o pedido que o navegador manda
- HTTP: o idioma da conversa entre navegador e servidor

### Cena 2 - Metodo: GET e POST (3:00-5:00)

### Falar

"Todo request tem um metodo. O metodo diz o que você quer fazer com o pedido."

"Dois metodos cobrem 90% do que acontece na web. GET e POST."

"GET e pedir. Quando você abre uma página, carrega uma lista, ve um produto, o navegador manda um GET. Ele esta dizendo: 'me da isso'. Só isso. Pela convenção, não muda nada no servidor. Só pede."

"POST e enviar. Quando você preenche um formulario, cria uma conta, adiciona um item no carrinho, o navegador manda um POST. Ele esta dizendo: 'aqui estão dados, faz algo com isso'."

### Mostrar

Dois exemplos lado a lado:
- GET: clicar num link de produtos, lista aparece
- POST: preencher cadastro, conta criada

### Falar

"A diferença e simples: GET pede. POST envia. Se a IA falar em 'fazer um GET' ou 'mandar um POST', ela esta dizendo qual o tipo do pedido."

"Existem outros metodos. PUT, PATCH, DELETE. Mas por enquanto, GET e POST são suficientes para entender a conversa."

### Cena 3 - Endpoint: cada URL e uma porta (5:00-7:00)

### Falar

"O servidor não tem uma única porta de entrada. Ele tem varias. Cada uma atende um pedido diferente."

"Isso e o endpoint. Endpoint e uma porta especifica no balcao do servidor. Cada URL e uma porta."

Exemplos na tela:
- `/api/produtos` devolve a lista de produtos
- `/api/usuarios` devolve a lista de usuarios
- `/api/pedidos` devolve os pedidos

"Cada um desses e um endpoint diferente. O navegador sabe qual porta bater porque a URL diz."

"Pense num banco. Você não vai no caixa eletronico pedir um sanduiche. Cada balcao atende um tipo de pedido. O servidor funciona igual."

### Mostrar

Diagrama com o servidor tendo varias portas (endpoints), cada uma com uma URL. Setas do navegador batendo em portas diferentes.

### Falar

"Quando a IA fala em 'chamar o endpoint' ou 'criar um endpoint novo', ela esta falando de abrir ou usar uma dessas portas."

### Fechamento do ATO 1

Mostrar o diagrama com request, metodo (GET/POST) e endpoint destacados.

"O navegador sempre faz a mesma coisa: manda um pedido, com um metodo, para uma porta. Agora vem a pergunta: o que volta?"

---

## ATO 2 - A resposta (7:00-13:30)

### Cena 1 - JSON: o formato da resposta (7:00-9:00)

### Falar

"O servidor recebe o pedido, processa, e devolve uma resposta. Essa resposta se chama response."

"Mas o que vem dentro da resposta? Dados. E esses dados viajam em um formato chamado JSON."

"JSON e texto organizado. Com chaves para agrupar e listas para sequencias. Facil para o computador ler, facil para o humano entender."

Exemplo na tela:

```
{
  "nome": "Produto A",
  "preco": 29.90,
  "estoque": true
}
```

"Isso e JSON. Nome do produto, preco, se tem estoque. Tudo em texto, organizado."

### Mostrar

Um response JSON simples na tela. Destacar: chaves, aspas, valores.

### Falar

"Quando a IA fala em 'retornar JSON' ou 'parsear JSON', ela esta lidando com esse formato. O front recebe esse texto, le, e monta na tela."

### Cena 2 - O contrato: o que peco vs o que recebo (9:00-11:30)

### Falar

"Aqui vem o conceito mais importante deste vídeo. Presta atencao."

"Quando o front faz um pedido, ele espera algo especifico de volta. Se pediu a lista de produtos, espera produtos. Se pediu o usuario, espera um usuario."

"Isso e o contrato. Contrato e o combinado entre front e servidor: o que eu peco, e o que recebo de volta."

"Se o servidor devolve `nome` e o front espera `título`, quebra. Se o servidor devolve um número e o front espera texto, quebra. O contrato e o que mantem os dois lados sincronizados."

### Mostrar

Dois exemplos:
- Contrato certo: front pede produto, servidor devolve `{ nome, preco }`. Front le nome e preco. Funciona.
- Contrato quebrado: front espera `título`, servidor devolve `nome`. Front procura `título`, não acha. Tela em branco.

### Falar

"E aqui que a IA se confunde. A IA as vezes inventa contrato."

"Você pede para ela fazer o front consumir uma API. Ela escreve o código esperando que o servidor devolva `{ título, descrição }`. Mas o servidor nunca disse que devolve isso. A IA chutou. E quando o código roda, a tela fica vazia."

"Por isso a primeira pergunta ao trabalhar com API e 'qual e o contrato'. O que o servidor realmente devolve?"

"Quando a IA sugerir consumir uma API, pergunte: 'você viu o contrato real, ou você esta chutando os campos?'."

### Cena 3 - Status codes: respostas honestas (11:30-13:30)

### Falar

"Alem do JSON, o servidor devolve um código de status. Esse código diz, de forma honesta, o que aconteceu com o pedido."

"Cinco codigos cobrem 95% dos casos."

### Traduzir

- **200 (OK)** - deu certo, aqui esta a resposta
- **404 (Not Found)** - não achei o que você pediu
- **401 (Unauthorized)** - você não esta logado, não sei quem você e
- **403 (Forbidden)** - sei quem você e, mas você não pode acessar isso
- **500 (Internal Server Error)** - quebrou la dentro, não foi culpa sua

### Falar

"O status code e a forma honesta do servidor falar o que aconteceu. 200 e sucesso. 404 e 'não achei'. 401 e 'não te conheco'. 403 e 'te conheco, mas não pode'. 500 e 'deu ruim no meu lado'."

"Um dos problemas mais comuns da web e o crash silencioso. O servidor quebra, mas em vez de devolver um 500 honesto, devolve algo vazio ou uma resposta generica. O front não sabe o que aconteceu. A tela fica parada, sem mensagem."

### Mostrar

Comparacao na tela:
- Cenário honesto: request vai, servidor quebra, devolve 500, front mostra mensagem de erro
- Cenário silencioso: request vai, servidor quebra, devolve resposta vazia, front fica parado, sem feedback

### Falar

"Quando a IA falar em 'tratar erro', pergunte: 'tratar que tipo de erro? 404? 401? 500?'. Cada um e uma coisa. Se ela só fala 'tratar erro' sem especificar, ela não esta pensando no contrato."

### Fechamento do ATO 2

Mostrar o diagrama completo do dialogo: request (com metodo, endpoint) indo, servidor processando, response voltando (com JSON, contrato, status code).

"O navegador pede. O servidor responde com dados (JSON), dentro de um contrato, e com um status honesto. Essa e a conversa inteira."

---

## ATO 3 - A fronteira (13:30-17:30)

### Cena 1 - Front não sabe do banco (13:30-15:00)

### Falar

"Se o servidor e que consulta o banco, o front não deveria saber que o banco existe."

"O front só conversa com a API. Ele manda request, recebe response. O que acontece atras da API, dentro do servidor, e caixa preta para o front."

"Pense no balcao de novo. Você bate no balcao e pede um produto. O atendente vai no almoxarifado, pega, traz. Você não precisa saber onde fica o almoxarifado, como ele esta organizado, ou se o produto estava na prateleira 3 ou 7."

"O front e o cliente do balcao. O banco e o almoxarifado. A API e o balcao."

### Mostrar

Diagrama com tres blocos:
- Front (navegador), seta "request / response" para API (balcao), seta "consulta" de API para Banco (almoxarifado)
- A seta do front Não cruza direto para o banco. Ela para na API.

### Falar

"Se o front comeca a saber detalhes do banco (nomes de tabela, tipo de coluna, como os dados estão guardados), algo esta errado. A separacao quebrou."

### Cena 2 - Por que essa separacao importa (15:00-16:00)

### Falar

"Essa separacao tem um nome: camadas. Cada camada tem um trabalho. O front mostra. A API atende e processa. O banco guarda."

"Por que separar? Porque quando as camadas estão separadas, você pode trocar uma sem quebrar a outra. Troca um banco por outro: o front nem percebe. Troca o framework do front por outro: o servidor não se importa."

"Se as camadas estão misturadas, qualquer mudança quebra tudo. E ai que o caos comeca."

### Falar

"Para quem programa com IA: quando a IA sugerir uma mudança, pergunte: 'isso mora no front, na API, ou no banco?'. Se ela misturar, você já sabe que tem risco."

### Cena 3 - Onde a IA se confunde com API (16:00-17:30)

### Falar

"A IA tem tres armadilhas classicas quando trabalha com API."

"Armadilha 1: inventar contrato. Ela escreve o front esperando campos que o servidor nunca confirmou. Solucao: pergunte 'você viu o contrato ou chutou?'."

"Armadilha 2: ignorar status code. Ela trata todo erro como se fosse igual. Um 404 (não achei) e diferente de um 500 (quebrou). Solucao: pergunte 'qual status code eu devo tratar?'."

"Armadilha 3: misturar camadas. Ela poe lógica de banco no front, ou lógica de front no servidor. Solucao: pergunte 'isso mora em qual camada?'."

"Essas tres perguntas são o seu crivo. Toda vez que a IA mexer com API, faca elas."

### Fechamento do ATO 3

Mostrar o diagrama completo com as tres camadas destacadas: front, API, banco.

"O front pede. A API atende. O banco guarda. Cada um no seu lugar."

---

## ENCERRAMENTO (17:30-19:00)

### Na camera

"Praticamente tudo que acontece na web e uma conversa de duas partes. Request e response. O navegador pede com um metodo (GET ou POST), bate num endpoint, e recebe de volta um JSON dentro de um contrato, com um status code honesto."

"O front não sabe do banco. Só conversa com a API. Essa fronteira e o que mantem o sistema são."

"Quando a IA trabalhar com API, faca tres perguntas: qual e o contrato real? Qual status code eu trato? Isso mora em qual camada?"

"Na descrição tem o glossario com todos os termos que apareceram."

### Ponte para o próximo episodio

"Mas fica uma pergunta no ar. O servidor devolve dados. De onde ele tira esses dados? A resposta e o próximo vídeo: banco de dados. A memória de longo prazo do servidor."

### Call to action

- Inscreva-se para a série
- Comente qual conceito você quer aprofundar
- Repo com o glossario: [link]
