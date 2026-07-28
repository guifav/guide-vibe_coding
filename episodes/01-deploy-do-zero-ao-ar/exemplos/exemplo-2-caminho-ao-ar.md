# Exemplo 2 - Caminho ao ar

## O que ilustra

A jornada de **publicação** do episódio 01, passo a passo: do commit local até a URL acessível. É a linha principal do vídeo — distinta do fluxo de uso (navegador acessando a URL pronta).

## Trecho / sequência

```
commit  -->  repo  -->  build  -->  CI  -->  deploy  -->  domínio
   |          |          |         |          |            |
 salva      central   transforma  valida    publica     endereço
 mudança    histórico  em artefato antes     na nuvem    legível
 local                 publicável  de ir
                                  ao ar
```

Detalhe de cada etapa:

1. **Commit** — você grava uma versão do código na sua máquina (com versionamento).
2. **Repo** — o histórico fica centralizado; outras pessoas (e o pipeline) conseguem puxar a mesma base.
3. **Build** — em projetos que exigem, o código-fonte vira arquivos prontos para servir (bundle, assets, etc.). Projetos simples podem pular.
4. **CI** — testes e checagens automáticas rodam antes de publicar; falha aqui impede deploy quebrado.
5. **Deploy** — o artefato (ou o código, se não houver build) sobe para um servidor acessível na rede.
6. **Domínio** — um nome legível aponta para onde o deploy mora; o usuário digita isso no navegador.

## O que observar

- A ordem importa: commit sem push para o repo não alimenta CI nem deploy.
- Build nem sempre existe — página estática simples pode ir direto do repo ao deploy.
- CI é o filtro: o que passa daqui é o que o mundo vê.
- Deploy e domínio são camadas diferentes: o site pode estar no ar com URL técnica antes de ter domínio bonito.
- Esta sequência **não** inclui o que acontece quando alguém abre a URL (isso é a jornada de uso, no encerramento do vídeo).

## O que quebra se faltar

| Etapa ausente | Consequência |
|---|---|
| Commit | Mudanças ficam só na sua cabeça ou em arquivos soltos; nada versionado. |
| Repo remoto | CI e deploy não têm de onde puxar; só funciona na sua máquina. |
| Build (quando necessário) | Servidor recebe código que o navegador não interpreta direto. |
| CI | Bug óbvio ou teste quebrado vai ao ar; descoberta pelo usuário. |
| Deploy | Repo cheio de código, site fora do ar. |
| Domínio | Site no ar, mas só quem tem o endereço técnico encontra. |
