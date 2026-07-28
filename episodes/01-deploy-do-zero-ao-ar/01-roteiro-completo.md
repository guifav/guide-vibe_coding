# Roteiro completo - Deploy do Zero ao Ar

**Duração alvo:** 16-18 min
**Formato:** Gui falando para câmera, alternando com diagrama simples na tela
**Regra pedagógica:** cada termo técnico é traduzido em 1 frase antes de continuar. Nenhum termo fica sem tradução.
**Estrutura:** duas jornadas distintas. O fluxo de publicação (código -> git -> build -> deploy) é a linha principal, percorrida nos atos 1 e 3. O fluxo de uso (navegador -> domínio -> servidor -> API -> banco -> resposta -> navegador) é a volta final de ~90 segundos, no encerramento.

---

## ABERTURA (0:00-0:45)

### Na câmera

"Você escreve código. Aperta um botão. E de repente tem um site no ar que o mundo inteiro pode acessar. Mas o que acontece entre o código que você escreve e o site que abre no navegador?"

"Se você usa IA para programar, a IA escreve texto e diz que está pronto. Mas para você confiar, para você saber quando ela está certa e quando ela está errada, você precisa enxergar as camadas que existem no meio."

"Neste vídeo vou contar duas histórias que andam juntas. A primeira é como o código sai do seu computador e chega ao ar: o fluxo de publicação. A segunda é o que acontece quando alguém acessa a URL pronta: o fluxo de uso. Cada camada aparece no momento em que ela se torna necessária."

### Mostrar

Diagrama do mapa (arquivo 02) com as duas jornadas em cor clara. Só mostrar, sem explicar. Dizer: "esses dois caminhos vão ganhando vida aos poucos. No fim você vai enxergar eles inteiros."

---

## ATO 1 - No seu computador (0:45-3:30)

### Cena 1 - O código (0:45-2:15)

### Falar

"Tudo começa com código. Quando você escreve uma linha de código, você está dando uma instrução para o computador executar. Pode ser um botão, um texto, um cálculo."

"O código mora em arquivos. Igual um documento de texto, mas com regras estritas."

"O navegador, que é o programa que abre sites, sabe ler certos tipos de arquivo e transformar em algo visual. Os principais são três: HTML, CSS e JavaScript."

### Mostrar

Um arquivo de código simples aberto. Sem framework. Sem dependência. Só um arquivo HTML com um botão.

### Traduzir

- HTML: o que aparece na tela (texto, botão, imagem)
- CSS: como aparece (cor, tamanho, posição)
- JavaScript: o que acontece (clicou, mudou, calculou)

### Gancho para o próximo vídeo (2:00-2:15)

"Essa página é dinâmica. Ela muda sem recarregar: você clica e algo reage. A página tem uma memória própria enquanto está aberta. Como isso funciona, com estado e variáveis, é o assunto do próximo vídeo da série. Aqui, o que importa é que o código que monta a página mora no seu computador."

### Cena 2 - Por que git (2:15-3:30)

### Falar

"Imagina que você escreveu 500 linhas de código. Quebrou algo. Como volta? Copia e cola em outro arquivo? Salva versão 1, versão 2, versão final final v2?"

"Git é o sistema de versionamento. Ele tira fotos do seu código em momentos específicos. Você pode voltar no tempo, criar uma linha paralela para testar algo sem estragar o original, e juntar tudo de novo."

"Essas fotos podem morar só no seu computador, mas na prática o repo também vive na nuvem: as plataformas de hospedagem de código que você vê por aí servem exatamente para isso, guardar as fotos do código num lugar que o time inteiro acessa."

### Mostrar

Um `git log` simples, mostrando commits como fotos no tempo. Ou só o conceito desenhado: linha do tempo com pontos.

### Falar

"Termo que vai aparecer muito: commit. Commit é o momento de tirar uma foto. Branch é a linha paralela. Merge é juntar de volta."

"Para o deploy, o que importa: na configuração mais comum, o código que vai para o ar é o código que está no repo na nuvem, na versão principal. Existem fluxos diferentes, mas esse é o padrão que você vai encontrar na maioria dos projetos."

### Fechamento do ATO 1

Mostrar o mapa de camadas com as partes do ATO 1 destacadas: código e git. Dizer: "isso tudo acontece dentro do seu computador. Agora o passo seguinte é entender as camadas que vivem do outro lado, no servidor."

---

## ATO 2 - Saindo do seu computador (3:30-9:30)

### Cena 1 - Por que precisa de servidor (3:30-4:45)

### Falar

