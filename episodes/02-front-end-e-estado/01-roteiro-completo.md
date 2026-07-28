# Roteiro completo - Front-end e Estado

**Duração alvo:** 15-20 min
**Formato:** Gui falando para câmera, alternando com diagrama simples na tela e uma página rodando
**Regra pedagógica:** cada termo técnico é traduzido em 1 frase antes de continuar. Nenhum termo fica sem tradução.

---

## ABERTURA (0:00-0:45)

### Na câmera

"No vídeo anterior eu contei a história de um deploy: o site no ar. Mostrei várias camadas: front, servidor, banco, deploy. Mas passei rápido por cada uma."

"Hoje a gente entra dentro da primeira. A camada do navegador. A camada que você toca primeiro quando abre o site. A camada onde a IA mais escreve código, e onde mais coisas quebram sem ninguém perceber."

"Quando você pede para a IA fazer um botão, uma lista, um formulário, tudo isso mora no navegador. E dentro do navegador existe um mecanismo. Se você não enxerga ele, você aceita o resultado sem saber onde mora o risco."

### Mostrar

Diagrama do mapa do episódio 01, com a camada "navegador" destacada (piscando ou com cor diferente). Dizer: "hoje a gente entra aqui dentro".

---

## ATO 1 - O navegador monta a página (0:45-6:00)

### Cena 1 - O que acontece quando você abre um site (0:45-2:15)

### Falar

"Você digita um endereço. Aperta enter. O que acontece?"

"O navegador manda um pedido para o servidor. O servidor responde com arquivos. Arquivos de texto. Direto assim."

"Esses arquivos são principalmente três. Você já viu eles no vídeo anterior, mas hoje a gente olha com atenção."

### Mostrar

Uma aba do navegador abrindo um site, com o DevTools (ferramenta de desenvolvedor) aberto na aba Network, mostrando os arquivos chegando.

### Traduzir

- HTML: o que aparece na tela (texto, botão, imagem)
- CSS: como aparece (cor, tamanho, posição)
- JavaScript: o que acontece (clicou, mudou, calculou)

### Falar

"Só que o navegador não mostra esses arquivos crus. Ele lê eles e monta uma estrutura interna. Essa estrutura se chama DOM."

### Cena 2 - O DOM (2:15-4:00)

### Falar

"DOM. Três letras que assustam, mas é simples."

"DOM quer dizer Document Object Model. Nome técnico para uma coisa direta: a árvore de elementos que o navegador cria a partir do HTML."

### Mostrar

Uma página simples. No DevTools, aba Elements, mostrando a árvore de tags (`<html>`, `<body>`, `<div>`, `<button>`).

### Falar

"Pense no DOM como uma árvore genealógica. O html é o tronco. Dentro dele tem o body. Dentro do body tem divs, botões, textos. Cada elemento que você vê na tela é um nó nessa árvore."

"Por que isso importa? Porque quando o JavaScript quer mudar a tela, ele não escreve na tela diretamente. Ele mexe no DOM. Muda um nó, e o navegador pinta o resultado."

"Termo que vai aparecer muito: renderizar. Renderizar é o ato do navegador pintar os pixels na tela a partir do DOM. Render é o desenho que você vê."

### Cena 3 - Estrutura, aparência, comportamento (4:00-5:15)

### Falar

"Essa divisão de três é útil de decorar."

### Mostrar

Tela dividida em três colunas, ou três blocos: HTML / CSS / JS, cada um com uma frase.

### Falar

"HTML: estrutura. O que existe na página. Um botão, um texto, uma imagem."

"CSS: aparência. Como aquilo aparece. Cor, tamanho, posição, fonte."

"JavaScript: comportamento. O que acontece quando você interage. Clicou, digitou, passou o mouse."

"Quando a IA fala em 'mudar o estilo', ela mexe no CSS. Quando fala em 'adicionar um botão', mexe no HTML. Quando fala em 'quando clicar faz isso', mexe no JavaScript. São camadas diferentes dentro do navegador."

### Cena 4 - A página é dinâmica (5:15-6:00)

### Falar

"É aqui que a coisa fica interessante. O DOM é vivo. Ele muda."

"Você clica num botão e ele muda de cor. Digita num campo e o texto aparece em outro lugar. Marca uma opção e outra parte da tela reage."

"Tudo isso acontece sem recarregar a página. O código JavaScript está mudando o DOM por baixo, e o navegador repinta a tela."

"Essa é a ponte para o segundo ato. A página muda porque ela tem memória. Essa memória tem nome: estado."

### Fechamento do ATO 1

Mostrar o mapa do ciclo (arquivo 02) apenas com a primeira parte: arquivos chegam, DOM montado, render. Dizer: "isso é o que acontece quando a página abre. Agora vamos ver por que ela vive."

