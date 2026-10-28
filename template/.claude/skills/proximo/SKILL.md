---
name: proximo
description: Executa a próxima tarefa da montagem do cérebro (_montagem/TAREFAS.md) de ponta a ponta e para. Use quando o usuário disser "próximo", "next", "segue", "continua", "próximos 3" ou perguntar "o que falta na montagem".
---

# Próximo

Uma tarefa por vez, com prova. Nunca emende a seguinte sem um novo "próximo".

## 1. Retomar

Leia `_montagem/TAREFAS.md` e `_montagem/PROGRESSO.md`. Tarefa marcada `[X]` sem linha no
progresso: complete o registro antes de seguir. Nunca marque duas vezes.

## 2. Escolher

1. Pegue a **primeira** linha `[ ]` cujas dependências estão todas `[X]` ou `[-]`.
2. **MANUAL:** não execute nada. Mostre o passo a passo da seção "Detalhe das tarefas" em
   lista numerada e diga: "Quando terminar, me diga **feito**." Ao ouvir "feito", confira o
   que der para conferir e só então marque. Tarefa opcional que o usuário não quer: `[-]` com
   o motivo no progresso.
3. **PORTÃO:** mostre o roteiro de teste da T10 e espere o usuário trazer o resultado da
   sessão nova. Só marque com as 5 respostas citando arquivo.
4. Diga em uma linha: `Fazendo T0N: <descrição>`.

## 3. Fazer

- Leia só a seção da tarefa em "Detalhe das tarefas" e as notas que ela cita.
- **Entrevista (T02–T06):** uma pergunta por vez. Escreva a resposta na nota assim que ela
  chegar, com as palavras do usuário. Não invente número, cliente, preço ou diferencial; o que
  ele não souber vira "a definir".
- **Dado sensível na resposta** (senha, chave, token, CPF de pessoa): não escreva em nota.
  Diga onde guardar (gerenciador de senhas) e anote só a localização.

### Verificação de segredos (T08 e antes de todo commit)

Rode `python ferramentas/verificar-segredos.py .` (ou `python3`). Se o Python não existir na
máquina, faça a varredura com a ferramenta de busca, nos arquivos do cofre, procurando:
`sk-`, `sk-ant-`, `eyJ` seguido de `.eyJ`, `ghp_`, `github_pat_`, `AIza`, `AKIA`, `xox`,
`sk_live_`, `EAA`, `PRIVATE KEY`, `://usuario:senha@`, `Bearer ` seguido de token longo, e
`senha`/`password`/`token`/`api_key` com `=` ou `:` e um valor entre aspas.
Achado: mostre arquivo e linha **sem repetir o valor inteiro**, tire o valor da nota e
recomende trocar a chave.

## 4. Provar e fechar

1. Confira a coluna **Prova** da tarefa. Não marque sem ter visto.
2. Troque `[ ]` por `[X]` em `_montagem/TAREFAS.md`.
3. Acrescente ao fim de `_montagem/PROGRESSO.md`:
   `| <data e hora local> | T0N | <o que foi feito, 1 frase> | <arquivos> |`
   Pegue a data e hora do sistema (`date` no Bash ou `Get-Date` no PowerShell), no fuso do
   `CLAUDE.md`.
4. Se a pasta tem Git: rode a verificação de segredos, `git add` só dos arquivos da tarefa e
   `git commit -m "T0N: <descrição curta>"`.

## 5. Responder e parar

No máximo 5 linhas: o que foi feito, **qual nota abrir no Obsidian para conferir**, e a
próxima tarefa (`T0N: <descrição>`). Pare.

## "Próximos N"

Repita até N vezes. Pare antes de qualquer MANUAL ou PORTÃO e responda uma vez no fim.
