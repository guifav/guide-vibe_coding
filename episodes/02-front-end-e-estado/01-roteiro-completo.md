# Roteiro completo - Front-end e Estado

**Duracao alvo:** 15-20 min
**Formato:** Gui falando para camera, alternando com diagrama simples na tela e uma página rodando
**Regra pedagogica:** cada termo técnico e traduzido em 1 frase antes de continuar. Nenhum termo fica sem tradução.

---

## ABERTURA (0:00-0:45)

### Na camera

"No vídeo anterior eu contei a história de um deploy, do zero ao ar. Mostrei varias camadas: front, servidor, banco, deploy. Mas passei rápido por cada uma."

"Hoje a gente entra dentro da primeira. A camada do navegador. A camada que você toca primeiro quando abre o site. A camada onde a IA mais escreve código, e onde mais coisas quebram sem ninguém perceber."

"Quando você pede para a IA fazer um botao, uma lista, um formulario, tudo isso mora no navegador. E dentro do navegador existe um mecanismo. Se você não enxerga ele, você aceita o resultado sem saber onde mora o risco."

### Mostrar

Diagrama do mapa do episodio 01, com a camada "navegador" destacada (piscando ou com cor diferente). Dizer: "hoje a gente entra aqui dentro".

---

## ATO 1 - O navegador monta a página (0:45-6:00)

### Cena 1 - O que acontece quando você abre um site (0:45-2:15)

### Falar

"Você digita um endereço. Aperta enter. O que acontece?"

"O navegador manda um pedido para o servidor. O servidor responde com arquivos. Arquivos de texto. Nada de mágica."

"Esses arquivos são principalmente tres. Você já viu eles no vídeo anterior, mas hoje a gente olha com atencao."

### Mostrar

Uma aba do navegador abrindo um site, com o DevTools (ferramenta de desenvolvedor) aberto na aba Network, mostrando os arquivos chegando.

### Traduzir

- HTML: o que aparece na tela (texto, botao, imagem)
- CSS: como aparece (cor, tamanho, posição)
- JavaScript: o que acontece (clicou, mudou, calculou)

### Falar

"Só que o navegador não mostra esses arquivos crus. Ele le eles e monta uma estrutura interna. Essa estrutura se chama DOM."

### Cena 2 - O DOM (2:15-4:00)

### Falar

"DOM. Tres letras que assustam, mas e simples."

"DOM quer dizer Document Object Model. Nome técnico para uma coisa direta: a árvore de elementos que o navegador cria a partir do HTML."

### Mostrar

Uma página simples. No DevTools, aba Elements, mostrando a árvore de tags (`<html>`, `<body>`, `<div>`, `<button>`).

### Falar

"Pense no DOM como uma árvore genealogica. O html e o tronco. Dentro dele tem o body. Dentro do body tem divs, botoes, textos. Cada elemento que você ve na tela e um no nessa árvore."

"Por que isso importa? Porque quando o JavaScript quer mudar a tela, ele não escreve na tela diretamente. Ele mexe no DOM. Muda um no, e o navegador pinta o resultado."

"Termo que vai aparecer muito: renderizar. Renderizar e o ato do navegador pintar os pixels na tela a partir do DOM. Render e o desenho que você ve."

### Cena 3 - Estrutura, aparencia, comportamento (4:00-5:15)

### Falar

"Essa divisao de tres e util de decorar."

### Mostrar

Tela dividida em tres colunas, ou tres blocos: HTML / CSS / JS, cada um com uma frase.

### Falar

"HTML: estrutura. O que existe na página. Um botao, um texto, uma imagem."

"CSS: aparencia. Como aquilo aparece. Cor, tamanho, posição, fonte."

"JavaScript: comportamento. O que acontece quando você interage. Clicou, digitou, passou o mouse."

"Quando a IA fala em 'mudar o estilo', ela mexe no CSS. Quando fala em 'adicionar um botao', mexe no HTML. Quando fala em 'quando clicar faz isso', mexe no JavaScript. São camadas diferentes dentro do navegador."

### Cena 4 - A página não e estática (5:15-6:00)

### Falar

"E aqui que a coisa fica interessante. O DOM não e uma foto. Ele muda."

"Você clica num botao e ele muda de cor. Digita num campo e o texto aparece em outro lugar. Marca uma opcao e outra parte da tela reage."

"Tudo isso acontece sem recarregar a página. O navegador esta mudando o DOM por baixo, e repintando a tela."

"Essa e a ponte para o segundo ato. A página muda porque ela tem memória. Essa memória tem nome: estado."

### Fechamento do ATO 1

Mostrar o mapa do ciclo (arquivo 02) apenas com a primeira parte: arquivos chegam, DOM montado, render. Dizer: "isso e o que acontece quando a página abre. Agora vamos ver por que ela vive."

