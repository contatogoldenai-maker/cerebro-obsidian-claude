# 7. A rotina que mantém o cérebro vivo

Montar é uma tarde. O que faz funcionar é o hábito depois.

## Regra de ouro: toda sessão que mudou algo fecha com registro

Diga **"fecha a sessão"** no fim. A skill `fechar-sessao`:

1. escreve no `UPDATES.md` do cliente o que mudou e por quê;
2. atualiza o `PROJETO.md` se o estado mudou;
3. atualiza o `_cerebro/INDICE.md` se entrou cliente ou mudou status;
4. roda o verificador de segredos e faz commit, se o cofre usa Git.

Sem isso, na semana seguinte ninguém lembra o que foi decidido na terça.

## Correção vira regra

Quando você corrige o Claude com algo permanente ("na verdade a gente não atende fora do
estado", "nunca manda proposta sem o prazo"), ele pergunta se deve salvar e grava a linha no
arquivo certo. A tabela de destino está no fim do `CLAUDE.md`.

## Cicatriz: o erro e a regra

Algo deu errado e custou caro? Escreva em `_cerebro/CICATRIZES.md`: o que aconteceu, quanto
custou, a regra que nasceu, onde ela mora. Seis meses depois, quando a regra parecer chata,
o motivo está escrito.

## O que não fazer

- **Não encher o `CLAUDE.md`.** Ele é mapa. Conteúdo vai nas notas.
- **Não pedir para ele "ler tudo".** Ele lê o que o pedido precisa, pelo mapa.
- **Não deixar duas pessoas editando o mesmo arquivo ao mesmo tempo** se o cofre está no Git.

---
Anterior: [6. Processos e skills](06-processos-e-skills.md) · Próximo: [8. Segurança](08-seguranca.md)
