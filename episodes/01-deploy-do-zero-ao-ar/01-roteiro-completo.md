# Roteiro completo - Deploy do Zero ao Ar

**Duracao alvo:** 16-18 min
**Formato:** Gui falando para camera, alternando com diagrama simples na tela
**Regra pedagogica:** cada termo técnico e traduzido em 1 frase antes de continuar. Nenhum termo fica sem tradução.
**Estrutura:** duas jornadas distintas. O fluxo de publicação (código -> git -> build -> deploy) e a linha principal, percorrida nos atos 1 e 3. O fluxo de uso (navegador -> domínio -> servidor -> API -> banco -> resposta -> navegador) e a volta final de ~90 segundos, no encerramento.

---

## ABERTURA (0:00-0:45)

### Na camera

"Você escreve código. Aperta um botao. E de repente tem um site no ar que o mundo inteiro pode acessar. Mas o que acontece entre o código que você escreve e o site que abre no navegador?"

"Se você usa IA para programar, a IA escreve texto e diz que esta pronto. Mas para você confiar, para você saber quando ela esta certa e quando ela esta errada, você precisa enxergar as camadas que existem no meio."

"Neste vídeo não vou ensinar a programar. Vou contar duas histórias que andam juntas. A primeira e como o código sai do seu computador e chega ao ar: o fluxo de publicação. A segunda e o que acontece quando alguém acessa a URL pronta: o fluxo de uso. Cada camada aparece no momento em que ela se torna necessária."

### Mostrar

Diagrama do mapa (arquivo 02) com as duas jornadas em cor clara. Só mostrar, sem explicar. Dizer: "esses dois caminhos vão ganhando vida aos poucos. No fim você vai enxergar eles inteiros."

---

## ATO 1 - No seu computador (0:45-3:30)

### Cena 1 - O código (0:45-2:15)

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

### Gancho para o próximo vídeo (2:00-2:15)

"Essa página não e estática. Ela muda sem recarregar: você clica e algo reage. A página tem uma memória própria enquanto esta aberta. Como isso funciona, com estado e variáveis, e o assunto do próximo vídeo da série. Aqui, o que importa e que o código que monta a página mora no seu computador."

### Cena 2 - Por que git (2:15-3:30)

### Falar

"Imagina que você escreveu 500 linhas de código. Quebrou algo. Como volta? Copia e cola em outro arquivo? Salva versao 1, versao 2, versao final final v2?"

"Git e o sistema de versionamento. Ele tira fotos do seu código em momentos especificos. Você pode voltar no tempo, criar uma linha paralela para testar algo sem estragar o original, e juntar tudo de novo."

"O repositório na nuvem que você ve por ai e onde essas fotos do código ficam guardadas, na nuvem, acessiveis pelo time."

### Mostrar

Um `git log` simples, mostrando commits como fotos no tempo. Ou só o conceito desenhado: linha do tempo com pontos.

### Falar

"Termo que vai aparecer muito: commit. Commit e o momento de tirar uma foto. Branch e a linha paralela. Merge e juntar de volta."

"Para o deploy, o que importa: na configuração mais comum, o código que vai para o ar não e o código no seu computador. E o código que esta no repo na nuvem, na versao principal. Existem fluxos diferentes, mas esse e o padrão que você vai encontrar na maioria dos projetos."

### Fechamento do ATO 1

Mostrar o mapa de camadas com as partes do ATO 1 destacadas: código e git. Dizer: "isso tudo acontece dentro do seu computador. Agora o passo seguinte e entender as camadas que vivem do outro lado, no servidor."

---

## ATO 2 - Saindo do seu computador (3:30-9:30)

### Cena 1 - Por que precisa de servidor (3:30-4:45)

### Falar

"O computador da sua casa não e um bom lugar para servir um site. Ele desliga, troca de IP, fica atras de um roteador."

"E possível expor um computador doméstico para a internet, mas e instável e exige configuração e cuidado com segurança. Para algo que precisa estar sempre acessivel, o comum e usar um servidor."

"Servidor e outro computador, otimizado para ficar ligado 24 horas e responder rapidinho a muitos pedidos ao mesmo tempo."

### Mostrar

No diagrama, o servidor aparece como outra máquina, separada do computador de casa. Setinha: o código viaja do computador para o servidor.

