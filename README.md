# CTF 03: Rota /admin sem proteção

Projeto criado a partir do [template-seguranca](https://github.com/renanscarmo/template-seguranca)
para praticar segurança em Python.

## Objetivo

Descobrir um painel de administrador que não pede login e depois corrigir a falha.

## Como foi

1. **Antes:** a rota `/admin` não tinha verificação nenhuma. Nenhum link levava até ela, mas bastou adivinhar o endereço.
2. **Detecção:** o Bandit e o pip-audit ficaram verdes, porque falhas de lógica não são detectadas por eles. Quem achou a falha foi o teste manual.
3. **Depois:** o `/admin` exige login (senha conferida por hash) e uma sessão. Sem isso, retorna 403.

## O que aprendi

- Esconder um endereço não é proteção (segurança por obscuridade)
- Controle de acesso quebrado é o item número 1 do OWASP Top 10
- Cada rota sensível precisa verificar quem está acessando
- Ferramentas automáticas não pegam falhas de lógica
- A chave que assina a sessão não pode ficar escrita no código

## Ferramentas

- SAST com Bandit
- SCA com pip-audit
- GitHub Actions