---

## ATO 2 - A página vive: estado e o ciclo de re-render (6:00-12:00)

### Cena 1 - O que e estado (6:00-7:30)

### Falar

"Estado. A palavra mais importante do front-end moderno."

"Estado e a memória da página enquanto ela esta aberta. Tudo que a página precisa lembrar para funcionar."

### Mostrar

Uma página simples com um contador. Botao "+1" e o número na tela.

### Falar

"Exemplo classico: um contador. Comeca em zero. Você clica, vira um. Clica de novo, vira dois."

"Esse número que muda e um estado. A página lembra dele enquanto esta aberta. Se você recarrega, some."

"Estado e a diferença entre uma página morta, que só mostra texto, e uma página viva, que reage ao que você faz."

### Cena 2 - Onde o estado mora (7:30-9:30)

### Falar

"Mas onde exatamente esse valor fica guardado? Depende da categoria."

### Mostrar

O diagrama "Onde o estado mora" do arquivo 02, com quatro blocos: variável local, hook, store, servidor.

### Falar

"Primeira categoria: variável local. Uma variável e uma caixinha com um nome. Você coloca um valor dentro, e pode ler ou trocar. O contador que acabamos de ver e uma variável local. Ela mora na página, e some quando a página fecha."

"Segunda categoria: hook. Em frameworks modernos como React, o estado de um pedaco da tela e organizado numa estrutura chamada hook. Hook e só um nome chique para uma forma organizada de guardar o estado de um componente. Componente, por sua vez, e um pedaco reutilizavel da tela, tipo um botao ou uma lista."

"Terceira categoria: store, ou estado global. Quando varias partes da tela precisam ler o mesmo valor, tipo quem e o usuario logado ou o que tem no carrinho, você não espalha isso em variáveis soltas. Você coloca num lugar central, chamado store. Store e a prateleira compartilhada da página."

"Quarta categoria: servidor. Tem estado que não pode sumir quando a página fecha. Tipo o seu perfil, seu histórico, suas preferencias. Esse estado não mora no navegador. Mora no servidor. E isso e assunto do próximo episodio."

### Cena 3 - O ciclo: evento, estado, re-render (9:30-11:00)

### Falar

"Agora o coração do vídeo. O ciclo."

### Mostrar

O diagrama do ciclo principal do arquivo 02, com as tres etapas: evento, estado, re-render.

### Falar

"Toda vez que você interage com a página, o mesmo ciclo acontece."

"Primeiro: evento. Você clica, digita, arrasta. O navegador percebe e dispara um evento. Evento e o aviso de que algo aconteceu."

"Segundo: estado muda. O código que trata o evento atualiza o valor na variável, no hook ou no store."

"Terceiro: re-render. O navegador percebe que o estado mudou e repinta a parte da tela que depende daquele valor."

### Mostrar

O contador de novo. Clicar no botao e destacar as tres etapas visualmente: (1) evento dispara, (2) contador passa de 0 para 1, (3) tela mostra 1.

### Falar

"Esse ciclo se repete toda vez. Evento, estado, re-render. Evento, estado, re-render."

"Isso e o que chamam de reatividade. Uma página reativa e aquela em que a tela se atualiza sozinha quando o estado muda, sem você ter que mandar repintar nada manualmente."

### Cena 4 - Por que isso importa para quem usa IA (11:00-12:00)

### Falar

"Por que você precisa saber disso?"

"Porque quando a IA escreve front-end, ela esta o tempo todo mexendo nesse ciclo. Ela cria variável, ela mexe em hook, ela monta componente. E quando algo para de funcionar, o problema quase sempre esta em um desses tres pontos."

"Pergunta util para fazer para a IA quando algo quebra: 'o evento esta disparando? O estado esta mudando? A tela esta re-renderizando?'. Essa pergunta em tres partes isola o problema."

### Fechamento do ATO 2

Mostrar o ciclo completo novamente. Dizer: "isso cobre o caminho feliz. Mas a página real não e só caminho feliz. E no próximo ato que a coisa costuma quebrar."

---

## ATO 3 - Os estados que a IA esquece (12:00-17:00)

### Cena 1 - O caminho feliz e o caminho real (12:00-13:00)

### Falar

"Quando você pede para a IA fazer uma tela que mostra uma lista de produtos, ela faz o seguinte: busca os produtos, mostra na tela. Pronto."

"Isso e o caminho feliz. O dado chegou, a lista esta cheia, tudo funciona."

"Só que a vida real não e assim. Tela que mostra dados tem varios momentos. E a IA costuma tratar só um deles."

### Mostrar

O diagrama dos 5 estados do arquivo 02: loading, empty, error, partial, stale.

### Falar

