
# 🔍 DirbH - URL Brute-Force Tool

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)

DirbH é uma ferramenta simples de força bruta para descobrir diretórios e arquivos ocultos em websites. Desenvolvida em Python, ela realiza requisições HTTP utilizando uma wordlist personalizada e retorna os diretórios encontrados com base nos códigos de status definidos pelo usuário.

---

## 🚀 Funcionalidades

- 🔍 Busca por diretórios ocultos em websites.
- 🎯 Permite filtrar resultados pelos códigos de status HTTP (ex.: 200, 301, 403...).
- ⚙️ Customização via linha de comando (URL alvo, wordlist e status codes).
- 🖥️ Feedback em tempo real no terminal.
- 💡 Leve, rápida e fácil de usar.

---

## 📦 Instalação

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/dirbh.git
cd dirbh
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```
> **Obs:** Caso não tenha o arquivo `requirements.txt`, basta instalar manualmente:
```bash
pip install requests
```

---

## ⚙️ Uso

### ✅ Sintaxe:

```bash
python dirbh.py --url site.com --wordlist wordlist.txt --status 200 301 403
```

### 🔧 Parâmetros:

| Parâmetro    | Descrição                                           | Obrigatório |
| -------------| --------------------------------------------------- | ------------|
| `--url`      | URL alvo (sem https://, exemplo: site.com)          | ✅           |
| `--wordlist` | Caminho da wordlist com os diretórios a testar      | ✅           |
| `--status`   | Status HTTP que deseja exibir (ex.: 200 301 403)    | ✅           |

---

### 📄 Exemplo de uso:

```bash
python dirbh.py --url example.com --wordlist paths.txt --status 200 301 403
```

---

## 📜 Exemplo de saída:

```bash
[*] URL ALVO: https://example.com
[*] Wordlist: paths.txt
[*] Status Codes: ['200', '301', '403']

[*] DirbH ESTÁ VERIFICANDO OS DIRETÓRIOS, AGUARDE [CTRL+C STOP]...

Status 200 => https://example.com/admin
Status 301 => https://example.com/login
Status 403 => https://example.com/hidden
```

---

## 🛠️ Requisitos

- Python 3.x
- Biblioteca `requests`

---

## ⚠️ Aviso Legal

> ⚠️ Esta ferramenta foi desenvolvida apenas para fins educacionais e para testes de segurança autorizados. O uso indevido contra sistemas sem autorização constitui crime segundo a legislação vigente.

---

## 🤖 Desenvolvido por

- Higor Santos

---

## 📃 Licença

Este projeto está sob a licença [MIT](LICENSE).
