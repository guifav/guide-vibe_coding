# Conceito do vídeo - Secrets e Variáveis de Ambiente

## Tese

O erro mais caro que um vibe coder comete não é bug. É publicar a própria senha. A IA pede uma chave de API para conectar um serviço, a pessoa cola a chave no código, o código vai para o repo, e pronto: a senha do negócio está pública. E por causa de como o git funciona (commit é foto imutável, ep06), apagar depois não resolve.

Este vídeo conta a história de uma chave: o que é um segredo, por que ele não pode morar no código, onde ele mora de verdade (variável de ambiente), e o que fazer quando ele vaza. O espectador sai sabendo a regra de ouro: **código diz o que fazer; segredo diz com qual chave. Os dois nunca viajam juntos.**

## Por que esse formato funciona

- É o risco número 1 real do público-alvo: quem programa com IA conecta serviços externos o tempo todo (pagamento, e-mail, modelos de IA), e cada conexão pede uma chave.
- Retoma e paga conceitos dos episódios anteriores: o commit imutável do ep06 explica por que "apaguei o arquivo" não resolve; os ambientes do ep07 explicam onde os valores moram em produção.
- Tem final acionável: uma checklist de 3 perguntas e um protocolo de emergência (vazou → rotaciona).

## Público

- Vibe coders que usam IA para conectar serviços externos e nunca pensaram onde a chave fica
- Quem já viu um arquivo .env e não sabe o que ele faz
- Pessoas de produto / negócio que querem entender por que "a chave vazou" é incidente grave

## Tom

Direto, sem terrorismo. O objetivo não é assustar, é dar o mapa: segredo existe, tem lugar certo, e tem protocolo quando escapa. Cada termo técnico traduzido em uma frase. Gui falando para câmera, alternando com diagrama e exemplos de tela (um .env, um .gitignore, um diff).

## Estrutura em 3 atos

**ATO 1 - O que é um segredo e por que ele não pode morar no código**
A chave de API entra em cena: o que ela é, o que ela abre. A diferença entre código (a fechadura, que todo mundo pode ver) e segredo (a chave, que só o dono carrega). E o motivo de commitou = vazou: o repo é compartilhado, bots varrem repos públicos, e o git nunca esquece.

**ATO 2 - Variáveis de ambiente: onde o segredo mora**
O código pede o valor pelo nome; quem responde é o ambiente. Variável de ambiente como caixinha que mora no ambiente, não no código. No local, o arquivo .env (sempre no .gitignore) e o .env.example com os nomes sem os valores. Em produção, o painel de configuração da plataforma. Mesmo nome, valores diferentes por ambiente: chave de teste em dev, chave real em prod.

**ATO 3 - Onde a IA erra e o que fazer quando vaza**
As três armadilhas da IA: colar a chave no código para "funcionar logo", commitar o .env, imprimir o segredo em log. Como pedir certo. E o protocolo de emergência: revogar e rotacionar a chave é o único passo que resolve; apagar o arquivo do repo não desfaz a foto.

**ENCERRAMENTO**
Checklist de 3 perguntas para toda mudança que toca segredo. Ponte para temas futuros da sequência.

## O que NÃO entra neste vídeo

- Cofres de segredo de plataformas específicas (secret managers)
- Criptografia, HTTPS/TLS (candidato a episódio próprio)
- Gestão de identidade corporativa, SSO, chaves por usuário
- Limpeza de histórico do git (reescrever histórico é avançado; o protocolo aqui é rotacionar)
- Permissões finas de chave (escopos, least privilege em profundidade)

Esses viram vídeos futuros. Este vídeo é o mapa do segredo.
