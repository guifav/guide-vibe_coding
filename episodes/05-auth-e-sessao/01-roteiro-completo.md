# Roteiro completo - Auth e Sessao

**Duracao alvo:** 15-20 min
**Formato:** Gui falando para camera, alternando com diagrama simples na tela
**Regra pedagogica:** cada termo técnico e traduzido em 1 frase antes de continuar. Nenhum termo fica sem tradução.

---

## ABERTURA (0:00-0:45)

### Na camera

"Você abre um site. Digita seu email e senha. Clica em entrar. E de repente o site te reconhece: mostra seu nome, seus arquivos, suas permissoes. Mas o que aconteceu entre o clique e o servidor saber quem e você?"

"Se você usa IA para programar, a IA vai sugerir bibliotecas de auth, vai falar em token, em sessao, em JWT. Mas para você confiar, para você saber quando ela esta certa e quando ela esta te colocando em risco, você precisa enxergar o que acontece por tras."

"Neste vídeo vou contar a história de um login, do visitante anônimo ate o logoff. Cada conceito aparece no momento em que ele se torna necessário."

### Mostrar

Diagrama do fluxo de auth (arquivo 02) com todas as etapas em cor clara. Só mostrar, sem explicar. Dizer: "esse mapa vai ganhando vida aos poucos. No fim você vai enxergar ele inteiro."

---

## ATO 1 - O problema e o login (0:45-5:30)

### Cena 1 - O mundo sem auth (0:45-2:00)

### Falar

"Imagina um servidor sem auth. Sem auth quer dizer: sem camada de controle de quem pede o que."

"Qualquer pessoa no mundo manda um request. Request e o pedido que o navegador faz para o servidor. E o servidor responde igual para todo mundo."

"Você pede a lista de usuarios? Entrega. Você pede o perfil de outra pessoa? Entrega. Você pede para apagar um dado que não e seu? Faz."

"Isso parece óbvio que e problema. Mas e exatamente o que acontece quando a auth e removida ou mal configurada. O servidor não discrimina. Ele obedece quem chega primeiro."

### Mostrar

No diagrama, um visitante anônimo (sem nome, sem cracha) mandando requests e o servidor respondendo tudo. Sem filtro.

### Falar

"O primeiro problema e privacidade. O segundo, maior, e que qualquer um pode alterar ou apagar dados dos outros. Um servidor sem auth e um servidor onde todo mundo e admin sem saber."

### Cena 2 - O que muda com o login (2:00-3:30)

### Falar

"A solucao comeca com login. Login e o momento em que você se identifica. Você diz quem e você e prova que e você, normalmente com uma senha."

"Depois do login, você deixa de ser visitante. Agora o servidor tem um nome para você. E a partir desse nome, ele pode tratar você diferente dos outros."

"Isso e a mudança fundamental. Antes do login, você e um estranho. Depois do login, você e alguém especifico, com um histórico, com permissoes, com dados que são seus."

### Mostrar

No diagrama, o visitante anônimo vira um usuario com nome. Aparece uma seta: login.

### Traduzir

- Visitante (guest): quem chega sem se identificar
- Usuario (user): quem fez login e tem um nome para o servidor
- Login: o ato de se identificar e provar quem e você

### Cena 3 - Senha e o que ela prova (3:30-4:30)

### Falar

"A senha e a prova de que você e quem diz ser para o servidor."

"Pense assim: o servidor já conhece você. Ele tem seu email e uma versao embaralhada da sua senha guardada. Quando você digita a senha no login, o servidor embaralha o que você digitou e compara. Se bate, e você."

"Termo que aparece aqui: hash. Hash e o embaralhamento que não tem volta. O servidor não guarda sua senha. Guarda o hash dela. Por isso ninguém, nem o dono do sistema, consegue te dizer sua senha. Só consegue gerar uma nova."

### Mostrar

Diagrama simples: senha digitada -> hash -> comparada com hash guardado. Se igual, login OK.

### Cena 4 - O que o servidor agora sabe sobre você (4:30-5:30)

### Falar

"Depois que o login da certo, o servidor sabe varias coisas sobre você. Ele sabe seu ID, seu nome, seu email, e crucialmente: ele sabe quais permissoes você tem."

"Permissoes significam: o que você pode fazer. Você pode ver? Pode editar? Pode apagar? Pode ver os dados dos outros?"

"Essa informação, de quem e você e o que você pode, e o que vamos carregar pelo resto do vídeo. Tudo a partir de agora e sobre como o servidor lembra disso entre um request e outro."

### Fechamento do ATO 1

Mostrar o mapa com as partes do ATO 1 destacadas: visitante, login, usuario, permissoes. Dizer: "agora o servidor sabe quem e você. Mas como ele vai lembrar disso no próximo request? Isso e o próximo ato."

---

## ATO 2 - Como o servidor lembra de você (5:30-11:00)

### Cena 1 - HTTP não tem memória (5:30-6:45)

### Falar

"Aqui chegamos no coração do problema. O protocolo que a web usa, o HTTP, não tem memória."

