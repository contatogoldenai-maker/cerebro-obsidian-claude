# 3. Conectar o Claude ao cofre

Não existe plugin nem integração para instalar. A conexão é: **abrir o Claude Code na mesma
pasta que o Obsidian abriu.**

- **App desktop:** aba Code → escolha a pasta do cofre.
- **Terminal:** entre na pasta e rode `claude`.
  ```bash
  cd Documentos/acme-cerebro
  claude
  ```

## O que acontece

Ao abrir uma pasta, o Claude Code procura um arquivo chamado `CLAUDE.md` e lê antes de
qualquer conversa. O `CLAUDE.md` deste modelo é um **mapa**: diz quais 3 notas ler sempre e
onde procurar o resto. Por isso ele é curto. Se o mapa ficar gigante, toda conversa começa
gastando contexto com coisa que não importa.

As skills ficam em `.claude/skills/`. Cada uma é uma pasta com um `SKILL.md`, e o Claude
escolhe qual usar pela `description` dela. Este modelo traz três:

| Skill | Dispara quando você diz |
|---|---|
| `proximo` | "próximo", "segue", "continua" (só durante a montagem) |
| `novo-cliente` | "cliente novo", "fechamos com…", "lead novo" |
| `fechar-sessao` | "fecha a sessão", "atualiza o cérebro" |

## Primeiro teste

Pergunte: **"O que você sabe sobre esta empresa?"**

Ele deve responder que o cérebro ainda está em branco e que a montagem está em andamento.
É isso que você quer ver: ele leu o `CLAUDE.md` e não inventou uma empresa.

Agora diga **"próximo"**. A montagem começa.

---
Anterior: [2. Criar o cofre](02-criar-o-cofre.md) · Próximo: [4. Ensinar a empresa](04-ensinar-a-empresa.md)
