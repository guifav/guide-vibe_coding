# Roteiro completo - Build, CI/CD e Deploy (profundo)

**Duração alvo:** 20-25 min
**Formato:** Gui falando para câmera, alternando com diagrama simples na tela (o cano build/CI/CD/deploy e o mapa da temporada)
**Regra pedagógica:** cada termo técnico é traduzido em 1 frase antes de continuar. Nenhum termo fica sem tradução.

---

## ABERTURA (0:00-1:30)

### Na câmera

"No episódio 01 desta série, eu contei a história de um deploy indo ao ar. Mostrei que entre o código e o site existe um servidor, um banco, auth, e no fim existe uma coisa chamada build, CI/CD e deploy. Mas eu só mostrei o nome."

"Nos cinco episódios seguintes fomos fundo em cada camada. Front-end, API, banco, auth, git. Agora chegamos na última. O que realmente acontece quando o código vai para o ar?"

"Este é o último vídeo da temporada. Vou abrir a camada final, a que eu só mostrei por cima no episódio 01, e no fim vou voltar ao mapa completo. Se você assistiu à série toda, vai sair com o mapa inteiro na cabeça. Se caiu neste vídeo agora, também dá para acompanhar."

### Mostrar

O mapa do episódio 01 (arquivo 02 do ep01) com todas as camadas em cor clara. Dizer: "esse mapa nasceu no episódio 01. Hoje ele fecha."

---

## ATO 1 - O build e por que ele quebra (1:30-8:00)

### Cena 1 - Recap rápido: o que é build (1:30-3:00)

### Falar

"No episódio 01 eu disse que build é a cozinha do restaurante. Você entrega ingredientes crus, o build cozinha, e o servidor só serve o prato pronto. Agora vamos abrir a porta dessa cozinha."

"O código que vai para o servidor passa por uma transformação. O build é essa transformação."

"Transformar por quê? Porque o navegador e o servidor não leem o código da mesma forma que você escreve. Você escreve de um jeito fácil para humanos lerem e modificarem. O build reescreve para um jeito fácil para a máquina executar, otimizar e enviar pela rede."

### Mostrar

Lado a lado: o arquivo de código fonte (com indentação, comentários, nomes longos) e o mesmo arquivo depois do build (compactado, sem comentários, nomes curtos). Não precisa explicar linha a linha. Só o efeito visual.

### Cena 2 - O que o build realmente faz (3:00-5:30)

### Falar

"Dependendo do projeto, o build pode fazer várias coisas. Nem todo build faz tudo isso: tem projeto que só traduz a sintaxe, tem projeto que faz tudo junto. Mas vale conhecer o que pode acontecer dentro dele, para quando a IA falar o nome você saber do que se trata. Os nomes que você vai ouvir: compile (traduz), minify (reduz), bundle (junta), tree-shake (remove o que ninguém usa)."

"Ele pode traduzir a sintaxe. Pegar código escrito em uma linguagem que o humano gosta e transformar em uma versão que a máquina executa. É como traduzir de um idioma para outro."

"Pode também reduzir o tamanho dos arquivos: remover espaços, comentários e encurtar nomes, para o arquivo viajar mais rápido pela rede."

"E pode remover o que não usa e juntar os arquivos. Código que você importou mas não chamou sai fora. Vários arquivos viram um só, ou em poucos. Menos viagens pela rede, mais rápido."

### Mostrar

Diagrama simples: vários arquivos à esquerda, uma seta com a palavra BUILD, e um arquivo só, compactado, à direita. Três etiquetas na seta: traduz sintaxe, reduz tamanho, remove e junta.

### Cena 3 - Por que build quebra (5:30-8:00)

### Falar

"Se o build só transformasse, seria tranquilo. Mas ele também verifica. E quando ele não consegue transformar, ele quebra."

"Três motivos principais de build quebrado."

"Primeiro: sintaxe inválida. Sintaxe é a gramática do código. Você abriu um parêntese e não fechou. Faltou um ponto e vírgula. A máquina não entende e para."

"Segundo: erro de tipo. Tipo é a categoria de um valor. Número, texto, data são tipos diferentes. Se o código tenta fazer algo que não faz sentido para o tipo, o build reclama."

"Terceiro: dependência faltando. Dependência é um pedaço de código de outra pessoa que o seu código precisa para funcionar. Se você usa mas não declarou, ou declarou uma versão errada, o build não encontra e quebra."

### Mostrar

