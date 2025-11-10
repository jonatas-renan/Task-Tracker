import sys
from functions import *

def main():
    """Função principal que roteia os comandos da CLI"""

    # Pega todos os argumentos, exceto o nome do script (sys.argv[0])
    args = sys.argv[1:]

    # Se nenhum comando foi dado, mostre a ajuda
    if not args:
        mostrar_ajuda()
        return # Isso para a execução da função 'main' aqui

    # O comando principal é o primeiro argumento
    comando = args[0]

    # Os argumentos específicos do comando são o resto da lista
    argumentos_comando = args[1:]

    try:
        if comando == 'add':
            if not argumentos_comando:
                print("❌ Erro: 'add' precisa de uma descrição.")
                print("   Exemplo: python task_cli.py add \"Comprar pão\"")
            else:
                # Junta todos os argumentos em uma única string de descrição
                descricao = " ".join(argumentos_comando)
                adicionar_tarefa(descricao)

        elif comando == 'list':
            filtro = 'all' # Padrão
            if argumentos_comando:
                # Opções de status/filtro
                filtro_valido = ["to-do", "in-progress", "done"]
                # Se o argumento do comando filtra estiver dentro da lista
                if argumentos_comando[0] in filtro_valido:
                    filtro = argumentos_comando[0]
                else:
                    print(f"❌ Erro: Filtro '{argumentos_comando[0]}' inválido.")
                    return
            listar_tarefas(filtro)

        # Atualizar descricao da tarefa
        elif comando == "update":
            if len(argumentos_comando) < 2:
                print("❌ Erro: 'update' precisa de um ID e uma nova descrição.")
                print("   Exemplo: python task_cli.py update 1 \"Novo texto da tarefa\"")
            else:
                task_id = argumentos_comando[0]
                nova_descricao = " ".join(argumentos_comando[1:])
                atualizar_tarefa(task_id, nova_descricao)

        elif comando == "delete":
            if not argumentos_comando:
                print("❌ Erro: 'delete' precisa de um ID.")
                print("   Exemplo: python task_cli.py delete 1")
            else:
                task_id = argumentos_comando[0]
                deletar_tarefa(task_id)

        # Marcar alguma tarefa em andamento
        elif comando == "mark-in-progress":
            if not argumentos_comando:
                print("❌ Erro: 'mark-in-progress' precisa de um ID.")
            else:
                task_id = argumentos_comando[0]
                marcar_status(task_id, "in-progress")

        # Marcar alguma tarefa como feito
        elif comando == "mark-done":
            if not argumentos_comando:
                print("❌ Erro: 'mark-done' precisa de um ID.")
            else:
                task_id = argumentos_comando[0]
                marcar_status(task_id, "done")
        
        elif comando == "help":
             mostrar_ajuda()

        # Comando digitado errado
        else:
            print(f"❌ Erro: Comando '{comando}' desconhecido.")
            mostrar_ajuda()

    except Exception as e:
        # Um "pega-tudo" simples para erros inesperados
        print(f"🔥 Ocorreu um erro inesperado: {e}")

# Ponto de entrada do script
if __name__ == "__main__":
    main()