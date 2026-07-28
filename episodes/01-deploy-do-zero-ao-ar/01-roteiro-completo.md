# Roteiro completo - Deploy do Zero ao Ar

**Duracao alvo:** 15-20 min
**Formato:** Gui falando para camera, alternando com diagrama simples na tela
**Regra pedagogica:** cada termo técnico e traduzido em 1 frase antes de continuar. Nenhum termo fica sem tradução.

---

## ABERTURA (0:00-0:45)

### Na camera

"Você escreve código. Aperta um botao. E de repente tem um site no ar que o mundo inteiro pode acessar. Mas o que acontece entre o código que você escreve e o site que abre no navegador?"

"Se você usa IA para programar, a IA escreve texto e diz que esta pronto. Mas para você confiar, para você saber quando ela esta certa e quando ela esta errada, você precisa enxergar as camadas que existem no meio."

"Neste vídeo não vou ensinar a programar. Vou contar a história de um deploy, do zero ao ar. Cada camada aparece no momento em que ela se torna necessária na jornada."

### Mostrar

Diagrama do mapa (arquivo 02) com todas as camadas em cor clara. Só mostrar, sem explicar. Dizer: "esse mapa vai ganhando vida aos poucos. No fim você vai enxergar ele inteiro."

---

## ATO 1 - No seu computador (0:45-5:30)

### Cena 1 - O código (0:45-2:00)

### Falar

"Tudo comeca com código. Quando você escreve uma linha de código, você esta dando uma instrução para o computador executar. Pode ser um botao, um texto, um calculo."

"O código mora em arquivos. Igual um documento de texto, mas com regras estritas."

"O navegador, que e o programa que abre sites, sabe ler certos tipos de arquivo e transformar em algo visual. Os principais são tres: HTML, CSS e JavaScript."

### Mostrar

Um arquivo de código simples aberto. Sem framework. Sem dependencia. Só um arquivo HTML com um botao.

### Traduzir

- HTML: o que aparece na tela (texto, botao, imagem)
- CSS: como aparece (cor, tamanho, posição)
- JavaScript: o que acontece (clicou, mudou, calculou)

### Cena 2 - A página e o estado (2:00-3:30)

### Falar

"Quando o navegador abre esses arquivos, ele monta uma página. Mas a página não e estática. Ela muda sem recarregar."

"Isso e o que chamamos de estado. Estado e a memória da página enquanto ela esta aberta."

Exemplos:
- Você clica num botao e ele muda de cor
- Você digita num campo e o texto aparece em outro lugar
- Você marca uma opcao e outra parte da tela reage

"Estado e a diferença entre uma página morta e uma página viva."

### Mostrar

Um clique mudando algo na tela sem recarregar. Sem código denso. Só o efeito visivel.

### Cena 3 - Variáveis (3:30-4:30)

### Falar

"Para a página lembrar das coisas, ela precisa de nomes para guardar valores. Isso são variáveis."

"Uma variável e uma caixinha com um nome. Você coloca algo dentro, e depois pode ler ou trocar."

Exemplo: `contador = 0`. Clicou: `contador = 1`. Mais um clique: `contador = 2`.

"Quando a IA fala em 'variável', ela esta dizendo: dei um nome para um valor que pode mudar."

### Cena 4 - Por que git (4:30-5:30)

### Falar

"Imagina que você escreveu 500 linhas de código. Quebrou algo. Como volta? Copia e cola em outro arquivo? Salva versao 1, versao 2, versao final final v2?"

"Git e o sistema de versionamento. Ele tira fotos do seu código em momentos especificos. Você pode voltar no tempo, criar uma linha paralela para testar algo sem estragar o original, e juntar tudo de novo."

"O repositório na nuvem que você ve por ai e onde essas fotos do código ficam guardadas, na nuvem, acessiveis pelo time."

### Mostrar

Um `git log` simples, mostrando commits como fotos no tempo. Ou só o conceito desenhado: linha do tempo com pontos.

### Falar

"Termo que vai aparecer muito: commit. Commit e o momento de tirar uma foto. Branch e a linha paralela. Merge e juntar de volta."

