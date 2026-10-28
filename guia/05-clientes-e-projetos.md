# 5. Clientes e projetos (tarefa T05)

Todo cliente tem uma pasta com **os mesmos quatro arquivos**. A repetição é proposital: o
Claude (e qualquer pessoa nova) sabe onde está cada coisa sem procurar.

| Arquivo | Responde |
|---|---|
| `INDICE.md` | Quem é, status, o que fazemos para ele |
| `PROJETO.md` | Onde estamos, próximo passo, o que foi combinado, decisões |
| `UPDATES.md` | O que mudou e quando (diário, mais recente em cima) |
| `CREDENCIAIS.md` | Onde está cada acesso. **Nunca o valor** |

E uma linha no `_cerebro/INDICE.md`, separada por status:

- 🟢 **Ativo**: em produção, atendendo gente real
- 🟡 **Em construção**: fechado, sendo entregue
- 🔵 **Lead**: conversa, sem contrato
- ⚫ **Encerrado**: entregue

## Como cadastrar

Diga: **"cliente novo: <nome>"**. A skill `novo-cliente` pergunta o que falta, copia o modelo
e liga no índice.

Ainda sem cliente? Cadastre um projeto interno ("site da empresa", "organizar o financeiro")
para aprender o formato.

## Por que o contato vai pelo papel

O modelo pede "sócia", "gerente comercial", e não o telefone. O cofre pode ir para um sócio,
um funcionário, um repositório. Telefone e e-mail de cliente moram no CRM ou na agenda; a nota
diz onde.

---
Anterior: [4. Ensinar a empresa](04-ensinar-a-empresa.md) · Próximo: [6. Processos e skills](06-processos-e-skills.md)
