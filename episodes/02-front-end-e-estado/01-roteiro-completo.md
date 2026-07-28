# Roteiro completo - Front-end e Estado

**Duracao alvo:** 15-20 min
**Formato:** Gui falando para camera, alternando com diagrama simples na tela e uma pagina rodando
**Regra pedagogica:** cada termo tecnico e traduzido em 1 frase antes de continuar. Nenhum termo fica sem traducao.

---

## ABERTURA (0:00-0:45)

### Na camera

"No video anterior eu contei a historia de um deploy, do zero ao ar. Mostrei varias camadas: front, servidor, banco, deploy. Mas passei rapido por cada uma."

"Hoje a gente entra dentro da primeira. A camada do navegador. A camada que voce toca primeiro quando abre o site. A camada onde a IA mais escreve codigo, e onde mais coisas quebram sem ninguem perceber."

"Quando voce pede para a IA fazer um botao, uma lista, um formulario, tudo isso mora no navegador. E dentro do navegador existe um mecanismo. Se voce nao enxerga ele, voce aceita o resultado sem saber onde mora o risco."

### Mostrar

Diagrama do mapa do episodio 01, com a camada "navegador" destacada (piscando ou com cor diferente). Dizer: "hoje a gente entra aqui dentro".

---

## ATO 1 - O navegador monta a pagina (0:45-6:00)

### Cena 1 - O que acontece quando voce abre um site (0:45-2:15)

### Falar

"Voce digita um endereco. Aperta enter. O que acontece?"

"O navegador manda um pedido para o servidor. O servidor responde com arquivos. Arquivos de texto. Nada de magica."

"Esses arquivos sao principalmente tres. Voce ja viu eles no video anterior, mas hoje a gente olha com atencao."

### Mostrar

Uma aba do navegador abrindo um site, com o DevTools (ferramenta de desenvolvedor) aberto na aba Network, mostrando os arquivos chegando.

### Traduzir

- HTML: o que aparece na tela (texto, botao, imagem)
- CSS: como aparece (cor, tamanho, posicao)
- JavaScript: o que acontece (clicou, mudou, calculou)

### Falar

"So que o navegador nao mostra esses arquivos crus. Ele le eles e monta uma estrutura interna. Essa estrutura se chama DOM."

### Cena 2 - O DOM (2:15-4:00)

### Falar

"DOM. Tres letras que assustam, mas e simples."

"DOM quer dizer Document Object Model. Nome tecnico para uma coisa direta: a arvore de elementos que o navegador cria a partir do HTML."

### Mostrar

Uma pagina simples. No DevTools, aba Elements, mostrando a arvore de tags (`<html>`, `<body>`, `<div>`, `<button>`).

### Falar

"Pense no DOM como uma arvore genealogica. O html e o tronco. Dentro dele tem o body. Dentro do body tem divs, botoes, textos. Cada elemento que voce ve na tela e um no nessa arvore."

"Por que isso importa? Porque quando o JavaScript quer mudar a tela, ele nao escreve na tela diretamente. Ele mexe no DOM. Muda um no, e o navegador pinta o resultado."

"Termo que vai aparecer muito: renderizar. Renderizar e o ato do navegador pintar os pixels na tela a partir do DOM. Render e o desenho que voce ve."

### Cena 3 - Estrutura, aparencia, comportamento (4:00-5:15)

### Falar

"Essa divisao de tres e util de decorar."

### Mostrar

Tela dividida em tres colunas, ou tres blocos: HTML / CSS / JS, cada um com uma frase.

### Falar

"HTML: estrutura. O que existe na pagina. Um botao, um texto, uma imagem."

"CSS: aparencia. Como aquilo aparece. Cor, tamanho, posicao, fonte."

"JavaScript: comportamento. O que acontece quando voce interage. Clicou, digitou, passou o mouse."

"Quando a IA fala em 'mudar o estilo', ela mexe no CSS. Quando fala em 'adicionar um botao', mexe no HTML. Quando fala em 'quando clicar faz isso', mexe no JavaScript. Sao camadas diferentes dentro do navegador."

### Cena 4 - A pagina nao e estatica (5:15-6:00)

### Falar

"E aqui que a coisa fica interessante. O DOM nao e uma foto. Ele muda."

"Voce clica num botao e ele muda de cor. Digita num campo e o texto aparece em outro lugar. Marca uma opcao e outra parte da tela reage."

"Tudo isso acontece sem recarregar a pagina. O navegador esta mudando o DOM por baixo, e repintando a tela."

"Essa e a ponte para o segundo ato. A pagina muda porque ela tem memoria. Essa memoria tem nome: estado."

### Fechamento do ATO 1

Mostrar o mapa do ciclo (arquivo 02) apenas com a primeira parte: arquivos chegam, DOM montado, render. Dizer: "isso e o que acontece quando a pagina abre. Agora vamos ver por que ela vive."

