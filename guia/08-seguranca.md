# 8. Segurança desde o primeiro dia (tarefa T08)

O cofre tem a empresa inteira dentro. Trate como trata o financeiro.

## As quatro regras

1. **Segredo não entra no cofre.** Senha, chave de API e token ficam num gerenciador de
   senhas (Bitwarden, 1Password, o do navegador) ou num arquivo **fora** da pasta. A nota diz
   só *onde* está: "chave do WhatsApp → gerenciador de senhas, cofre Clientes".
2. **Segredo não vai para o chat.** Colou uma chave na conversa? Considere vazada: troque a
   chave no sistema de origem. O Claude é instruído a não gravar o valor em nota.
3. **Verificar antes de commitar.**
   ```bash
   python ferramentas/verificar-segredos.py .
   ```
   Procura chaves de OpenAI, Anthropic, Google, AWS, GitHub, Stripe, Meta, Slack, tokens JWT
   (inclusive a chave do Supabase), chaves privadas, conexão de banco com senha e senha
   escrita em texto. Mostra só o começo do achado, nunca o valor inteiro.
4. **Repositório do cofre é privado.** Sempre. Antes de publicar qualquer coisa que saiu do
   cofre (página, PDF, repositório público), rode no modo público, que também barra telefone,
   CPF, CNPJ, e-mail, IP e caminho de pasta do seu computador:
   ```bash
   python ferramentas/verificar-segredos.py . --publico
   ```

## O que já vem configurado

- **`.gitignore`**: impede que `.env`, `_local/`, `SEGREDOS*`, `*.pem` e `*.key` entrem no Git,
  e deixa fora o estado de janela do Obsidian, que muda a cada clique.
- **`.claude/settings.json`**: nega ao Claude a leitura de `.env`, `_local/`, `*.pem` e `*.key`.
  Se alguém deixar um segredo nesses lugares por engano, ele não lê.

## Se vazou

1. Troque a chave no sistema de origem **antes** de apagar do arquivo. Apagar não desfaz: o
   valor fica no histórico do Git e em qualquer cópia.
2. Tire o valor da nota e escreva só onde a nova chave está guardada.
3. Registre em `_cerebro/CICATRIZES.md`.

---
Anterior: [7. A rotina](07-a-rotina.md) · Próximo: [9. Backup e sócios](09-backup-e-socios.md)
