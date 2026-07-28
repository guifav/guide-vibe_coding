# Glossario minimo (aparece na descrição do YouTube)

Só os termos que aparecem no roteiro. Um por linha, tradução direta.

---

## No seu computador

- **HTML** - o que aparece na tela (texto, botao, imagem)
- **CSS** - como aparece (cor, tamanho, posição)
- **JavaScript** - o que acontece (clicou, mudou, calculou)
- **Estado (state)** - a memória da página enquanto ela esta aberta
- **Variável** - um nome para guardar um valor que pode mudar
- **Git** - sistema de versionamento; tira fotos do código no tempo
- **Commit** - o ato de tirar uma foto no git
- **Branch** - linha paralela para testar sem estragar o original
- **Merge** - juntar a branch de volta na linha principal
- **Repo (repositorio)** - onde as fotos do código ficam guardadas (ex: repositório na nuvem)

## No servidor

- **Servidor** - outro computador, sempre ligado, que responde a pedidos
- **Request** - pedido que o navegador manda para o servidor
- **Response** - resposta que o servidor devolve
- **API** - o balcao de atendimento do servidor; contrato de pedido/resposta
- **Endpoint** - uma porta especifica da API (ex: /api/clusters)
- **JSON** - formato de texto organizado para dados trafegarem
- **Banco de dados** - memória de longo prazo do servidor
- **Auth (autenticação)** - camada que responde "quem e você?"
- **Token** - cracha que o servidor da depois do login; cada request carrega

## Indo ao ar

- **Build** - transformação do código em algo servivel (cozinha)
- **CI/CD** - cano automatizado que testa o código antes de publicar
- **Lint** - verificador de estilo do código dentro do CI
- **Deploy** - ato de colocar a nova versao no servidor na nuvem
- **Nuvem (cloud)** - computadores de outras empresas que você aluga
- **Domínio** - o nome que o usuario digita (ex: meuapp.com)
- **DNS** - lista telefonica que traduz o domínio no endereço do servidor

---

## Pergunta-chave para usar com IA

Quando a IA sugerir uma mudança, pergunte:

"Em qual camada essa mudança mora?"

As opcoes são:
- Front (navegador, UI, estado)
- Servidor (API, lógica)
- Banco (dados persistentes)
- Auth (quem pode acessar)
- Deploy/infra (como chega ao ar)

A resposta diz o tamanho do risco.
