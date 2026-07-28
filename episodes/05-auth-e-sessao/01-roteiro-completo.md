# Roteiro completo — Auth e Sessao

**Duracao alvo:** 15-20 min
**Formato:** Gui falando para camera, alternando com diagrama simples na tela
**Regra pedagogica:** cada termo tecnico e traduzido em 1 frase antes de continuar. Nenhum termo fica sem traducao.

---

## ABERTURA (0:00-0:45)

### Na camera

"Voce abre um site. Digita seu email e senha. Clica em entrar. E de repente o site te reconhece: mostra seu nome, seus arquivos, suas permissoes. Mas o que aconteceu entre o clique e o servidor saber quem e voce?"

"Se voce usa IA para programar, a IA vai sugerir bibliotecas de auth, vai falar em token, em sessao, em JWT. Mas para voce confiar, para voce saber quando ela esta certa e quando ela esta te colocando em risco, voce precisa enxergar o que acontece por tras."

"Neste video nao vou ensinar a implementar auth. Vou contar a historia de um login, do visitante anonimo ate o logoff. Cada conceito aparece no momento em que ele se torna necessario."

### Mostrar

Diagrama do fluxo de auth (arquivo 02) com todas as etapas em cor clara. So mostrar, sem explicar. Dizer: "esse mapa vai ganhando vida aos poucos. No fim voce vai enxergar ele inteiro."

---

## ATO 1 — O problema e o login (0:45-5:30)

### Cena 1 — O mundo sem auth (0:45-2:00)

### Falar

"Imagina um servidor sem auth. Sem auth quer dizer: sem camada de controle de quem pede o que."

"Qualquer pessoa no mundo manda um request. Request e o pedido que o navegador faz para o servidor. E o servidor responde igual para todo mundo."

"Voce pede a lista de usuarios? Entrega. Voce pede o perfil de outra pessoa? Entrega. Voce pede para apagar um dado que nao e seu? Faz."

"Isso parece obvio que e problema. Mas e exatamente o que acontece quando a auth e removida ou mal configurada. O servidor nao discrimina. Ele obedece quem chega primeiro."

### Mostrar

No diagrama, um visitante anonimo (sem nome, sem cracha) mandando requests e o servidor respondendo tudo. Sem filtro.

### Falar

"O primeiro problema e privacidade. O segundo, maior, e que qualquer um pode alterar ou apagar dados dos outros. Um servidor sem auth e um servidor onde todo mundo e admin sem saber."

### Cena 2 — O que muda com o login (2:00-3:30)

### Falar

"A solucao comeca com login. Login e o momento em que voce se identifica. Voce diz quem e voce e prova que e voce, normalmente com uma senha."

"Depois do login, voce deixa de ser visitante. Agora o servidor tem um nome para voce. E a partir desse nome, ele pode tratar voce diferente dos outros."

"Isso e a mudanca fundamental. Antes do login, voce e um estranho. Depois do login, voce e alguem especifico, com um historico, com permissoes, com dados que sao seus."

### Mostrar

No diagrama, o visitante anonimo vira um usuario com nome. Aparece uma seta: login.

### Traduzir

- Visitante (guest): quem chega sem se identificar
- Usuario (user): quem fez login e tem um nome para o servidor
- Login: o ato de se identificar e provar quem e voce

### Cena 3 — Senha e o que ela prova (3:30-4:30)

### Falar

"A senha nao e segredo para o servidor por ser segredo. Ela e a prova de que voce e quem diz ser."

"Pense assim: o servidor ja conhece voce. Ele tem seu email e uma versao embaralhada da sua senha guardada. Quando voce digita a senha no login, o servidor embaralha o que voce digitou e compara. Se bate, e voce."

"Termo que aparece aqui: hash. Hash e o embaralhamento que nao tem volta. O servidor nao guarda sua senha. Guarda o hash dela. Por isso ninguem, nem o dono do sistema, consegue te dizer sua senha. So consegue gerar uma nova."

### Mostrar

