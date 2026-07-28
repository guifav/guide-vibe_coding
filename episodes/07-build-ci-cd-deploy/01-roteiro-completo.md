# Roteiro completo — Build, CI/CD e Deploy (profundo)

**Duracao alvo:** 20-25 min
**Formato:** Gui falando para camera, alternando com diagrama simples na tela (o cano build/CI/CD/deploy e o mapa da temporada)
**Regra pedagogica:** cada termo tecnico e traduzido em 1 frase antes de continuar. Nenhum termo fica sem traducao.

---

## ABERTURA (0:00-1:30)

### Na camera

"No episodio 01 desta serie, eu contei a historia de um deploy, do zero ao ar. Mostrei que entre o codigo e o site existe um servidor, um banco, auth, e no fim existe uma coisa chamada build, CI/CD e deploy. Mas eu so mostrei o nome."

"Nos seis episodios seguintes fomos fundo em cada camada. Front-end, API, banco, auth, git. Agora chegamos na ultima. O que realmente acontece quando o codigo vai para o ar?"

"Este e o ultimo video da temporada. Vou abrir a camada final, a que eu so mostrei por cima no episodio 01, e no fim vou voltar ao mapa completo. Se voce assistiu a serie toda, vai sair com o mapa inteiro na cabeca. Se caiu neste video agora, tambem da para acompanhar."

### Mostrar

O mapa do episodio 01 (arquivo 02 do ep01) com todas as camadas em cor clara. Dizer: "esse mapa nasceu no episodio 01. Hoje ele fecha."

---

## ATO 1 — O build e por que ele quebra (1:30-8:00)

### Cena 1 — Recap rapido: o que e build (1:30-3:00)

### Falar

"No episodio 01 eu disse que build e a cozinha do restaurante. Voce entrega ingredientes crus, o build cozinha, e o servidor so serve o prato pronto. Agora vamos abrir a porta dessa cozinha."

"O codigo que voce escreve no seu computador nao e o codigo que vai para o servidor. Ele precisa ser transformado. O build e essa transformacao."

"Transformar por que? Porque o navegador e o servidor nao leem o codigo da mesma forma que voce escreve. Voce escreve de um jeito facil para humanos lerem e modificarem. O build reescreve para um jeito facil para a maquina executar, otimizar e enviar pela rede."

### Mostrar

Lado a lado: o arquivo de codigo fonte (com indentacao, comentarios, nomes longos) e o mesmo arquivo depois do build (compactado, sem comentarios, nomes curtos). Nao precisa explicar linha a linha. So o efeito visual.

### Cena 2 — O que o build realmente faz (3:00-5:30)

### Falar

"O build faz varias coisas ao mesmo tempo. Nao preciso que voce decore os nomes. Preciso que voce saiba o que cada uma faz, para quando a IA falar o nome voce saber do que se trata."

"Primeiro: compile. Compile e pegar codigo escrito em uma linguagem que o humano gosta e transformar em uma versao que a maquina executa. E como traduzir de um idioma para outro."

"Segundo: minify. Minify e remover tudo que o computador nao precisa para executar. Espacos, quebras de linha, comentarios, nomes longos de variaveis viram nomes curtos. O arquivo fica menor e viaja mais rapido pela rede."

"Terceiro: tree-shake. Tree-shake e remover codigo que voce escreveu ou importou mas nao usa. Imagine uma arvore: voce sacode e as folhas mortas caem. O que fica e so o que o app realmente precisa."

"Quarto: bundle. Bundle e juntar varios arquivos em um so, ou em poucos. Em vez do navegador baixar cinquenta arquivos separados, baixa um. Menos viagens, mais rapido."

### Mostrar

Diagrama simples: varios arquivos a esquerda, uma seta com a palavra BUILD, e um arquivo so, compactado, a direita. Quatro etiquetas na seta: compile, minify, tree-shake, bundle.

### Cena 3 — Por que build quebra (5:30-8:00)

### Falar

"Se o build so transformasse, seria tranquilo. Mas ele tambem verifica. E quando ele nao consegue transformar, ele quebra."

"Tres motivos principais de build quebrado."