---

## ATO 2 - A página vive: estado e o ciclo de re-render (6:00-12:00)

### Cena 1 - O que é estado (6:00-7:30)

### Falar

"Estado. A palavra mais importante do front-end moderno."

"Estado é a memória da página enquanto ela está aberta. Tudo que a página precisa lembrar para funcionar."

### Mostrar

Uma página simples com um contador. Botão "+1" e o número na tela.

### Falar

"Exemplo clássico: um contador. Começa em zero. Você clica, vira um. Clica de novo, vira dois."

"Esse número que muda é um estado. A página lembra dele enquanto está aberta. Se você recarrega, some."

"Estado é a diferença entre uma página morta, que só mostra texto, e uma página viva, que reage ao que você faz."

### Cena 2 - Onde o estado mora (7:30-9:30)

### Falar

"Mas onde exatamente esse valor fica guardado? Depende da categoria."

### Mostrar

O diagrama "Onde o estado mora" do arquivo 02, com quatro blocos: variável local, hook, store, servidor.

### Falar

"Primeira categoria: variável local. Uma variável é uma caixinha com um nome. Você coloca um valor dentro, e pode ler ou trocar. O contador que acabamos de ver é uma variável local. Ela mora na página, e some quando a página fecha."

"Segunda categoria: estado de componente. Componente é um pedaço reutilizável da tela, tipo um botão ou uma lista. Em alguns frameworks, a forma organizada de guardar o estado de um componente se chama hook; outros frameworks usam outros nomes para a mesma ideia. Hook é só um nome chique para isso."

"Terceira categoria: store, ou estado global. Quando várias partes da tela precisam ler o mesmo valor, tipo quem é o usuário logado ou o que tem no carrinho, você não espalha isso em variáveis soltas. Você coloca num lugar central, chamado store. Store é a prateleira compartilhada da página."

"Quarta categoria: servidor. Tem estado que não pode sumir quando a página fecha. Tipo o seu perfil, seu histórico, suas preferências. Esse estado não mora no navegador. Mora no servidor. E isso é assunto do próximo episódio."

### Cena 3 - O ciclo: evento, estado, re-render (9:30-11:00)

### Falar

"Agora o coração do vídeo. O ciclo."

### Mostrar

O diagrama do ciclo principal do arquivo 02, com as três etapas: evento, estado, re-render.

### Falar

"Toda vez que você interage com a página, o mesmo ciclo acontece."

"Primeiro: evento. Você clica, digita, arrasta. O navegador percebe e dispara um evento. Evento é o aviso de que algo aconteceu."

"Segundo: estado muda. O código que trata o evento atualiza o valor na variável, no hook ou no store."

"Terceiro: re-render. Alguém precisa atualizar o DOM para refletir o valor novo, e o navegador repinta a parte da tela que mudou. Quem atualiza o DOM depende do projeto: em JavaScript puro, é o seu código que mexe no DOM na mão. Em frameworks modernos, o framework percebe que o estado mudou e atualiza o DOM por você."

### Mostrar

O contador de novo. Clicar no botão e destacar as três etapas visualmente: (1) evento dispara, (2) contador passa de 0 para 1, (3) tela mostra 1.

### Falar

"Esse ciclo se repete toda vez. Evento, estado, re-render. Evento, estado, re-render."

"Isso é o que os frameworks chamam de reatividade. Uma página reativa é aquela em que a tela se atualiza sozinha quando o estado muda, sem você ter que mexer no DOM manualmente. Detalhe importante: esse trabalho é do framework, não do navegador. O navegador só repinta o que o DOM mandar. Quem liga o estado ao DOM é o código, seu ou do framework."

### Cena 4 - Por que isso importa para quem usa IA (11:00-12:00)

### Falar

"Por que você precisa saber disso?"

"Porque quando a IA escreve front-end, ela está o tempo todo mexendo nesse ciclo. Ela cria variável, ela mexe em hook, ela monta componente. E quando algo para de funcionar, o problema quase sempre está em um desses três pontos."

"Pergunta útil para fazer para a IA quando algo quebra: 'o evento está disparando? O estado está mudando? A tela está re-renderizando?'. Essa pergunta em três partes isola o problema."

### Fechamento do ATO 2

Mostrar o ciclo completo novamente. Dizer: "isso cobre o caminho feliz. A página real tem muito mais. É no próximo ato que a coisa costuma quebrar."

---

## ATO 3 - Os estados que a IA esquece (12:00-17:00)

### Cena 1 - O caminho feliz e o caminho real (12:00-13:00)

### Falar

"Quando você pede para a IA fazer uma tela que mostra uma lista de produtos, ela faz o seguinte: busca os produtos, mostra na tela. Pronto."