Diagrama simples: senha digitada -> hash -> comparada com hash guardado. Se igual, login OK.

### Cena 4 — O que o servidor agora sabe sobre voce (4:30-5:30)

### Falar

"Depois que o login da certo, o servidor sabe varias coisas sobre voce. Ele sabe seu ID, seu nome, seu email, e crucialmente: ele sabe quais permissoes voce tem."

"Permissoes significam: o que voce pode fazer. Voce pode ver? Pode editar? Pode apagar? Pode ver os dados dos outros?"

"Essa informacao, de quem e voce e o que voce pode, e o que vamos carregar pelo resto do video. Tudo a partir de agora e sobre como o servidor lembra disso entre um request e outro."

### Fechamento do ATO 1

Mostrar o mapa com as partes do ATO 1 destacadas: visitante, login, usuario, permissoes. Dizer: "agora o servidor sabe quem e voce. Mas como ele vai lembrar disso no proximo request? Isso e o proximo ato."

---

## ATO 2 — Como o servidor lembra de voce (5:30-11:00)

### Cena 1 — HTTP nao tem memoria (5:30-6:45)

### Falar

"Aqui chegamos no coracao do problema. O protocolo que a web usa, o HTTP, nao tem memoria."

"Isso significa o seguinte: cada request e tratado como se fosse o primeiro. O servidor recebe o pedido, responde, e esquece de voce. O proximo request, ele te trata como estranho de novo."

"Isso e loucura para um sistema com login. Voce faz login, e no request seguinte o servidor ja nao sabe quem e voce?"

### Mostrar

Dois requests seguidos. O servidor responde igual, sem ligar um ao outro. "Quem e voce?" aparece nos dois.

### Falar

"E por isso que precisamos de um mecanismo de memoria entre requests. Esse mecanismo tem dois nomes principais: sessao e token. Vamos nos dois."

### Cena 2 — Sessao: a memoria no servidor (6:45-8:15)

### Falar

"Sessao e a memoria que mora no servidor. Funciona assim: voce faz login, o servidor cria uma sessao para voce, guarda essa sessao na memoria dele ou no banco, e te da um identificador dessa sessao."

"Esse identificador se chama session ID. Session ID e so um numero ou texto longo que aponta para a sessao guardada no servidor."

"A partir dai, cada request seu carrega esse session ID. O servidor recebe o request, le o session ID, vai na memoria dele, descobre que e voce, e responde como se voce tivesse acabado de fazer login."

### Mostrar

Diagrama: login -> servidor cria sessao (memoria do servidor) -> devolve session ID -> request seguinte carrega session ID -> servidor consulta memoria -> sabe quem e.

### Falar

"Termo que aparece muito: cookie. Cookie e um pedacinho de texto que o navegador guarda e envia junto com cada request para o mesmo site. E como o session ID viaja: o servidor da o cookie, o navegador guarda, e cada request leva o cookie de volta."

"Resumo da sessao: a memoria mora no servidor. O navegador so carrega o identificador."

### Cena 3 — Token: o cracha que o cliente carrega (8:15-9:45)

### Falar

"Tem um outro modelo, mais moderno, chamado token. A diferenca fundamental e onde a memoria mora."

"No token, depois do login o servidor nao guarda sessao nenhuma. Em vez disso, ele te da um cracha. Um texto longo, codificado, que carrega dentro dele a informacao de quem e voce."

"Esse cracha e o token. Voce guarda no navegador, e cada request carrega esse token. O servidor recebe o token, le, e descobre quem e voce sem precisar ir na memoria dele."

### Mostrar

Diagrama: login -> servidor gera token (carrega dentro a identidade) -> token vai para o navegador -> request seguinte carrega token -> servidor le o token e sabe quem e.

### Traduzir

- Token: cracha que o servidor da depois do login; carrega dentro quem e voce
- JWT (JSON Web Token): um formato especifico de token, muito comum, mas e so um formato

### Falar

