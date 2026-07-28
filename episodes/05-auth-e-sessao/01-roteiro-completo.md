# Roteiro completo - Auth e Sessão

**Duração alvo:** 15-20 min
**Formato:** Gui falando para câmera, alternando com diagrama simples na tela
**Regra pedagógica:** cada termo técnico é traduzido em 1 frase antes de continuar. Nenhum termo fica sem tradução.

---

## ABERTURA (0:00-0:45)

### Na câmera

"Você abre um site. Digita seu email e senha. Clica em entrar. E de repente o site te reconhece: mostra seu nome, seus arquivos, suas permissões. Mas o que aconteceu entre o clique e o servidor saber quem é você?"

"Se você usa IA para programar, a IA vai sugerir bibliotecas de auth, vai falar em token, em sessão, em JWT. Mas para você confiar, para você saber quando ela está certa e quando ela está te colocando em risco, você precisa enxergar o que acontece por trás."

"Se você viu o episódio 03, lembra do 401 e do 403 na tabela de status codes. Hoje você vê de onde os dois nascem."

"Neste vídeo vou contar a história de um login, do visitante anônimo até o logoff. Cada conceito aparece no momento em que ele se torna necessário."

### Mostrar

Diagrama do fluxo de auth (arquivo 02) com todas as etapas em cor clara. Só mostrar, sem explicar. Dizer: "a gente vai acender uma etapa por vez, do visitante anônimo até o logoff."

---

## ATO 1 - O problema e o login (0:45-5:30)

### Cena 1 - O mundo sem auth (0:45-2:00)

### Falar

"Imagina um servidor sem auth. Sem auth quer dizer: sem camada de controle de quem pede o que."

"Qualquer pessoa no mundo manda um request. Request é o pedido que o navegador faz para o servidor. E o servidor responde igual para todo mundo."

"Você pede a lista de usuários? Entrega. Você pede o perfil de outra pessoa? Entrega. Você pede para apagar um dado que não é seu? Faz."

"Isso parece óbvio que é problema. Mas é exatamente o que acontece quando a auth é removida ou mal configurada. O servidor não discrimina. Ele obedece quem chega primeiro."

### Mostrar

No diagrama, um visitante anônimo (sem nome, sem crachá) mandando requests e o servidor respondendo tudo. Sem filtro.

### Falar

"O primeiro problema é privacidade. O segundo, maior, é que qualquer um pode alterar ou apagar dados dos outros. Um servidor sem auth é um servidor onde todo mundo é admin sem saber."

### Cena 2 - O que muda com o login (2:00-3:30)

### Falar

"A solução começa com login. Login é o momento em que você se identifica. Você diz quem é você e prova que é você, normalmente com uma senha."

"Depois do login, você deixa de ser visitante. Agora o servidor tem um nome para você. E a partir desse nome, ele pode tratar você diferente dos outros."

"Isso é a mudança fundamental. Antes do login, você é um estranho. Depois do login, você é alguém específico, com um histórico, com permissões, com dados que são seus."

### Mostrar

No diagrama, o visitante anônimo vira um usuário com nome. Aparece uma seta: login.

### Traduzir

- Visitante (guest): quem chega sem se identificar
- Usuário (user): quem fez login e tem um nome para o servidor
- Login: o ato de se identificar e provar quem é você

### Cena 3 - Senha e o que ela prova (3:30-4:30)

### Falar

"A senha é a prova de que você é quem diz ser para o servidor."

"Pense assim: o servidor já conhece você. Ele tem seu email e uma versão embaralhada da sua senha guardada. Quando você digita a senha no login, o servidor embaralha o que você digitou e compara. Se bate, é você."

"Termo que aparece aqui: hash. Hash é o embaralhamento que não tem volta. O servidor não guarda sua senha. Guarda o hash dela. Por isso ninguém, nem o dono do sistema, consegue te dizer sua senha. Só consegue gerar uma nova."

### Mostrar

Diagrama simples: senha digitada -> hash -> comparada com hash guardado. Se igual, login OK.

