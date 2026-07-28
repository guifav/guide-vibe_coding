# YouTube ia-aplicada - Secrets e Variáveis de Ambiente (vídeo simples, arquitetural)

**Eixo:** narrativa única linear. A história de uma chave de API: da IA colando ela no código, ao vazamento, à forma certa de guardar (variável de ambiente) e ao que fazer quando vaza. Cada conceito (secret, configuração, .env, .gitignore, rotação) explicado no momento em que aparece na jornada.

**Não é:** curso de segurança, tutorial de cofre de segredos de plataforma específica, gestão de identidade corporativa, criptografia. É o mapa mental do segredo: onde ele mora, onde ele não pode morar, e o que fazer quando ele escapa.

**Público:** vibe coders que colam chave de API onde a IA mandar / quem já commitou um .env sem saber o que era / quem quer conectar serviços externos sem publicar a senha do próprio negócio.

**Duração alvo:** 15-18 min.

| Arquivo | O que é |
|---|---|
| `00-conceito-do-video.md` | Tese, público, 3 atos, tom |
| `01-roteiro-completo.md` | Roteiro falado linear com timestamps (o coração) |
| `02-mapa-de-camadas.md` | Visual de onde os segredos moram / base do thumbnail |
| `03-glossario-minimo.md` | Só os termos que aparecem no roteiro, 1 linha cada |
| `04-titulos-thumbnail-seo.md` | Títulos, thumbnail, tags |
| `05-shorts-cortes.md` | 4 cortes curtos, cada um isola um conceito |

**Princípios do canal aplicados**
- Didática por analogia operacional: código é a fechadura, segredo é a chave; ambiente é o prédio, o quadro de chaves da portaria é a configuração do ambiente, e cada variável é uma chave pendurada nele
- Conceito só entra se responde "o que quebra se isso faltar"
- Retoma conceitos da temporada 1: commit imutável (ep06), ambientes local/dev/staging/prod (ep07)
- Abre a temporada 2, sobre operar com segurança o que a temporada 1 mapeou
