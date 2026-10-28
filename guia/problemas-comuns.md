# Problemas comuns

**O Claude não sabe nada da empresa.**
Ele foi aberto em outra pasta. Confira se a pasta aberta no Claude Code é a mesma do Obsidian
e se o `CLAUDE.md` está na raiz dela (e não dentro de uma subpasta).

**"Próximo" não faz nada de especial.**
A pasta `.claude/skills/proximo/` não veio na cópia. Em alguns sistemas, pastas que começam com
ponto ficam ocultas e são puladas ao copiar. Mostre os arquivos ocultos e copie de novo.

**Apareceram notas vazias no Obsidian.**
Alguém clicou num `[[link]]` para uma nota que não existe. Apague as vazias e corrija o link.

**O Obsidian não mostra a pasta `.claude`.**
Normal: o Obsidian esconde pastas que começam com ponto. Elas continuam lá.

**`python` não é reconhecido.**
Tente `python3`. Sem Python instalado, peça ao Claude: "verifica segredos no cofre". A skill
`proximo` tem a lista de padrões para ele procurar com a busca dele.

**Conflito no Git ao puxar mudanças.**
Duas pessoas editaram o mesmo arquivo. Peça ao Claude para mostrar o conflito e escolher, com
você, o que fica.

**O cofre ficou lento para o Claude.**
O `CLAUDE.md` cresceu demais ou alguém pediu para ele ler tudo. Deixe no `CLAUDE.md` só o mapa
e as regras; o resto vai para as notas.
