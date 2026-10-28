# 6. Processos e a primeira skill (tarefas T06 e T07)

## Processo

Pergunta que abre a tarefa: **"O que vocês fazem toda semana do mesmo jeito e que só uma
pessoa sabe fazer?"** Fechamento do mês, relatório para cliente, proposta, onboarding.

O processo é escrito em `empresa/PROCESSOS/<nome>.md`: quando acontece, quem faz, qual o
resultado e os passos numerados. Teste: uma pessoa que nunca fez consegue seguir e chegar ao
mesmo resultado?

## Skill

A skill é o processo em forma que o Claude executa sozinho. Uma pasta em `.claude/skills/`
com um `SKILL.md`:

```markdown
---
name: relatorio-mensal
description: Monta o relatório mensal do cliente a partir do PROJETO.md e do UPDATES.md. Use quando disserem "relatório do mês", "fecha o mês do cliente", "monta o resumo pro cliente".
---

# Relatório mensal

1. Leia `clientes/<nome>/PROJETO.md` e as entradas do mês em `UPDATES.md`.
2. ...
```

**A `description` decide quando a skill dispara.** O Claude compara o que você escreveu com
a descrição de cada skill. Por isso:

- escreva em português, se a equipe pede em português;
- coloque as frases literais que a equipe usa ("fecha o mês", não "realizar o fechamento
  contábil mensal");
- diga também quando **não** usar, se houver confusão com outra skill.

Skill com descrição em inglês, numa equipe que pede em português, perde a disputa e o Claude
responde de conhecimento geral. Aprendemos isso na prática.

---
Anterior: [5. Clientes e projetos](05-clientes-e-projetos.md) · Próximo: [7. A rotina](07-a-rotina.md)