---

## ATO 2 - A pagina vive: estado e o ciclo de re-render (6:00-12:00)

### Cena 1 - O que e estado (6:00-7:30)

### Falar

"Estado. A palavra mais importante do front-end moderno."

"Estado e a memoria da pagina enquanto ela esta aberta. Tudo que a pagina precisa lembrar para funcionar."

### Mostrar

Uma pagina simples com um contador. Botao "+1" e o numero na tela.

### Falar

"Exemplo classico: um contador. Comeca em zero. Voce clica, vira um. Clica de novo, vira dois."

"Esse numero que muda e um estado. A pagina lembra dele enquanto esta aberta. Se voce recarrega, some."

"Estado e a diferenca entre uma pagina morta, que so mostra texto, e uma pagina viva, que reage ao que voce faz."

### Cena 2 - Onde o estado mora (7:30-9:30)

### Falar

"Mas onde exatamente esse valor fica guardado? Depende da categoria."

### Mostrar

O diagrama "Onde o estado mora" do arquivo 02, com quatro blocos: variavel local, hook, store, servidor.

### Falar

"Primeira categoria: variavel local. Uma variavel e uma caixinha com um nome. Voce coloca um valor dentro, e pode ler ou trocar. O contador que acabamos de ver e uma variavel local. Ela mora na pagina, e some quando a pagina fecha."

"Segunda categoria: hook. Em frameworks modernos como React, o estado de um pedaco da tela e organizado numa estrutura chamada hook. Hook e so um nome chique para uma forma organizada de guardar o estado de um componente. Componente, por sua vez, e um pedaco reutilizavel da tela, tipo um botao ou uma lista."

"Terceira categoria: store, ou estado global. Quando varias partes da tela precisam ler o mesmo valor, tipo quem e o usuario logado ou o que tem no carrinho, voce nao espalha isso em variaveis soltas. Voce coloca num lugar central, chamado store. Store e a prateleira compartilhada da pagina."

"Quarta categoria: servidor. Tem estado que nao pode sumir quando a pagina fecha. Tipo o seu perfil, seu historico, suas preferencias. Esse estado nao mora no navegador. Mora no servidor. E isso e assunto do proximo episodio."

### Cena 3 - O ciclo: evento, estado, re-render (9:30-11:00)

### Falar

"Agora o coracao do video. O ciclo."

### Mostrar

O diagrama do ciclo principal do arquivo 02, com as tres etapas: evento, estado, re-render.

### Falar

"Toda vez que voce interage com a pagina, o mesmo ciclo acontece."

"Primeiro: evento. Voce clica, digita, arrasta. O navegador percebe e dispara um evento. Evento e o aviso de que algo aconteceu."

"Segundo: estado muda. O codigo que trata o evento atualiza o valor na variavel, no hook ou no store."

"Terceiro: re-render. O navegador percebe que o estado mudou e repinta a parte da tela que depende daquele valor."

### Mostrar

O contador de novo. Clicar no botao e destacar as tres etapas visualmente: (1) evento dispara, (2) contador passa de 0 para 1, (3) tela mostra 1.

### Falar

"Esse ciclo se repete toda vez. Evento, estado, re-render. Evento, estado, re-render."

"Isso e o que chamam de reatividade. Uma pagina reativa e aquela em que a tela se atualiza sozinha quando o estado muda, sem voce ter que mandar repintar nada manualmente."

### Cena 4 - Por que isso importa para quem usa IA (11:00-12:00)

### Falar

"Por que voce precisa saber disso?"

"Porque quando a IA escreve front-end, ela esta o tempo todo mexendo nesse ciclo. Ela cria variavel, ela mexe em hook, ela monta componente. E quando algo para de funcionar, o problema quase sempre esta em um desses tres pontos."

"Pergunta util para fazer para a IA quando algo quebra: 'o evento esta disparando? O estado esta mudando? A tela esta re-renderizando?'. Essa pergunta em tres partes isola o problema."

### Fechamento do ATO 2

Mostrar o ciclo completo novamente. Dizer: "isso cobre o caminho feliz. Mas a pagina real nao e so caminho feliz. E no proximo ato que a coisa costuma quebrar."

---

## ATO 3 - Os estados que a IA esquece (12:00-17:00)

### Cena 1 - O caminho feliz e o caminho real (12:00-13:00)

### Falar

"Quando voce pede para a IA fazer uma tela que mostra uma lista de produtos, ela faz o seguinte: busca os produtos, mostra na tela. Pronto."

"Isso e o caminho feliz. O dado chegou, a lista esta cheia, tudo funciona."

"So que a vida real nao e assim. Tela que mostra dados tem varios momentos. E a IA costuma tratar so um deles."

### Mostrar

O diagrama dos 5 estados do arquivo 02: loading, empty, error, partial, stale.

### Falar

