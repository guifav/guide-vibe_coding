# Exemplo 3 - Rotação (extra)

## O que ilustra

O ATO 3 do episódio 08: quando um segredo **vazou**, apagar o arquivo do repo **não resolve** (commit imutável, ep06). O protocolo certo é **revogar → trocar → verificar** em todos os ambientes que usavam a chave antiga.

## Trecho / arquivo

Checklist de emergência (ordem importa):

```
1. REVOGAR
   └── Invalidar a chave exposta no painel do serviço (ela para de funcionar agora)

2. TROCAR
   ├── Gerar chave nova
   ├── Atualizar .env local (cada dev)
   ├── Atualizar staging e produção (painel de config)
   └── Nunca reutilizar a chave vazada

3. VERIFICAR
   ├── App sobe sem erro de variável faltando
   ├── Fluxo que usa a chave (ex.: pagamento) funciona com a nova
   └── Logs não imprimem o valor da chave

O que NÃO basta:
   └── git rm .env && commit "remove segredo"  → foto antiga ainda tem a chave
```

- **Revogar** — corta o dano imediato; quem pegou a chave não usa mais.
- **Trocar** — novo segredo em todo lugar que o antigo morava.
- **Verificar** — confirma que nenhum ambiente ficou com nome certo e valor errado/ausente.

## O que observar

- Assuma que a chave vazada já foi copiada — bots varrem repos públicos em minutos.
- Rotação inclui CI, staging e prod; esquecer um ambiente deixa porta aberta.
- Depois do incidente: post-mortem curto — como entrou, como detectou, o que mudou no processo.
- Prevenção: `.gitignore`, example sem valores reais, nunca logar segredo.

## O que quebra se faltar

| Ausência | Consequência |
|---|---|
| Revogação imediata | Atacante continua usando a chave até alguém lembrar de trocar. |
| Atualização em todos os ambientes | Prod ok, staging ainda com chave morta — deploy seguinte derruba tudo. |
| Só apagar arquivo do repo | Histórico git ainda expõe; scanners continuam encontrando. |
| Verificação pós-troca | Acha que resolveu; app quebra na madrugada por variável faltando. |
