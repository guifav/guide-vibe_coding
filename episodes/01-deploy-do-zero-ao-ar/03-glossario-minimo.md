# Glossário mínimo (aparece na descrição do YouTube)

Só os termos que aparecem no roteiro. Um por linha, tradução direta.

---

## No seu computador

- **HTML** - o que aparece na tela (texto, botão, imagem)
- **CSS** - como aparece (cor, tamanho, posição)
- **JavaScript** - o que acontece (clicou, mudou, calculou)
- **Git** - sistema de versionamento; tira fotos do código no tempo
- **Commit** - o ato de tirar uma foto no git
- **Branch** - linha paralela para testar sem estragar o original
- **Merge** - juntar a branch de volta na linha principal
- **Repo (repositório)** - onde as fotos do código ficam guardadas (no seu computador ou na nuvem)

> Estado e variáveis não entram no ep01. São o tema do ep02 (front-end e estado).

## No servidor

- **Servidor** - outro computador, sempre ligado, que responde a pedidos
- **IP** - o endereço numérico de uma máquina na rede; o DNS traduz nome em IP
- **Request** - pedido que o navegador manda para o servidor
- **Response** - resposta que o servidor devolve
- **API** - o balcão de atendimento do servidor; contrato de pedido/resposta
- **Endpoint** - uma porta específica da API (ex: /api/produtos)
- **JSON** - formato de texto organizado para dados trafegarem
- **Banco de dados** - memória de longo prazo do servidor
- **Autenticação** - identifica quem é você (o login)
- **Autorização** - decide o que você pode fazer, depois de autenticado
- **Auth** - nome coletivo que costuma cobrir autenticação e autorização juntas
- **Token** - crachá que o servidor dá depois do login; em muitos projetos, cada request o carrega

## Indo ao ar

- **Build** - transformação do código em algo servível (cozinha); em projetos simples pode não existir
- **Framework** - kit de estrutura pronta sobre o qual o seu código roda
- **CI/CD** - cano automatizado que testa o código antes de publicar
- **Lint** - verificador de estilo do código dentro do CI
- **Deploy** - ato de colocar a nova versão no servidor na nuvem
- **Nuvem (cloud)** - computadores de outras empresas que você aluga
- **Domínio** - o nome que o usuário digita (ex: meuapp.com)
- **DNS** - lista telefônica que traduz o domínio no endereço do servidor; costuma continuar apontando para o mesmo serviço

---

## Pergunta-chave para usar com IA

Quando a IA sugerir uma mudança, pergunte:

"Em qual camada essa mudança mora? E ela afeta o fluxo de publicação (como o código chega ao ar) ou o fluxo de uso (o que acontece quando alguém acessa)?"

As opções são:
- Front (navegador, UI)
- Servidor (API, lógica)
- Banco (dados persistentes)
- Auth (autenticação e autorização)
- Deploy/infra (como chega ao ar)

A resposta diz o tamanho do risco.