### Cena 2 - O pedido e a resposta (request e response) (4:45-5:45)

### Falar

"Quando alguém digita o endereço do seu site, o navegador dele manda um pedido para o servidor. Esse pedido se chama request."

"O servidor recebe, processa, e devolve uma resposta. Essa resposta pode ser a página pronta para renderizar, ou pode ser um dado (uma lista de produtos, por exemplo) que o navegador vai montar na tela."

"Dois termos que aparecem juntos: request (pedido) e response (resposta). Tudo que acontece na web e uma conversa dessas."

### Cena 3 - API (5:45-7:00)

### Falar

"Para o servidor saber o que fazer com o pedido, ele precisa de uma porta de entrada organizada. Isso e a API."

"Pense na API como o balcao de atendimento do servidor. O navegador bate no balcao e pede: 'quero a lista de produtos'. O servidor executa a lógica correspondente, busca, e devolve."

"API não e tecnologia especifica. E um contrato: qual pedido eu aceito, qual resposta eu devolvo. Quando a IA fala em 'chamar a API' ou 'endpoint', ela esta falando de uma dessas portas."

### Mostrar

Um diagrama simples: navegador -> seta com "request" -> servidor -> seta com "response (JSON)" -> navegador.

"Dado que viaja na resposta costuma vir em um formato chamado JSON. JSON e só texto organizado com chaves e listas, facil para o computador ler."

### Cena 4 - Banco de dados (7:00-8:15)

### Falar

"Se o servidor só respondesse pedido a pedido, ele esqueceria tudo depois. Precisa de um lugar onde os dados ficam guardados. Isso e o banco de dados."

"Banco de dados e a memória de longo prazo do servidor. La moram os usuarios, os produtos, os pedidos, tudo que precisa sobreviver entre um request e outro."

"Tem varios tipos. O importante agora não e saber qual. E saber que existe um lugar separado, com dados estruturados, e que o servidor consulta antes de responder."

### Mostrar

No diagrama, o banco aparece conectado ao servidor. Seta: servidor consulta banco -> banco devolve dado.

### Cena 5 - Auth: autenticação e autorização (8:15-9:30)

### Falar

"Se qualquer pessoa pode pedir qualquer coisa para o servidor, e óbvio que precisa de controle. Nem todo pedido e legitimo. Nem todo mundo pode ver tudo."

"Aqui existem duas coisas distintas, que costumam vir juntas sob o nome de auth."

"A primeira e autenticação: responder quem e você. E o login. O servidor te da um token, tipo um crachá, que prova quem você e."

"A segunda e autorização: decidir o que você pode fazer. Mesmo autenticado, você não pode tudo. Um usuario comum não apaga o banco; um administrador pode."

"A partir do login, cada request carrega esse cracha, e o servidor sabe quem esta pedindo e o que essa pessoa tem permissao de fazer."

"Quando a IA fala em 'auth', em 'token', em 'permissao', ela pode estar lidando com qualquer um dos dois. Se ela propoe remover auth, perigo. Se ela propoe mexer nela sem você entender o impacto, pergunte."

### Fechamento do ATO 2

Mostrar o mapa com servidor, API, banco e auth destacados.

"Tudo isso esta no lado do servidor. O navegador não enxerga banco, não enxerga auth diretamente. Ele manda request e recebe response. O resto acontece atrás."

---

## ATO 3 - Indo ao ar (9:30-14:30)

### Cena 1 - Build (9:30-10:30)

### Falar

"Em muitos projetos, o código que você escreve não vai direto para o servidor. Ele passa por uma transformação primeiro."

"Esse processo se chama build. O build pega seu código, otimiza, junta arquivos, remove coisas que não precisa, e gera uma versao final pronta para servir."

"Pense no build como a cozinha de um restaurante. Você tem os ingredientes crus (seu código). O build cozinha, prato fica pronto, e o servidor só serve."

"Importante: nem todo projeto precisa de build. Projetos simples, com arquivos estáticos, podem ir direto para o servidor. Mas na maioria dos projetos com framework, o build faz parte do caminho."

"Para a IA: quando ela fala em 'build quebrado' ou 'build passou', ela esta dizendo se a transformação do seu código em algo servivel funcionou."