"Toda tela que mostra dados tem, no minimo, cinco momentos. Vamos passar por cada um."

### Cena 2 - Loading e empty (13:00-14:00)

### Falar

"Loading. A pagina pediu os dados para o servidor, mas ainda nao chegou. Enquanto espera, o que o usuario ve?"

### Mostrar

Uma tela com um spinner (aquele circulo girando) ou a palavra "Carregando...".

### Falar

"Se a IA nao tratar o loading, o usuario ve uma tela vazia. Parece quebrado. Parece que o site nao funciona. Na verdade so esta esperando."

"Segundo momento: empty. O dado chegou, mas a lista esta vazia. Nao tem nenhum produto. O que o usuario ve?"

### Mostrar

Uma tela com a mensagem "Nenhum produto encontrado" e talvez uma ilustracao simples.

### Falar

"Se a IA nao tratar o empty, o usuario ve a mesma tela vazia do loading. Mas o motivo e outro: o dado chegou, so nao tem nada. Sao duas situacoes completamente diferentes, e a IA costuma confundir as duas."

### Cena 3 - Error e partial (14:00-15:15)

### Falar

"Terceiro momento: error. A chamada deu erro. O servidor esta fora, a internet caiu, o usuario nao tem permissao. O dado nao vai chegar."

### Mostrar

Uma tela com a mensagem "Algo deu errado" e um botao "Tentar novamente".

### Falar

"Se a IA nao tratar o error, a pagina fica presa no loading para sempre. Spinner girando eternamente. O usuario nao sabe se esta carregando ou se ja deu erro."

"Quarto momento: partial. O dado chegou pela metade. A lista veio com 3 itens de 10. Ou veio sem um campo importante."

"Isso e mais raro, mas acontece. E a IA quase nunca trata. Ela assume que ou veio tudo, ou veio nada."

### Cena 4 - Stale (15:15-16:00)

### Falar

"Quinto e mais sutil: stale. Stale quer dizer velho, desatualizado."

### Mostrar

Uma tela mostrando uma lista. Ao lado, um relogio. A lista foi carregada ha 10 minutos. O dado la no servidor ja mudou, mas a tela ainda mostra o antigo.

### Falar

"A pagina carregou os dados, mostrou, e o usuario ficou mexendo. Enquanto isso, o dado la no servidor mudou. Outro usuario adicionou um produto, o preco alterou. A tela mostra informacao velha."

"Isso e stale. A IA trata o momento de carregar, mas raramente trata o momento de atualizar. O resultado: o usuario ve coisa que ja nao e verdade."

### Cena 5 - A checklist para usar com IA (16:00-16:45)

### Falar

"Esses cinco momentos sao uma checklist. Toda vez que a IA gerar uma tela que mostra dados, pergunte:"

### Mostrar

A checklist dos 5 estados, uma linha por item:

- Tratei o loading?
- Tratei o empty?
- Tratei o error?
- Tratei o partial?
- Tratei o stale?

### Falar

"Ela provavelmente tratou so o caminho feliz. Os outros ela esquece. Quem programa com IA sem saber disso entrega telas que funcionam quando tudo da certo e quebram quando algo da errado."

### Cena 6 - Quando o estado precisa ir para o servidor (16:45-17:00)

### Falar

"E tem um limite. Algum estado nao pode morar no navegador."

"O contador que some quando fecha, tudo bem. Mas o seu perfil, suas preferencias, seu historico, seus dados salvo. Isso nao pode sumir."

"Esse estado precisa viajar do navegador para o servidor, onde sobrevive entre sessoes. E isso e o assunto do proximo episodio."

### Fechamento do ATO 3

Mostrar o mapa completo do ciclo, agora com os 5 estados em volta dele. Dizer: "o ciclo e simples. Os cinco estados sao o que a IA esquece. Se voce cobrir os dois, seu front-end sobrevive ao mundo real."

---

## ENCERRAMENTO (17:00-18:30)

### Na camera

"O front-end nao e so desenho de tela. E um mecanismo. O navegador monta uma arvore, o DOM, a partir dos arquivos. Essa arvore muda porque existe estado. E o estado muda porque o usuario interage."

"O ciclo se repete: evento, estado, re-render. Evento, estado, re-render. Quando voce entende isso, voce para de tratar a tela como uma coisa so e comeca a enxergar as tres partes."

"E quando a IA gerar uma tela que mostra dados, cobre os cinco estados. Loading, empty, error, partial, stale. Ela vai ter tratado so o caminho feliz."

### Call to action

"Na descricao tem o glossario com todos os termos que apareceram. Repo publico [link] para consultar depois."

"O proximo video da serie vai pro servidor. Porque o estado que precisa sobreviver entre sessoes nao mora no navegador. Mora la."

- Inscreva-se para a serie
- Comente qual dos cinco estados voce mais esquece
- Repo com o glossario: [link]