Uma tela de terminal com uma mensagem de erro de build. Sem precisar ler o erro. Só mostrar: texto vermelho, a palavra "error", a build parou. Dizer: "essa é a cara de build quebrado. A IA vai te mostrar isso muitas vezes. O importante é saber ler o motivo do erro."

### Falar

"Quando a IA fala 'build failed' ou 'build quebrado', ela está dizendo: a transformação não conseguiu terminar. Leia a mensagem. Ela quase sempre diz o arquivo e a linha. O problema mora lá."

### Fechamento do ATO 1

No diagrama do cano, destacar a etapa BUILD. Dizer: "o build é a primeira porta. Se ele não passa, nada passa. Agora vem a segunda porta, que é o CI."

---

## ATO 2 - O cano: CI e CD (8:00-17:30)

### Cena 1 - CI: o portão automático (8:00-10:30)

### Falar

"Imagina que toda vez que alguém do time manda código novo para o repo, um humano precisasse conferir se não quebrou nada. Ia ser lento. Ia ter erro humano. Então a gente automatiza."

"CI significa Continuous Integration, integração contínua. É um cano que roda sozinho toda vez que código entra no repo. Ele pega o código novo e passa por várias verificações, uma após a outra."

"Cada verificação é uma etapa. Se a etapa passa, fica verde. Se falha, fica vermelho. Vermelho em qualquer etapa, o cano para. Ninguém publica nada até consertar."

### Mostrar

Diagrama do cano: commit -> [lint] -> [testes] -> [build] -> [pronto para deploy]. Bolinhas verdes em cada etapa. Depois mostrar uma etapa vermelha e o cano parando.

### Cena 2 - As três verificações principais (10:30-13:00)

### Falar

"As verificações mais comuns são três. Você não precisa saber todas que existem. Precisa saber o que cada uma protege."

"Primeiro: lint. Lint é verificador de estilo. Ele não olha se o código funciona. Ele olha se o código está escrito do jeito que o time combinou. Indentação, nomes, aspas simples ou dupla. Parece bobo, mas código padronizado é mais fácil de ler e de manter."

"Segundo: testes. Teste é um pedaço de código que verifica se outro pedaço de código faz o que deveria. Você escreve: 'se eu passar X, espero Y'. O cano roda todos os testes. Se algum falha, vermelho. Teste não garante que o código está certo, mas garante que os comportamentos que você prometeu continuam funcionando."

"Terceiro: o build. Sim, o mesmo build do ATO 1. O CI também roda o build, porque se o build não passa na máquina do cano, é um sinal forte de problema. Mas atenção: o CI não replica o ambiente de produção por completo. O que passa no CI ainda pode quebrar em produção. Mesmo assim, é a melhor porta que temos antes do ar."

### Mostrar

O diagrama do cano de novo, agora com as três etiquetas explicadas: lint (estilo), testes (comportamento), build (transformação).

### Falar

"Quando a IA fala 'CI vermelho', 'pipeline falhou', 'teste quebrou', ela está falando desse cano. Vermelho em qualquer etapa bloqueia o caminho. Alguém precisa ir lá, ler o erro, consertar."

### Cena 3 - CD: publicar automaticamente (13:00-14:30)

### Falar

"CI para no 'pronto para deploy'. Quem publica? Em times modernos, outra parte do cano, chamada CD."

"CD pode significar duas coisas parecidas que vale distinguir, já que este é o episódio profundo. Continuous Delivery prepara uma versão publicável e para: o código passa em tudo, fica pronto, mas exige um humano apertar o botão de publicar. Continuous Deployment vai além: depois do CI verde, publica em produção automaticamente, sem decisão humana. Delivery prepara com portão humano; Deployment publica sozinho. Na prática os dois se chamam CD. O que importa é saber que existe essa fronteira de automação."

"No modo Deployment: você dá um push, o cano roda sozinho, e se tudo verde, o código vai para o ar sem nenhum humano apertar botão."

"Em times mais conservadores, o CD para antes de publicar e espera um humano aprovar. Em times mais soltos, publica direto. Cada equipe escolhe o nível de confiança."

### Mostrar

O diagrama do cano estendido: commit -> lint -> testes -> build -> [CD: publica no servidor]. Setinha final chegando no servidor.

### Cena 4 - Ambientes: onde o código mora em cada etapa (14:30-16:00)

### Falar

"O código não vai direto para o ar. Ele passa por ambientes. Ambiente é um lugar onde o código roda, com um propósito."

