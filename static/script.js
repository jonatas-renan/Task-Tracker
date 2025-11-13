/* ==================================================================================
BLOCO 1: O "START" DO APLICATIVO
==================================================================================
*/

/* document.addEventListener: É o "ouvinte" principal do JavaScript.
 * 'DOMContentLoaded': É o nome do evento. Significa: "Quando toda a estrutura HTML 
 * (os tijolos e paredes) da página terminar de carregar, execute o código abaixo".
 * () => { ... }: É a função (arrow function) que contém todo o nosso aplicativo.
 *
 * Isso garante que o JavaScript não tente encontrar botões (como 'add-button') 
 * que ainda não existem na tela, evitando erros.
 */
document.addEventListener('DOMContentLoaded', () => {

/* ==================================================================================
BLOCO 2: O "MAPA" (VARIÁVEIS GLOBAIS E CONSTANTES)
==================================================================================
*/

  // Guarda o endereço da nossa API Flask para não termos que repeti-lo.
  const API_URL = 'http://127.0.0.1:5000/tasks';

  // Cria "controles remotos" em JavaScript para os elementos do nosso HTML.
  // document.getElementById('ID_DO_HTML') encontra o elemento no HTML pelo seu 'id'.
  const taskInput = document.getElementById('task-input'); // A caixa de digitar a tarefa
  const addButton = document.getElementById('add-button'); // O botão de "Adicionar"
  const taskList = document.getElementById('task-list');   // A <div> onde as tarefas vão aparecer

  // Controles remotos para os botões de filtro
  const filterAll = document.getElementById('filter-all');
  const filterTodo = document.getElementById('filter-todo');
  const filterProgress = document.getElementById('filter-progress');
  const filterDone = document.getElementById('filter-done');

/* ==================================================================================
BLOCO 3: AS "RECEITAS" (DEFINIÇÃO DAS FUNÇÕES)
==================================================================================
*/

  /* --- RECEITA 1: Buscar e Mostrar Tarefas (Método GET) ---
   * 'async' marca a função como "assíncrona", ou seja, ela vai
   * fazer operações de rede (que demoram) e precisa "esperar" (await).
   * (status = ''): Define um valor padrão. Se a função for chamada 
   * como fetchTasks(), o status será uma string vazia.
   */
  async function fetchTasks(status = '') {
    let url = API_URL; // Começa com a URL base

    // Se um status foi passado (ex: 'done'), adiciona ele na URL
    // A URL vira: http://127.0.0.1:5000/tasks?status=done
    if (status) url += `?status=${status}`;

    // 'try...catch' é o 'try...except' do Python. Tenta fazer o código.
    try {
      // 'await fetch(url)': PAUSA a função e ESPERA a API responder.
      // 'res' (response) é a resposta crua da API.
      const res = await fetch(url);
      
      // 'await res.json()': PAUSA de novo e ESPERA o "tradutor" 
      // (res.json()) converter o texto JSON em um objeto/lista JavaScript.
      const data = await res.json();
      
      // Chama a função que "desenha" os dados na tela.
      renderTasks(data);
      
    } catch { // Se a API estiver offline ou der erro, o 'catch' é executado.
      taskList.innerHTML = '<p style="color:red;">Erro ao carregar tarefas.</p>';
    }
  }

  /* --- RECEITA 2: Adicionar Nova Tarefa (Método POST) --- */
  async function addTask() {
    // Pega o texto da caixa de input e .trim() remove espaços em branco inúteis.
    const description = taskInput.value.trim();

    // Validação: Se a caixa estiver vazia, não faz nada.
    if (!description) return alert('Digite uma tarefa!');

    // 'await fetch(...)': Envia a requisição para a API
    await fetch(API_URL, {
      method: 'POST', // Método HTTP para CRIAR um novo recurso.
      headers: {
        // O "selo" do envelope, dizendo: "O conteúdo deste corpo é JSON".
        'Content-Type': 'application/json' 
      },
      // O "tradutor" do JS (igual ao json.dumps): Converte um objeto 
      // JavaScript { description: "..." } em uma STRING de texto JSON.
      body: JSON.stringify({ description })
    });

    // Depois de adicionar, limpa a caixa de input
    taskInput.value = '';
    // E busca a lista de tarefas atualizada na tela.
    fetchTasks();
  }

  /* --- RECEITA 3: Atualizar o Status da Tarefa (Método PATCH) --- */
  async function updateTaskStatus(id, status) {
    // A URL agora inclui o ID da tarefa (ex: /tasks/5)
    await fetch(`${API_URL}/${id}`, {
      method: 'PATCH', // Método HTTP para ATUALIZAR PARCIALMENTE um recurso.
      headers: {
        'Content-Type': 'application/json'
      },
      // Envia o novo status no corpo da requisição
      body: JSON.stringify({ status }) // ex: {"status": "done"}
    });
    
    // Atualiza a lista na tela (a depender do filtro, a tarefa pode sumir)
    // NOTA: Aqui, o fetchTasks() vai pegar o filtro que ESTÁ ATIVO no momento.
    // Se o filtro for 'to-do' e você marcar como 'done', ela vai sumir da lista!
    // Para evitar isso, teríamos que guardar o filtro atual em uma variável global.
    // Mas para este app, vamos manter simples e recarregar a lista inteira
    // (ou o filtro que o usuário clicou por último).
    
    // Vamos corrigir isso:
    // Pega o filtro que está ativo (ou recarrega tudo se for 'all')
    const filtroAtivo = document.querySelector('.filters button.active')?.dataset.filter || '';
    fetchTasks(filtroAtivo); // Recarrega a lista com o filtro correto
  }

  /* --- RECEITA 4: Deletar uma Tarefa (Método DELETE) --- */
  async function deleteTask(id) {
    // confirm() mostra uma caixa de "OK/Cancelar" no navegador.
    // Se o usuário clicar "Cancelar", a função para aqui (return).
    if (!confirm('Deseja realmente deletar esta tarefa?')) return;

    // A URL inclui o ID. O método é 'DELETE'.
    await fetch(`${API_URL}/${id}`, { method: 'DELETE' });

    // Atualiza a lista na tela.
    const filtroAtivo = document.querySelector('.filters button.active')?.dataset.filter || '';
    fetchTasks(filtroAtivo);
  }

  /* --- RECEITA 5: O "Desenhista" (Renderizar HTML) --- */
  // Esta função não é 'async' porque ela não faz requisições de rede.
  // Ela só trabalha com os dados que já recebeu.
  function renderTasks(tasks) {
    // 1. Limpa a lista atual (apaga todo o HTML de dentro da <div>)
    taskList.innerHTML = '';

    // 2. Se a lista de tarefas (tasks) estiver vazia...
    if (tasks.length === 0) {
      taskList.innerHTML = '<p>Nenhuma tarefa encontrada.</p>';
      return; // Para a execução da função aqui.
    }

    // 3. Loop "para cada" (forEach) - O "for task in tasks:" do Python
    tasks.forEach(task => {
      // 4. Cria novos elementos HTML "na memória" (ainda não estão na tela)
      
      // Cria a <div> principal do item da tarefa
      const div = document.createElement('div');
      div.className = 'task-item'; // Adiciona a classe CSS
      if (task.status === 'done') {
        div.classList.add('done'); // Adiciona uma classe extra se estiver 'done'
      }

      // Cria o <span> para o texto da tarefa
      const text = document.createElement('span');
      text.textContent = `[${task.id}] ${task.description}`;
      text.className = 'task-text';

      // Cria a <div> para os botões de ação
      const actions = document.createElement('div');
      actions.className = 'task-actions';

      // --- Lógica para criar botões condicionalmente ---
      
      // Se a tarefa NÃO estiver 'done', mostra o botão de Concluir
      if (task.status !== 'done') {
        const btnDone = document.createElement('button');
        btnDone.textContent = '✅ Concluir';
        btnDone.className = 'btn-done';
        // Define a AÇÃO do botão: ao clicar, chama a Receita 3 (update)
        btnDone.onclick = () => updateTaskStatus(task.id, 'done');
        actions.appendChild(btnDone); // Adiciona o botão na div de ações
      }

      // Se a tarefa estiver 'to-do', mostra o botão "Em progresso"
      if (task.status === 'to-do') {
        const btnProgress = document.createElement('button');
        btnProgress.textContent = '🚧 Em progresso';
        btnProgress.className = 'btn-progress';
        btnProgress.onclick = () => updateTaskStatus(task.id, 'in-progress');
        actions.appendChild(btnProgress);
      }
      
      // O botão de deletar sempre aparece
      const btnDelete = document.createElement('button');
      btnDelete.textContent = '🗑️ Deletar';
      btnDelete.className = 'btn-delete';
      // Define a AÇÃO: ao clicar, chama a Receita 4 (delete)
      btnDelete.onclick = () => deleteTask(task.id);
      actions.appendChild(btnDelete);

      // 5. "Monta o quebra-cabeça"
      div.appendChild(text);      // Coloca o texto dentro da <div> principal
      div.appendChild(actions); // Coloca a <div> de ações dentro da <div> principal

      // 6. ADICIONA NA TELA
      // Coloca a <div> principal (com tudo dentro) na <div> da lista
      taskList.appendChild(div);
    });
  }

/* ==================================================================================
BLOCO 4: OS "INTERRUPTORES" (LIGANDO OS EVENTOS)
==================================================================================
*/
  
  // Aqui conectamos nossas "Receitas" (Funções) aos nossos "Controles" (Botões).

  // Quando o botão de adicionar for clicado, executa a função addTask.
  addButton.onclick = addTask;

  // Quando uma tecla for pressionada DENTRO da caixa de input...
  taskInput.onkeypress = e => { 
    // ...verifica se a tecla pressionada (e.key) foi 'Enter'.
    if (e.key === 'Enter') {
      addTask(); // Se sim, executa a função addTask.
    }
  };

  // Funções de filtro
  // (Aqui, usamos () => ... para poder passar um argumento para a função)
  filterAll.onclick = () => fetchTasks(); // Chama fetchTasks com o padrão (vazio)
  filterTodo.onclick = () => fetchTasks('to-do'); // Chama fetchTasks com 'to-do'
  filterProgress.onclick = () => fetchTasks('in-progress');
  filterDone.onclick = () => fetchTasks('done');

/* ==================================================================================
BLOCO 5: A "IGNIÇÃO" (PRIMEIRA EXECUÇÃO)
==================================================================================
*/

  // Agora que tudo está definido (Receitas prontas, Botões ligados),
  // chamamos a função fetchTasks() pela primeira vez para carregar
  // a lista inicial de tarefas assim que a página abrir.
  fetchTasks();
});