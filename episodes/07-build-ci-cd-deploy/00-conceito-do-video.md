# Conceito do vídeo - Build, CI/CD e Deploy (profundo)

## Tese

No episódio 01 vimos que existe build, CI/CD e deploy. Vimos que eles moram na camada "indo ao ar". Mas vimos só o nome. Este vídeo abre essa camada e mostra o que realmente acontece dentro de cada etapa.

O código que o usuario recebe passa por um cano antes de chegar la. Entre o que você escreve e o que vai ao ar existe um cano: o build transforma, o CI valida, o CD publica, o ambiente recebe, o deploy troca de versao. Cada etapa desse cano pode quebrar, pode bloquear, pode salvar. Quem programa com IA e não enxerga o cano fica refem da mensagem de erro que aparece na tela, sem saber onde o problema mora.

Este vídeo também e o fechamento da temporada. No fim, voltamos ao mapa do episódio 01, agora com cada camada explicada pelos sete vídeos da série. O espectador que assistiu tudo sai com o mapa completo na cabeça.

## Por que esse formato funciona

- Linear: continua a jornada do episódio 01, agora na etapa final, sem pular.
- Profundo mas sem ferramenta: o foco e o que cada etapa faz e por que existe, não qual botao apertar em qual plataforma.
- Fechamento circular: voltar ao mapa do episódio 01 da a sensação de ciclo completo e reforca o aprendizado de toda a série.

## Público

- Quem assistiu ao episodio 01 e quer entender o que acontece depois do commit
- Vibe coders que já encontraram "build failed" ou "CI vermelho" e não sabiam o que isso significava
- Pessoas de produto / negocio que querem entender o risco de um deploy e por que ele pode derrubar o site

## Tom

Direto, sem jargao desnecessario. Cada termo técnico que aparece e imediatamente traduzido em uma frase. Didático. Gui falando para camera ou com tela mostrando um diagrama simples do cano. Fechamento com tom de conclusão da temporada, sem ser melodramatico.

## Estrutura em 3 atos

**ATO 1 - O build e por que ele quebra (transformação do código)**
O que o build realmente faz: dependendo do projeto, pode traduzir a sintaxe, reduzir arquivos, remover partes não usadas e organizar módulos para publicação. Apresentado como possibilidades, não como regras, porque nem todo build faz tudo. Por que build quebra: dependencia faltando, erro de tipo, sintaxe invalida. O build e a cozinha do restaurante que vimos no episódio 01, agora com a porta aberta.

**ATO 2 - O cano: CI e CD (validar e publicar automaticamente)**
CI como portao automatico que roda toda vez que código entra no repo: lint, testes, build, cada etapa verde ou vermelho. Se vermelho, bloqueia, mas com a ressalva de que o CI não replica o ambiente de produção por completo. CD como a continuacao: depois do CI verde, publica. Aqui o episódio distingue Continuous Delivery (prepara versão publicável com portão humano) de Continuous Deployment (publica automaticamente sem decisão humana). Ambientes: local, dev, staging, prod. Estratégias de deploy: blue-green, canary. O ciclo completo: commit, push, CI, CD, ambiente, usuario percebe.

**ATO 3 - Quando algo da errado e o fechamento da temporada**
Rollback, e principalmente quando o rollback não é trivial: se o deploy alterou schema do banco ou quebrou compatibilidade de API, voltar apenas o código pode piorar o incidente. Incidente, post-mortem. Depois, fechamento da temporada: o mapa do episódio 01 revisitado por completo, agora com cada camada explicada pelos sete vídeos da série.

## O que Não entra neste vídeo

- Tutorial de GitHub Actions, Vercel, Jenkins, GitLab CI ou qualquer ferramenta especifica
- Containers, Kubernetes, Docker a fundo
- Infraestrutura como código (Terraform, Pulumi)
- Monitoramento e observabilidade a fundo (metricas, logs, traces)
- Seguranca no deploy (secretos, certificacao, supply chain) alem do conceito
- Comparativo de clouds (AWS, GCP, Azure)

Esses viram material futuro ou referencias na descrição. Este vídeo fecha a temporada com o cano completo explicado.
