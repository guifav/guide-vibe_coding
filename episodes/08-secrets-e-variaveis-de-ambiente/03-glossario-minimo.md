# Glossário mínimo (aparece na descrição do YouTube)

Só os termos que aparecem no roteiro. Um por linha, tradução direta.

---

## O segredo

- **Secret (segredo)** - qualquer valor que dá acesso a algo em seu nome
- **Chave de API** - a senha que um serviço externo dá para o seu sistema usar ele
- **Credencial** - o par "quem sou" + "prova de que sou" (usuário e senha, por exemplo)
- **Hardcoded** - valor escrito direto no código (o que segredo nunca pode ser)

## Onde ele mora

- **Ambiente** - um lugar onde o código roda (local, dev, staging, prod)
- **Variável de ambiente** - caixinha com nome que mora no ambiente; o código pede pelo nome e recebe o valor
- **.env** - arquivo local com os pares nome-valor de verdade; nunca vai para o repo
- **.gitignore** - a lista do que o git deve fingir que não existe; o .env mora nela (entrar na lista não remove o que já foi commitado)
- **.env.example** - a lista dos nomes sem os valores; esse sim vai para o repo
- **Placeholder** - valor de mentira que marca o lugar do valor real
- **Painel de configuração** - onde a plataforma de deploy guarda as variáveis de produção

## Quando ele escapa

- **Vazamento** - o segredo ficou acessível a quem não devia (ex: commitado em repo)
- **Revogar** - cancelar a chave no serviço que emitiu; ela para de abrir
- **Rotacionar** - revogar a antiga e gerar uma nova (o serviço troca a fechadura dele e te dá outra chave)
- **Log** - o registro do que o sistema fez; segredo impresso em log é segredo gravado em texto plano

---

## Pergunta-chave para usar com IA

Quando a IA mexer em qualquer coisa que conecta um serviço, pergunte:

1. Essa chave está no código ou no ambiente?
2. O .env está no .gitignore?
3. Algum segredo aparece em log ou mensagem de erro?

E se vazou: revoga, troca, verifica. Apagar o arquivo não desfaz a foto (ep06).
