---
name: novo-cliente
description: Cadastra um cliente, lead ou projeto novo no cérebro, copiando clientes/_MODELO e ligando no índice. Use quando disserem "cliente novo", "fechamos com", "cadastra o cliente", "abre a pasta do cliente", "lead novo", "começamos a conversar com".
---

# Novo cliente

1. Pergunte, uma de cada vez, só o que faltar no pedido:
   - nome do cliente;
   - status (🟢 ativo, 🟡 em construção, 🔵 lead);
   - o que a empresa faz ou vai fazer para ele, em uma frase;
   - contato principal **pelo papel** (sócia, gerente), não por telefone;
   - próximo passo, com quem e até quando.
2. Crie `clientes/<nome-em-minusculas-com-hifen>/` copiando os 4 arquivos de
   `clientes/_MODELO/` e preencha com as respostas. O que não foi dito fica "a definir".
3. Em `UPDATES.md`, a primeira entrada: data de hoje, "cliente cadastrado", e o contexto.
4. Acrescente uma linha na seção certa de `_cerebro/INDICE.md`, com link para
   `[[clientes/<nome>/INDICE]]`.
5. Responda em 3 linhas: pasta criada, status, próximo passo.

**Nunca** escreva senha, token ou chave em `CREDENCIAIS.md`: só o sistema, o papel do login e
onde o segredo está guardado.
