# 🚀 API de Task Tracker (Gerenciador de Tarefas)

Projeto de desenvolvimento full-stack que simula um sistema de gerenciamento de tarefas (To-Do list), construído com um back-end em Python (Flask) e um front-end em HTML, CSS e JavaScript.

🎯 Objetivo

O objetivo deste projeto foi aplicar conhecimentos de desenvolvimento back-end e front-end para construir uma aplicação web funcional (Full-Stack).

**Requisitos do Back-end (API):**
* Desenvolver uma API RESTful usando Python e o framework Flask.
* Criar endpoints para todas as operações CRUD (Criar, Ler, Atualizar, Deletar).
* Utilizar o método `fetch` do JavaScript para consumir os endpoints da API.
* Lidar com requisições HTTP (GET, POST, PATCH, DELETE).
* Gerenciar a persistência de dados (atualmente em um arquivo JSON).
* Configurar CORS para permitir a comunicação entre o front-end e o back-end.

**Requisitos do Front-end (Interface):**
* Criar uma interface de usuário (UI) interativa com HTML, CSS e JavaScript.
* Consumir dados da API de forma assíncrona (sem recarregar a página).
* Permitir ao usuário adicionar, deletar e atualizar tarefas.
* Implementar um sistema de filtros para visualizar tarefas por status.

---

## 🗺️ Mapa interno dos arquivos

Este projeto é dividido em duas partes principais: o servidor (back-end) e o cliente (front-end).

* `app.py`
    * **Função:** O cérebro da aplicação. Este é o servidor Flask que define todas as rotas da API (ex: `/tasks`, `/tasks/<id>`) e lida com as requisições HTTP.

* `functions.py`
    * **Função:** Módulo auxiliar (a "cozinha"). Contém as funções que `app.py` usa para manipular os dados, como `ler_json()`, `adicionar_tarefa()`, etc.

* `data/tasks.json`
    * **Função:** Nosso "banco de dados" temporário. É um arquivo de texto estruturado onde todas as tarefas são fisicamente armazenadas.

* `templates/index.html`
    * **Função:** A estrutura (esqueleto) da página web que o usuário vê no navegador.

* `static/style.css`
    * **Função:** O arquivo de estilização (a "decoração") da página web.

* `static/script.js`
    * **Função:** O "cérebro" do front-end. Este arquivo contém todo o JavaScript que se comunica com a API em Flask, pede os dados e desenha as tarefas na tela.

---

## 💰 Funcionalidades da API (Endpoints)

A API RESTful oferece os seguintes endpoints para gerenciar tarefas:

* **`GET /tasks`**
    * **Descrição:** Lista todas as tarefas cadastradas.
    * **Filtro:** Aceita um parâmetro de consulta (query parameter) para filtrar por status.
    * **Exemplo:** `GET /tasks?status=done` (Lista apenas as tarefas concluídas).

* **`POST /tasks`**
    * **Descrição:** Cria uma nova tarefa. Requer um JSON no corpo da requisição.
    * **Corpo:** `{ "description": "Nova tarefa aqui" }`

* **`PATCH /tasks/<int:task_id>`**
    * **Descrição:** Atualiza parcialmente uma tarefa existente (ex: mudar o status).
    * **Corpo:** `{ "status": "in-progress" }`

* **`DELETE /tasks/<int:task_id>`**
    * **Descrição:** Deleta uma tarefa específica com base no seu ID.

* **`GET /`**
    * **Descrição:** Renderiza a página web principal (`index.html`) para o usuário.

---

## 🛠 Tecnologias Utilizadas

* **Back-End:**
    * ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
    * ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
    * ![Flask-CORS](https://img.shields.io/badge/Flask_CORS-F05032?style=for-the-badge&logo=flask&logoColor=white)
* **Front-End:**
    * ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
    * ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
    * ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

---

## 🚀 Como Executar o Projeto

Para executar este projeto localmente, você precisará ter o **Python 3** instalado.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
    ```

2.  **Crie e ative um ambiente virtual** (Recomendado):
    ```bash
    # Para Windows
    python -m venv venv
    venv\Scripts\activate

    # Para Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências (Flask):**
    ```bash
    pip install Flask Flask-CORS
    ```

4.  **Execute o servidor (Back-end):**
    ```bash
    python app.py
    ```
    * O servidor Flask estará rodando em `http://127.0.0.1:5000/`.

5.  **Acesse o Front-End:**
    * Abra seu navegador e acesse a URL `http://127.0.0.1:5000/`.
    * A interface web (`index.html`) será carregada e você poderá começar a usar o Task Tracker.

---

## 📂 Sugestões de melhorias / futuras implementações

* **Migração para Banco de Dados:** Substituir o `tasks.json` por um banco de dados real (como **SQLite** ou **PostgreSQL**) para permitir persistência de dados de forma mais segura e escalável.
* **Autenticação de Usuários:** Implementar um sistema de login e cadastro (com JWT) para que cada usuário tenha sua própria lista de tarefas privada.
* **Melhorar o Front-End:** Utilizar um framework moderno (como React ou Vue.js) para criar uma interface mais dinâmica e componentizada.
* **Testes:** Adicionar testes unitários para a API.