# 9. Backup e sócios com Git (tarefa T09, opcional)

Com Git, cada mudança no cofre vira um ponto no histórico, a pasta tem cópia na nuvem e um
sócio trabalha no mesmo cérebro do computador dele.

## Montar

1. Crie uma conta em [github.com](https://github.com), se não tiver.
2. **New repository** → nome do cofre → marque **Private** → crie sem README.
3. No Claude Code, dentro do cofre, diga:
   > inicia o git neste cofre e conecta no repositório https://github.com/<usuario>/<cofre>
   Ele roda o verificador de segredos, faz o primeiro commit e o push.
4. Para o sócio: no GitHub, **Settings → Collaborators → Add people**. Ele clona o
   repositório, abre a pasta no Obsidian e no Claude Code, e pronto.

## No dia a dia

- `fecha a sessão` já faz o commit e o push.
- Antes de começar a trabalhar, peça "puxa as mudanças" (ele roda `git pull`).
- Um dono por arquivo por vez. Se os dois editam o mesmo arquivo ao mesmo tempo, o Git pede
  para escolher qual versão fica.

## O que não vai para o Git

Vídeo, ZIP e arquivo grande: o GitHub recusa arquivos acima de 100 MB, e o histórico fica
pesado. Guarde no drive da empresa e deixe a nota apontando para lá. O `.gitignore` do modelo
já bloqueia `*.mp4`, `*.mov`, `*.zip` e `*.psd`.

---
Anterior: [8. Segurança](08-seguranca.md) · Próximo: [10. Teste do cérebro](10-teste-do-cerebro.md)