"Para o deploy, o que importa: o código que vai para o ar não e o código no seu computador. E o código que esta no repo, na nuvem, na versao principal."

### Fechamento do ATO 1

Mostrar o mapa de camadas com as partes do ATO 1 destacadas: código, estado, variáveis, git. Dizer: "isso tudo acontece dentro do seu computador. Agora o passo seguinte e fazer isso sair de la."

---

## ATO 2 - Saindo do seu computador (5:30-11:30)

### Cena 1 - Por que precisa de servidor (5:30-6:45)

### Falar

"O computador da sua casa não e acessivel pelo mundo. Ele desliga, troca de IP, fica atras de um roteador. Ninguém de fora consegue chegar nele."

"Para que o mundo alcance seu código, ele precisa morar em um computador que esta sempre ligado, sempre conectado, sempre pronto para responder. Isso e o servidor."

"Servidor não e nada mistico. E outro computador. As vezes um computador otimizado para ficar ligado 24 horas e responder rapidinho a muitos pedidos ao mesmo tempo."

### Mostrar

No diagrama, o servidor aparece como outra máquina, separada do computador de casa. Setinha: o código viaja do computador para o servidor.

### Cena 2 - O pedido e a resposta (request e response) (6:45-7:45)

### Falar

"Quando alguém digita o endereço do seu site, o navegador dele manda um pedido para o servidor. Esse pedido se chama request."

"O servidor recebe, processa, e devolve uma resposta. Essa resposta pode ser a página pronta para renderizar, ou pode ser um dado (uma lista de produtos, por exemplo) que o navegador vai montar na tela."

"Dois termos que aparecem juntos: request (pedido) e response (resposta). Tudo que acontece na web e uma conversa dessas."

### Cena 3 - API (7:45-9:00)

### Falar

"Para o servidor saber o que fazer com o pedido, ele precisa de uma porta de entrada organizada. Isso e a API."

"Pense na API como o balcao de atendimento do servidor. Você bate no balcao e pede: 'quero a lista de produtos'. O servidor vai atrás, busca, e devolve."

"API não e tecnologia especifica. E um contrato: qual pedido eu aceito, qual resposta eu devolvo. Quando a IA fala em 'chamar a API' ou 'endpoint', ela esta falando de uma dessas portas."

### Mostrar

Um diagrama simples: navegador -> seta com "request" -> servidor -> seta com "response (JSON)" -> navegador.

"Dado que viaja na resposta costuma vir em um formato chamado JSON. JSON e só texto organizado com chaves e listas, facil para o computador ler."

### Cena 4 - Banco de dados (9:00-10:15)

### Falar

"Se o servidor só respondesse pedido a pedido, ele esqueceria tudo depois. Precisa de um lugar onde os dados ficam guardados. Isso e o banco de dados."

"Banco de dados e a memória de longo prazo do servidor. La moram os usuarios, os produtos, os pedidos, tudo que precisa sobreviver entre um request e outro."

"Tem varios tipos. O importante agora não e saber qual. E saber que existe um lugar separado, com dados estruturados, e que o servidor consulta antes de responder."

### Mostrar

No diagrama, o banco aparece conectado ao servidor. Seta: servidor consulta banco -> banco devolve dado.

### Cena 5 - Auth (10:15-11:30)

### Falar

"Se qualquer pessoa pode pedir qualquer coisa para o servidor, e óbvio que precisa de controle. Nem todo pedido e legitimo. Nem todo mundo pode ver tudo."

"Auth e a camada que responde duas perguntas: quem e você? e você pode fazer isso?"

"Depois que você se loga, o servidor te da um token, tipo um crachá. A partir dai, cada request carrega esse cracha, e o servidor sabe quem esta pedindo."

"Quando a IA fala em 'auth', em 'token', em 'permissao', ela esta lidando com essa camada. Se ela propoe remover auth, perigo. Se ela propoe mexer nela sem você entender o impacto, pergunte."

### Fechamento do ATO 2

Mostrar o mapa com servidor, API, banco e auth destacados.

