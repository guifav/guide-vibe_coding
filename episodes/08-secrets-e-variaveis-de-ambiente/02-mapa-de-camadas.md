# Mapa: onde os segredos moram (para mostrar na tela / base do thumbnail)

Este é o diagrama que Gui desenha ou mostra durante o vídeo. Simples, sem ferramentas, só a separação código vs ambiente.

## O mapa central: código vs ambiente

```
  +--------------------------------+       +--------------------------------+
  |  CÓDIGO (a fechadura)          |       |  AMBIENTE (o quadro de chaves) |
  |  - todo mundo pode ver         |       |  - só o dono acessa            |
  |  - vai para o repo             |       |  - NUNCA vai para o repo       |
  |                                |       |                                |
  |  pede: "CHAVE_PAGAMENTO"  -----+------>|  CHAVE_PAGAMENTO = (valor)     |
  |  (só o NOME)                   |       |  SENHA_BANCO     = (valor)     |
  +--------------------------------+       +--------------------------------+
```

Regra de ouro em cima do diagrama: **no código, só o nome. O valor, nunca.**

## Onde os valores moram, por ambiente

```
  LOCAL (sua máquina)          DEV / STAGING              PROD (o ar)
  +-------------------+       +-------------------+      +-------------------+
  |  arquivo .env     |       |  painel da        |      |  painel da        |
  |  (no .gitignore!) |       |  plataforma       |      |  plataforma       |
  |  chave de TESTE   |       |  chave de TESTE   |      |  chave REAL       |
  +-------------------+       +-------------------+      +-------------------+
           \                          |                          /
            +----------- mesmo NOME, valores diferentes --------+
```

## O fluxo do vazamento (para o ATO 1)

```
  chave colada no código
          |
        commit  <- a foto imutável (ep06)
          |
        push -> repo público
          |
    robôs varrendo repos acham em minutos
          |
    conta estourada / dados expostos

  "apaguei o arquivo depois"  ->  a foto antiga continua no álbum. NÃO resolve.
```

## O protocolo de emergência (para o ATO 3)

```
  VAZOU?
    1. REVOGAR a chave no painel do serviço (trocar a fechadura)
    2. Chave NOVA no lugar certo (.env local / painel em prod)
    3. VERIFICAR uso: chamadas estranhas? cobranças?

  apagar o commit NÃO é um dos passos.
```

## Como usar no vídeo

- Abertura: mostrar só a linha de código com a chave dentro e o X vermelho.
- ATO 1: porta/fechadura/chave, depois o fluxo do vazamento.
- ATO 2: o mapa central (código vs ambiente) e a linha dos três ambientes.
- ATO 3: os três cards de armadilha e o protocolo de emergência.
- Encerramento: o mapa central de novo, com a regra de ouro por cima.

## Versão para thumbnail

- Imagem: uma chave gigante pendurada numa fechadura, com X vermelho.
- Título sobre a imagem: "Sua CHAVE está no CÓDIGO?"
- Alternativa: um .env com cadeado vs um commit com a chave vazando.
- Sem palavras densas; só "chave", "código", "vazou".