"Quatro ambientes que você vai encontrar."

"Local: é o seu computador. Você escreve, roda, testa no seu. Ninguém mais vê."

"Dev: é um servidor compartilhado de teste. O time joga código lá para ver funcionando junto. Quebra à vontade, tudo bem."

"Staging: é o ensaio. Uma cópia o mais próxima possível do ambiente real. Aqui não se quebra à toa. Aqui se ensaia o deploy antes do show."

"Prod: é o ar. É o servidor que o usuário acessa. Aqui não se mexe sem cuidado."

### Mostrar

Quatro caixas em linha: local, dev, staging, prod. Cada uma com uma cor. Local em cinza, dev em amarelo, staging em laranja, prod em vermelho (ou verde, se preferir "vivo"). Setinha mostrando o código subindo de uma para a outra.

### Falar

"O cano CI/CD costuma publicar em dev e em staging automaticamente. Publicar em prod é o passo que pede mais cuidado. Às vezes automático, às vezes com botão humano."

### Cena 5 - Estratégias de deploy (16:00-17:30)

### Falar

"Quando o código chega em prod, como ele entra? Tem vários jeitos. Você não precisa saber todos. Precisa conhecer dois, que são os que importam para a conversa sobre risco."

"Primeiro: blue-green. Você sobe a versão nova em um servidor paralelo, ao lado da antiga. Testa. Quando tem confiança, troca o tráfego de uma vez: todo mundo que chega agora vai para a nova. A antiga fica lá, pronta para voltar se der problema. Ninguém vê janela de indisponibilidade: é o tal do zero downtime."

"Segundo: canary. Você libera a versão nova para uma pequena parcela dos usuários primeiro. Cinco por cento, dez por cento. Se nada quebra, vai aumentando até cem. Se quebra, só poucos perceberam e você volta rápido."

"Existe também o tudo-de-uma-vez, que derruba a antiga e sobe a nova sem paralelo. Mas ele não te dá rede de segurança nenhuma, então vou pular ele aqui. O que interessa é entender que estratégia existe justamente para reduzir o risco de publicar."

### Mostrar

Dois mini-diagramas lado a lado.

Blue-green: duas caixas lado a lado, uma seta de "troca" apontando para a nova.

Canary: uma caixa nova recebendo uma setinha pequena de tráfego, e crescendo.

### Fechamento do ATO 2

Mostrar o cano completo: commit -> push -> CI (lint, testes, build) -> CD -> ambiente (dev/staging/prod) -> usuário. Dizer: "esse é o cano. Cada etapa tem um trabalho. Quando o usuário reclama que o site tá diferente, algo nesse cano acabou de chegar nele."

---

## ATO 3 - Quando algo dá errado e o fechamento (17:30-24:00)

### Cena 1 - Rollback: voltar atrás (17:30-19:00)

### Falar

"E quando o deploy publicou, o CI deu verde, tudo parecia bem, e mesmo assim o site quebra em prod? Acontece. Nem todo bug aparece no CI. Tem bug que só aparece com usuário de verdade, com dado de verdade, com volume de verdade."

"O primeiro movimento é voltar atrás. Isso se chama rollback. Rollback é desfazer o deploy, colocar de volta a versão anterior, a que estava funcionando."

"Se você deployou com blue-green, é fácil: aponta o tráfego de volta para o servidor antigo, que ainda está lá. Sem estratégia de paralelo, precisa re-deployar a versão anterior, e isso pode levar alguns minutos."

"Mas aqui é onde mora o detalhe que quase ninguém te conta: rollback do código só é seguro quando o banco, a API e a versão anterior continuam compatíveis."

"Exemplo. A versão nova mudou o schema do banco de dados, criando uma coluna nova. O código novo gravou dado nessa coluna. Você faz rollback para o código antigo. O código antigo não conhece aquela coluna. Ele pode quebrar, ou simplesmente ignorar dado importante. Em vez de resolver o incidente, você acabou de criar um segundo."

"Ou então a versão nova mudou o formato de resposta da API. Outros sistemas que dependem dela já se adaptaram. Você volta o código. Agora a API fala um idioma que ninguém mais espera. Rollback de código não desfaz mudança de dado. Ele só troca de versão."

"Então antes de puxar o rollback, pergunte: essa versão nova mexeu em schema de banco ou quebrou compatibilidade de API? Se sim, voltar o código pode piorar o incidente. Nesses casos o caminho costuma ser avançar: corrigir à frente e fazer um novo deploy."

