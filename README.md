# Supermarket POS System

## Português

### Descrição

Sistema completo de **Ponto de Venda (POS)** para supermercados desenvolvido em **Python**. Este projeto demonstra o uso de **ORM (SQLAlchemy)**, **SQLite** para gerenciamento de banco de dados, **web scraping** para coleta de dados de produtos, e implementa funcionalidades completas de um sistema de caixa.  
**Além disso, o projeto foi expandido para incluir um SIG (Sistema de Informação Gerencial), exigindo uma remodelagem completa do banco de dados para suportar novas regras de negócio, incluindo compras, itens, fornecedores e relações produto-fornecedor carregadas via planilha Excel.**

### Funcionalidades

- **Gerenciamento de Produtos**: Listagem, consulta e controle de estoque
- **Gerenciamento de Clientes**: Cadastro e consulta de clientes
- **Carrinho de Compras**: Adicionar, remover e visualizar itens
- **Registro de Vendas**: Histórico completo de transações
- **Relatórios**: Fechamento de caixa com relatórios de vendas
- **Web Scraping**: Coleta automática de dados de produtos via web
- **Persistência de Dados**: Banco de dados SQLite com SQLAlchemy ORM
- **Interface CLI**: Tabelas formatadas e organizadas usando `tabulate`
- **Importação de Fornecedores via Excel** (aba *fornecedores*)
- **Importação de Produtos-Fornecedores via Excel** (aba *produtos-fornecedores*)
- **Associação Produto ↔ Fornecedor** (relação muitos-para-muitos)
- **Consultas SIG:**
  - Clientes com compras
  - Clientes sem compras
  - Detalhamento de compras de um cliente (ordenadas por data desc)
  - Exibição de compra estilo nota fiscal
  - Clientes que mais compram (quantidade)
  - Clientes que mais gastam (valor total)
  - Produtos mais vendidos / menos vendidos
  - Produtos com baixo estoque (por parâmetro)
  - Fornecedores de um produto
- **CRUD completo de produtos**, incluindo associar/desassociar fornecedores

### Tecnologias Utilizadas

- **Python 3.x**
- **SQLAlchemy** (ORM)
- **SQLite** (Banco de dados)
- **BeautifulSoup4** (Web Scraping)
- **Pandas** (Manipulação de dados)
- **Tabulate** (Formatação de tabelas)
- **OpenPyXL** (Leitura das planilhas Excel do SIG)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/supermarket-pos-system.git
cd supermarket-pos-system
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
```

3. Ative o ambiente:

**Windows:**
```bash
.env\Scriptsctivate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

4. Instale dependências:
```bash
pip install sqlalchemy pandas beautifulsoup4 tabulate openpyxl
```

### Como Usar

```bash
python caixa.py
```

```bash
python sig.py
```

### Conceitos Demonstrados

- **OOP**
- **ORM**
- **Arquitetura em Camadas**
- **Web Scraping**
- **Manipulação de Dados**
- **Tratamento de Exceções**
- **Persistência**
- **Modelagem de Banco**
- **Relacionamento N:N**
- **Consultas Analíticas**
- **Integração Excel/CSV/JSON/Web**

---

# Supermarket POS System

## English

### Description

A complete **Point of Sale (POS)** system for supermarkets developed in **Python**. This project demonstrates the use of **ORM (SQLAlchemy)**, **SQLite** for database management, **web scraping** for product data collection, and implements full checkout system features.
**Additionally, the project was expanded to include a MIS (Management Information System), requiring a full database remodel to support new business rules, including purchases, items, suppliers, and product-supplier relations loaded via an Excel spreadsheet.**

### Features

- **Product Management**: Listing, querying, and stock control  
- **Customer Management**: Customer registration and lookup  
- **Shopping Cart**: Add, remove, and view items  
- **Sales Records**: Complete transaction history  
- **Reports**: Checkout summary with sales reports  
- **Web Scraping**: Automatic product data collection  
- **Data Persistence**: SQLite database with SQLAlchemy ORM  
- **CLI Interface**: Organized, formatted tables using `tabulate`  
- **Supplier Import via Excel** (sheet *fornecedores*)  
- **Product‑Supplier Import via Excel** (sheet *produtos-fornecedores*)  
- **Product ↔ Supplier Association** (many‑to‑many relationship)

### MIS Queries

- Customers with purchases  
- Customers without purchases  
- Detailed customer purchases (ordered by date desc)  
- Invoice‑style purchase display  
- Customers who buy the most (quantity)  
- Customers who spend the most (total value)  
- Best‑selling / least‑selling products  
- Low‑stock products (parameter‑based)  
- Suppliers of a given product  
- Full product CRUD, including associating/dissociating suppliers  

### Technologies Used

- **Python 3.x**
- **SQLAlchemy** (ORM)
- **SQLite** (Database)
- **BeautifulSoup4** (Web Scraping)
- **Pandas** (Data manipulation)
- **Tabulate** (Table formatting)
- **OpenPyXL** (Excel import for MIS)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/supermarket-pos-system.git
cd supermarket-pos-system
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the environment:

**Windows:**
```bash
.env\Scriptsctivate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install sqlalchemy pandas beautifulsoup4 tabulate openpyxl
```

### How to Use

```bash
python caixa.py
```

```bash
python sig.py
```

### Concepts Demonstrated

- **OOP**
- **ORM**
- **Layered Architecture**
- **Web Scraping**
- **Data Manipulation**
- **Exception Handling**
- **Persistence**
- **Database Modeling**
- **Many‑to‑Many Relationships**
- **Analytical Queries**
- **Excel/CSV/JSON/Web Integration**
