# Glossario minimo (aparece na descricao do YouTube)

So os termos que aparecem no roteiro. Um por linha, traducao direta.

---

## No seu computador

- **HTML** - o que aparece na tela (texto, botao, imagem)
- **CSS** - como aparece (cor, tamanho, posicao)
- **JavaScript** - o que acontece (clicou, mudou, calculou)
- **Estado (state)** - a memoria da pagina enquanto ela esta aberta
- **Variavel** - um nome para guardar um valor que pode mudar
- **Git** - sistema de versionamento; tira fotos do codigo no tempo
- **Commit** - o ato de tirar uma foto no git
- **Branch** - linha paralela para testar sem estragar o original
- **Merge** - juntar a branch de volta na linha principal
- **Repo (repositorio)** - onde as fotos do codigo ficam guardadas (ex: GitHub)

## No servidor

- **Servidor** - outro computador, sempre ligado, que responde a pedidos
- **Request** - pedido que o navegador manda para o servidor
- **Response** - resposta que o servidor devolve
- **API** - o balcao de atendimento do servidor; contrato de pedido/resposta
- **Endpoint** - uma porta especifica da API (ex: /api/clusters)
- **JSON** - formato de texto organizado para dados trafegarem
- **Banco de dados** - memoria de longo prazo do servidor
- **Auth (autenticacao)** - camada que responde "quem e voce?"
- **Token** - cracha que o servidor da depois do login; cada request carrega

## Indo ao ar

- **Build** - transformacao do codigo em algo servivel (cozinha)
- **CI/CD** - cano automatizado que testa o codigo antes de publicar
- **Lint** - verificador de estilo do codigo dentro do CI
- **Deploy** - ato de colocar a nova versao no servidor na nuvem
- **Nuvem (cloud)** - computadores de outras empresas que voce aluga
- **Dominio** - o nome que o usuario digita (ex: meuapp.com)
- **DNS** - lista telefonica que traduz o dominio no endereco do servidor

---

## Pergunta-chave para usar com IA

Quando a IA sugerir uma mudanca, pergunte:

"Em qual camada essa mudanca mora?"

As opcoes sao:
- Front (navegador, UI, estado)
- Servidor (API, logica)
- Banco (dados persistentes)
- Auth (quem pode acessar)
- Deploy/infra (como chega ao ar)

A resposta diz o tamanho do risco.