"Por isso blue-green e canary existem. Não é só para evitar problemas. É para voltar rápido quando o problema acontece. E principalmente, é para voltar de um jeito que não arraste o banco junto."

### Mostrar

Diagrama: versão nova no ar -> problema detectado -> seta de "rollback" -> versão antiga volta.

### Cena 2 - Incidente e post-mortem (19:00-20:30)

### Falar

"Quando algo dá errado em prod e afeta o usuário, chamamos de incidente. Incidente é uma quebra com impacto real: gente não consegue logar, não consegue comprar, não consegue acessar."

"Depois que o incidente foi controlado, o time senta e faz o que se chama post-mortem. Post-mortem é uma conversa estruturada depois do problema resolvido. É para entender o que aconteceu, por que aconteceu, e o que mudar para evitar repetir."

"As perguntas clássicas do post-mortem: o que aconteceu? Como detectamos? Como resolvemos? O que vamos mudar para evitar?"

### Falar

"Quando a IA sugerir um deploy grande, uma mudança que mexe em várias camadas, pergunte duas coisas. Primeiro: se isso der errado em prod, conseguimos voltar rápido? Tem rollback? Tem blue-green? Segunda, a mais importante: essa mudança mexe em schema de banco ou quebra compatibilidade de API? Se sim, rollback de código não resolve. As duas respostas juntas dizem o tamanho do risco."

### Cena 3 - O ciclo completo, resumido (20:30-22:00)

### Falar

"Vamos resumir o ciclo inteiro, até o usuário perceber."

"Você escreve código no seu computador. Dá um commit, que é a foto do código no tempo. Dá um push, que manda essa foto para o repo na nuvem."

"O repo dispara o CI. O CI roda lint, testes e build. Se tudo verde, segue. Se algo vermelho, para."

"Depois do CI verde, o CD entra. Publica em dev, depois em staging. Em prod, publica com a estratégia escolhida: blue-green ou canary."

"O novo código está no ar. O usuário acessa o site e percebe algo diferente: um botão novo, uma tela nova, uma correção. Ele não viu nenhum dos passos. Só viu o resultado."

"Se o resultado está bom, acabou. Se está ruim, rollback, entender, consertar, deployar de novo."

### Mostrar

O diagrama do cano completo, agora em uma linha só, com todas as etapas e setas. Destacar que o usuário só enxerga a última ponta.

### Cena 4 - Fechamento da temporada: o mapa revisitado (22:00-24:00)

### Falar

"Esse vídeo fecha a temporada. No episódio 01 eu desenhei um mapa com todas as camadas entre o código e o ar. Hoje, seis episódios depois, cada uma dessas camadas já foi aberta."

Mostrar o mapa do episódio 01 na tela, completo.

"Vamos revisitar rápido."

Apontar para cada camada à medida que fala:

"Código, estado, variáveis. Isso mora no navegador. A gente abriu no episódio 02, front-end e estado."

"Request, response, API. Isso é a ponte entre navegador e servidor. Episódio 03."

"Banco de dados. A memória de longo prazo. Episódio 04."

"Auth. Quem é você, o que você pode fazer. Episódio 05."

"Git. A rede de segurança que te deixa voltar no tempo. Episódio 06."

"E hoje, build, CI/CD e deploy. O cano que leva o código ao ar."

"O mapa ficou inteiro. Quando a IA sugerir uma mudança, você já sabe perguntar: em qual camada isso mora? A resposta diz o risco."

---

## ENCERRAMENTO (24:00-25:00)

### Na câmera

"Essa foi a primeira temporada. Sete vídeos: o primeiro desenhou o mapa, os outros seis aprofundaram as camadas."

"Se você assistiu tudo, parabéns. Você saiu de 'a IA escreve e eu aprovo sem ler' para 'a IA escreve e eu sei em qual camada isso mora'. Isso muda tudo."

"Na descrição tem o glossário completo da temporada, com todos os termos dos sete vídeos. Repo público [link] para consultar quando precisar."

"Se a série te ajudou, tem dois jeitos de ajudar de volta. Inscreva-se, e comente qual camada você quer ver na próxima temporada. O canal cresce com isso."

"Obrigado por assistir até aqui. Te vejo na próxima."

### Call to action

- Inscreva-se
- Comente qual camada você quer aprofundar na próxima temporada
- Repo com o glossário completo da temporada: [link]
