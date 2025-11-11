# ✅ Task Tracker (CLI) - Gerenciador de Tarefas no Terminal

Um simples e eficiente **gerenciador de tarefas via linha de comando (CLI)**, desenvolvido em **Python**, que permite adicionar, listar, atualizar, remover e alterar o status de tarefas.  
Os dados são salvos em um arquivo **JSON**, garantindo persistência entre execuções.

---

## 🧠 Descrição do Projeto

O **Task Tracker** é uma aplicação de terminal que simula um sistema de gerenciamento de tarefas (to-do list).  
Ele é ideal para quem deseja organizar suas atividades diretamente no terminal, sem precisar de interfaces gráficas.

O projeto foi desenvolvido com foco em **colocar em prática meus conhecimentos em Python**, **boas práticas de programação**, **manipulação de arquivos JSON**, **tratamento de exceções**, e **estruturação modular em Python**.

---

## ⚙️ Funcionalidades

O sistema oferece os seguintes comandos:

| Comando | Descrição | Exemplo de uso |
|----------|------------|----------------|
| `add <descrição>` | Adiciona uma nova tarefa | `python task_cli.py add "Estudar Python"` |
| `list` | Lista todas as tarefas | `python task_cli.py list` |
| `list to-do` | Lista apenas tarefas pendentes | `python task_cli.py list to-do` |
| `list in-progress` | Lista apenas tarefas em andamento | `python task_cli.py list in-progress` |
| `list done` | Lista apenas tarefas concluídas | `python task_cli.py list done` |
| `update <id> <nova descrição>` | Atualiza a descrição de uma tarefa | `python task_cli.py update 1 "Estudar Python por 2h"` |
| `delete <id>` | Remove uma tarefa pelo ID | `python task_cli.py delete 2` |
| `mark-in-progress <id>` | Marca a tarefa como “em andamento” | `python task_cli.py mark-in-progress 3` |
| `mark-done <id>` | Marca a tarefa como “concluída” | `python task_cli.py mark-done 1` |
| `help` | Mostra a lista de comandos disponíveis | `python task_cli.py help` |

---

## 📂 Estrutura do Projeto

task_cli/
│
├── task_tracker_main.py # Arquivo principal que gerencia os comandos da CLI
├── functions.py # Contém todas as funções auxiliares do sistema
├── tasks.json # Arquivo onde as tarefas são armazenadas (criado automaticamente)
└── README.md # Este arquivo de documentação

## ⚙️ Instalação e Execução

Siga estes 3 passos para configurar e rodar o projeto localmente.

### 1. Pré-requisitos

Antes de começar, garanta que você tenha os seguintes softwares instalados:
* **[Python 3](https://www.python.org/downloads/)**
* **[Git](https://git-scm.com/downloads)**

---

### 2. Instalação (Clone)

Abra seu terminal, navegue até o diretório onde você quer salvar o projeto e execute os comandos abaixo.

```bash
# 1. Clone este repositório
# (Copie a URL HTTPS clicando no botão "<> Code" no topo desta página)
git clone https://github.com/jonatas-renan/Task-Tracker

# 2. Navegue para o diretório do projeto
cd Task-Tracker
Todos os comandos a partir de agora devem ser executados de dentro da pasta Task-Tracker.

3. Guia de Comandos (Uso)
Este programa é executado diretamente no terminal. O arquivo principal é o task_tracker_main.py.

Nota: Use py (no Windows) ou python3 (no macOS/Linux) para executar os comandos.

Exemplo de Fluxo de Trabalho:
Bash

# 1. Peça ajuda para ver todos os comandos disponíveis
py task_tracker_main.py help

# 2. Adicione sua primeira tarefa
py task_tracker_main.py add "Criar o README do projeto"
# Saída: ✅ Tarefa adicionada com sucesso (ID: 1)

# 3. Adicione outra tarefa
py task_tracker_main.py add "Enviar para o GitHub"
# Saída: ✅ Tarefa adicionada com sucesso (ID: 2)

# 4. Liste todas as suas tarefas
py task_tracker_main.py list
# Saída:
# --- 📋 Suas Tarefas (all) ---
#   [1] (to-do) - Criar o README do projeto
#   [2] (to-do) - Enviar para o GitHub
# ----------------------------------

# 5. Marque a primeira tarefa como concluída
py task_tracker_main.py mark-done 1
# Saída: ✅ Status da tarefa 1 modificado com sucesso.

# 6. Liste apenas as tarefas pendentes
py task_tracker_main.py list to-do
# Saída:
# --- 📋 Suas Tarefas (to-do) ---
#   [2] (to-do) - Enviar para o GitHub
# ----------------------------------
O arquivo tasks.json será criado (ou atualizado) automaticamente no mesmo diretório sempre que você modificar uma tarefa.

```
---

## 🧩 Tecnologias Utilizadas

| Tecnologia | Descrição |
|:---|:---|
| Python 3 | Linguagem principal usada no projeto |
| Módulo json | Usado para leitura e escrita dos dados das tarefas |
| Módulo os | Verifica a existência de arquivos e diretórios |
| Módulo datetime | Gera as datas de criação e atualização das tarefas |
| Módulo sys | Usado para ler os argumentos da linha de comando |
| CLI (Command Line Interface) | Permite interagir com o programa via terminal |

---

## 📘 Conhecimentos Adquiridos

Durante o desenvolvimento deste projeto, foram aplicados e reforçados os seguintes conceitos:

✅ Manipulação de arquivos JSON (leitura, escrita e validação)

✅ Boas práticas de organização de código em módulos (import/export)

✅ Uso de tratamento de exceções (try/except) para evitar erros em tempo de execução

✅ Uso do sys.argv para capturar argumentos via terminal

✅ Estruturação de uma interface de linha de comando (CLI) funcional

✅ Criação de funções com responsabilidade única

✅ Implementação de um sistema de status de tarefas (“to-do”, “in-progress”, “done”)

---

## 🚧 Implementações Futuras (Roadmap)

O projeto ainda pode evoluir com novas funcionalidades.
Aqui estão algumas ideias planejadas para versões futuras:

🔹 Adicionar campo de prioridade (baixa, média, alta) às tarefas.

🔹 Filtrar e ordenar tarefas por data de criação, status ou prioridade.

🔹 Adicionar suporte a prazos (deadlines) com alertas visiais.

🔹 Exportar tarefas para CSV ou TXT.

🔹 Adicionar suporte a cores no terminal (usando a biblioteca colorama).

🔹 Implementar testes automatizados (pytest) para garantir estabilidade.

🔹 Criar interface web simples (Flask) que use o mesmo arquivo tasks.json.

🔹 Internacionalização (i18n) — suporte a múltiplos idiomas.