"A analogia que fica: sessao e como um guarda-volumes. Voce da seu casaco (sua identidade) pro servidor guardar, ele te da um bilhetinho com numero. Cada vez que voce volta, mostra o bilhetinho e ele te devolve o casaco."

"Token e como um cracha. O servidor te da o cracha na entrada, voce carrega no pescoco, e cada mesa que voce chega le o cracha e sabe quem e voce. O servidor nao guarda nada."

### Cena 4 — Sessao vs token: quando usar qual (9:45-11:00)

### Falar

"Nao existe certo ou errado absoluto. Sessao e mais simples para o servidor controlar, porque ele pode invalidar quando quiser, so apagando da memoria. Token e melhor quando voce tem varios servidores, porque nenhum precisa guardar nada, so precisa saber ler o token."

"O que importa para voce, que programa com IA: quando a IA falar em sessao, ela esta falando da memoria no servidor. Quando falar em token ou JWT, ela esta falando do cracha que o cliente carrega."

"Os dois resolvem o mesmo problema: como o servidor lembra de voce entre requests. Onde a memoria mora e o que muda."

### Fechamento do ATO 2

Mostrar o mapa com login, sessao e token destacados.

"Agora o servidor sabe quem e voce e lembra entre requests. Mas saber quem e voce nao e suficiente. Falta a pergunta mais importante: o que voce pode fazer? Isso e o proximo ato."

---

## ATO 3 — Quem pode o que (11:00-16:30)

### Cena 1 — Autenticacao vs autorizacao (11:00-12:30)

### Falar

"Aqui esta a diferenca que mais confunde. Autenticacao e autorizacao sao duas coisas diferentes, e confundir as duas e onde a maioria dos problemas comeca."

"Autenticacao responde: quem e voce? E o login. E a senha. E o token que prova identidade."

"Autorizacao responde: o que voce pode fazer? E a pergunta que vem depois da autenticacao."

"Exemplo: eu me logo, estou autenticado. Mas posso apagar a conta de outro usuario? Nao. Estou autenticado, mas nao autorizado a fazer aquilo."

### Mostrar

Duas setas separadas: autenticacao (quem e voce) -> autorizacao (o que pode fazer). Nunca confundir.

### Falar

"Autenticacao sem autorizacao e perigoso: voce sabe quem e, mas deixa fazer tudo. Autorizacao sem autenticacao nao faz sentido: como saber o que pode se nao sabe quem e?"

"As duas juntas e o que chamamos de auth. Mas internamente sao duas perguntas, duas camadas, dois lugares diferentes do codigo."

### Cena 2 — Permissoes por papel (role) (12:30-13:45)

### Falar

"Autorizacao se implementa de dois jeitos principais. O primeiro e por papel, em ingles role."

"Papel e um grupo com um conjunto de permissoes. Os papeis mais comuns sao admin, user e guest."

"Admin pode tudo: ver, editar, apagar, gerenciar outros. User pode ver e editar o que e dele. Guest so pode ver o que e publico."

"Quando o servidor recebe um request, depois de autenticar, ele pergunta: esse usuario e admin? Se sim, deixa apagar. Se for user, bloqueia."

### Mostrar

Tabela simples: admin | user | guest, com X e check para cada acao.

### Falar

"Termo que aparece aqui: RBAC, Role-Based Access Control. E so o nome chique para permissao por papel. Nao se assuste com a sigla."

### Cena 3 — Permissoes por recurso (ownership) (13:45-14:45)

### Falar

"O segundo jeito e por recurso. Aqui a pergunta nao e qual e seu papel, e sim: esse item e seu?"

"Exemplo: voce e user. Voce pode editar seus proprios comentarios. Mas nao pode editar o comentario de outro user, mesmo ele sendo user tambem."

"Aqui a permissao depende da relacao entre o usuario e o recurso. Esse artigo e seu? Essa conta e sua? Esse arquivo pertence a voce?"

### Mostrar

Dois usuarios, cada um com seus itens. User A tenta editar item do user B. Bloqueado: "esse item nao e seu".