"Tudo isso esta no lado do servidor. O navegador não enxerga banco, não enxerga auth diretamente. Ele manda request e recebe response. O resto acontece atrás."

---

## ATO 3 - Indo ao ar (11:30-16:30)

### Cena 1 - Build (11:30-12:30)

### Falar

"O código que você escreve no computador não e exatamente o código que vai para o servidor. Ele precisa ser transformado."

"Esse processo se chama build. O build pega seu código, otimiza, junta arquivos, remove coisas que não precisa, e gera uma versao final pronta para servir."

"Pense no build como a cozinha de um restaurante. Você tem os ingredientes crus (seu código). O build cozinha, prato fica pronto, e o servidor só serve."

"Para a IA: quando ela fala em 'build quebrado' ou 'build passou', ela esta dizendo se a transformação do seu código em algo servivel funcionou."

### Cena 2 - CI/CD (12:30-13:45)

### Falar

"Antes do código ir para o ar, alguém precisa conferir se ele não quebrou nada. Isso podia ser humano, mas e lento. Então a gente automatiza."

"CI/CD e um cano automatizado. Toda vez que você manda código novo para o repo, ele passa por esse cano: roda lint (verifica estilo), roda testes, roda build. Se tudo verde, pode ir para o ar. Se algo vermelho, bloqueia."

"CI significa Continuous Integration. CD significa Continuous Deployment. O detalhe não importa agora. O que importa: e um portao automatico que impede código quebrado de chegar no ar."

"Quando a IA fala em 'CI vermelho', 'CI verde', 'pipeline', 'teste falhou', ela esta falando desse cano."

### Mostrar

Diagrama do pipeline: commit -> lint -> testes -> build -> deploy. Cores: verde/vermelho nos passos.

### Cena 3 - Deploy (13:45-14:45)

### Falar

"Depois que o build passou e o CI deu verde, o código finalmente vai para a nuvem. Isso e o deploy."

"Deploy e o ato de colocar a nova versao no servidor que esta sempre ligado, substituindo a anterior."

"Tem varios jeitos de fazer deploy. O importante agora e o conceito: o código vive no servidor. Deploy e trocar a versao que esta la."

"Algumas equipes fazem deploy com zero downtime (ninguém percebe a troca). Outras precisam derrubar o servidor por alguns segundos. Para o vídeo, o que importa: deploy e a publicação."

### Cena 4 - Domínio e DNS (14:45-16:30)

### Falar

"O servidor esta na nuvem, mas o usuario não vai digitar um endereço numerico. Ele vai digitar um nome: meuapp.com."

"Domínio e o nome. DNS e o sistema que traduz esse nome no endereço do servidor."

"Pense no DNS como uma lista telefonica. Você não decora o número, você procura pelo nome."

"Quando você deploya, você precisa garantir que o domínio aponta para o servidor certo. Se o deploy mudou o servidor, o DNS precisa ser atualizado."

### Fechamento do ATO 3

Mostrar o mapa completo, agora com todas as camadas: código, estado, variáveis, git, servidor, API, banco, auth, build, CI/CD, deploy, domínio.

"Essa e a história. De um arquivo no seu computador ate uma URL que alguém digita do outro lado do mundo."

---

## ENCERRAMENTO (16:30-18:00)

### Na camera

"Para programar com IA sem ser enganado, você não precisa saber cada detalhe de cada camada. Precisa saber que elas existem, e qual delas você esta tocando."

"Quando a IA sugerir uma mudança, pergunte: isso mora no front? No servidor? No banco? Mexe em auth? Tem deploy?"

"Se você não soube responder, pergunte para ela mesma: 'em qual camada essa mudança mora?'. A resposta te da o contexto do risco."

"Na descrição tem o glossario com todos os termos que apareceram. Repo público [link] para consultar depois."

"Se quiser aprofundar em uma camada especifica, tem vídeos da série chegando. O próximo vai ser sobre front-end e estado, porque e onde a maioria das pessoas começa."

### Call to action

- Inscreva-se para a série
- Comente qual camada você quer aprofundar
- Repo com o glossario: [link]
