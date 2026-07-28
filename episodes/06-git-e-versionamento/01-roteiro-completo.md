# Roteiro completo - Git e Versionamento

**Duracao alvo:** 15-20 min
**Formato:** Gui falando para camera, alternando com diagrama simples na tela
**Regra pedagogica:** cada termo técnico e traduzido em 1 frase antes de continuar. Nenhum termo fica sem tradução.

---

## ABERTURA (0:00-0:45)

### Na camera

"Você mudou 500 linhas de código. Quebrou algo. Como volta? Copia e cola em outro arquivo? Salva versao 1, versao 2, versao final final v2?"

"Se você usa IA para programar, a IA escreve e reescreve sem parar. Cada iteracao pode ter quebrado algo que funcionava. Sem rede de seguranca, você esta andando na corda bamba sem rede."

"Neste vídeo vou contar a história do versionamento: por que ele existe, como funciona, e por que o deploy nunca usa o código do seu computador."

### Mostrar

Diagrama de uma linha do tempo com pontos (commits) e um ramal (branch) saindo dela. Só mostrar, sem explicar. Dizer: "essa rede de seguranca vai ganhando forma aos poucos. No fim você vai enxergar ela inteira."

---

## ATO 1 - O problema e a foto (0:45-5:30)

### Cena 1 - O problema: como volta no tempo? (0:45-2:00)

### Falar

"Antes do git existir, o jeito de versionar código era manual. Você terminava um dia de trabalho, copiava a pasta inteira, e renomeava para algo como 'projeto_final_v3_agora_vai'."

"Funciona para um arquivo. Para um projeto inteiro, vira um caos. Você não lembra o que mudou entre a versao 2 e a versao 3. Você apaga sem querer uma versao boa achando que era a velha. E quando algo quebra, você não faz ideia de quando quebrou."

"O problema e saber, para cada mudança, o que mudou, quem mudou, quando, e por que."

### Mostrar

Uma pasta com varios arquivos nomeados caoticamente: `app.js`, `app_v2.js`, `app_final.js`, `app_final_agora_vai.js`, `app_velho_nao_apagar.js`.

### Falar

"Git e o sistema de versionamento. Ele resolve esse problema de forma automatica. Em vez de copiar pastas, ele tira fotos do seu código em momentos especificos."

### Cena 2 - O commit: a foto do código (2:00-3:15)

### Falar

"A foto se chama commit. Commit e o ato de dizer para o git: salva o estado do código agora, nesse momento."

"Pense no commit como uma foto polaroid do seu código. Ele registra exatamente como estavam todos os arquivos naquele instante."

"Cada commit tem quatro coisas. Mensagem: o que mudou, escrito por você. Autor: quem tirou a foto. Data: quando. E um identificador único, tipo um número de série."

"E tem uma coisa importante: commit e imutavel. Depois que a foto foi tirada, ela não muda. Ficou ruim? Você tira uma foto nova por cima, e a antiga continua la no album."

### Mostrar

Um `git log` simples na tela, mostrando commits como pontos numa linha do tempo. Cada um com mensagem curta, autor, data.

### Traduzir

- Commit: a foto do código em um momento especifico
- Mensagem: o que mudou, escrito em uma frase
- Imutavel: depois de tirada, a foto não muda

### Cena 3 - O repository: onde as fotos ficam (3:15-4:30)

### Falar

"Essas fotos precisam de um lugar para ficar guardadas. Esse lugar e o repository, ou repo."

"O repo e o album de fotos do seu código. Ele guarda todos os commits, em ordem, formando a linha do tempo do projeto."

"O repo pode morar só no seu computador. Mas na prática ele também vive na nuvem: a mesma ideia de album de fotos, hospedado em um servidor que o time inteiro consegue acessar. Essa copia na nuvem se chama repo remoto."

"Existem varias plataformas que hospedam repos na nuvem. Você já viu os nomes por ai. Não importa qual: o conceito e o mesmo, um repo e onde as fotos do código moram."

### Mostrar

No diagrama, o repo aparece como uma caixa com varios commits dentro, em ordem. Setinha: o código viaja do computador para o repo.

### Cena 4 - Por que isso já muda tudo (4:30-5:30)

### Falar

"Só com commit e repo, você já tem a rede de seguranca básica. Quebrou algo? Volta para a foto anterior. Quer saber o que mudou? Compara duas fotos. Quer saber quem fez aquela mudança estranha? Olha o autor e a data."

"Isso já resolve 80% do problema. Mas tem uma coisa que ainda não resolve: e se você quer testar algo arriscado sem estragar a linha principal?"

### Fechamento do ATO 1

Mostrar o mapa com as partes do ATO 1 destacadas: commit, repo, linha do tempo. Dizer: "isso e a rede de seguranca básica. Mas projetos reais precisam de mais uma coisa: trabalhar em paralelo sem se atrapalhar."