"Isso é o caminho feliz. O dado chegou, a lista está cheia, tudo funciona."

"Só que a vida real tem vários momentos. Tela que mostra dados tem vários estados. E a IA costuma tratar só um deles."

### Mostrar

O diagrama dos 5 estados do arquivo 02: loading, empty, error, partial, stale.

### Falar

"Toda tela que mostra dados tem, no mínimo, cinco momentos. Vamos passar por cada um."

### Cena 2 - Loading e empty (13:00-14:00)

### Falar

"Loading. A página pediu os dados para o servidor, mas ainda não chegou. Enquanto espera, o que o usuário vê?"

### Mostrar

Uma tela com um spinner (aquele círculo girando) ou a palavra "Carregando...".

### Falar

"Se a IA não tratar o loading, o usuário vê uma tela vazia. Parece quebrado. Parece que o site não funciona. Na verdade só está esperando."

"Segundo momento: empty. O dado chegou, mas a lista está vazia. Não tem nenhum produto. O que o usuário vê?"

### Mostrar

Uma tela com a mensagem "Nenhum produto encontrado" e talvez uma ilustração simples.

### Falar

"Se a IA não tratar o empty, o usuário vê a mesma tela vazia do loading. Mas o motivo é outro: o dado chegou, só não tem nada. São duas situações completamente diferentes, e a IA costuma confundir as duas."

### Cena 3 - Error e partial (14:00-15:15)

### Falar

"Terceiro momento: error. A chamada deu erro. O servidor está fora, a internet caiu, o usuário não tem permissão. O dado não vai chegar."

### Mostrar

Uma tela com a mensagem "Algo deu errado" e um botão "Tentar novamente".

### Falar

"Se a IA não tratar o error, a página fica presa no loading para sempre. Spinner girando eternamente. O usuário não sabe se está carregando ou se já deu erro."

"Quarto momento: partial. O dado chegou pela metade. A lista veio com 3 itens de 10. Ou veio sem um campo importante."

"Isso é mais raro, mas acontece. E a IA quase nunca trata. Ela assume que ou veio tudo, ou veio nada."

### Cena 4 - Stale (15:15-16:00)

### Falar

"Quinto e mais sutil: stale. Stale quer dizer velho, desatualizado."

### Mostrar

Uma tela mostrando uma lista. Ao lado, um relógio. A lista foi carregada há 10 minutos. O dado lá no servidor já mudou, mas a tela ainda mostra o antigo.

### Falar

"A página carregou os dados, mostrou, e o usuário ficou mexendo. Enquanto isso, o dado lá no servidor mudou. Outro usuário adicionou um produto, o preço alterou. A tela mostra informação velha."

"Isso é stale. A IA trata o momento de carregar, mas raramente trata o momento de atualizar. O resultado: o usuário vê coisa que já não é verdade."

### Cena 5 - A checklist para usar com IA (16:00-16:30)

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

"Ela provavelmente tratou só o caminho feliz. Os outros ela esquece. Quem programa com IA sem saber disso entrega telas que funcionam quando tudo dá certo e quebram quando algo dá errado."

### Cena 6 - Quando o estado precisa ir para o servidor (16:30-17:00)

### Falar

"E tem um limite. Algum estado não pode morar no navegador."

"O contador que some quando fecha, tudo bem. Mas o seu perfil, suas preferências, seu histórico, seus dados salvo. Isso não pode sumir."

"Esse estado precisa viajar do navegador para o servidor, onde sobrevive entre sessões. E isso é o assunto do próximo episódio."

### Fechamento do ATO 3

Mostrar o mapa completo do ciclo, agora com os 5 estados em volta dele. Dizer: "o ciclo é simples. Os cinco estados são o que a IA esquece. Se você cobrir os dois, seu front-end sobrevive ao mundo real."

---

## ENCERRAMENTO (17:00-18:30)

### Na câmera

"O front-end é um mecanismo. O navegador monta uma árvore, o DOM, a partir dos arquivos. Essa árvore muda porque existe estado. E o estado muda porque o usuário interage."

"O ciclo se repete: evento, estado, re-render. Evento, estado, re-render. Quando você entende isso, você para de tratar a tela como uma coisa só e começa a enxergar as três partes."

"E quando a IA gerar uma tela que mostra dados, cobre os cinco estados. Loading, empty, error, partial, stale. Ela provavelmente tratou só o caminho feliz."

### Call to action

"Na descrição tem o glossário com todos os termos que apareceram. Repo público [link] para consultar depois."

"O próximo vídeo da série vai pro servidor. Porque o estado que precisa sobreviver entre sessões não mora no navegador. Mora lá."

- Inscreva-se para a série
- Comente qual dos cinco estados você mais esquece
- Repo com o glossário: [link]
