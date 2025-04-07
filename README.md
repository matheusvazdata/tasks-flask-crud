# 📝 Tasks API - CRUD com Flask

Projeto de uma API RESTful para gerenciamento de tarefas (to-do list) utilizando **Python + Flask**, com funcionalidades de **CRUD (Create, Read, Update, Delete)**.

Essa aplicação foi construída com foco em aprendizado prático de back-end e testes automatizados com `pytest`, sendo ideal para compor um portfólio profissional.

## 📌 Funcionalidades

- ✅ Criar tarefas
- 🔍 Listar todas as tarefas
- 📄 Consultar tarefa por ID
- ✏️ Atualizar título, descrição e status de uma tarefa
- ❌ Deletar tarefa

## 🧱 Estrutura do Projeto

```
tasks-flask-crud/
│
├── app.py               # Aplicação Flask
├── tests.py             # Testes com pytest + requests
├── requirements.txt     # Dependências do projeto
├── README.md            # Documentação do projeto
├── models/
│   └── task.py          # Modelo da entidade Task
└── .venv/               # Ambiente virtual (opcional)
```

## 🚀 Como Executar o Projeto

### 1. Clone o repositório:

```bash
git clone https://github.com/matheusvazdata/tasks-flask-crud.git
cd tasks-flask-crud
```

### 2. Crie e ative o ambiente virtual (opcional, mas recomendado):

```bash
python -m venv .venv
# Ative o ambiente:
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
```

### 3. Instale as dependências:

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação:

```bash
python app.py
```

A aplicação será executada em `http://127.0.0.1:5000`

## 🧪 Rodando os testes

Com o servidor rodando em um terminal, em outro execute:

```bash
pytest tests.py
```

Você verá o resultado dos testes para cada rota da API.

## 🔄 Endpoints

| Método | Rota               | Descrição                         |
|--------|--------------------|-----------------------------------|
| POST   | `/tasks`           | Criar uma nova tarefa             |
| GET    | `/tasks`           | Listar todas as tarefas           |
| GET    | `/tasks/<id>`      | Buscar tarefa por ID              |
| PUT    | `/tasks/<id>`      | Atualizar uma tarefa existente    |
| DELETE | `/tasks/<id>`      | Remover uma tarefa                |

## 📚 Tecnologias Utilizadas

- [Python 3.12+](https://www.python.org)
- [Flask](https://flask.palletsprojects.com/)
- [Pytest](https://docs.pytest.org/)
- [Requests](https://docs.python-requests.org/)

## 🧠 Próximos Passos (Foco em Dados e Análises com Flask)

- 🗂️ **Salvar as tarefas em CSV (pandas)**  
  Simula persistência de dados e uso básico de bibliotecas de dados.

- 📊 **Criar endpoint `/analytics` com métricas**  
  Retornar contagem total de tarefas, concluídas, pendentes e percentual.

- 🏷️ **Adicionar campos extras como categoria e data**  
  Permite enriquecer os dados para análises futuras.

- 📤 **Exportar tarefas como JSON ou CSV via endpoint**  
  Simula entrega de dados para outras aplicações ou times de BI.

- 🧪 **Criar filtros por status ou data nos endpoints**  
  Treina lógica condicional e estruturação de rotas dinâmicas.

## 👨‍💻 Autor

**Matheus Vaz**  
Analytics Engineer em transição de carreira para a área de dados e tecnologia.  
Apaixonado por aprender, resolver problemas e criar soluções com propósito.

[🔗 LinkedIn](https://www.linkedin.com/in/matheusvazdata/) • [💻 Portfólio](https://www.datacamp.com/portfolio/matheusvazdata) • [🐙 GitHub](https://github.com/matheusvazdata)

> Este projeto faz parte do meu processo de transição de carreira para a área de dados e tecnologia. Se quiser trocar ideia, colaborar ou dar feedback, será muito bem-vindo(a)!