# 2. Criar o cofre

"Cofre" (*vault*) é como o Obsidian chama a pasta em que ficam as suas notas. Não tem
formato especial: são arquivos `.md` (texto com marcação simples) dentro de pastas.

1. Baixe este repositório: botão verde **Code → Download ZIP**, e extraia.
2. Copie a pasta `template/` para o lugar onde o cérebro vai morar. Sugestão: a pasta
   Documentos. **Não** coloque dentro de uma pasta sincronizada por dois programas ao mesmo
   tempo (OneDrive e Git, por exemplo): dá conflito.
3. Renomeie a pasta com o nome da empresa, sem acento e sem espaço (`acme-cerebro`).
4. Abra o Obsidian → **Abrir pasta como cofre** → escolha essa pasta.

Você vai ver na lateral:

```
_cerebro/      como a empresa opera com o Claude
_montagem/     as 10 tarefas da montagem (some do uso diário depois)
clientes/      uma pasta por cliente
empresa/       quem é a empresa, marca, processos, receitas
ferramentas/   o verificador de segredos
CLAUDE.md      o mapa que o Claude lê ao abrir a pasta
```

A pasta `.claude/` (com as skills) existe, mas o Obsidian esconde pastas que começam com ponto.

**Erro comum:** abrir no Obsidian a pasta do repositório inteiro, e não a cópia do `template/`.
O cofre é só o `template/`, renomeado.

---
Anterior: [1. Instalar](01-instalar.md) · Próximo: [3. Conectar o Claude](03-conectar-o-claude.md)