---

## ATO 2 - Trabalhando em paralelo (5:30-11:30)

### Cena 1 - O medo de estragar o original (5:30-6:45)

### Falar

"Imagina que seu projeto esta funcionando. Linha do tempo limpa, tudo no ar. Você quer adicionar uma funcionalidade nova, mas não tem certeza se vai funcionar. Se você mexe direto na linha principal e quebra, quebrou para todo mundo."

"A solucao intuitiva seria: copia o projeto inteiro, mexe na copia, e se ficar bom, junta de volta. Exatamente isso. Só que com git, e automatico."

"Isso se chama branch. Branch e uma linha paralela na linha do tempo. Você cria uma branch, mexe nela, e a linha principal fica intocada enquanto você experimenta."

### Mostrar

No diagrama, a linha principal (main) e uma linha secundaria (branch) saindo dela, como um ramal de estrada.

### Traduzir

- Branch: linha paralela para mexer sem estragar o original
- Main: a linha principal, a versao que esta no ar

### Cena 2 - Main e branches: a linha principal (6:45-7:45)

### Falar

"A linha principal tem um nome especial: main. Antigamente se chamava master, você ainda vai ver esse nome por ai. Hoje o padrao e main."

"Main e a versao oficial do projeto. E o que esta em produção, e o que o deploy usa. Em time, na maioria dos projetos serios, ninguém mexe direto na main."

"O fluxo e: você cria uma branch a partir da main, faz seus commits nessa branch, e a main continua limpa, intacta, enquanto você trabalha."

"Uma branch e um ponteiro com nome. Criar branch não copia o projeto: e só um ponteiro novo apontando para uma foto que ja existe. Por isso e instantaneo e não duplica nada."

### Mostrar

Diagrama: main no centro, com varias branches saindo dela, cada uma com seu nome (feature-login, fix-bug-123, experimento-novo-layout).

### Cena 3 - Merge: juntar de volta (7:45-9:00)

### Falar

"Quando você termina de mexer na branch e o código ficou bom, hora de juntar de volta na main. Isso se chama merge."

"Merge e o ato de pegar a linha paralela e trazer as mudanças para a linha principal. Depois do merge, a main tem tudo que estava na branch."

"Pense no merge como uma confluencia de rios. Dois rios se encontram e viram um só. A branch entrega suas mudanças para a main."

"Merge pode ser simples ou complicado. Simples quando a branch só adicionou coisas novas, sem tocar no que já existia. Complicado quando... bem, e o próximo topico."

### Mostrar

No diagrama, a branch encontra a main e some, virando parte dela. Setinha indicando o ponto de merge.

### Cena 4 - Conflito: quando duas pessoas mexem no mesmo lugar (9:00-11:30)

### Falar

"O problema classico do versionamento. Você e outra pessoa estão mexendo no projeto ao mesmo tempo. Cada um na sua branch. Voces dois mexem no mesmo arquivo, na mesma parte."

"O git tenta juntar automaticamente. Se as mudanças são em lugares diferentes do arquivo, ele consegue. Se as mudanças são no mesmo lugar, na mesma linha, ele não decide sozinho. Isso e um conflito."

"Conflito e quando o git não sabe qual versao manter. Ele para, marca o arquivo com uns simbolos, e diz: resolve na mao."

### Mostrar

Um arquivo com marcadores de conflito: `<<<<<<<`, `=======`, `>>>>>>>`. Mostrando as duas versoes lado a lado dentro do arquivo.

### Falar

"Resolver conflito e manual. Você abre o arquivo, le as duas versoes, decide qual manter (ou junta as duas), apaga as marcas, e segue. Não tem atalho automatico confiavel."

"Por isso que comunicação no time importa. Se duas pessoas vao mexer no mesmo arquivo, combinem antes. Conflito bem resolvido e coisa de humano."

"Quando a IA sugerir um merge e falar 'conflito', preste atencao. Não aceite resolvido sem você olhar. Conflito mal resolvido e uma das formas mais comuns de introduzir bug silencioso."

### Fechamento do ATO 2

Mostrar o mapa com branch, main, merge e conflito destacados.

"Branch para experimentar sem estragar. Merge para juntar. Conflito quando duas pessoas pisam no mesmo lugar. Mas ainda falta uma coisa: em projetos serios, não se faz merge direto. Existe um portao no meio."

---

## ATO 3 - O fluxo profissional (11:30-16:30)

### Cena 1 - Pull request: o pedido formal (11:30-13:00)

### Falar

"Em um projeto profissional em time, você não faz merge direto na main. Você abre um pedido formal para alguém revisar antes. Esse pedido se chama pull request, ou PR."

"PR e exatamente isso: um pedido. Você diz 'tenho uma branch pronta, olha aqui o que mudei, posso juntar na main?'."

