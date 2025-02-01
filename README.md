# Cadastro de Empresas, Produtos e Vendas

Este projeto foi desenvolvido utilizando **Django**, **Django REST Framework** e **Django Template** para o frontend. Ele permite a criação e gerenciamento de **empresas, seus produtos e vendas**. O CRUD pode ser realizado pelo **sistema web, API ou painel de administração (admin)**.

## 📌 Funcionalidades

- **Cadastro de Empresas, Produtos e Vendas**
- **CRUD completo via sistema web, API e admin**
- **Controle de acesso baseado em usuários** (apenas o dono da empresa pode visualizar o faturamento total)
- **Restrição de acesso à API para usuários autenticados e funcionários**
- **Regras de deleção encadeada**:
  - 🔹 Ao excluir um **dono**, tudo relacionado a ele será removido.
  - 🔹 Ao excluir uma **empresa**, todos os seus produtos e vendas serão excluídos.
  - 🔹 Ao excluir um **produto**, todas as vendas associadas a ele serão removidas.
  - 🔹 Ao excluir uma **venda**, apenas a venda específica será removida.

## 🚀 Tecnologias Utilizadas

- **Django** (Backend)
- **Django REST Framework** (API)
- **Django Template** (Frontend)
- **Swagger e Redoc** (Documentação da API)

## 🔑 Credenciais de Acesso

Para testar a visualização do faturamento total:

- **Usuário:** dono
- **Senha:** dono1234

Para acesso total como superusuário:

- **Usuário:** aroldo
- **Senha:** 123456

## 📖 Documentação da API

A documentação está disponível em:

- [Swagger](http://localhost:8000/swagger/)
- [Redoc](http://localhost:8000/redoc/)

## ⚙️ Endpoints da API

A API está disponível em: [http://localhost:8000/api/](http://localhost:8000/api/)

### Recursos disponíveis:

- **/api/empresa/** → CRUD de empresas
- **/api/produto/** → CRUD de produtos
- **/api/venda/** → CRUD de vendas
- **/api/usuario/** → CRUD de usuários

## 🎯 Como Executar o Projeto

### 1️⃣ Criar e ativar um ambiente virtual

#### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

#### Linux/Mac

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2️⃣ Instalar as dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Aplicar as migrações do banco de dados

```bash
python manage.py migrate
```

### 4️⃣ Executar o servidor

```bash
python manage.py runserver
```

## 🌍 Acessando a Aplicação

- **Frontend:** [http://localhost:8000/](http://localhost:8000/)
- **Admin:** [http://localhost:8000/admin/](http://localhost:8000/admin/)

🚀 **Este projeto foi desenvolvido em pouco tempo para a trilha de backend do NADIC e continuará sendo atualizado ao longo do tempo.** 🎉