"Primeiro: sintaxe invalida. Sintaxe e a gramatica do codigo. Voce abriu um parentese e nao fechou. Faltou um ponto e virgula. A maquina nao entende e para."

"Segundo: erro de tipo. Tipo e a categoria de um valor. Um numero nao e um texto. Uma data nao e um numero. Se o codigo tenta fazer algo que nao faz sentido para o tipo, o build reclama."

"Terceiro: dependencia faltando. Dependencia e um pedaco de codigo de outra pessoa que o seu codigo precisa para funcionar. Se voce usa mas nao declarou, ou declarou uma versao errada, o build nao encontra e quebra."

### Mostrar

Uma tela de terminal com uma mensagem de erro de build. Sem precisar ler o erro. So mostrar: texto vermelho, a palavra "error", a build parou. Dizer: "essa e a cara de build quebrado. A IA vai te mostrar isso muitas vezes. O importante e saber ler o motivo, nao decore o nome da ferramenta."

### Falar

"Quando a IA fala 'build failed' ou 'build quebrado', ela esta dizendo: a transformacao nao conseguiu terminar. Leia a mensagem. Ela quase sempre diz o arquivo e a linha. O problema mora la."

### Fechamento do ATO 1

No diagrama do cano, destacar a etapa BUILD. Dizer: "o build e a primeira porta. Se ele nao passa, nada passa. Agora vem a segunda porta, que e o CI."

---

## ATO 2 — O cano: CI e CD (8:00-17:30)

### Cena 1 — CI: o portao automatico (8:00-10:30)

### Falar

"Imagina que toda vez que alguem do time manda codigo novo para o repo, um humano precisasse conferir se nao quebrou nada. Ia ser lento. Ia ter erro humano. Entao a gente automatiza."

"CI significa Continuous Integration, integracao continua. E um cano que roda sozinho toda vez que codigo entra no repo. Ele pega o codigo novo e passa por varias verificacoes, uma apos a outra."

"Cada verificacao e uma etapa. Se a etapa passa, fica verde. Se falha, fica vermelho. Vermelho em qualquer etapa, o cano para. Ninguem publica nada ate consertar."

### Mostrar

Diagrama do cano: commit -> [lint] -> [testes] -> [build] -> [pronto para deploy]. Bolinhas verdes em cada etapa. Depois mostrar uma etapa vermelha e o cano parando.

### Cena 2 — As tres verificacoes principais (10:30-13:00)

### Falar

"As verificacoes mais comuns sao tres. Voce nao precisa saber todas que existem. Precisa saber o que cada uma protege."

"Primeiro: lint. Lint e verificador de estilo. Ele nao olha se o codigo funciona. Ele olha se o codigo esta escrito do jeito que o time combinou. Indentacao, nomes, aspas simples ou dupla. Parece bobo, mas codigo padronizado e mais facil de ler e de manter."

"Segundo: testes. Teste e um pedaco de codigo que verifica se outro pedaco de codigo faz o que deveria. Voce escreve: 'se eu passar X, espero Y'. O cano roda todos os testes. Se algum falha, vermelho. Teste nao garante que o codigo esta certo, mas garante que os comportamentos que voce prometeu continuam funcionando."

"Terceiro: o build. Sim, o mesmo build do ATO 1. O CI tambem roda o build, porque se o build nao passa na maquina do cano, ele nao vai passar em lugar nenhum."

### Mostrar

O diagrama do cano de novo, agora com as tres etiquetas explicadas: lint (estilo), testes (comportamento), build (transformacao).

### Falar

"Quando a IA fala 'CI vermelho', 'pipeline falhou', 'teste quebrou', ela esta falando desse cano. Vermelho em qualquer etapa bloqueia o caminho. Alguem precisa ir la, ler o erro, consertar."

### Cena 3 — CD: publicar automaticamente (13:00-14:30)

### Falar

"CI para no 'pronto para deploy'. Quem publica? Em times modernos, outra parte do cano, chamada CD."

"CD significa Continuous Deployment, ou Continuous Delivery, dependendo de quem fala. O detalhe nao importa agora. O que importa: e a continuacao do cano. Depois que o CI da verde, o CD pega o codigo e publica no servidor, automaticamente."

