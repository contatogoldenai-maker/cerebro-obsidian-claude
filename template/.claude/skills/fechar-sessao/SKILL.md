---
name: fechar-sessao
description: Fecha a sessão de trabalho deixando o cérebro atualizado (diário do cliente, estado do projeto, índice, correções aprendidas, commit). Use quando disserem "fecha a sessão", "encerra", "terminamos por hoje", "registra o que fizemos", "atualiza o cérebro", ou ao fim de qualquer sessão que mudou algo.
---

# Fechar a sessão

Revise a conversa e, para cada coisa que mudou:

1. **Cliente afetado:** nova entrada no topo de `clientes/<nome>/UPDATES.md` com data, o que
   mudou e por quê. Se o estado ou o próximo passo mudou, atualize `PROJETO.md`.
2. **Status mudou ou entrou cliente:** atualize `_cerebro/INDICE.md`.
3. **Correção que soa permanente** ("na verdade é assim", "não faz mais isso"): pergunte se
   deve salvar e grave só a linha nova no arquivo da tabela "Aprender com correções" do
   `CLAUDE.md`.
4. **Algo deu errado e custou caro:** proponha uma entrada em `_cerebro/CICATRIZES.md`.
5. **Git:** se a pasta é um repositório, rode `python ferramentas/verificar-segredos.py .`.
   LIMPO: `git add` dos arquivos alterados, commit com mensagem curta do que mudou, e
   `git push` se houver remoto. Achado: pare e mostre (sem repetir o valor).

Responda com a lista do que foi registrado, arquivo por arquivo. Se nada mudou, diga isso em
uma linha e não crie entrada vazia.
