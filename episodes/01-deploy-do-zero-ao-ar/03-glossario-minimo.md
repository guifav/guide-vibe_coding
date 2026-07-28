# Glossario minimo (aparece na descrição do YouTube)

Só os termos que aparecem no roteiro. Um por linha, tradução direta.

---

## No seu computador

- **HTML** - o que aparece na tela (texto, botao, imagem)
- **CSS** - como aparece (cor, tamanho, posição)
- **JavaScript** - o que acontece (clicou, mudou, calculou)
- **Git** - sistema de versionamento; tira fotos do código no tempo
- **Commit** - o ato de tirar uma foto no git
- **Branch** - linha paralela para testar sem estragar o original
- **Merge** - juntar a branch de volta na linha principal
- **Repo (repositorio)** - onde as fotos do código ficam guardadas (no seu computador ou na nuvem)

> Estado e variáveis não entram no ep01. São o tema do ep02 (front-end e estado).

## No servidor

- **Servidor** - outro computador, sempre ligado, que responde a pedidos
- **Request** - pedido que o navegador manda para o servidor
- **Response** - resposta que o servidor devolve
- **API** - o balcao de atendimento do servidor; contrato de pedido/resposta
- **Endpoint** - uma porta especifica da API (ex: /api/clusters)
- **JSON** - formato de texto organizado para dados trafegarem
- **Banco de dados** - memória de longo prazo do servidor
- **Autenticação** - identifica quem e você (o login)
- **Autorização** - decide o que você pode fazer, depois de autenticado
- **Auth** - nome coletivo que costuma cobrir autenticação e autorização juntas
- **Token** - cracha que o servidor da depois do login; cada request carrega

## Indo ao ar

- **Build** - transformação do código em algo servivel (cozinha); em projetos simples pode não existir
- **CI/CD** - cano automatizado que testa o código antes de publicar
- **Lint** - verificador de estilo do código dentro do CI
- **Deploy** - ato de colocar a nova versao no servidor na nuvem
- **Nuvem (cloud)** - computadores de outras empresas que você aluga
- **Domínio** - o nome que o usuario digita (ex: meuapp.com)
- **DNS** - lista telefonica que traduz o domínio no endereço do servidor; costuma continuar apontando para o mesmo serviço

---

## Pergunta-chave para usar com IA

Quando a IA sugerir uma mudança, pergunte:

"Em qual camada essa mudança mora? E ela afeta o fluxo de publicação (como o código chega ao ar) ou o fluxo de uso (o que acontece quando alguém acessa)?"

As opcoes são:
- Front (navegador, UI)
- Servidor (API, lógica)
- Banco (dados persistentes)
- Auth (autenticação e autorização)
- Deploy/infra (como chega ao ar)

A resposta diz o tamanho do risco.