"Ou seja: voce da um push, o cano roda sozinho, e se tudo verde, o codigo vai para o ar sem nenhum humano apertar botao."

"Em times mais conservadores, o CD para antes de publicar e espera um humano aprovar. Em times mais soltos, publica direto. Cada equipe escolhe o nivel de confianca."

### Mostrar

O diagrama do cano estendido: commit -> lint -> testes -> build -> [CD: publica no servidor]. Setinha final chegando no servidor.

### Cena 4 — Ambientes: onde o codigo mora em cada etapa (14:30-16:00)

### Falar

"O codigo nao vai direto para o ar. Ele passa por ambientes. Ambiente e um servidor, ou um conjunto de servidores, com um proposito."

"Quatro ambientes que voce vai encontrar."

"Local: e o seu computador. Voce escreve, roda, testa no seu. Ninguem mais ve."

"Dev: e um servidor compartilhado de teste. O time joga codigo la para ver funcionando junto. Quebra a vontade, tudo bem."

"Staging: e o ensaio. Uma copia o mais proxima possivel do ambiente real. Aqui nao se quebra a toa. Aqui se ensaia o deploy antes do show."

"Prod: e o ar. E o servidor que o usuario acessa. Aqui nao se mexe sem cuidado."

### Mostrar

Quatro caixas em linha: local, dev, staging, prod. Cada uma com uma cor. Local em cinza, dev em amarelo, staging em laranja, prod em vermelho (ou verde, se preferir "vivo"). Setinha mostrando o codigo subindo de uma para a outra.

### Falar

"O cano CI/CD costuma publicar em dev e em staging automaticamente. Publicar em prod e o passo que pede mais cuidado. As vezes automatico, as vezes com botao humano."

### Cena 5 — Estrategias de deploy (16:00-17:30)

### Falar

"Quando o codigo chega em prod, como ele entra? Tem varios jeitos. Voce nao precisa saber todos. Precisa conhecer tres."

"Primeiro: tudo-de-uma-vez. E o mais simples. Derruba a versao antiga, sobe a nova. O usuario pode perceber uma pausa, uma indisponibilidade de alguns segundos. Em sites pequenos, tudo bem. Em sites grandes, nao da."

"Segundo: blue-green. Voce sobe a versao nova em um servidor paralelo, ao lado da antiga. Testa. Quando tem confianca, troca o trafego de uma vez: todo mundo que chega agora vai para a nova. A antiga fica la, pronta para voltar se der problema."

"Terceiro: canary. Voce libera a versao nova para uma pequena parcela dos usuarios primeiro. Cinco por cento, dez por cento. Se nada quebra, vai aumentando ate cem. Se quebra, so poucos perceberam e voce volta rapido."

### Mostrar

Tres mini-diagramas lado a lado.

Tudo-de-uma-vez: uma caixa antiga some, outra nova aparece.

Blue-green: duas caixas lado a lado, uma seta de "troca" apontando para a nova.

Canary: uma caixa nova recebendo uma setinha pequena de trafego, e crescendo.

### Fechamento do ATO 2

Mostrar o cano completo: commit -> push -> CI (lint, testes, build) -> CD -> ambiente (dev/staging/prod) -> usuario. Dizer: "esse e o cano. Cada etapa tem um trabalho. Quando o usuario reclama que o site ta diferente, algo nesse cano acabou de chegar nele."

---

## ATO 3 — Quando algo da errado e o fechamento (17:30-24:00)

### Cena 1 — Rollback: voltar atras (17:30-19:00)

### Falar

"E quando o deploy publicou, o CI deu verde, tudo parecia bem, e mesmo assim o site quebra em prod? Acontece. Nem todo bug aparece no CI. Tem bug que so aparece com usuario de verdade, com dado de verdade, com volume de verdade."

"O primeiro movimento e voltar atras. Isso se chama rollback. Rollback e desfazer o deploy, colocar de volta a versao anterior, a que estava funcionando."

"Se voce deployou com blue-green, e facil: aponta o trafego de volta para o servidor antigo, que ainda esta la. Se deployou tudo-de-uma-vez, precisa re-deployar a versao anterior, e isso pode levar alguns minutos."

"Por isso blue-green e canary existem. Nao e so para evitar problemas. E para voltar rapido quando o problema acontece."