"Toda tela que mostra dados tem, no minimo, cinco momentos. Vamos passar por cada um."

### Cena 2 - Loading e empty (13:00-14:00)

### Falar

"Loading. A página pediu os dados para o servidor, mas ainda não chegou. Enquanto espera, o que o usuario ve?"

### Mostrar

Uma tela com um spinner (aquele circulo girando) ou a palavra "Carregando...".

### Falar

"Se a IA não tratar o loading, o usuario ve uma tela vazia. Parece quebrado. Parece que o site não funciona. Na verdade só esta esperando."

"Segundo momento: empty. O dado chegou, mas a lista esta vazia. Não tem nenhum produto. O que o usuario ve?"

### Mostrar

Uma tela com a mensagem "Nenhum produto encontrado" e talvez uma ilustração simples.

### Falar

"Se a IA não tratar o empty, o usuario ve a mesma tela vazia do loading. Mas o motivo e outro: o dado chegou, só não tem nada. São duas situacoes completamente diferentes, e a IA costuma confundir as duas."

### Cena 3 - Error e partial (14:00-15:15)

### Falar

"Terceiro momento: error. A chamada deu erro. O servidor esta fora, a internet caiu, o usuario não tem permissao. O dado não vai chegar."

### Mostrar

Uma tela com a mensagem "Algo deu errado" e um botao "Tentar novamente".

### Falar

"Se a IA não tratar o error, a página fica presa no loading para sempre. Spinner girando eternamente. O usuario não sabe se esta carregando ou se já deu erro."

"Quarto momento: partial. O dado chegou pela metade. A lista veio com 3 itens de 10. Ou veio sem um campo importante."

"Isso e mais raro, mas acontece. E a IA quase nunca trata. Ela assume que ou veio tudo, ou veio nada."

### Cena 4 - Stale (15:15-16:00)

### Falar

"Quinto e mais sutil: stale. Stale quer dizer velho, desatualizado."

### Mostrar

Uma tela mostrando uma lista. Ao lado, um relogio. A lista foi carregada ha 10 minutos. O dado la no servidor já mudou, mas a tela ainda mostra o antigo.

### Falar

"A página carregou os dados, mostrou, e o usuario ficou mexendo. Enquanto isso, o dado la no servidor mudou. Outro usuario adicionou um produto, o preco alterou. A tela mostra informação velha."

"Isso e stale. A IA trata o momento de carregar, mas raramente trata o momento de atualizar. O resultado: o usuario ve coisa que já não e verdade."

### Cena 5 - A checklist para usar com IA (16:00-16:45)

### Falar

"Esses cinco momentos são uma checklist. Toda vez que a IA gerar uma tela que mostra dados, pergunte:"

### Mostrar

A checklist dos 5 estados, uma linha por item:

- Tratei o loading?
- Tratei o empty?
- Tratei o error?
- Tratei o partial?
- Tratei o stale?

### Falar

"Ela provavelmente tratou só o caminho feliz. Os outros ela esquece. Quem programa com IA sem saber disso entrega telas que funcionam quando tudo da certo e quebram quando algo da errado."

### Cena 6 - Quando o estado precisa ir para o servidor (16:45-17:00)

### Falar

"E tem um limite. Algum estado não pode morar no navegador."

"O contador que some quando fecha, tudo bem. Mas o seu perfil, suas preferencias, seu histórico, seus dados salvo. Isso não pode sumir."

"Esse estado precisa viajar do navegador para o servidor, onde sobrevive entre sessoes. E isso e o assunto do próximo episodio."

### Fechamento do ATO 3

Mostrar o mapa completo do ciclo, agora com os 5 estados em volta dele. Dizer: "o ciclo e simples. Os cinco estados são o que a IA esquece. Se você cobrir os dois, seu front-end sobrevive ao mundo real."

---

## ENCERRAMENTO (17:00-18:30)

### Na camera

"O front-end não e só desenho de tela. E um mecanismo. O navegador monta uma árvore, o DOM, a partir dos arquivos. Essa árvore muda porque existe estado. E o estado muda porque o usuario interage."

"O ciclo se repete: evento, estado, re-render. Evento, estado, re-render. Quando você entende isso, você para de tratar a tela como uma coisa só e comeca a enxergar as tres partes."

"E quando a IA gerar uma tela que mostra dados, cobre os cinco estados. Loading, empty, error, partial, stale. Ela vai ter tratado só o caminho feliz."

### Call to action

"Na descrição tem o glossario com todos os termos que apareceram. Repo público [link] para consultar depois."

"O próximo vídeo da série vai pro servidor. Porque o estado que precisa sobreviver entre sessoes não mora no navegador. Mora la."

- Inscreva-se para a série
- Comente qual dos cinco estados você mais esquece
- Repo com o glossario: [link]
