# ==========================
# BLOCO 1 — IMPORTAÇÕES
# ==========================

from flask import Flask, jsonify, request, render_template
import functions  # Módulo com as funções auxiliares de backend
from flask_cors import CORS


"""
Flask: Classe principal usada para criar a aplicação web.
jsonify: Converte objetos Python (dict, list) em JSON e adiciona os cabeçalhos corretos (Content-Type: application/json).
request: Objeto que contém os dados da requisição HTTP (headers, body, método, etc.).
"""
    
# ==========================
# BLOCO 2 — INICIALIZAÇÃO
# ==========================

# Cria a instância principal da aplicação Flask.
# Este objeto controla rotas, configuração e execução do servidor.
app = Flask(__name__)
CORS(app)  # <-- habilita o CORS para todas as rotas

"""
__name__: Variável especial do Python. 
O Flask a utiliza para localizar recursos internos (templates, arquivos estáticos etc.).
Quando o arquivo é executado diretamente, __name__ = "__main__".
"""

# ==========================
# BLOCO 3 — ENDPOINTS DA API
# ==========================

@app.route("/")
def home():
    """Renderiza a página principal do app"""
    return render_template("index.html")

# --- Endpoint 1: Listar todas as tarefas e filtradas(GET) ---
@app.route("/tasks", methods=["GET"])
def get_all_tasks():
    """
    Este é o item para LISTAR todas as tarefas.
    Ele também aceita um filtro de status via query parameter.
    Ex: /tasks?status=done
    """
    
    #    LÊ o parâmetro de consulta 'status' da URL.
    #    request.args é um dicionário com os parâmetros (ex: '?status=done')
    #    Se o parâmetro não existir, 'status_filter' será None.
    status_filter = request.args.get('status')
    
    #  Pega TODAS as tarefas da nossa "cozinha"
    tarefas = functions.ler_json()
    
    #  FILTRA a lista SE um filtro foi fornecido
    if status_filter:
        tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa['status'] == status_filter]
        # Retorna a lista já filtrada
        return jsonify(tarefas_filtradas)
    else:
        # Se NENHUM filtro foi fornecido, retorna a lista completa
        return jsonify(tarefas)


# --- Endpoint 2: Criar nova tarefa (POST) ---
@app.route("/tasks", methods=["POST"])
def add_new_task():
    """
    Cria uma nova tarefa e a adiciona ao arquivo JSON.
    Método: POST
    """
    dados = request.get_json()  # Lê o corpo da requisição e converte de JSON para dict

    descricao = dados.get("description")  # Extrai a descrição da tarefa

    # Validação simples
    if not descricao:
        return jsonify({"erro": "O campo 'description' é obrigatório."}), 400  # Bad Request

    # Cria nova tarefa usando função auxiliar
    nova_tarefa = functions.adicionar_tarefa(descricao)

    # Retorna a nova tarefa com status 201 (Created)
    return jsonify(nova_tarefa), 201

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """
    Este é o item para DELETAR uma tarefa específica.
    """
    
    #    O Flask pega o 'task_id' (ex: 3) da URL e o entrega
    #    para esta função como um argumento.
    #    O '<int:task_id>' no decorator já o converte para um inteiro
    
    #    Chama sua função ORIGINAL do functions.py,
    #    passando o ID (convertido para string, como sua função espera)
    sucesso = functions.deletar_tarefa(str(task_id))
    
    # 3. Verifica o que a função retornou (True ou False)
    if not sucesso:
        # Se retornou Falso, o ID não existia.
        # Retorna um erro 404 (Not Found)
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    else:
        # Se retornou Verdadeiro, a exclusão deu certo.
        # Retorna um 200 OK com uma mensagem.
        return jsonify({"mensagem": "Tarefa deletada com sucesso"}), 200
    
@app.route("/tasks/<int:task_id>", methods=["PATCH"])
def update_task(task_id):
    """
    Este é o item do cardápio para ATUALIZAR (parcialmente)
    uma tarefa específica.
    """
    
    #  Pega o JSON do "Body" (ex: {"status": "done"})
    dados_para_atualizar = request.get_json()
    
    if not dados_para_atualizar:
        return jsonify({"erro": "Nenhum dado fornecido para atualização"}), 400
    
    #  Chama sua NOVA função do functions.py
    sucesso = functions.atualizar_tarefa(str(task_id), dados_para_atualizar)
    
    #  Retorna a resposta
    if not sucesso:
        # Se retornou Falso, o ID não existia
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    else:
        # Se retornou Verdadeiro, a atualização deu certo
        return jsonify({"mensagem": "Tarefa atualizada com sucesso"}), 200
    
@app.route("/help", methods=["GET"])
def index():
    """
    Este é o endpoint Raiz (/).
    Serve como uma "página de boas-vindas" ou "ajuda"
    para quem acessar a API.
    """
    # Cria um dicionário (JSON) que descreve sua API
    info_api = {
        "api_name": "Task Tracker API",
        "version": "v1.0.0",
        "message": "Bem-vindo à API de Gerenciamento de Tarefas!",
        "endpoints": {
            "listar_tarefas": {
                "method": "GET",
                "path": "/tasks"
            },
            "adicionar_tarefa": {
                "method": "POST",
                "path": "/tasks",
                "body": "{ 'description': '...' }"
            },
            "deletar_tarefa": {
                "method": "DELETE",
                "path": "/tasks/<task_id>"
            },
            "atualizar_tarefa": {
                "method": "PATCH",
                "path": "/tasks/<task_id>",
                "body": "{ 'description': '...', 'status': '...' }"
            }
        }
    }
    return jsonify(info_api)

# ==========================
# BLOCO 4 — EXECUÇÃO DO SERVIDOR
# ==========================

if __name__ == "__main__":
    """
    Este bloco garante que o servidor Flask será executado apenas
    quando o arquivo for rodado diretamente (e não importado).
    """
    app.run(debug=True)
    """
    app.run(): Inicia o servidor local na porta 5000 (padrão).
    """
