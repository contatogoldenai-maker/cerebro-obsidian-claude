#!/usr/bin/env python3
"""Procura segredo e dado pessoal nos arquivos de texto de uma pasta.

Uso:
    python ferramentas/verificar-segredos.py .            # falha só com segredo
    python ferramentas/verificar-segredos.py . --publico  # falha também com dado pessoal

Rode antes de todo commit. Use --publico antes de publicar qualquer coisa
(repositório público, página, PDF): ali até um telefone de cliente é vazamento.
Só usa a biblioteca padrão do Python.
"""
import os
import re
import sys

# Segredo: se aparecer, nunca é aceitável em lugar nenhum.
SEGREDO = [
    ("chave OpenAI", r"sk-(?!ant-)(?:proj-)?[A-Za-z0-9_\-]{20,}"),
    ("chave Anthropic", r"sk-ant-[A-Za-z0-9_\-]{20,}"),
    ("JWT (inclui chave anon do Supabase)", r"eyJ[A-Za-z0-9_\-]{10,}\.eyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}"),
    ("token GitHub", r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}|\bgithub_pat_[A-Za-z0-9_]{30,}"),
    ("chave Google", r"\bAIza[0-9A-Za-z_\-]{35}\b"),
    ("chave AWS", r"\bAKIA[0-9A-Z]{16}\b"),
    ("token Slack", r"\bxox[abprs]-[A-Za-z0-9\-]{10,}"),
    ("chave Stripe", r"\b(?:sk|rk)_live_[A-Za-z0-9]{20,}"),
    ("token Meta", r"\bEAA[A-Za-z0-9]{60,}"),
    ("chave privada", r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    ("conexão de banco com senha", r"(?:postgres(?:ql)?|mysql|mongodb(?:\+srv)?)://[^\s:/'\"<]+:[^\s@'\"<]+@"),
    ("Bearer literal", r"Bearer\s+[A-Za-z0-9_\-\.]{24,}"),
    ("senha ou chave atribuída", r"(?i)\b(?:api[_-]?key|secret|password|senha|token)\s*[:=]\s*['\"][^'\"\s{}]{12,}['\"]"),
]

# Dado pessoal e de máquina: normal num cofre privado, vazamento num lugar público.
PESSOAL = [
    ("telefone BR", r"\b55\d{10,11}\b|\(?\b\d{2}\)?\s?9\d{4}[-\s]\d{4}\b"),
    ("CPF", r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b"),
    ("CNPJ", r"\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b"),
    ("e-mail", r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    ("caminho de usuário da máquina", r"[A-Za-z]:\\Users\\[^\\\s]+|/Users/[^/\s]+/|/home/[^/\s]+/"),
    ("webhook", r"https?://[^\s'\"<)]*/webhook[^\s'\"<)]*"),
    ("IP", r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
]

# E-mails e IPs de exemplo que podem aparecer em documentação.
PERMITIDO = re.compile(
    r"@(?:exemplo|example)\.(?:com|org)|noreply@|users\.noreply\.github\.com"
    r"|\b(?:127\.0\.0\.1|0\.0\.0\.0)\b"
)

EXTENSOES = (".md", ".txt", ".json", ".yml", ".yaml", ".toml", ".js", ".mjs", ".ts",
             ".py", ".ps1", ".sh", ".html", ".css", ".csv", ".env", ".ini", ".cfg")
PULAR_PASTAS = {".git", ".obsidian", "node_modules", ".trash", "__pycache__", ".venv"}


def arquivos(raiz):
    for pasta, subpastas, nomes in os.walk(raiz):
        subpastas[:] = [s for s in subpastas if s not in PULAR_PASTAS]
        for nome in nomes:
            caminho = os.path.join(pasta, nome)
            if os.path.abspath(caminho) == os.path.abspath(__file__):
                continue  # este arquivo contém os padrões
            if nome.lower().endswith(EXTENSOES) or nome.startswith(".env"):
                yield caminho


def varrer(raiz, regras):
    achados = []
    for caminho in arquivos(raiz):
        try:
            texto = open(caminho, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        texto = re.sub(r"data:(?:image|font)/[a-z0-9.+-]+;base64,[A-Za-z0-9+/=\s]+", "", texto)
        for rotulo, padrao in regras:
            for m in re.finditer(padrao, texto):
                trecho = m.group(0)
                if PERMITIDO.search(trecho):
                    continue
                linha = texto.count("\n", 0, m.start()) + 1
                mascara = trecho[:6] + "…" if len(trecho) > 10 else trecho
                achados.append((rotulo, os.path.relpath(caminho, raiz), linha, mascara))
    return achados


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")  # terminal do Windows não é UTF-8 por padrão
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    publico = "--publico" in sys.argv
    raiz = args[0] if args else "."

    segredos = varrer(raiz, SEGREDO)
    pessoais = varrer(raiz, PESSOAL)

    for rotulo, arq, linha, trecho in segredos:
        print(f"  SEGREDO  [{rotulo}] {arq}:{linha} :: {trecho}")
    for rotulo, arq, linha, trecho in pessoais:
        nivel = "PESSOAL " if publico else "aviso   "
        print(f"  {nivel} [{rotulo}] {arq}:{linha} :: {trecho}")

    bloqueia = segredos or (publico and pessoais)
    if bloqueia:
        print("\nRESOLVER OS ACHADOS ANTES DE COMMITAR OU PUBLICAR")
        sys.exit(1)
    print("LIMPO" + (" (modo público)" if publico else ""))


if __name__ == "__main__":
    main()
