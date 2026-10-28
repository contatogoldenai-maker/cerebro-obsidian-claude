# 1. Instalar o que precisa

Três programas. Só os dois primeiros são obrigatórios.

## Obsidian

Editor de notas que trabalha numa pasta comum do computador. Gratuito, inclusive para uso
em empresa.

1. Baixe em [obsidian.md/download](https://obsidian.md/download) e instale.
2. Não precisa criar conta nem assinar o Sync.

## Claude Code

É o Claude que trabalha dentro de uma pasta: lê, cria e edita arquivos. Precisa de um plano
pago do Claude (Pro, Max, Team ou Enterprise). O plano gratuito não inclui o Claude Code.

**Caminho mais fácil: o app desktop.** Baixe em [claude.com/download](https://claude.com/download),
entre com a sua conta e use a aba **Code**. Lá você escolhe a pasta em que ele vai trabalhar.

**Pelo terminal** (se preferir):

Windows, no PowerShell:
```powershell
irm https://claude.ai/install.ps1 | iex
```

macOS e Linux:
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Depois feche e abra o terminal e confira:
```bash
claude --version
```

Instruções oficiais e solução de problemas: [code.claude.com/docs/en/setup](https://code.claude.com/docs/en/setup).

## Git (opcional)

Serve para ter histórico de tudo que mudou, backup na nuvem e trabalhar com sócio na mesma
pasta. Dá para começar sem ele e ligar depois (passo 9).

- Windows: [git-scm.com/downloads/win](https://git-scm.com/downloads/win). No Windows, o Git
  também dá ao Claude Code o terminal Bash, que algumas tarefas usam.
- macOS: já vem com o sistema; o primeiro uso de `git` oferece a instalação.

## Python (opcional)

O verificador de segredos (`ferramentas/verificar-segredos.py`) é um script Python. Sem
Python, o Claude faz a mesma varredura com a busca dele. Se quiser instalar:
[python.org/downloads](https://www.python.org/downloads/).

---
Próximo: [2. Criar o cofre](02-criar-o-cofre.md)
