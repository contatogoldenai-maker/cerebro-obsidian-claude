# Montagem do cérebro: tarefas

Lista executável, na ordem. Diga **"próximo"** no Claude Code e ele segue a skill `proximo`:
pega a primeira tarefa `[ ]` cujas dependências estão `[X]`, faz, confere a prova, marca,
anota em [[_montagem/PROGRESSO]] e para.

- **MANUAL** = só você faz. O Claude mostra o passo a passo e espera você dizer **feito**.
- **PORTÃO** = teste final. Só fecha se tudo passar.
- **Prova** = o que precisa ser verdade para marcar `[X]`.
- `[-]` = tarefa dispensada (só as opcionais), com o motivo anotado no progresso.

| ID | Tarefa | Depende de | Prova | Status |
|---|---|---|---|---|
| T01 | **MANUAL.** Abrir esta pasta como cofre no Obsidian | — | Você vê `_cerebro`, `empresa` e `clientes` na lateral do Obsidian | [ ] |
| T02 | Entrevista da empresa, uma pergunta por vez → `empresa/EMPRESA.md`; nome da empresa e fuso no `CLAUDE.md` | T01 | `EMPRESA.md` e `CLAUDE.md` sem `{{`; o que você não soube responder está como "a definir" | [ ] |
| T03 | Marca e tom de voz → `empresa/MARCA.md` | T02 | `MARCA.md` sem `{{` (seção sem resposta vira "a definir") | [ ] |
| T04 | Pessoas e papéis → tabela "Quem é quem" em `_cerebro/OPERACAO.md` | T02 | Tabela com uma linha por pessoa, sem `{{` | [ ] |
| T05 | Primeiro cliente (ou projeto interno) com a skill `novo-cliente` | T02 | Pasta `clientes/<nome>/` com os 4 arquivos; linha no `_cerebro/INDICE.md` | [ ] |
| T06 | Primeiro processo: o que a empresa repete toda semana, escrito como passo a passo → `empresa/PROCESSOS/<nome>.md` | T02 | Arquivo com gatilho, responsável e passos numerados | [ ] |
| T07 | Primeira skill da empresa, a partir do processo da T06 → `.claude/skills/<nome>/SKILL.md` | T06 | `SKILL.md` com `name` e `description` em português, com as frases que você usaria para pedir | [ ] |
| T08 | Segurança: conferir `.gitignore` e `.claude/settings.json`, rodar a verificação de segredos | T05 | Saída `LIMPO` de `python ferramentas/verificar-segredos.py .` (ou varredura equivalente, ver skill) | [ ] |
| T09 | **MANUAL (opcional).** Backup e sócios: Git com repositório **privado** no GitHub | T08 | `git remote -v` aponta para o repositório privado e o primeiro push foi feito; ou `[-]` | [ ] |
| T10 | **PORTÃO.** Teste do cérebro em sessão nova e limpeza da montagem | T01–T09 | As 5 perguntas do teste respondidas citando o arquivo de onde veio cada resposta | [ ] |

## Detalhe das tarefas

### T01: abrir no Obsidian
1. Abra o Obsidian.
2. Na tela inicial, clique em **Abrir pasta como cofre** (*Open folder as vault*).
3. Escolha esta pasta (a mesma que está aberta no Claude Code).
4. Se o Obsidian perguntar sobre confiar em plugins, pode recusar: este cofre não usa plugin.

### T02: entrevista da empresa
Faça **uma pergunta por vez**, espere a resposta e escreva na hora em `empresa/EMPRESA.md`.
Ordem: nome da empresa → o que fazem em uma frase → quem compra e quem decide → para quem não
vendem → o que vendem e por quanto → como o cliente chega → por que escolhem vocês (nas
palavras do cliente) → 1 a 3 números que importam → ferramentas que usam → o que não fazem →
cidade/fuso. Não melhore a resposta com adjetivos; escreva o que a pessoa disse. Se ela não
souber, escreva "a definir" e siga.

### T03: marca
Pergunte como a empresa fala com o cliente, peça uma frase real que eles já mandaram, palavras
que usam e que evitam, cores e fontes se existirem. Sem identidade visual definida: "a definir".

### T04: quem é quem
Uma linha por pessoa: nome, papel, do que cuida, sobre o que decide. Se for uma pessoa só,
uma linha só.

### T05: primeiro cliente
Use a skill `novo-cliente`. Se a empresa ainda não tem cliente, cadastre um projeto interno
(ex.: "site da empresa") para aprender o formato.

### T06: primeiro processo
Pergunte: "O que vocês fazem toda semana do mesmo jeito e que só uma pessoa sabe fazer?".
Escreva a partir de `empresa/PROCESSOS/_MODELO.md`.

### T07: primeira skill
Transforme o processo da T06 em skill: `.claude/skills/<nome-curto>/SKILL.md` com o
cabeçalho abaixo e o passo a passo no corpo, apontando para as notas que ele precisa ler.
```
---
name: nome-curto
description: O que faz e quando usar, com as frases literais que a equipe diria ("fecha o mês", "monta o relatório").
---
```
A `description` decide quando a skill dispara: escreva em português, com as palavras da equipe.

### T08: segurança
1. Confira que `.gitignore` existe e bloqueia `.env`, `_local/` e `SEGREDOS*`.
2. Confira que `.claude/settings.json` existe e nega leitura de `.env`.
3. Rode a verificação (skill `proximo`, passo de segurança). Achado de SEGREDO: tire o valor
   da nota, escreva só onde ele está guardado e avise que a chave deve ser trocada.

### T09: Git privado (opcional)
1. Crie uma conta no GitHub, se não tiver.
2. Crie um repositório novo e marque **Private**. Nunca público: aqui mora a empresa.
3. Peça ao Claude: "inicia o git neste cofre e conecta no repositório <endereço>". Ele roda a
   verificação de segredos antes do primeiro commit.
4. Sócio entra pelo convite do repositório (Settings → Collaborators).

### T10: portão
Feche esta sessão e abra **uma sessão nova** do Claude Code nesta pasta. Pergunte:
1. "O que a empresa vende e para quem?"
2. "Qual o status do <cliente da T05> e qual o próximo passo?"
3. "Como faço <processo da T06>?"
4. Peça a tarefa da skill da T07 com as suas palavras, sem citar o nome da skill.
5. "Fecha a sessão."

Passa se cada resposta **cita o arquivo** de onde veio. Resposta boa sem arquivo citado é
sinal de que o Claude respondeu de memória geral, não pelo cérebro: corrija o mapa no
`CLAUDE.md` e repita. Com tudo verde: apague a seção "Montagem em andamento" do `CLAUDE.md`
e marque T10.
