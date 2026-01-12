# 🤖 Automação de Inventário Patrimonial (RPA)

> Ferramenta de automação desenvolvida em Python para migração e gestão de dados de inventário entre planilhas e sistemas web.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green?style=for-the-badge&logo=selenium)
![Google Sheets](https://img.shields.io/badge/Google%20Sheets-API-yellow?style=for-the-badge&logo=google-sheets)

## 📌 Sobre o Projeto

Este projeto foi desenvolvido para resolver um problema real de **Data Entry** (entrada de dados). O objetivo era migrar centenas de registros de equipamentos de TI de uma planilha legada (Google Sheets) para um novo sistema web de gerenciamento de patrimônio.

A automação elimina erros humanos de digitação, padroniza os dados e reduz drasticamente o tempo necessário para o cadastro.

## 🚀 Funcionalidades Principais

* **Integração via API:** Conexão direta com Google Sheets para leitura de dados em tempo real.
* **Web Scraping & Automação:** Preenchimento automático de formulários web complexos usando Selenium.
* **Tratamento de Dados Inteligente:**
    * Formatação automática de códigos de patrimônio (ex: `123` -> `00000123`).
    * Lógica para lidar com campos vazios ou nulos.
* **Mapeamento de Status:** Algoritmo de "Busca Flexível" que traduz o status da planilha (ex: "em uso", "baixado") para a opção correspondente no menu suspenso do sistema, independente de formatação (maiúsculas/minúsculas).
* **Filtros de Execução:** Capacidade de processar apenas unidades específicas (ex: Filial "JP") e ignorar linhas ocultas ou de outras unidades.
* **Segurança:** Utilização de variáveis de ambiente e arquivos ignorados pelo Git (`.gitignore`) para proteção de credenciais sensíveis.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Automação Web:** Selenium WebDriver (Chrome)
* **Manipulação de Dados:** Google Spreadsheets API (`gspread`, `oauth2client`)
* **Gerenciamento de Drivers:** Webdriver Manager
* **Controle de Versão:** Git & GitHub

## ⚙️ Como Executar

### Pré-requisitos

1.  Python 3 instalado.
2.  Google Chrome instalado.
3.  Arquivo `credenciais.json` (Chave de API do Google Cloud) na raiz do projeto.

### Instalação

```bash
# Clone este repositório
git clone https://github.com/jnszin/bot-automa-o-selenium.git

# Instale as dependências
pip install -r requirements.txt

```

### Configuração

Certifique-se de que o arquivo `credenciais.json` está na pasta do projeto (este arquivo não é versionado por segurança).

### Executando o Bot

```bash
python bot_patrimonio.py

```

## 🧠 Desafios e Aprendizados

Durante o desenvolvimento, enfrentei desafios como a sincronia do carregamento de páginas web (resolvido com esperas explícitas/implícitas) e a inconsistência dos dados de entrada (resolvida com tratamentos de strings e validações condicionais no Python).

---

**Desenvolvido por Jonas Alves Pacheco**

```
