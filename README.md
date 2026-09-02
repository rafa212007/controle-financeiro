# 💰 Controle Financeiro Pessoal

<div align="center">

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=for-the-badge&logo=python&logoColor=white)
![Oracle](https://img.shields.io/badge/Oracle-Database-F80000?style=for-the-badge&logo=oracle&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

**Sistema web completo de controle financeiro pessoal, com autenticação de usuários, cadastro de transações, filtros por período e relatórios visuais.**

[Funcionalidades](#-funcionalidades) •
[Tecnologias](#️-tecnologias-utilizadas) •
[Arquitetura](#-arquitetura-do-projeto) •
[Como rodar](#-como-rodar-o-projeto-localmente) •
[Prints](#-capturas-de-tela)

</div>

---

## 📖 Sobre o projeto

O **Controle Financeiro Pessoal** é uma aplicação web desenvolvida para resolver um problema simples e universal: **saber para onde o dinheiro está indo**. A aplicação permite que qualquer pessoa registre suas receitas e despesas, acompanhe o saldo em tempo real e visualize relatórios claros sobre sua situação financeira — sem depender de planilhas manuais ou cálculos feitos "de cabeça".

Mais do que uma ferramenta funcional, este projeto foi construído como um estudo prático e progressivo de **desenvolvimento web com banco de dados relacional**, cobrindo desde a modelagem de dados até autenticação de usuários, segurança de credenciais e apresentação visual — evoluindo em etapas, como acontece em projetos reais de software.

### Por que esse projeto é relevante

- Demonstra domínio do ciclo completo de uma aplicação web: **banco de dados → lógica de negócio → interface → segurança**
- Mostra capacidade de **modelar um problema do mundo real** em tabelas relacionais
- Evidencia conhecimento de **boas práticas de segurança** (senhas criptografadas, variáveis de ambiente, isolamento de dados por usuário)
- Reflete um processo de desenvolvimento **incremental**: o projeto nasceu simples (CRUD básico) e foi evoluindo com login, filtros, visual e gráficos — a mesma lógica usada na construção de produtos reais

---

## ✨ Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| 🔐 **Autenticação de usuários** | Cadastro e login com senha criptografada (hash) — cada usuário só visualiza suas próprias informações |
| 💵 **Cadastro de transações** | Registro de receitas e despesas com descrição, valor, data e tipo |
| ✏️ **Edição e exclusão** | Cada transação pode ser editada ou removida a qualquer momento |
| 📅 **Filtro por período** | Visualização das transações filtradas por intervalo de datas |
| 📊 **Relatório financeiro** | Cálculo automático de receitas, despesas e saldo, com gráfico comparativo |
| 🎨 **Interface responsiva** | Visual próprio em estilo *dashboard financeiro*, com cores semânticas (verde para receita, vermelho para despesa) |
| 🔒 **Dados isolados por usuário** | Nenhum usuário tem acesso às transações de outra conta |

---

## 🛠️ Tecnologias utilizadas

### Back-end

| Tecnologia | Função no projeto |
|---|---|
| **[Python](https://www.python.org/)** | Linguagem principal do projeto, responsável por toda a lógica de negócio |
| **[Flask](https://flask.palletsprojects.com/)** | Micro-framework web utilizado para criar as rotas, controlar requisições HTTP e renderizar as páginas |
| **[SQLAlchemy](https://www.sqlalchemy.org/)** | ORM (*Object-Relational Mapper*) que permite manipular o banco de dados usando classes e objetos Python, em vez de SQL escrito manualmente |
| **[Flask-Login](https://flask-login.readthedocs.io/)** | Gerenciamento de sessões de autenticação — controla quem está logado e protege rotas restritas |
| **[Werkzeug (security)](https://werkzeug.palletsprojects.com/)** | Geração e verificação de hash de senha, garantindo que nenhuma senha seja armazenada em texto puro |
| **[python-dotenv](https://pypi.org/project/python-dotenv/)** | Carregamento de variáveis de ambiente (credenciais do banco, chave secreta) a partir de um arquivo `.env`, mantendo dados sensíveis fora do código-fonte |

### Banco de dados

| Tecnologia | Função no projeto |
|---|---|
| **[Oracle Database](https://www.oracle.com/database/)** | Sistema gerenciador de banco de dados relacional utilizado para armazenar usuários e transações |
| **[python-oracledb](https://oracle.github.io/python-oracledb/)** | Driver oficial que permite ao Python se comunicar com o Oracle Database |

### Front-end

| Tecnologia | Função no projeto |
|---|---|
| **HTML5 + Jinja2** | Estrutura das páginas, com templates dinâmicos alimentados por dados vindos do back-end |
| **CSS3** | Estilização visual das telas, incluindo o layout de dashboard, cards de resumo e badges de receita/despesa |
| **[Chart.js](https://www.chartjs.org/)** | Biblioteca JavaScript utilizada para renderizar o gráfico comparativo de receitas e despesas no relatório |

---

## 🏗️ Arquitetura do projeto

```
controle-financeiro/
│
├── app.py                  # Rotas da aplicação (login, cadastro, CRUD de transações, relatório)
├── models.py                # Modelos das tabelas (Usuario, Transacao) via SQLAlchemy
├── database.py               # Configuração da conexão com o Oracle Database
├── criar_tabelas.py           # Script utilitário para criação das tabelas no banco
├── requirements.txt            # Lista de dependências do projeto
├── .env.example               # Modelo de variáveis de ambiente (sem dados sensíveis)
│
├── templates/                # Páginas HTML (Jinja2)
│   ├── login.html
│   ├── cadastro.html
│   ├── index.html
│   ├── editar.html
│   └── relatorio.html
│
└── static/
    └── style.css              # Estilização visual da aplicação
```

### Modelo de dados

O projeto utiliza duas tabelas principais, relacionadas entre si:

```
┌─────────────────┐         ┌──────────────────────┐
│     usuarios     │         │      transacoes       │
├─────────────────┤         ├──────────────────────┤
│ id (PK)          │ 1     N │ id (PK)                │
│ nome             │────────▶│ descricao              │
│ email            │         │ valor                  │
│ senha_hash       │         │ data                   │
└─────────────────┘         │ tipo (receita/despesa)  │
                             │ usuario_id (FK)         │
                             └──────────────────────┘
```

Cada transação pertence obrigatoriamente a um usuário (`usuario_id`), o que garante o isolamento de dados: toda consulta ao banco filtra os resultados pelo usuário autenticado na sessão.

### Como funciona o fluxo de dados

1. O usuário interage com a interface (HTML) no navegador
2. O **Flask** recebe a requisição e decide qual função executar, de acordo com a rota acessada
3. A função utiliza o **SQLAlchemy** para consultar ou modificar dados no **Oracle Database**, sem a necessidade de escrever SQL manualmente
4. Os dados retornados são inseridos nos templates HTML (via Jinja2) e devolvidos como página pronta para o navegador
5. Em todo esse processo, o **Flask-Login** garante que apenas usuários autenticados acessem as rotas protegidas, e que cada um veja somente seus próprios dados

---

## 🔒 Segurança implementada

- **Senhas criptografadas**: nenhuma senha é armazenada em texto puro — utiliza-se `generate_password_hash` e `check_password_hash` do Werkzeug
- **Variáveis de ambiente**: credenciais do banco e chave secreta da aplicação ficam fora do código-fonte, em um arquivo `.env` (não versionado)
- **Isolamento de dados por usuário**: todas as consultas de transações são filtradas pelo `usuario_id` da sessão ativa, impedindo acesso cruzado entre contas
- **Proteção de rotas**: rotas sensíveis exigem autenticação (`@login_required`), redirecionando usuários não autenticados para a tela de login

---

## 🚀 Como rodar o projeto localmente

### Pré-requisitos

- [Python 3.10+](https://www.python.org/downloads/)
- [Oracle Database](https://www.oracle.com/database/free/) (Free/Express Edition) instalado e em execução

### Passo a passo

**1. Clone o repositório**
```bash
git clone https://github.com/rafa212007/controle-financeiro.git
cd controle-financeiro
```

**2. Crie e ative um ambiente virtual**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Configure as variáveis de ambiente**

Copie o arquivo de exemplo e preencha com os dados do seu banco:
```bash
cp .env.example .env
```
```env
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=1521
DB_SERVICE=nome_do_servico
SECRET_KEY=uma-chave-secreta-aleatoria
```

**5. Crie as tabelas no banco**
```bash
python criar_tabelas.py
```

**6. Inicie a aplicação**
```bash
python app.py
```

**7. Acesse no navegador**
```
http://127.0.0.1:5000
```

---

## 📸 Ilustração do Projeto

<div align="center">

### 🔑 Autenticação
| Tela de Login | Tela de Cadastro |
| :---: | :---: |
| <img width="400" alt="Tela de Login" src="https://github.com/user-attachments/assets/0a79506c-886f-4b35-b1cb-cb9cf0826949" /> | <img width="400" alt="Tela de Cadastro" src="https://github.com/user-attachments/assets/4662ccbf-ea1a-4829-a966-6ce45d890053" /> |

### 📊 Sistema
| Tela Principal | Relatório |
| :---: | :---: |
| <img width="400" alt="Tela Principal" src="https://github.com/user-attachments/assets/c729825c-fc35-44fa-bbf6-c6476eac10f7" /> | <img width="400" alt="Relatório" src="https://github.com/user-attachments/assets/837cef5c-10f4-4a65-94ec-e6785f5e162e" /> |

</div>

---

## 🗺️ Possíveis evoluções futuras

- [ ] Migração do banco de dados para a nuvem (Oracle Autonomous Database)
- [ ] Deploy da aplicação em serviço de hospedagem (Render/Railway)
- [ ] Categorização mais granular das transações (ex: Alimentação, Transporte, Lazer)
- [ ] Exportação de relatórios em PDF
- [ ] Metas de gastos mensais por categoria

---

## 👤 Autor

| Função | Membro |
| :--- | :--- | :--- |
| Desenvolvedor | **Rafael Augusto Carmona** |


### 📚 Orientação Acadêmica
* **Curso:** Engenharia de Software – FIAP
---

### Redes Sociais
* **Linkedin:** www.linkedin.com/in/rafael-augusto-carmona-287230361

* **instagram:** rafa_212007

---

<div align="center">

Se este projeto foi útil ou interessante, considere deixar uma ⭐!

</div>
