# Roteiro completo - Secrets e Variáveis de Ambiente

**Duração alvo:** 15-18 min
**Formato:** Gui falando para câmera, alternando com diagrama simples na tela e exemplos reais (um .env, um .gitignore, um diff)
**Regra pedagógica:** cada termo técnico é traduzido em 1 frase antes de continuar. Nenhum termo fica sem tradução.
**Regra de gravação:** nenhuma chave real aparece na tela, nem de teste. Todos os exemplos usam valores obviamente falsos (`chave_exemplo_nao_usar`).

---

## ABERTURA (0:00-0:45)

### Na câmera

"Você pede para a IA conectar seu app num serviço de pagamento. Ela diz: 'preciso da sua chave de API'. Você copia a chave do painel do serviço, cola no código, funciona. Você commita, sobe para o repo. Pronto."

"Você acabou de publicar a senha do seu negócio."

"Se o repo é público, é questão de minutos até alguém achar. E mesmo que você apague depois, o git lembra. Neste vídeo eu conto onde os segredos moram de verdade, por que o código é o pior lugar do mundo para eles, e o que fazer quando um escapa."

### Mostrar

Uma linha de código com uma chave falsa colada dentro (`chave = "chave_exemplo_nao_usar"`), com um X vermelho por cima. Só mostrar, sem explicar. Dizer: "no fim do vídeo, você vai saber exatamente por que isso está errado e o que fazer no lugar."

---

## ATO 1 - O que é um segredo e por que ele não pode morar no código (0:45-5:30)

### Cena 1 - O que é um secret (0:45-2:15)

### Falar

"Todo app de verdade conversa com serviços de fora. Um serviço de pagamento, um serviço de e-mail, um modelo de IA. E cada serviço desses precisa saber que é o SEU sistema chamando, e não um estranho."

"Para isso ele te dá uma chave de API. Chave de API é a senha que um serviço dá para o seu sistema usar ele. Quem tem a chave, usa o serviço em seu nome, e a conta chega para você."

"Chave de API, senha do banco de dados, token de acesso: tudo isso tem um nome coletivo. Segredo, ou secret. Segredo é qualquer valor que dá acesso a algo em seu nome."

### Mostrar

Três exemplos na tela, com valores falsos: chave de API de um serviço de pagamento, senha de banco de dados, token de um serviço de IA. Etiqueta em cima: SEGREDOS.

### Traduzir

- Chave de API: a senha que um serviço externo dá para o seu sistema usar ele
- Secret (segredo): qualquer valor que dá acesso a algo em seu nome
- Credencial: nome genérico para o par "quem sou" + "prova de que sou" (usuário e senha, por exemplo)

### Cena 2 - Código é fechadura, segredo é chave (2:15-3:30)

### Falar

"Aqui vem a distinção que carrega o vídeo inteiro. Pensa numa porta."

"O código é a fechadura. A fechadura pode ser vista por todo mundo: qualquer um olha, estuda o mecanismo, entende como funciona. Em projeto open source, o mundo inteiro literalmente lê a fechadura. E tudo bem."

"O segredo é a chave. A chave só o dono carrega. Se você cola a chave na porta, do lado de fora, a fechadura vira decoração."

"Traduzindo: o código diz O QUE fazer. O segredo diz COM QUAL CHAVE. Os dois nunca viajam juntos."

### Mostrar

Diagrama: uma porta com fechadura (rotulada CÓDIGO, com um olho em cima: "todo mundo pode ver") e uma chave separada (rotulada SEGREDO, com um cadeado: "só o dono"). Depois a imagem errada: a chave pendurada na fechadura, com X vermelho.

### Cena 3 - Por que commitou = vazou (3:30-5:30)

### Falar

"Agora o motivo de eu dizer que colar a chave no código é publicar a senha."

"O código não fica só na sua máquina. Ele vai para o repo, lembra do episódio 06? E o repo é compartilhado: o time inteiro vê, e se for público, o mundo inteiro vê."

"E tem o detalhe que muda tudo: commit é uma foto imutável. Foi o que a gente viu no episódio 06. Se a chave entrou num commit, ela está naquela foto para sempre. Você pode apagar o arquivo hoje e commitar de novo: a foto de ontem continua no álbum, com a chave dentro."

"E não é risco teórico. Existem robôs varrendo repos públicos o tempo inteiro, procurando exatamente isso: padrões de chave. Uma chave de serviço pago commitada em repo público costuma ser encontrada em minutos. O resultado é conta estourada, banco de dados exposto, dado de cliente vazado."

### Mostrar

Linha do tempo de commits (o álbum do ep06). Um commit no meio com uma chave dentro, destacada em vermelho. Um commit posterior "apaguei a chave" com o arquivo limpo. Seta voltando para o commit antigo: "a foto antiga continua aqui".

### Fechamento do ATO 1

"Então o segredo não pode morar no código. Mas o código PRECISA do segredo para funcionar. Como é que o código usa uma chave que não está nele? Esse é o próximo ato."

---

## ATO 2 - Variáveis de ambiente: onde o segredo mora (5:30-11:30)

