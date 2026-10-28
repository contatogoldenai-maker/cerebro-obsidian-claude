# Cérebro da empresa: IA com mais tempo e mais controle

A IA não te devolve tempo enquanto a empresa morar na sua cabeça.

Preço, cliente, o que foi combinado, o jeito de falar com cada um. Se está tudo com você, cada
conversa com a IA começa com você explicando a empresa de novo. Ela vira mais uma pessoa para
treinar todo dia.

Este kit monta o que a [Golden AI](https://site.goldenailtda.com) usa no próprio dia a dia: a
operação escrita uma vez, numa pasta que a IA lê sozinha toda vez que começa a trabalhar.

- **Mais tempo.** Você para de explicar a empresa a cada conversa, de lembrar o que foi combinado
  com cada cliente e de ensinar o mesmo processo para cada pessoa nova. Explica uma vez; a IA e a
  equipe leem o mesmo lugar.
- **Mais controle.** Cada cliente tem status, próximo passo e o que mudou, com data. Toda sessão
  de trabalho termina com registro. Senha e chave ficam fora da pasta, e a IA trabalha sem
  enxergar o cofre.

As ferramentas são duas: o **Obsidian** (grátis) guarda as notas e o **Claude Code** (plano pago)
trabalha em cima delas. A estrutura vem sem nenhum cliente nem dado nosso dentro, pronta para
você preencher com a sua empresa.

## Como funciona

O cofre do Obsidian é uma pasta comum com arquivos de texto (`.md`). O Claude Code trabalha
em pastas, lê e escreve esses arquivos, e procura um arquivo chamado `CLAUDE.md` toda vez que
abre uma pasta. Juntando as três coisas, o Claude passa a lembrar da empresa de uma conversa
para outra, num formato que você também lê e corrige.

Não precisa de plugin, servidor nem integração para começar.

## O que você tem no fim

- **Um mapa** (`CLAUDE.md`) que o Claude lê ao abrir a pasta: o que existe e onde procurar.
- **A empresa por escrito**: oferta, público, marca, quem é quem, processos.
- **Uma pasta por cliente**, sempre com os mesmos quatro arquivos, e um índice por status.
- **Três skills prontas**: `proximo` (conduz a montagem), `novo-cliente` e `fechar-sessao`,
  e a sua primeira skill, feita a partir de um processo da empresa.
- **Uma rotina**: toda sessão que muda algo termina com o cérebro atualizado.
- **Segurança desde o primeiro dia**: segredos fora do cofre, `.gitignore` e permissões já
  configurados, e um verificador que roda antes de cada commit.

## Antes de começar

| Precisa | Onde | Obrigatório |
|---|---|---|
| Obsidian | [obsidian.md/download](https://obsidian.md/download) | sim |
| Claude Code (plano Pro ou superior) | [claude.com/download](https://claude.com/download), aba Code | sim |
| Git | [git-scm.com](https://git-scm.com/downloads) | para backup e sócios |
| Python | [python.org](https://www.python.org/downloads/) | para o verificador; sem ele o Claude faz a varredura |

Passo a passo de cada um: [guia/01-instalar.md](guia/01-instalar.md).

## Como começar

1. Baixe este repositório: **Code → Download ZIP**, e extraia.
2. Copie a pasta **`template/`** para onde o cérebro vai morar e renomeie com o nome da empresa.
3. No Obsidian: **Abrir pasta como cofre** → essa pasta.
4. No Claude Code: abra a mesma pasta.
5. Diga **"próximo"**.

O Claude conduz a montagem em 10 tarefas, uma por vez: entrevista sobre a empresa, marca,
pessoas, primeiro cliente, primeiro processo, primeira skill, segurança, backup e o teste
final. A cada resposta ele diz qual nota abrir no Obsidian para conferir. Você confere e diz
"próximo" de novo.

Ele para sozinho em dois casos:

- **MANUAL**: algo que só você faz (abrir o Obsidian, criar o repositório privado). Ele mostra
  o passo a passo e espera você dizer **feito**.
- **PORTÃO**: o teste final, numa sessão nova, para provar que o conhecimento ficou nas notas.

Prefere ler antes de fazer? O mesmo caminho está no guia, um arquivo por passo:

1. [Instalar](guia/01-instalar.md)
2. [Criar o cofre](guia/02-criar-o-cofre.md)
3. [Conectar o Claude](guia/03-conectar-o-claude.md)
4. [Ensinar a empresa](guia/04-ensinar-a-empresa.md)
5. [Clientes e projetos](guia/05-clientes-e-projetos.md)
6. [Processos e skills](guia/06-processos-e-skills.md)
7. [A rotina](guia/07-a-rotina.md)
8. [Segurança](guia/08-seguranca.md)
9. [Backup e sócios](guia/09-backup-e-socios.md)
10. [Teste do cérebro](guia/10-teste-do-cerebro.md)

[Problemas comuns](guia/problemas-comuns.md)

## O que tem aqui

```
guia/                         o passo a passo para ler
template/                     o cofre: é esta pasta que você copia
├── CLAUDE.md                 o mapa que o Claude lê ao abrir
├── _cerebro/                 operação, índice de clientes, cicatrizes
├── _montagem/                as 10 tarefas e o diário da montagem
├── empresa/                  empresa, marca, processos, receitas
├── clientes/_MODELO/         os 4 arquivos de todo cliente
├── ferramentas/              verificar-segredos.py
├── .claude/skills/           proximo, novo-cliente, fechar-sessao
├── .claude/settings.json     nega leitura de .env, chaves e _local/
└── .gitignore                segredo e arquivo pesado fora do Git
```

## Três ideias que fazem diferença

1. **O `CLAUDE.md` é mapa, não enciclopédia.** Diz quais 3 notas ler sempre e onde procurar
   o resto. Ler o cofre inteiro a cada conversa gasta contexto e piora a resposta.
2. **Resposta boa sem nota citada é sinal de alerta.** Quando o Claude responde bem e não
   cita nenhum arquivo, ele respondeu de conhecimento geral, e não pelo cérebro da empresa.
3. **Skill dispara pela descrição.** Escreva a `description` em português, com as frases que
   a equipe realmente usa.

## Segurança

O verificador procura chave de API, token, JWT, chave privada e senha escrita em texto. No
modo `--publico` também barra telefone, CPF, CNPJ, e-mail, IP e caminho de pasta do
computador. Este próprio repositório passa por ele a cada push
([.github/workflows/verificar.yml](.github/workflows/verificar.yml)). Detalhes em
[guia/08-seguranca.md](guia/08-seguranca.md) e [SECURITY.md](SECURITY.md).

## Quem fez

[Golden AI](https://site.goldenailtda.com): automação com IA para PMEs. No Instagram,
[@golden.ai_](https://www.instagram.com/golden.ai_/).

Achou um erro ou travou num passo? Abra uma *issue* neste repositório.

## Licença

[MIT](LICENSE): use, copie e adapte, inclusive na sua empresa e com os seus clientes.
