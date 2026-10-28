# Segurança

Este repositório é público e não contém, nem deve conter, segredo, dado de cliente ou dado
pessoal. Todo push passa pelo verificador em modo público
(`template/ferramentas/verificar-segredos.py --publico`).

## O cofre que você monta a partir daqui

- O repositório do **seu** cofre deve ser **privado**.
- Segredos ficam fora do cofre (gerenciador de senhas). As notas dizem só onde estão.
- Rode `python ferramentas/verificar-segredos.py .` antes de cada commit.

## Encontrou um problema neste repositório?

Se for um segredo ou dado pessoal publicado aqui por engano, **não abra issue pública**:
use **Security → Report a vulnerability** neste repositório (aviso privado ao mantenedor).
Para qualquer outra coisa, abra uma issue.
