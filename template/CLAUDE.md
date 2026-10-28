# {{NOME_DA_EMPRESA}}: cérebro operacional

> O Claude Code lê este arquivo toda vez que esta pasta é aberta. Ele é o mapa: diz o que
> existe e onde procurar. Mantenha curto. O conteúdo mora nas outras notas.

## Montagem em andamento

Enquanto `_montagem/TAREFAS.md` tiver tarefa aberta: quando o usuário disser **"próximo"**
(ou "segue", "continua", "próximos N"), use a skill `proximo` e siga a lista.
A tarefa T10 apaga esta seção.

## Ler ao iniciar qualquer sessão

1. `_cerebro/OPERACAO.md`: como eu trabalho aqui (comportamento, status, regra de ouro).
2. `_cerebro/INDICE.md`: clientes e projetos por status.
3. `empresa/EMPRESA.md`: quem somos, o que vendemos, para quem.

O resto **não** se lê por padrão. Procure pelo mapa abaixo quando o pedido precisar. Ler o
cofre inteiro a cada sessão gasta contexto e piora a resposta.

## Mapa

```
./
├── CLAUDE.md                ← este arquivo
├── _cerebro/                ← COMO a empresa opera com o Claude
│   ├── OPERACAO.md          ← comportamento, quem é quem, status, regra de ouro
│   ├── INDICE.md            ← clientes e projetos por status
│   └── CICATRIZES.md        ← incidente + a regra que nasceu dele
├── empresa/                 ← O QUE a empresa é
│   ├── EMPRESA.md           ← oferta, público, números que importam
│   ├── MARCA.md             ← tom de voz, palavras, visual
│   ├── PROCESSOS/           ← o que se repete, escrito como passo a passo
│   └── receitas/            ← solução que já deu certo e serve para o próximo cliente
├── clientes/                ← uma pasta por cliente, sempre com os mesmos arquivos
│   └── _MODELO/             ← copiar daqui (skill `novo-cliente`)
├── ferramentas/             ← scripts (verificar-segredos.py)
└── .claude/skills/          ← skills: proximo, novo-cliente, fechar-sessao e as suas
```

Arquivos de cada `clientes/<nome>/`: `INDICE.md` (porta de entrada) · `PROJETO.md` (estado
atual) · `UPDATES.md` (diário do que mudou) · `CREDENCIAIS.md` (onde está cada acesso, nunca o valor).

## Regras

- **Segredo nunca entra nesta pasta.** Senha, chave de API, token: ficam num gerenciador de
  senhas ou num arquivo fora do cofre. Aqui só se escreve *onde* está. Se o usuário colar um
  segredo no chat, não escreva em nota nenhuma e avise que ele deve trocar a chave.
- **Antes de commitar:** `python ferramentas/verificar-segredos.py .` precisa dar LIMPO.
- **Link `[[ ]]` só para nota que existe.** No Obsidian, clicar num link quebrado cria um
  arquivo vazio na hora. Na dúvida, escreva o caminho completo (`[[clientes/acme/PROJETO]]`).
- **Fuso:** {{FUSO}}. Toda data em nota usa esse fuso.
- **Fonte de verdade é o sistema ao vivo.** Se a nota diz uma coisa e o sistema mostra outra,
  vale o sistema, e a nota é corrigida.
- **Fechar a sessão:** toda sessão que mudou algo termina com a skill `fechar-sessao`.

## Aprender com correções

Quando alguém corrigir algo que soa permanente ("na verdade é assim", "não faz mais isso",
"sempre que…"), pergunte se deve salvar e grave **só a linha nova** no lugar certo:

| Tipo de correção | Vai para |
|---|---|
| Fato da empresa (oferta, preço, público) | `empresa/EMPRESA.md` |
| Como o Claude deve se comportar | `_cerebro/OPERACAO.md` |
| Tom de voz, palavra, visual | `empresa/MARCA.md` |
| Fato de um cliente | `clientes/<nome>/PROJETO.md` |
| Erro que custou caro | `_cerebro/CICATRIZES.md` |
| Solução que serve para outros clientes | `empresa/receitas/` |