"Isso significa o seguinte: cada request e tratado como se fosse o primeiro. O servidor recebe o pedido, responde, e esquece de você. O próximo request, ele te trata como estranho de novo."

"Isso e loucura para um sistema com login. Você faz login, e no request seguinte o servidor já não sabe quem e você?"

### Mostrar

Dois requests seguidos. O servidor responde igual, sem ligar um ao outro. "Quem e você?" aparece nos dois.

### Falar

"E por isso que precisamos de um mecanismo de memória entre requests. Esse mecanismo tem dois nomes principais: sessao e token. Vamos nos dois."

### Cena 2 - Sessao: a memória no servidor (6:45-8:15)

### Falar

"Sessao e a memória que mora no servidor. Funciona assim: você faz login, o servidor cria uma sessao para você, guarda essa sessao na memória dele ou no banco, e te da um identificador dessa sessao."

"Esse identificador se chama session ID. Session ID e só um número ou texto longo que aponta para a sessao guardada no servidor."

"A partir dai, cada request seu carrega esse session ID. O servidor recebe o request, le o session ID, vai na memória dele, descobre que e você, e responde como se você tivesse acabado de fazer login."

### Mostrar

Diagrama: login -> servidor cria sessao (memória do servidor) -> devolve session ID -> request seguinte carrega session ID -> servidor consulta memória -> sabe quem e.

### Falar

"Termo que aparece muito: cookie. Cookie e um pedacinho de texto que o navegador guarda e envia junto com cada request para o mesmo site. E como o session ID viaja: o servidor da o cookie, o navegador guarda, e cada request leva o cookie de volta."

"Resumo da sessao: a memória mora no servidor. O navegador só carrega o identificador."

### Cena 3 - Token: o cracha que o cliente carrega (8:15-9:45)

### Falar

"Tem um outro modelo, mais moderno, chamado token. A diferença fundamental e onde a memória mora."

"No token, depois do login o servidor não guarda sessao nenhuma. Em vez disso, ele te da um cracha. Um texto longo, codificado, que carrega dentro dele a informação de quem e você."

"Esse cracha e o token. Você guarda no navegador, e cada request carrega esse token. O servidor recebe o token, le, e descobre quem e você sem precisar ir na memória dele."

### Mostrar

Diagrama: login -> servidor gera token (carrega dentro a identidade) -> token vai para o navegador -> request seguinte carrega token -> servidor le o token e sabe quem e.

### Traduzir

- Token: cracha que o servidor da depois do login; carrega dentro quem e você
- JWT (JSON Web Token): um formato especifico de token, muito comum, mas e só um formato

### Falar

"A analogia que fica: sessao e como um guarda-volumes. Você da seu casaco (sua identidade) pro servidor guardar, ele te da um bilhetinho com número. Cada vez que você volta, mostra o bilhetinho e ele te devolve o casaco."

"Token e como um cracha. O servidor te da o cracha na entrada, você carrega no pescoco, e cada mesa que você chega le o cracha e sabe quem e você. O servidor não guarda nada."

### Cena 4 - Sessao vs token: quando usar qual (9:45-11:00)

### Falar

"Não existe certo ou errado absoluto. Sessao e mais simples para o servidor controlar, porque ele pode invalidar quando quiser, só apagando da memória. Token e melhor quando você tem varios servidores, porque nenhum precisa guardar nada, só precisa saber ler o token."

"O que importa para você, que programa com IA: quando a IA falar em sessao, ela esta falando da memória no servidor. Quando falar em token ou JWT, ela esta falando do cracha que o cliente carrega."

"Os dois resolvem o mesmo problema: como o servidor lembra de você entre requests. Onde a memória mora e o que muda."

### Fechamento do ATO 2

Mostrar o mapa com login, sessao e token destacados.

"Agora o servidor sabe quem e você e lembra entre requests. Saber quem e você e só o começo. Falta a pergunta mais importante: o que você pode fazer? Isso e o próximo ato."

---

## ATO 3 - Quem pode o que (11:00-16:30)

### Cena 1 - Autenticação vs autorização (11:00-12:30)

### Falar

"Aqui esta a diferença que mais confunde. Autenticação e autorização são duas coisas diferentes, e confundir as duas e onde a maioria dos problemas comeca."

"Autenticação responde: quem e você? E o login. E a senha. E o token que prova identidade."

"Autorização responde: o que você pode fazer? E a pergunta que vem depois da autenticação."

"Exemplo: eu me logo, estou autenticado. Mas posso apagar a conta de outro usuario? Não. Estou autenticado, mas não autorizado a fazer aquilo."

### Mostrar

Duas setas separadas: autenticação (quem e você) -> autorização (o que pode fazer). Nunca confundir.

### Falar

"Autenticação sem autorização e perigoso: você sabe quem e, mas deixa fazer tudo. Autorização sem autenticação não faz sentido: como saber o que pode se não sabe quem e?"

"As duas juntas e o que chamamos de auth. Mas internamente são duas perguntas, duas camadas, dois lugares diferentes do código."

### Cena 2 - Permissoes por papel (role) (12:30-13:45)

### Falar