### Cena 4 - O que o servidor agora sabe sobre você (4:30-5:30)

### Falar

"Depois que o login dá certo, o servidor sabe várias coisas sobre você. Ele sabe seu ID, seu nome, seu email, e crucialmente: ele sabe quais permissões você tem."

"Permissões significam: o que você pode fazer. Você pode ver? Pode editar? Pode apagar? Pode ver os dados dos outros?"

"Essa informação, de quem é você e o que você pode, é o que vamos carregar pelo resto do vídeo. Tudo a partir de agora é sobre como o servidor lembra disso entre um request e outro."

### Fechamento do ATO 1

Mostrar o mapa com as partes do ATO 1 destacadas: visitante, login, usuário, permissões. Dizer: "agora o servidor sabe quem é você. Mas como ele vai lembrar disso no próximo request? Isso é o próximo ato."

---

## ATO 2 - Como o servidor lembra de você (5:30-11:00)

### Cena 1 - HTTP não tem memória (5:30-6:45)

### Falar

"Aqui chegamos no coração do problema. O protocolo que a web usa, o HTTP, não tem memória."

"Isso significa o seguinte: cada request é tratado como se fosse o primeiro. O servidor recebe o pedido, responde, e esquece de você. O próximo request, ele te trata como estranho de novo."

"Isso é loucura para um sistema com login. Você faz login, e no request seguinte o servidor já não sabe quem é você?"

### Mostrar

Dois requests seguidos. O servidor responde igual, sem ligar um ao outro. "Quem é você?" aparece nos dois.

### Falar

"É por isso que precisamos de um mecanismo de memória entre requests. Esse mecanismo tem dois nomes principais: sessão e token. Vamos nos dois."

### Cena 2 - Sessão: a memória no servidor (6:45-8:15)

### Falar

"Sessão é a memória que mora no servidor. Funciona assim: você faz login, o servidor cria uma sessão para você, guarda essa sessão na memória dele ou no banco, e te dá um identificador dessa sessão."

"Esse identificador se chama session ID. Session ID é só um texto longo e aleatório que aponta para a sessão guardada no servidor."

"A partir daí, cada request seu carrega esse session ID. O servidor recebe o request, lê o session ID, vai na memória dele, descobre que é você, e responde como se você tivesse acabado de fazer login."

### Mostrar

Diagrama: login -> servidor cria sessão (memória do servidor) -> devolve session ID -> request seguinte carrega session ID -> servidor consulta memória -> sabe quem é.

### Falar

"Termo que aparece muito: cookie. Cookie é um pedacinho de texto que o navegador guarda e envia junto com cada request para o mesmo site. É como o session ID viaja: o servidor dá o cookie, o navegador guarda, e cada request leva o cookie de volta."

"Resumo da sessão: a memória mora no servidor. O navegador só carrega o identificador."

### Cena 3 - Token: o crachá que o cliente carrega (8:15-9:45)

### Falar

"Tem um outro modelo, chamado token. A diferença fundamental é onde a memória mora."

"No token, depois do login o servidor não guarda sessão nenhuma. Em vez disso, ele te dá um crachá. Um texto longo, codificado, que carrega dentro dele a informação de quem é você."

"Esse crachá é o token. Você guarda no navegador, e cada request carrega esse token. O servidor recebe o token, lê, e descobre quem é você sem precisar ir na memória dele."

"E por que ninguém falsifica um crachá desses? Porque o token sai carimbado. O servidor gera ele com uma assinatura que só ele sabe fazer. Se alguém mexe no conteúdo, a assinatura não bate, e o servidor rejeita. Ler, qualquer um lê. Forjar, não."

### Mostrar

Diagrama: login -> servidor gera token (carrega dentro a identidade) -> token vai para o navegador -> request seguinte carrega token -> servidor lê o token e sabe quem é.

### Traduzir

- Token: crachá que o servidor dá depois do login; carrega dentro quem é você
- JWT (JSON Web Token): um formato específico de token, muito comum, mas é só um formato

