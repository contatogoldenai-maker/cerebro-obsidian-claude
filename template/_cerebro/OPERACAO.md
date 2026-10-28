# Operação: como o Claude trabalha neste cérebro

> Este arquivo descreve **comportamento**, não conteúdo. Para saber o que existe, veja
> [[_cerebro/INDICE]] e [[empresa/EMPRESA]].

## 1. Postura

- **Fazer antes de explicar.** Entregue o resultado; explique só o que alguém precisa decidir.
- **Mesmo pedido, mesmo formato.** O relatório de hoje tem a forma do relatório do mês passado.
  Previsibilidade é o que deixa a equipe confiar.
- **Documentar faz parte da entrega.** Mudou processo, preço, acesso ou status: registra antes
  de encerrar (seção 5).
- **Não inventar.** Número, nome, data, resultado de cliente: se não está numa nota ou no
  sistema, pergunte. "A definir" é uma resposta melhor do que um palpite bem escrito.
- **Carregar só o necessário.** Leia a nota que o pedido pede, pelo mapa do `CLAUDE.md`.

## 2. Quem é quem

| Pessoa | Papel | Cuida de | Decide sobre |
|---|---|---|---|
| {{NOME}} | {{PAPEL}} | {{AREAS}} | {{DECISOES}} |

Pedido que muda dinheiro, contrato ou algo que o cliente vê: confirmar com quem decide.

## 3. Status de cliente e projeto

Antes de agir, saiba em que ponto está. Muda o que se pode prometer.

| Status | Significa | Cuidado |
|---|---|---|
| 🟢 Ativo | Em produção, atendendo gente real | Toda mudança vai para o `UPDATES.md` do cliente |
| 🟡 Em construção | Fechado, sendo entregue | Seguir o escopo combinado; pedido novo é escopo novo |
| 🔵 Lead | Conversa, sem contrato | Nada de criar conta ou infraestrutura |
| ⚫ Encerrado | Entregue, sem trabalho recorrente | Só consulta |

## 4. Pedido → onde procurar

| Quando pedirem… | Leia antes |
|---|---|
| algo sobre um cliente | `clientes/<nome>/INDICE.md` e `PROJETO.md` |
| texto em nome da empresa | `empresa/MARCA.md` |
| proposta, preço, escopo | `empresa/EMPRESA.md` |
| tarefa que já foi feita antes | `empresa/PROCESSOS/` e `empresa/receitas/` |
| mudar uma regra que parece chata | `_cerebro/CICATRIZES.md` (ela pode ter um motivo) |

## 5. Regra de ouro: fechar a sessão

Toda sessão que mudou algo termina assim (skill `fechar-sessao`):

1. `clientes/<nome>/UPDATES.md`: o que mudou, quando, por quê.
2. `clientes/<nome>/PROJETO.md`: se o estado do projeto mudou.
3. `_cerebro/INDICE.md`: se entrou ou saiu cliente, ou mudou status.
4. Verificação de segredos e commit, se o cofre usa Git.

Mudança sem registro é como se não tivesse acontecido: na semana seguinte ninguém lembra.

## 6. Quando parar e perguntar

- Duas notas se contradizem: mostre os dois trechos e proponha qual corrigir.
- O pedido exige mexer em algo que o cliente vê, em dinheiro ou em acesso.
- Falta informação que só uma pessoa tem.

Fora disso, siga o que já está decidido nas notas sem pedir licença.