### Falar

"Os dois modelos se combinam. Um admin pode editar tudo (por papel). Um user so pode editar o que e dele (por recurso). Essa combinacao e o que chamamos de autorizacao."

### Cena 4 — Por que mexer em auth e perigoso (14:45-15:45)

### Falar

"Aqui o ponto mais importante para quem programa com IA. Auth e a camada que mais sofre com sugestoes de 'simplificacao'."

"A IA vai te dizer: 'para simplificar, vamos remover essa verificacao de permissao'. Ou: 'vamos desativar o token temporariamente para testar'. Ou: 'esse middleware de auth esta bloqueando, vou comentar'."

"Cada uma dessas frases e um sinal de perigo. Quando voce remove auth, voce abre o servidor para o mundo. O que era protegido vira publico. O que era restrito a voce vira restrito a ninguem."

### Mostrar

Tela com um diff de codigo. Uma linha de verificacao de permissao sendo removida. Destacar em vermelho.

### Falar

"A regra que fica: se a IA sugerir remover, comentar ou simplificar qualquer coisa que toca auth, pergunte antes de aceitar. Pergunte: 'o que para de ser verificado se eu remover isso?'. Se a resposta for 'nada' ou 'so um detalhe', desconfie."

"Auth nao e lugar de simplificacao. E lugar de explicitar. Cada verificacao que existe, existe porque sem ela alguem consegue fazer algo que nao deve."

### Cena 5 — Logoff, expiracao, token roubado (15:45-16:30)

### Falar

"Tres coisas que podem dar errado depois do login."

"Primeiro: logoff. Logoff e o ato de encerrar a sessao ou invalidar o token. Se o servidor nao trata logoff direito, o cracha continua valendo mesmo depois de voce sair."

"Segundo: expiracao. Token e sessao tem prazo de validade. Se nao expira, vale para sempre. Um cracha que nao expira e um risco: se alguem roubar, usa para sempre."

"Terceiro: token roubado. Se alguem intercepta seu token ou seu session ID, essa pessoa se passa por voce. O servidor nao sabe que nao e voce. Ele le o cracha e obedece."

### Mostrar

Tres cenas rapidas: logoff (cracha destruido), expiracao (cracha com data riscada), roubo (cracha copiado por outra pessoa).

### Falar

"E por isso que auth tem que ser pensada como um ciclo, nao so como o login. Login e o comeco. Logoff e expiracao sao o fim. E entre os dois, tudo que carrega o cracha e vulneravel se o cracha cair na mao errada."

### Fechamento do ATO 3

Mostrar o mapa completo: visitante, login, usuario, sessao, token, autenticacao, autorizacao, permissoes, logoff, expiracao.

"Essa e a historia. De um estranho batendo na porta do servidor ate um usuario com permissoes, carregando um cracha, ate o logoff. Cada conceito responde uma pergunta especifica."

---

## ENCERRAMENTO (16:30-18:00)

### Na camera

"Para programar com IA sem ser enganado, voce precisa saber a diferenca entre as duas perguntas que auth responde: quem e voce, e o que voce pode fazer."

"Quando a IA sugerir uma mudanca em codigo de auth, pergunte: isso mexe em autenticacao ou autorizacao? Se for autenticacao, o que para de ser verificado? Se for autorizacao, quem passa a conseguir fazer o que antes nao conseguia?"

"Se voce nao souber responder, nao aceite a mudanca. Pergunte para a IA: 'que pergunta essa verificacao responde?'. A resposta te diz o tamanho do risco."

"Na descricao tem o glossario com todos os termos que apareceram. Repo publico [link] para consultar depois."

"Ponte para o proximo episodio: antes de mexer em auth com seguranca, voce precisa de uma rede de protecao. Um jeito de voltar atras se algo quebrar. Isso se chama git, e e o topico do proximo video."

### Call to action

- Inscreva-se para a serie
- Comente qual parte de auth mais te confundia antes desse video
- Repo com o glossario: [link]