### Cena 1 - O ambiente (5:30-6:45)

### Falar

"No episódio 07 a gente viu que o código roda em ambientes: local, que é a sua máquina. Dev e staging, que são os servidores de teste e ensaio. E prod, que é o ar, onde o usuário de verdade está."

"Ambiente é um lugar onde o código roda. E aqui está o pulo do gato: o MESMO código roda em todos eles. O que muda de um ambiente para o outro não é o código. São os valores."

"Em dev, o código fala com um banco de teste. Em prod, com o banco real. Em dev, usa uma chave de pagamento de mentira, que não cobra ninguém. Em prod, a chave real. Mesmo código, valores diferentes."

### Mostrar

Quatro caixas (local, dev, staging, prod, as mesmas do ep07). O mesmo bloco de código dentro das quatro. Embaixo de cada uma, valores diferentes: "banco de teste / chave de teste" nas primeiras, "banco real / chave real" em prod.

### Cena 2 - A variável de ambiente (6:45-8:15)

### Falar

"E é assim que o código usa uma chave que não está nele: ele pede pelo nome."

"Isso é a variável de ambiente. Variável de ambiente é uma caixinha com nome que mora no ambiente, não no código. O código diz: 'me dá o valor de CHAVE_PAGAMENTO'. E o ambiente onde ele está rodando responde com o valor que tem lá."

"A analogia que fica: pensa no código como a planta de um prédio, e nos ambientes como prédios construídos com essa mesma planta. Cada prédio tem a sua portaria, e cada portaria tem o seu quadro de chaves. A planta diz 'pegue a chave chamada CHAVE_PAGAMENTO na portaria'. Qual chave vem, depende de qual prédio você está."

"No código, só existe o nome. O valor, nunca. Isso é a regra de ouro."

### Mostrar

Diagrama: o código com a linha "me dá CHAVE_PAGAMENTO" e setas para dois ambientes. No ambiente dev, a caixinha CHAVE_PAGAMENTO devolve "chave de teste". No prod, devolve "chave real". Etiqueta: "o código só conhece o NOME".

### Traduzir

- Variável de ambiente: caixinha com nome que mora no ambiente; o código pede pelo nome e recebe o valor
- Hardcoded: valor escrito direto no código (é disso que a gente está fugindo)

### Cena 3 - O .env e o .gitignore (8:15-10:00)

### Falar

"Beleza, mas na SUA máquina, no ambiente local, onde ficam esses valores? Na maioria dos projetos, num arquivo chamado .env."

".env é um arquivo de texto simples, na raiz do projeto, com um par nome-valor por linha. CHAVE_PAGAMENTO igual valor, SENHA_BANCO igual valor. Quando o projeto sobe, ele lê esse arquivo e preenche as caixinhas."

"Só que esse arquivo tem os valores de verdade. Então ele NUNCA pode ir para o repo. E como o git sabe o que não levar? Com o .gitignore."

".gitignore é a lista do que o git deve fingir que não existe. Arquivo listado ali não entra em foto nenhuma. O .env está nessa lista em qualquer projeto sério. Se não está, é a primeira coisa a corrigir."

"E como o resto do time sabe quais nomes o projeto precisa? Com um segundo arquivo, o .env.example: a mesma lista de nomes, mas com valores falsos ou vazios. Esse sim vai para o repo. Ele é o mapa das caixinhas, sem nenhuma chave dentro."

### Mostrar

Dois arquivos lado a lado. À esquerda, `.env` com valores falsos preenchidos e um cadeado: "fica na máquina, NUNCA no repo". À direita, `.env.example` com os mesmos nomes e valores vazios: "vai para o repo". Embaixo, o `.gitignore` com a linha `.env` destacada.

### Traduzir

- .env: arquivo local com os pares nome-valor de verdade; nunca vai para o repo
- .gitignore: a lista do que o git deve ignorar; o .env mora nela
- .env.example: a lista dos nomes sem os valores; esse vai para o repo
- Placeholder: valor de mentira que marca o lugar do valor real

### Cena 4 - E em produção? (10:00-11:30)

### Falar

"E em prod? Não tem .env commitado, não tem você digitando chave em servidor. Quem guarda os valores de produção é a plataforma onde você faz o deploy."

"Toda plataforma de deploy tem um painel de configuração: uma tela onde você cadastra as variáveis de ambiente daquele serviço. Nome e valor, uma a uma. Quando o servidor sobe, a plataforma entrega esses valores para o ambiente, e o código encontra as caixinhas preenchidas."

"Repara na simetria: mesmo nome em todo lugar, valor diferente em cada lugar. CHAVE_PAGAMENTO existe no seu .env local com a chave de teste, e existe no painel de prod com a chave real. O código não muda uma linha."

"E fecha o ciclo do episódio 01: o deploy leva o código. A configuração já está no ambiente esperando. Os dois se encontram só na hora de rodar."

### Mostrar

Diagrama do caminho: código (sem valores) viaja pelo deploy até o servidor; ao lado, o painel de configuração da plataforma injeta as variáveis no ambiente. Os dois se encontram no servidor rodando.