### Mostrar

Diagrama: versao nova no ar -> problema detectado -> seta de "rollback" -> versao antiga volta.

### Cena 2 — Incidente e post-mortem (19:00-20:30)

### Falar

"Quando algo da errado em prod e afeta o usuario, chamamos de incidente. Incidente nao e so um bug qualquer. E uma quebra com impacto real: gente nao consegue logar, nao consegue comprar, nao consegue acessar."

"Depois que o incidente foi controlado, o time senta e faz o que se chama post-mortem. Post-mortem e uma conversa estruturada depois do problema resolvido. Nao e para procurar culpado. E para entender o que aconteceu, por que aconteceu, e o que mudar para nao repetir."

"As perguntas classicas do post-mortem: o que aconteceu? Como detectamos? Como resolvemos? O que vamos mudar para evitar?"

### Falar

"Quando a IA sugerir um deploy grande, uma mudanca que mexe em varias camadas, pergunte: se isso der errado em prod, conseguimos voltar rapido? Tem rollback? Tem blue-green? A resposta diz o tamanho do risco."

### Cena 3 — O ciclo completo, resumido (20:30-22:00)

### Falar

"Vamos resumir o ciclo inteiro, do commit ate o usuario perceber."

"Voce escreve codigo no seu computador. Da um commit, que e a foto do codigo no tempo. Da um push, que manda essa foto para o repo na nuvem."

"O repo dispara o CI. O CI roda lint, testes e build. Se tudo verde, segue. Se algo vermelho, para."

"Depois do CI verde, o CD entra. Publica em dev, depois em staging. Em prod, publica com a estrategia escolhida: tudo-de-uma-vez, blue-green ou canary."

"O novo codigo esta no ar. O usuario acessa o site e percebe algo diferente: um botao novo, uma tela nova, uma correcao. Ele nao viu nenhum dos passos. So viu o resultado."

"Se o resultado esta bom, acabou. Se esta ruim, rollback, entender, consertar, deployar de novo."

### Mostrar

O diagrama do cano completo, agora em uma linha so, com todas as etapas e setas. Destacar que o usuario so enxerga a ultima ponta.

### Cena 4 — Fechamento da temporada: o mapa revisitado (22:00-24:00)

### Falar

"Esse video fecha a temporada. No episodio 01 eu desenhei um mapa com todas as camadas entre o codigo e o ar. Hoje, sete episodios depois, cada uma dessas camadas ja foi aberta."

Mostrar o mapa do episodio 01 na tela, completo.

"Vamos revisitar rapido."

Apontar para cada camada a medida que fala:

"Codigo, estado, variaveis. Isso mora no navegador. A gente abriu no episodio 02, front-end e estado."

"Request, response, API. Isso e a ponte entre navegador e servidor. Episodio 03."

"Banco de dados. A memoria de longo prazo. Episodio 04."

"Auth. Quem e voce, o que voce pode fazer. Episodio 05."

"Git. A rede de seguranca que te deixa voltar no tempo. Episodio 06."

"E hoje, build, CI/CD e deploy. O cano que leva o codigo ao ar."

"O mapa ficou inteiro. Quando a IA sugerir uma mudanca, voce ja sabe perguntar: em qual camada isso mora? A resposta diz o risco."

---

## ENCERRAMENTO (24:00-25:30)

### Na camera

"Essa foi a primeira temporada. Sete videos, do mapa ao profundo em cada camada."

"Se voce assistiu tudo, parabens. Voce saiu de 'a IA escreve e eu aprovo sem ler' para 'a IA escreve e eu sei em qual camada isso mora'. Isso muda tudo."

"Na descricao tem o glossario completo da temporada, com todos os termos dos sete videos. Repo publico [link] para consultar quando precisar."

"Se a serie te ajudou, tem dois jeitos de ajudar de volta. Inscreva-se, e comente qual camada voce quer ver na proxima temporada. O canal cresce com isso."

"Obrigado por assistir ate aqui. Te vejo na proxima."

### Call to action

- Inscreva-se
- Comente qual camada voce quer aprofundar na proxima temporada
- Repo com o glossario completo da temporada: [link]
