-- Migração segura: nova coluna com valor padrão para linhas existentes
ALTER TABLE pedidos ADD COLUMN observacao TEXT NOT NULL DEFAULT '';

-- Anti-padrão (NÃO fazer em produção sem plano de rollback):
-- ALTER TABLE pedidos DROP COLUMN total;
-- DROP TABLE pedidos;