### Cena 2 - CI/CD (10:30-11:45)

### Falar

"Antes do código ir para o ar, alguém precisa conferir se ele não quebrou nada. Isso podia ser humano, mas e lento. Então a gente automatiza."

"CI/CD e um cano automatizado. Toda vez que você manda código novo para o repo, ele passa por esse cano: roda lint (verifica estilo), roda testes, roda build. Se tudo verde, pode ir para o ar. Se algo vermelho, bloqueia."

"CI significa Continuous Integration. CD significa Continuous Deployment. O detalhe não importa agora. O que importa: e um portao automatico que impede código quebrado de chegar no ar."

"Quando a IA fala em 'CI vermelho', 'CI verde', 'pipeline', 'teste falhou', ela esta falando desse cano."

### Mostrar

Diagrama do pipeline: commit -> lint -> testes -> build -> deploy. Cores: verde/vermelho nos passos.

### Cena 3 - Deploy (11:45-12:45)

### Falar

"Depois que o build passou e o CI deu verde, o código finalmente vai para a nuvem. Isso e o deploy."

"Deploy e o ato de colocar a nova versao no servidor que esta sempre ligado, substituindo a anterior."

"Tem varios jeitos de fazer deploy. O importante agora e o conceito: o código vive no servidor. Deploy e trocar a versao que esta la."

"Algumas equipes fazem deploy com zero downtime (ninguém percebe a troca). Outras precisam derrubar o servidor por alguns segundos. Para o vídeo, o que importa: deploy e a publicação."

### Cena 4 - Domínio e DNS (12:45-14:30)

### Falar

"O servidor esta na nuvem, mas o usuario não vai digitar um endereço numerico. Ele vai digitar um nome: meuapp.com."

"Domínio e o nome. DNS e o sistema que traduz esse nome no endereço do servidor."

"Pense no DNS como uma lista telefonica. Você não decora o número, você procura pelo nome."

"Na maioria dos deploys, o endereço continua apontando para o mesmo serviço e nada muda no DNS. Atualizar o DNS e uma exceção: so e necessaria quando o servidor de destino realmente muda, o que não acontece no dia a dia de um deploy comum."

### Fechamento do ATO 3

Mostrar o mapa completo com o fluxo de publicação: código, git, build, CI/CD, deploy, domínio.

"Essa e a primeira jornada: de um arquivo no seu computador ate uma URL publicada. Mas publicar e so metade. Falta ver o que acontece quando alguém de fato acessa essa URL."

---

## ENCERRAMENTO - A volta final: o fluxo de uso (14:30-16:00)

### Na camera

"Agora que o deploy terminou, vamos percorrer a segunda jornada: o fluxo de uso. O que acontece quando alguém digita a URL e o site abre."

### Falar (percorrendo o fluxo de uso, ~90 segundos)

"O usuario digita meuapp.com no navegador. O DNS traduz esse nome no endereço do servidor."

"O navegador manda um request para uma entrada da API. O servidor recebe, executa a lógica correspondente, consulta o banco se precisar, verifica auth se for o caso, e devolve uma response."

"O navegador recebe a resposta e renderiza a página. Se a página tem estado, ela pode mudar sem recarregar, mas isso e o próximo vídeo."

"Esse ciclo request -> processa -> response -> renderiza acontece a cada interação. Cada clique pode ser uma nova conversa com o servidor."

### Fechamento

"Para programar com IA sem ser enganado, você não precisa saber cada detalhe de cada camada. Precisa saber que elas existem, e em qual das duas jornadas você esta tocando."

"Quando a IA sugerir uma mudança, pergunte: isso mora no front? No servidor? No banco? Mexe em auth? Tem deploy? E essa mudança afeta o fluxo de publicação ou o fluxo de uso?"

"Se você não soube responder, pergunte para ela mesma: 'em qual camada essa mudança mora?'. A resposta te da o contexto do risco."

"Na descrição tem o glossario com todos os termos que apareceram. Repo público [link] para consultar depois."

"Se quiser aprofundar em uma camada especifica, tem vídeos da série chegando. O próximo vai ser sobre front-end e estado, porque e onde a maioria das pessoas começa."

### Call to action

- Inscreva-se para a série
- Comente qual camada você quer aprofundar
- Repo com o glossario: [link]