"Para servir um site, você precisa de um servidor. O computador da sua casa desliga, troca de IP, fica atrás de um roteador."

"É possível expor um computador doméstico para a internet, mas é instável e exige configuração e cuidado com segurança. Para algo que precisa estar sempre acessível, o comum é usar um servidor."

"Servidor é outro computador, otimizado para ficar ligado 24 horas e responder rapidinho a muitos pedidos ao mesmo tempo."

### Mostrar

No diagrama, o servidor aparece como outra máquina, separada do computador de casa. Setinha: o código viaja do computador para o servidor.

### Cena 2 - O pedido e a resposta (request e response) (4:45-5:45)

### Falar

"Quando alguém digita o endereço do seu site, o navegador dele manda um pedido para o servidor. Esse pedido se chama request."

"O servidor recebe, processa, e devolve uma resposta. Essa resposta pode ser a página pronta para renderizar, ou pode ser um dado (uma lista de produtos, por exemplo) que o navegador vai montar na tela."

"Dois termos que aparecem juntos: request (pedido) e response (resposta). Praticamente tudo que acontece na web é uma conversa dessas."

### Cena 3 - API (5:45-7:00)

### Falar

"Para o servidor saber o que fazer com o pedido, ele precisa de uma porta de entrada organizada. Isso é a API."

"Pense na API como o balcão de atendimento do servidor. O navegador bate no balcão e pede: 'quero a lista de produtos'. O servidor executa a lógica correspondente, busca, e devolve."

"API é um contrato: qual pedido eu aceito, qual resposta eu devolvo. Quando a IA fala em 'chamar a API' ou 'endpoint', ela está falando de uma dessas portas."

### Mostrar

Um diagrama simples: navegador -> seta com "request" -> servidor -> seta com "response (JSON)" -> navegador.

"Dado que viaja na resposta costuma vir em um formato chamado JSON. JSON é só texto organizado com chaves e listas, fácil para o computador ler."

### Cena 4 - Banco de dados (7:00-8:15)

### Falar

"Se o servidor só respondesse pedido a pedido, ele esqueceria tudo depois. Precisa de um lugar onde os dados ficam guardados. Isso é o banco de dados."

"Banco de dados é a memória de longo prazo do servidor. Lá moram os usuários, os produtos, os pedidos, tudo que precisa sobreviver entre um request e outro."

"Tem vários tipos. O importante agora é saber que existe um lugar separado, com dados estruturados, e que o servidor consulta antes de responder."

### Mostrar

No diagrama, o banco aparece conectado ao servidor. Seta: servidor consulta banco -> banco devolve dado.

### Cena 5 - Auth: autenticação e autorização (8:15-9:30)

### Falar

"Se qualquer pessoa pode pedir qualquer coisa para o servidor, é óbvio que precisa de controle. Nem todo pedido é legítimo. Nem todo mundo pode ver tudo."

"Aqui existem duas coisas distintas, que costumam vir juntas sob o nome de auth."

"A primeira é autenticação: responder quem é você. É o login. O servidor te dá um token, tipo um crachá, que prova quem você é."

"A segunda é autorização: decidir o que você pode fazer. Mesmo autenticado, você não pode tudo. Um usuário comum não apaga o banco; um administrador pode."

"A partir do login, cada request carrega esse crachá, e o servidor sabe quem está pedindo e o que essa pessoa tem permissão de fazer."

"Quando a IA fala em 'auth', em 'token', em 'permissão', ela pode estar lidando com qualquer um dos dois. Se ela propõe remover auth, perigo. Se ela propõe mexer nela sem você entender o impacto, pergunte."

### Fechamento do ATO 2

Mostrar o mapa com servidor, API, banco e auth destacados.

"Tudo isso está no lado do servidor. O navegador só vê a resposta da API. Banco e auth ficam no servidor. Ele manda request e recebe response. O resto acontece atrás."

---

## ATO 3 - Indo ao ar (9:30-14:30)

### Cena 1 - Build (9:30-10:30)

### Falar

"Em muitos projetos, o código que você escreve não vai direto para o servidor. Ele passa por uma transformação primeiro."

"Esse processo se chama build. O build pega seu código, otimiza, junta arquivos, remove coisas que não precisa, e gera uma versão final pronta para servir."

"Pense no build como a cozinha de um restaurante. Você tem os ingredientes crus (seu código). O build cozinha, prato fica pronto, e o servidor só serve."

"Importante: nem todo projeto precisa de build. Projetos simples, com arquivos estáticos, podem ir direto para o servidor. Mas na maioria dos projetos com framework, o build faz parte do caminho."

