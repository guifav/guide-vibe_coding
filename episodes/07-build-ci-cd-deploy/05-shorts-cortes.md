# Shorts e cortes

Cada corte isola uma etapa do cano, com gancho para o vídeo completo.

---

## Short 1 - Build: por que seu código vira outra coisa antes de ir ao ar?

**Gancho (0-3s):** "O código que você escreve não é o código que vai para o servidor. Ele é transformado."

**Corpo:** o build pode fazer várias coisas, dependendo do projeto. Ele traduz a sintaxe para a máquina. Reduz o tamanho dos arquivos, tirando espaços e encurtando nomes. Remove o que não usa e junta os arquivos em poucos. O resultado é um arquivo otimizado, pronto para servir. Nem todo build faz tudo isso, mas vale conhecer o que pode acontecer. Quando a IA fala "build failed", a transformação não terminou. Leia o erro.

**CTA:** "No vídeo completo eu abro o cano inteiro, até o ar. Link na descrição."

---

## Short 2 - CI: o portão que bloqueia código quebrado

**Gancho:** "CI vermelho. O que isso significa?"

**Corpo:** CI é um cano que roda sozinho toda vez que código entra no repo. Três verificações principais. Lint confere estilo. Testes conferem comportamento. Build confere a transformação. Verde em tudo, segue. Vermelho em qualquer uma, para. Ninguém publica até consertar.

**CTA:** "Quer entender o cano inteiro? Vídeo completo no canal."

---

## Short 3 - Ambientes: por que o código não vai direto para o ar?

**Gancho:** "Código não vai do seu PC direto pro ar. Ele passa por ambientes."

**Corpo:** quatro ambientes. Local é o seu PC, só você vê. Dev é compartilhado, quebra à vontade. Staging é o ensaio, cópia do real. Prod é o ar, o que o usuário acessa. Cada ambiente tem um propósito. Pular etapas é onde mora o risco.

**CTA:** "O ciclo completo até o ar tá no vídeo principal."

---

## Short 4 - Rollback: como voltar atrás quando o deploy quebra em prod

**Gancho:** "Deployou, CI deu verde, e mesmo assim quebrou em prod. O que você faz?"

**Corpo:** o primeiro movimento é voltar atrás. Rollback é desfazer o deploy, colocar a versão anterior de volta. Com blue-green, é trocar o tráfego de volta. Depois de controlado, senta e faz post-mortem: entender o que aconteceu, não procurar culpado.

**CTA:** "Quando algo dá errado em prod, esse é o movimento. Vídeo completo no canal."

---

## Short 5 - Rollback que piora o incidente (schema e API)

**Gancho:** "Rollback exige cuidado. Em alguns casos ele piora o problema em vez de resolver."

**Corpo:** rollback do código só é seguro quando o banco, a API e a versão anterior continuam compatíveis. Se o deploy criou uma coluna nova no banco e o código novo gravou dado lá, voltar para o código antigo pode quebrar ou ignorar dado importante. Se mudou o formato de resposta da API, outros sistemas já se adaptaram, e voltar cria um segundo incidente. Nesses casos o caminho é avançar, não voltar: corrigir à frente e fazer novo deploy.

**CTA:** "Antes de puxar rollback, pergunte: mexeu em schema ou quebrou API? Vídeo completo no canal."