"Autorização se implementa de dois jeitos principais. O primeiro e por papel, em ingles role."

"Papel e um grupo com um conjunto de permissoes. Os papeis mais comuns são admin, user e guest."

"Admin pode tudo: ver, editar, apagar, gerenciar outros. User pode ver e editar o que e dele. Guest só pode ver o que e público."

"Quando o servidor recebe um request, depois de autenticar, ele pergunta: esse usuario e admin? Se sim, deixa apagar. Se for user, bloqueia."

### Mostrar

Tabela simples: admin | user | guest, com X e check para cada acao.

### Falar

"Termo que aparece aqui: RBAC, Role-Based Access Control. E só o nome chique para permissao por papel. Não se assuste com a sigla."

### Cena 3 - Permissoes por recurso (ownership) (13:45-14:45)

### Falar

"O segundo jeito e por recurso. Aqui a pergunta e só essa: esse item e seu?"

"Exemplo: você e user. Você pode editar seus proprios comentarios. Mas não pode editar o comentario de outro user, mesmo ele sendo user também."

"Aqui a permissao depende da relacao entre o usuario e o recurso. Esse artigo e seu? Essa conta e sua? Esse arquivo pertence a você?"

### Mostrar

Dois usuarios, cada um com seus itens. User A tenta editar item do user B. Bloqueado: "esse item não e seu".

### Falar

"Os dois modelos se combinam. Um admin pode editar tudo (por papel). Um user só pode editar o que e dele (por recurso). Essa combinacao e o que chamamos de autorização."

### Cena 4 - Por que mexer em auth e perigoso (14:45-15:45)

### Falar

"Aqui o ponto mais importante para quem programa com IA. Auth e a camada que mais sofre com sugestoes de 'simplificação'."

"A IA vai te dizer: 'para simplificar, vamos remover essa verificação de permissao'. Ou: 'vamos desativar o token temporariamente para testar'. Ou: 'esse middleware de auth esta bloqueando, vou comentar'."

"Cada uma dessas frases e um sinal de perigo. Quando você remove auth, você abre o servidor para o mundo. O que era protegido vira público. O que era restrito a você vira restrito a ninguém."

### Mostrar

Tela com um diff de código. Uma linha de verificação de permissao sendo removida. Destacar em vermelho.

### Falar

"A regra que fica: se a IA sugerir remover, comentar ou simplificar qualquer coisa que toca auth, pergunte antes de aceitar. Pergunte: 'o que para de ser verificado se eu remover isso?'. Se a resposta for 'nada' ou 'só um detalhe', desconfie."

"Auth e lugar de explicitar. Cada verificação que existe, existe porque sem ela alguém consegue fazer algo que não deve."

### Cena 5 - Logoff, expiracao, token roubado (15:45-16:30)

### Falar

"Tres coisas que podem dar errado depois do login."

"Primeiro: logoff. Logoff e o ato de encerrar a sessao ou invalidar o token. Se o servidor não trata logoff direito, o cracha continua valendo mesmo depois de você sair."

"Segundo: expiracao. Token e sessao tem prazo de validade. Se não expira, vale para sempre. Um cracha que não expira e um risco: se alguém roubar, usa para sempre."

"Terceiro: token roubado. Se alguém intercepta seu token ou seu session ID, essa pessoa se passa por você. O servidor le o cracha e obedece como se fosse você."

### Mostrar

Tres cenas rapidas: logoff (cracha destruido), expiracao (cracha com data riscada), roubo (cracha copiado por outra pessoa).

### Falar

"E por isso que auth tem que ser pensada como um ciclo, não só como o login. Login e o começo. Logoff e expiracao são o fim. E entre os dois, tudo que carrega o cracha e vulneravel se o cracha cair na mao errada."

### Fechamento do ATO 3

Mostrar o mapa completo: visitante, login, usuario, sessao, token, autenticação, autorização, permissoes, logoff, expiracao.

"Essa e a história. Um estranho bate na porta do servidor, vira um usuario com permissoes, carrega um cracha, ate o logoff. Cada conceito responde uma pergunta especifica."

---

## ENCERRAMENTO (16:30-18:00)

### Na camera

"Para programar com IA sem ser enganado, você precisa saber a diferença entre as duas perguntas que auth responde: quem e você, e o que você pode fazer."

"Quando a IA sugerir uma mudança em código de auth, pergunte: isso mexe em autenticação ou autorização? Se for autenticação, o que para de ser verificado? Se for autorização, quem passa a conseguir fazer o que antes não conseguia?"

"Se você não souber responder, não aceite a mudança. Pergunte para a IA: 'que pergunta essa verificação responde?'. A resposta te diz o tamanho do risco."

"Na descrição tem o glossario com todos os termos que apareceram. Repo público [link] para consultar depois."

"Ponte para o próximo episodio: antes de mexer em auth com seguranca, você precisa de uma rede de protecao. Um jeito de voltar atras se algo quebrar. Isso se chama git, e e o topico do próximo vídeo."

### Call to action

- Inscreva-se para a série
- Comente qual parte de auth mais te confundia antes desse vídeo
- Repo com o glossario: [link]