"O PR não e só um pedido. E uma sala de revisão. Dentro dele você ve todos os commits da branch, a diferença entre a branch e a main linha por linha, e as pessoas podem comentar."

### Mostrar

Interface de um PR na plataforma de repositório: título, descrição, lista de arquivos modificados, diff (diferença) de cada arquivo, área de comentarios.

### Traduzir

- Pull request (PR): pedido formal de merge, com revisão
- Review: o ato de alguém olhar o PR antes de aprovar
- Diff: a diferença entre a branch e a main, linha por linha

### Cena 2 - Review: por que existe esse portao (13:00-14:00)

### Falar

"Por que o PR existe? Por que código sem revisão e perigoso. Mesmo que você seja excelente, um segundo par de olhos pega coisas que você não pegou."

"Review e o ato de alguém olhar seu código antes de aprovar. Essa pessoa le o diff, pergunta 'por que você fez assim?', sugere melhorias, aponta riscos."

"Só depois que o review passa, o merge acontece. O PR e o portao entre 'eu fiz' e 'isso esta na main'."

"Em muitos projetos open source serios, todo código entra por PR: nem o criador do projeto joga direto na main. E cultura."

### Falar

"Quando a IA sugerir 'faz o merge direto' ou 'commits na main', pergunte. Em projeto serio isso não acontece. PR existe por um motivo."

### Cena 3 - O fluxo completo (14:00-15:15)

### Falar

"Vou juntar tudo no fluxo completo. Esse e o coração do vídeo. Presta atencao."

"Passo 1: você cria uma branch nova a partir da main. Da um nome que descreve o que você vai fazer: feature-login, fix-bug-123."

"Passo 2: você mexe no código, tira commits na branch. Cada commit com mensagem clara do que mudou."

"Passo 3: você faz push. Push e mandar a branch da máquina para o repo remoto. Agora ela não só existe no seu computador, existe na nuvem, visivel para o time."

"Passo 4: você abre um pull request. O repo monta o diff automatico, você escreve o que fez e por que."

"Passo 5: alguém revisa. Comenta, pede ajuste, ou aprova."

"Passo 6: merge. A branch entra na main. A linha principal agora tem seu código."

### Mostrar

Diagrama do fluxo completo, como uma esteira:
```
branch nova -> commit -> push -> PR -> review -> merge
```

### Traduzir

- Push: mandar a branch do computador para o repo na nuvem
- Branch nova: linha paralela com nome descritivo
- Merge: a branch entra oficialmente na main

### Cena 4 - Por que o deploy usa o repo, não seu computador (15:15-16:30)

### Falar

"Lembra do episodio 01? O deploy não pega o código do seu computador. Ele pega o código que esta no repo. Vou explicar por que."

"Seu computador e só de você. Se o deploy dependesse dele, o site cairia toda vez que você desligasse. E ninguém mais do time conseguiria mexer."

"O repo e a linha do tempo única do projeto. Ele e o ponto de verdade. Quando o deploy roda, ele pega a main do repo, não o que esta na sua máquina."

"Por isso que push e obrigatório. Enquanto o código só esta no seu computador, para o resto do mundo ele não existe. Só depois do push, do PR, e do merge e que o código realmente chega na main e pode ir para o ar."

"Isso também e o que torna o projeto colaborativo. Dez pessoas podem estar em dez branches ao mesmo tempo, cada uma mexendo no seu canto. Todas convergem no repo, na main, na linha do tempo única."

### Fechamento do ATO 3

Mostrar o mapa completo, agora com todas as partes: commit, repo, branch, main, merge, conflito, PR, review, push, fluxo completo, repo como ponto de verdade.

"Essa e a rede de seguranca. O fluxo profissional inteiro existe para que código novo chegue na main de forma controlada, revisada, sem surpresa."

---

## ENCERRAMENTO (16:30-18:00)

### Na camera

"Para programar com IA sem se afogar, você não precisa saber todos os comandos git. Precisa saber que existe uma rede de seguranca, e que qualquer projeto serio passa por ela."

"Quando a IA sugerir uma mudança, pergunte: isso vai entrar por PR ou direto na main? Se for direto na main, em projeto serio, pergunte por que."

"Quando ela falar em commit, em branch, em merge, em conflito, em push, você agora sabe o que cada um e. Não e jargao misterioso. E uma rede de fotos no tempo, com ramais e um portao de revisão."

"Na descrição tem o glossario com todos os termos que apareceram. Repo público [link] para consultar depois."

"O próximo vídeo da série vai ser sobre o que acontece depois do merge. A main atualizou, mas como que isso vira site no ar? Esse e o topico do episodio 07."

### Call to action

- Inscreva-se para a série
- Comente qual parte do fluxo você quer aprofundar
- Repo com o glossario: [link]
