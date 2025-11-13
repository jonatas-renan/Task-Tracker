import json 
from datetime import datetime
import os

FILENAME = 'tasks.json'  # Arquivo JSON

def ler_json():
    """Lê o arquivo JSON e o transforma em uma lista em Python"""

    # Verifica se o arquivo existe
    if not os.path.exists(FILENAME):
        # Se não existe, retorna uma lista vazia
        return []
    
    # Se o arquivo existe, mas está vazio, também retorna lista vazia
    if os.path.getsize(FILENAME) == 0:
        return []
    
    # Se existe e tem conteúdo, tenta ler
    try:
        with open(FILENAME, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            # Garante que as dados sejam uma lista
            return dados if isinstance(dados, list) else []
    except json.JSONDecodeError: # Exceção para arquivo corrompido
        print(f"❌ Erro: O arquivo {FILENAME} está corrompido. Criando um novo.")
        return []
    
def escrever_json(dados):
    """Escreve a lista em Python de volta no arquivo JSON"""

    with open(FILENAME, 'w', encoding='utf-8') as f:
        # indent=4 deixa o arquivo JSON formatado e legível
        json.dump(dados, f, indent=4)

def adicionar_tarefa(descricao):
    """Adicionar Tarefa ao arquivo JSON"""

    # Carrega todas as tarefas que já existem
    todas_as_tarefas = ler_json()

    # Calcula o novo id
    novo_id = 1
    if todas_as_tarefas: # Verifica se a lista não está vazia
        # Pega o id mais alto que existe na lista e soma 1
        novo_id = max(tarefa['id'] for tarefa in todas_as_tarefas) + 1

    # Estrutura do arquivo JSON
    nova_tarefa = {
        "id": novo_id,
        "description": descricao,
        "status": "to-do",   
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    
    # Adiciona a nova tarefa à lista
    todas_as_tarefas.append(nova_tarefa)

    # Escreve a lista completa de volta no arquivo
    escrever_json(todas_as_tarefas)

    print(f"✅ Tarefa adicionada com sucesso (id: {novo_id})")

    return nova_tarefa

def listar_tarefas(filtro_status='all'):
    """Lista as tarefas, opcionalmente filtrando por status"""
    
    # Ler
    todas_as_tarefas = ler_json()

    if not todas_as_tarefas:
        print("📋 Você ainda não tem tarefas.")
        return

    # Filtrar
    tarefas_para_mostrar = []
    if filtro_status == 'all': # Padrão 
        tarefas_para_mostrar = todas_as_tarefas
    else:
        # Filtra a lista para incluir apenas tarefas com o status do filtro
        tarefas_para_mostrar = [tarefa for tarefa in todas_as_tarefas if tarefa['status'] == filtro_status]

    # Imprimir
    print(f"\n--- 📋 Suas Tarefas ({filtro_status}) ---")
    
    if not tarefas_para_mostrar:
        print(f"Nenhuma tarefa encontrada com o status: '{filtro_status}'")
    else:
        for tarefa in tarefas_para_mostrar:
            print(f"  [{tarefa['id']}] ({tarefa['status']}) - {tarefa['description']}")
            
    print("----------------------------------\n")

def deletar_tarefa(task_id):
    """Deletar tarefas pelo id"""

    try:
        task_id = int(task_id)
    except ValueError:
        print(f"❌ Erro: O id '{task_id}' não é um número válido.")
        return False
    
    todas_as_tarefas = ler_json()

    # Ignora a tarefa pelo id, "removendo"
    tarefas_atualizadas = [tarefa for tarefa in todas_as_tarefas if tarefa['id'] != task_id]

    #  Verifica se o filtro removeu algo
    #  Se o tamanho das listas for o mesmo, é porque o id não foi encontrado
    if len(todas_as_tarefas) == len(tarefas_atualizadas):
        print(f"❌ Erro: Tarefa com id {task_id} não encontrada.")
        return False
    else:
        #  Se o tamanho for dferente, a exclusão funcionou. 
        escrever_json(tarefas_atualizadas)
        print(f"✅ Tarefa {task_id} deletada com sucesso.")
        return True
    
def mostrar_ajuda():
    """Fornece ajuda ao usuário na linha de comando"""

    print("Use: python task_cli.py <comando> [argumentos]")
    print("\nComandos:")
    print("  add <descricao>             Adiciona uma nova tarefa")
    print("  list [todo|in-progress|done]  Lista tarefas (filtro opcional)")
    print("  update <id> <nova_descricao>  Atualiza uma tarefa")
    print("  delete <id>                 Remove uma tarefa")
    print("  mark-in-progress <id>       Marca uma tarefa como 'em progresso'")
    print("  mark-done <id>              Marca uma tarefa como 'concluída'")


def atualizar_tarefa(task_id_str, dados_para_atualizar):
    """
    Atualiza uma tarefa (qualquer campo) a partir de um dicionário de mudanças.
    """
    try:
        id_para_atualizar = int(task_id_str)
    except ValueError:
        print(f"❌ Erro: O ID '{task_id_str}' não é um número válido.")
        return False # Retorna Falso (falha)

    todas_as_tarefas = ler_json()
    tarefa_encontrada = False
    
    # Itera sobre a lista de tarefas
    for tarefa in todas_as_tarefas:
        if tarefa['id'] == id_para_atualizar:
            
            # .update() mescla os dicionários.
            # Se dados_para_atualizar for {"description": "novo"}, ele muda a descrição.
            # Se for {"status": "done"}, ele muda o status.
            # Se a chave não existir, ela é adicionada
            tarefa.update(dados_para_atualizar)
            # --------------------------
            
            # Atualiza o timestamp
            tarefa['updatedAt'] = datetime.now().isoformat()
            
            tarefa_encontrada = True
            break # Para o loop, já que encontramos a tarefa

    if tarefa_encontrada:
        escrever_json(todas_as_tarefas)
        print(f"✅ Tarefa {id_para_atualizar} atualizada com sucesso.")
        return True # Retorna Verdadeiro (sucesso)
    else:
        print(f"❌ Erro: Tarefa com ID {id_para_atualizar} não encontrada.")
        return False # Retorna Falso (falha)
