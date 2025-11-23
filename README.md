# Supermarket POS System

## Português

### Descrição

Sistema completo de **Ponto de Venda (POS)** para supermercados desenvolvido em **Python**. Este projeto demonstra o uso de **ORM (SQLAlchemy)**, **SQLite** para gerenciamento de banco de dados, **web scraping** para coleta de dados de produtos, e implementa funcionalidades completas de um sistema de caixa.

### Funcionalidades

- **Gerenciamento de Produtos**: Listagem, consulta e controle de estoque
- **Gerenciamento de Clientes**: Cadastro e consulta de clientes
- **Carrinho de Compras**: Adicionar, remover e visualizar itens
- **Registro de Vendas**: Histórico completo de transações
- **Relatórios**: Fechamento de caixa com relatórios de vendas
- **Web Scraping**: Coleta automática de dados de produtos via web
- **Persistência de Dados**: Banco de dados SQLite com SQLAlchemy ORM
- **Interface CLI**: Tabelas formatadas e organizadas usando `tabulate`

### Tecnologias Utilizadas

- **Python 3.x**
- **SQLAlchemy** (ORM)
- **SQLite** (Banco de dados)
- **BeautifulSoup4** (Web Scraping)
- **Pandas** (Manipulação de dados)
- **Tabulate** (Formatação de tabelas)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/supermarket-pos-system.git
cd supermarket-pos-system
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
```

3. Ative o ambiente virtual:

**Windows:**
```bash
.\venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install sqlalchemy pandas beautifulsoup4 tabulate
```

### Como Usar

1. Execute o arquivo principal:
```bash
python caixa.py
```

2. Siga as instruções no terminal:
   - Abra o caixa escolhendo a opção `1`
   - Cadastre ou consulte um cliente
   - Navegue pelo menu para:
     - Visualizar produtos disponíveis
     - Adicionar produtos ao carrinho
     - Remover produtos do carrinho
     - Finalizar atendimento
     - Fechar o caixa

### Estrutura do Projeto

```
supermarket-pos-system/
├── caixa.py                 # Arquivo principal - ponto de entrada
├── menu.py                  # Definição dos menus do sistema
├── models.py                # Modelos de dados (ORM)
├── conexao.py               # Configuração do banco de dados
├── util.py                  # Funções utilitárias
├── arquivo.py               # Manipulação de arquivos CSV/JSON
├── Servicos/                # Camada de serviços
│   ├── servicos_atendimento.py
│   ├── servicos_carrinho.py
│   ├── servicos_cliente.py
│   └── servicos_produto.py
├── Servicos_db/             # Serviços de banco de dados
│   ├── servicos_carrinho_db.py
│   ├── servicos_clientes_db.py
│   ├── servicos_produtos_db.py
│   └── servicos_registros_db.py
├── WebScraping/             # Módulo de web scraping
│   └── produtoslp.py
├── produtos.csv             # Arquivo CSV com produtos
├── clientes.json            # Arquivo JSON com clientes
└── banco.db                 # Banco de dados SQLite (gerado automaticamente)
```

### Conceitos Demonstrados

- **Orientação a Objetos (OOP)**
- **ORM (Object-Relational Mapping)**
- **Padrão de Arquitetura em Camadas**
- **Web Scraping**
- **Manipulação de Dados (CSV, JSON)**
- **Tratamento de Exceções**
- **Persistência de Dados**

---

## English

### Description

Complete **Point of Sale (POS) System** for supermarkets developed in **Python**. This project demonstrates the use of **ORM (SQLAlchemy)**, **SQLite** for database management, **web scraping** for product data collection, and implements complete cashier system functionalities.

### Features

- **Product Management**: Listing, querying, and stock control
- **Customer Management**: Customer registration and queries
- **Shopping Cart**: Add, remove, and view items
- **Sales Records**: Complete transaction history
- **Reports**: Cash closing with sales reports
- **Web Scraping**: Automatic product data collection via web
- **Data Persistence**: SQLite database with SQLAlchemy ORM
- **CLI Interface**: Formatted and organized tables using `tabulate`

### Technologies Used

- **Python 3.x**
- **SQLAlchemy** (ORM)
- **SQLite** (Database)
- **BeautifulSoup4** (Web Scraping)
- **Pandas** (Data manipulation)
- **Tabulate** (Table formatting)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/supermarket-pos-system.git
cd supermarket-pos-system
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:

**Windows:**
```bash
.\venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install sqlalchemy pandas beautifulsoup4 tabulate
```

### Usage

1. Run the main file:
```bash
python caixa.py
```

2. Follow the terminal instructions:
   - Open the cash register by choosing option `1`
   - Register or query a customer
   - Navigate through the menu to:
     - View available products
     - Add products to cart
     - Remove products from cart
     - Complete service
     - Close cash register

### Project Structure

```
supermarket-pos-system/
├── caixa.py                 # Main file - entry point
├── menu.py                  # System menu definitions
├── models.py                # Data models (ORM)
├── conexao.py               # Database configuration
├── util.py                  # Utility functions
├── arquivo.py               # CSV/JSON file handling
├── Servicos/                # Service layer
│   ├── servicos_atendimento.py
│   ├── servicos_carrinho.py
│   ├── servicos_cliente.py
│   └── servicos_produto.py
├── Servicos_db/             # Database services
│   ├── servicos_carrinho_db.py
│   ├── servicos_clientes_db.py
│   ├── servicos_produtos_db.py
│   └── servicos_registros_db.py
├── WebScraping/             # Web scraping module
│   └── produtoslp.py
├── produtos.csv             # CSV file with products
├── clientes.json            # JSON file with customers
└── banco.db                 # SQLite database (auto-generated)
```

### Concepts Demonstrated

- **Object-Oriented Programming (OOP)**
- **ORM (Object-Relational Mapping)**
- **Layered Architecture Pattern**
- **Web Scraping**
- **Data Manipulation (CSV, JSON)**
- **Exception Handling**
- **Data Persistence**

---

## License

This project is part of an academic assignment and is provided as-is for educational purposes.

## Author

Developed as part of the academic curriculum at INFNET.