### Falar

"A analogia que fica: sessão é como um guarda-volumes. Você dá seu casaco (sua identidade) pro servidor guardar, ele te dá um bilhetinho com número. Cada vez que você volta, mostra o bilhetinho e ele te devolve o casaco."

"Token é como um crachá. O servidor te dá o crachá na entrada, você carrega no pescoço, e cada mesa que você chega lê o crachá e sabe quem é você. O servidor não guarda nada."

### Cena 4 - Sessão vs token: quando usar qual (9:45-11:00)

### Falar

"Não existe certo ou errado absoluto. Sessão é mais simples para o servidor controlar, porque ele pode invalidar quando quiser, só apagando da memória. Token é melhor quando você tem vários servidores, porque nenhum precisa guardar nada, só precisa saber ler o token."

"O que importa para você, que programa com IA: quando a IA falar em sessão, ela está falando da memória no servidor. Quando falar em token ou JWT, ela está falando do crachá que o cliente carrega."

"Os dois resolvem o mesmo problema: como o servidor lembra de você entre requests. Onde a memória mora é o que muda."

### Fechamento do ATO 2

Mostrar o mapa com login, sessão e token destacados.

"Agora o servidor sabe quem é você e lembra entre requests. Saber quem é você é só o começo. Falta a pergunta mais importante: o que você pode fazer? Isso é o próximo ato."

---

## ATO 3 - Quem pode o que (11:00-16:30)

### Cena 1 - Autenticação vs autorização (11:00-12:30)

### Falar

"Aqui está a diferença que mais confunde. Autenticação e autorização são duas coisas diferentes, e confundir as duas é onde a maioria dos problemas começa."

"Autenticação responde: quem é você? É o login. É a senha. É o token que prova identidade."

"Autorização responde: o que você pode fazer? É a pergunta que vem depois da autenticação."

"Exemplo: eu me logo, estou autenticado. Mas posso apagar a conta de outro usuário? Não. Estou autenticado, mas não autorizado a fazer aquilo."

### Mostrar

Duas setas separadas: autenticação (quem é você) -> autorização (o que pode fazer). Nunca confundir.

### Falar

"Autenticação sem autorização é perigoso: você sabe quem é, mas deixa fazer tudo. Autorização sem autenticação não faz sentido: como saber o que pode se não sabe quem é?"

"As duas juntas é o que chamamos de auth. Mas internamente são duas perguntas, duas camadas, dois lugares diferentes do código."

### Cena 2 - Permissões por papel (role) (12:30-13:45)

### Falar

"Autorização se implementa de dois jeitos principais. O primeiro é por papel, em inglês role."

"Papel é um grupo com um conjunto de permissões. Os papéis mais comuns são admin, user e guest."

"Admin pode tudo: ver, editar, apagar, gerenciar outros. User pode ver e editar o que é dele. Guest só pode ver o que é público."

"Quando o servidor recebe um request, depois de autenticar, ele pergunta: esse usuário é admin? Se sim, deixa apagar. Se for user, bloqueia."

### Mostrar

Tabela simples: admin | user | guest, com X e check para cada ação.

### Falar

"Termo que aparece aqui: RBAC, Role-Based Access Control. É só o nome chique para permissão por papel. Não se assuste com a sigla."

### Cena 3 - Permissões por recurso (ownership) (13:45-14:45)

### Falar

"O segundo jeito é por recurso. Aqui a pergunta é só essa: esse item é seu?"

"Exemplo: você é user. Você pode editar seus próprios comentários. Mas não pode editar o comentário de outro user, mesmo ele sendo user também."

"Aqui a permissão depende da relação entre o usuário e o recurso. Esse artigo é seu? Essa conta é sua? Esse arquivo pertence a você?"

### Mostrar

Dois usuários, cada um com seus itens. User A tenta editar item do user B. Bloqueado: "esse item não é seu".

### Falar

"Os dois modelos se combinam. Um admin pode editar tudo (por papel). Um user só pode editar o que é dele (por recurso). Essa combinação é o que chamamos de autorização."