### Fechamento do ATO 2

"Esse é o mapa: segredo mora no ambiente. Local no .env, produção no painel da plataforma. No código, só o nome. Agora vamos ver onde a IA tropeça nisso, porque ela tropeça."

---

## ATO 3 - Onde a IA erra e o que fazer quando vaza (11:30-16:00)

### Cena 1 - As três armadilhas da IA (11:30-13:30)

### Falar

"A IA quer que o código funcione agora. Segurança de longo prazo não é a prioridade dela. Três armadilhas clássicas."

"Armadilha 1: chave direto no código. Você cola a chave no chat para ela testar, e ela escreve a chave dentro do código, hardcoded. Funciona na hora. E planta a bomba. Pergunta-crivo: 'essa chave está no código ou no ambiente?'"

"Armadilha 2: o .env no repo. Ela cria o .env mas esquece do .gitignore. Ou pior: você pede para 'commitar tudo' e ela obedece, .env junto. Pergunta-crivo: 'o .env está no .gitignore?'"

"Armadilha 3: segredo no log. Para depurar, ela imprime tudo, inclusive a variável com a chave. O valor aparece no terminal, vai para o arquivo de log, às vezes vai parar numa mensagem de erro que o usuário vê. Log é a memória do que o sistema fez; segredo impresso em log é segredo gravado em texto plano. Pergunta-crivo: 'algum valor de segredo aparece em log ou mensagem de erro?'"

### Mostrar

As três armadilhas em cards, cada uma com a pergunta-crivo embaixo. Depois, um diff na tela com uma string longa suspeita destacada: "antes de commitar, procure por isso no diff".

### Cena 2 - Como pedir certo (13:30-14:30)

### Falar

"A boa notícia: a IA faz certo se você pedir certo. Três instruções que resolvem quase tudo."

"Primeira: 'use variável de ambiente, não escreva o valor no código'. Ela sabe fazer, só precisa do comando."

"Segunda: 'crie o .env.example e garanta que o .env está no .gitignore'. Uma frase, e a estrutura fica certa."

"Terceira: nunca cole a chave real no chat. A conversa com a IA também é um lugar: se a chave passou por lá, ela existe fora do seu controle. Use placeholder no chat, e preencha o valor você mesmo, direto no .env."

### Mostrar

As três instruções na tela, como prompts prontos para copiar.

### Cena 3 - Vazou. E agora? (14:30-16:00)

### Falar

"E se a chave já foi para o repo? Protocolo de emergência, nessa ordem."

"Passo 1: revogar a chave. Você vai no painel do serviço que emitiu a chave e cancela ela. A partir daí, aquela chave não abre mais nada. Isso se chama rotacionar: cancela a antiga, gera uma nova. É a versão digital de trocar a fechadura."

"Passo 2: colocar a chave nova no lugar certo. No .env local, no painel da plataforma em prod. Nunca no código."

"Passo 3: verificar o estrago. O painel do serviço mostra o uso da chave: teve chamada que você não reconhece? Cobrança estranha? Se sim, o problema é maior que a chave, e aí é suporte do serviço e revisão do que foi acessado."

"E o que NÃO resolve: apagar o arquivo e commitar de novo. Repete comigo: o git lembra. A foto antiga continua no álbum. Existe jeito de reescrever o histórico, mas é avançado e não desfaz cópias que já foram feitas. A chave exposta morreu no momento em que vazou. Rotacionar não é uma das opções. É a única."

### Mostrar

O protocolo em três passos numerados. Embaixo, em destaque: "apagar o commit NÃO desfaz o vazamento. Rotacione."

### Fechamento do ATO 3

"Segredo vaza até em empresa grande. A diferença entre incidente e catástrofe é ter o protocolo: revoga, troca, verifica. E a diferença entre quem vaza toda semana e quem quase nunca vaza é o hábito: valor no ambiente, nome no código."

---

## ENCERRAMENTO (16:00-17:30)

### Na câmera

"Recapitulando a regra de ouro: o código diz o que fazer. O segredo diz com qual chave. Os dois nunca viajam juntos."

"Quando a IA mexer em qualquer coisa que conecta um serviço, três perguntas: essa chave está no código ou no ambiente? O .env está no .gitignore? Algum segredo aparece em log?"

"E se vazou: revoga, troca, verifica. Apagar o arquivo não desfaz a foto."

"Na descrição tem o glossário com todos os termos que apareceram. Repo público [link] para consultar depois."

"Este vídeo abre a segunda temporada da série. Na temporada 1, a gente desenhou o mapa das camadas entre o código e o ar. Nesta, a gente aprende a operar esse mapa sem se machucar. Comente o que você quer ver: HTTPS e o cadeado do navegador? Como saber que o site quebrou antes do cliente reclamar? A fila decide."

### Call to action

- Inscreva-se para a temporada 2
- Comente se você já commitou uma chave sem querer (sem vergonha, todo mundo já)
- Repo com o glossário: [link]