"Para a IA: quando ela fala em 'build quebrado' ou 'build passou', ela está dizendo se a transformação do seu código em algo servível funcionou."

### Cena 2 - CI/CD (10:30-11:45)

### Falar

"Antes do código ir para o ar, alguém precisa conferir se ele não quebrou nada. Isso podia ser humano, mas é lento. Então a gente automatiza."

"CI/CD é um cano automatizado. Toda vez que você manda código novo para o repo, ele passa por esse cano: roda lint (verifica estilo), roda testes, roda build. Se tudo verde, pode ir para o ar. Se algo vermelho, bloqueia."

"CI significa Continuous Integration. CD tem duas leituras, Continuous Delivery ou Continuous Deployment (o ep07 abre essa diferença). O detalhe não importa agora. O que importa: é um portão automático que impede código quebrado de chegar no ar."

"Quando a IA fala em 'CI vermelho', 'CI verde', 'pipeline', 'teste falhou', ela está falando desse cano."

### Mostrar

Diagrama do pipeline: commit -> lint -> testes -> build -> deploy. Cores: verde/vermelho nos passos.

### Cena 3 - Deploy (11:45-12:45)

### Falar

"Depois que o build passou e o CI deu verde, o código finalmente vai para a nuvem. Isso é o deploy."

"Deploy é o ato de colocar a nova versão no servidor que está sempre ligado, substituindo a anterior."

"Tem vários jeitos de fazer deploy. O importante agora é o conceito: o código vive no servidor. Deploy é trocar a versão que está lá."

"Algumas equipes fazem deploy com zero downtime (ninguém percebe a troca). Outras precisam derrubar o servidor por alguns segundos. Para o vídeo, o que importa: deploy é a publicação."

### Cena 4 - Domínio e DNS (12:45-14:30)

### Falar

"O servidor está na nuvem, mas o usuário não vai digitar um endereço numérico. Ele vai digitar um nome: meuapp.com."

"Domínio é o nome. DNS é o sistema que traduz esse nome no endereço do servidor."

"Pense no DNS como uma lista telefônica. Você não decora o número, você procura pelo nome."

"Na maioria dos deploys, o endereço continua apontando para o mesmo serviço e nada muda no DNS. Atualizar o DNS é uma exceção: só é necessária quando o servidor de destino realmente muda, o que não acontece no dia a dia de um deploy comum."

### Fechamento do ATO 3

Mostrar o mapa completo com o fluxo de publicação: código, git, build, CI/CD, deploy, domínio.

"Essa é a primeira jornada: a URL publicada no ar. Mas publicar é só metade. Falta ver o que acontece quando alguém de fato acessa essa URL."

---

## ENCERRAMENTO - A volta final: o fluxo de uso (14:30-16:00)

### Na câmera

"Agora que o deploy terminou, vamos percorrer a segunda jornada: o fluxo de uso. O que acontece quando alguém digita a URL e o site abre."

### Falar (percorrendo o fluxo de uso, ~90 segundos)

"O usuário digita meuapp.com no navegador. O DNS traduz esse nome no endereço do servidor."

"O navegador manda o primeiro request pedindo a própria página. Depois, de dentro da página, os pedidos de dado batem nas entradas da API. Em cada request o servidor recebe, executa a lógica correspondente, consulta o banco se precisar, verifica auth se for o caso, e devolve uma response."

"O navegador recebe a resposta e renderiza a página. Se a página tem estado, ela pode mudar sem recarregar, mas isso é o próximo vídeo."

"Esse ciclo request -> processa -> response -> renderiza acontece a cada interação. Cada clique pode ser uma nova conversa com o servidor."

### Fechamento

"Para programar com IA sem ser enganado, você não precisa saber cada detalhe de cada camada. Precisa saber que elas existem, e em qual das duas jornadas você está tocando."

"Quando a IA sugerir uma mudança, pergunte: isso mora no front? No servidor? No banco? Mexe em auth? Tem deploy? E essa mudança afeta o fluxo de publicação ou o fluxo de uso?"

"Se você não soube responder, pergunte para ela mesma: 'em qual camada essa mudança mora?'. A resposta te dá o contexto do risco."

"Na descrição tem o glossário com todos os termos que apareceram. Repo público [link] para consultar depois."

"Se quiser aprofundar em uma camada específica, tem vídeos da série chegando. O próximo vai ser sobre front-end e estado, porque é onde a maioria das pessoas começa."

### Call to action

- Inscreva-se para a série
- Comente qual camada você quer aprofundar
- Repo com o glossário: [link]
