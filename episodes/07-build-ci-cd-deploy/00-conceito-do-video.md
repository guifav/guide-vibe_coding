# Conceito do video - Build, CI/CD e Deploy (profundo)

## Tese

No episódio 01 vimos que existe build, CI/CD e deploy. Vimos que eles moram na camada "indo ao ar". Mas vimos so o nome. Este video abre essa camada e mostra o que realmente acontece dentro de cada etapa.

O codigo que voce escreve nao e o codigo que o usuario recebe. Entre um e outro existe um cano: o build transforma, o CI valida, o CD publica, o ambiente recebe, o deploy troca de versao. Cada etapa desse cano pode quebrar, pode bloquear, pode salvar. Quem programa com IA e nao enxerga o cano fica refem da mensagem de erro que aparece na tela, sem saber onde o problema mora.

Este video tambem e o fechamento da temporada. No fim, voltamos ao mapa do episódio 01, agora com cada camada explicada pelos sete videos da serie. O espectador que assistiu tudo sai com o mapa completo na cabeça.

## Por que esse formato funciona

- Linear: continua a jornada do episódio 01, agora na etapa final, sem pular.
- Profundo mas sem ferramenta: o foco e o que cada etapa faz e por que existe, nao qual botao apertar em qual plataforma.
- Fechamento circular: voltar ao mapa do episódio 01 da a sensacao de ciclo completo e reforca o aprendizado de toda a serie.

## Publico

- Quem assistiu ao episodio 01 e quer entender o que acontece depois do commit
- Vibe coders que ja encontraram "build failed" ou "CI vermelho" e nao sabiam o que isso significava
- Pessoas de produto / negocio que querem entender o risco de um deploy e por que ele pode derrubar o site

## Tom

Direto, sem jargao desnecessario. Cada termo tecnico que aparece e imediatamente traduzido em uma frase. Didatico, nao academico. Gui falando para camera ou com tela mostrando um diagrama simples do cano. Fechamento com tom de conclusao da temporada, sem ser melodramatico.

## Estrutura em 3 atos

**ATO 1 - O build e por que ele quebra (transformacao do codigo)**
O que o build realmente faz: minify, tree-shake, compile, bundle. Cada um explicado no conceito, nao na ferramenta. Por que build quebra: dependencia faltando, erro de tipo, sintaxe invalida. O build e a cozinha do restaurante que vimos no episódio 01, agora com a porta aberta.

**ATO 2 - O cano: CI e CD (validar e publicar automaticamente)**
CI como portao automatico que roda toda vez que codigo entra no repo: lint, testes, build, cada etapa verde ou vermelho. Se vermelho, bloqueia. CD como a continuacao: depois do CI verde, publica automaticamente. Ambientes: local, dev, staging, prod. Estrategias de deploy: tudo-de-uma-vez, blue-green, canary. O ciclo completo: commit, push, CI, CD, ambiente, usuario percebe.

**ATO 3 - Quando algo da errado e o fechamento da temporada**
Rollback, incidente, post-mortem. O que acontece quando o ar cai e como se volta atras. Depois, fechamento da temporada: o mapa do episódio 01 revisitado por completo, agora com cada camada explicada pelos sete videos da serie.

## O que NAO entra neste video

- Tutorial de GitHub Actions, Vercel, Jenkins, GitLab CI ou qualquer ferramenta especifica
- Containers, Kubernetes, Docker a fundo
- Infraestrutura como codigo (Terraform, Pulumi)
- Monitoramento e observabilidade a fundo (metricas, logs, traces)
- Seguranca no deploy (secretos, certificacao, supply chain) alem do conceito
- Comparativo de clouds (AWS, GCP, Azure)

Esses viram material futuro ou referencias na descricao. Este video fecha a temporada com o cano completo explicado.