### Cena 4 - Por que mexer em auth é perigoso (14:45-15:45)

### Falar

"Aqui o ponto mais importante para quem programa com IA. Auth é a camada que mais sofre com sugestões de 'simplificação'."

"A IA vai te dizer: 'para simplificar, vamos remover essa verificação de permissão'. Ou: 'vamos desativar o token temporariamente para testar'. Ou: 'esse middleware de auth está bloqueando, vou comentar'. Middleware, aqui, é o porteiro do servidor: o código que roda antes de cada request para verificar o crachá."

"Cada uma dessas frases é um sinal de perigo. Quando você remove auth, você abre o servidor para o mundo. O que era protegido vira público. O que era restrito a você vira restrito a ninguém."

### Mostrar

Tela com um diff de código. Uma linha de verificação de permissão sendo removida. Destacar em vermelho.

### Falar

"A regra que fica: se a IA sugerir remover, comentar ou simplificar qualquer coisa que toca auth, pergunte antes de aceitar. Pergunte: 'o que para de ser verificado se eu remover isso?'. Se a resposta for 'nada' ou 'só um detalhe', desconfie."

"Auth é lugar de explicitar. Cada verificação que existe, existe porque sem ela alguém consegue fazer algo que não deve."

### Cena 5 - Logoff, expiração, token roubado (15:45-16:30)

### Falar

"Três coisas que podem dar errado depois do login."

"Primeiro: logoff. Logoff é o ato de encerrar a sessão ou invalidar o token. Se o servidor não trata logoff direito, o crachá continua valendo mesmo depois de você sair. E tem um detalhe do modelo token: como o servidor não guarda nada, o logoff muitas vezes é só jogar o crachá fora do lado do cliente. O servidor não tem uma lista do que anulou. É exatamente por isso que a expiração importa tanto."

"Segundo: expiração. Token e sessão têm prazo de validade. Se não expira, vale para sempre. Um crachá que não expira é um risco: se alguém roubar, usa para sempre."

"Terceiro: token roubado. Se alguém intercepta seu token ou seu session ID, essa pessoa se passa por você. O servidor lê o crachá e obedece como se fosse você."

### Mostrar

Três cenas rápidas: logoff (crachá destruído), expiração (crachá com data riscada), roubo (crachá copiado por outra pessoa).

### Falar

"É por isso que auth tem que ser pensada como um ciclo, não só como o login. Login é o começo. Logoff e expiração são o fim. E entre os dois, tudo que carrega o crachá é vulnerável se o crachá cair na mão errada."

### Fechamento do ATO 3

Mostrar o mapa completo: visitante, login, usuário, sessão, token, autenticação, autorização, permissões, logoff, expiração.

"Essa é a história. Um estranho bate na porta do servidor, vira um usuário com permissões, carrega um crachá, até o logoff. Cada conceito responde uma pergunta específica."

---

## ENCERRAMENTO (16:30-18:00)

### Na câmera

"Para programar com IA sem ser enganado, você precisa saber a diferença entre as duas perguntas que auth responde: quem é você, e o que você pode fazer."

"Quando a IA sugerir uma mudança em código de auth, pergunte: isso mexe em autenticação ou autorização? Se for autenticação, o que para de ser verificado? Se for autorização, quem passa a conseguir fazer o que antes não conseguia?"

"Se você não souber responder, não aceite a mudança. Pergunte para a IA: 'que pergunta essa verificação responde?'. A resposta te diz o tamanho do risco."

"Na descrição tem o glossário com todos os termos que apareceram. Repo público [link] para consultar depois."

"Ponte para o próximo episódio: antes de mexer em auth com segurança, você precisa de uma rede de proteção. Um jeito de voltar atrás se algo quebrar. Isso se chama git, e é o tópico do próximo vídeo."

### Call to action

- Inscreva-se para a série
- Comente qual parte de auth mais te confundia antes desse vídeo
- Repo com o glossário: [link]
