# 10. Teste do cérebro (tarefa T10)

O teste final é feito numa **sessão nova**, para provar que o conhecimento está nas notas e
não na memória da conversa da montagem.

Abra o Claude Code de novo na pasta do cofre e pergunte:

1. "O que a empresa vende e para quem?"
2. "Qual o status do <cliente que você cadastrou> e qual o próximo passo?"
3. "Como faço <o processo que você escreveu>?"
4. Peça a tarefa da sua skill com as suas palavras, sem dizer o nome da skill.
5. "Fecha a sessão."

## Como saber se passou

**Cada resposta tem que citar o arquivo de onde veio.** Uma resposta bem escrita que não cita
nenhuma nota é o sinal de que o Claude respondeu de conhecimento geral, e não pelo cérebro.

Se falhar:
- Pergunta 1 a 3 sem arquivo: o mapa do `CLAUDE.md` não aponta para a nota certa. Corrija o mapa.
- Pergunta 4 não disparou a skill: a `description` não tem as palavras que você usou. Reescreva
  com as suas frases.
- Pergunta 5 não registrou: confira se a skill `fechar-sessao` está em `.claude/skills/`.

Passou nas cinco: volte à sessão da montagem e diga "próximo". O Claude marca a T10 e apaga a
seção "Montagem em andamento" do `CLAUDE.md`. O cérebro está pronto para o uso diário.

---
Anterior: [9. Backup e sócios](09-backup-e-socios.md) · Dúvidas: [problemas comuns](problemas-comuns.md)
