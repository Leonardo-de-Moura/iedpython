

tarefas = []            # Lista principal de tarefas
historico = []          # Pilha para desfazer tarefas
fila_execucao = []      # Fila para executar tarefas
arquivo_tarefas = "tarefas.txt" # nome do arquivo de tarefas

def salvar_tarefas(): # função para salvar as tarefas no arquivo
    with open(arquivo_tarefas, 'w') as f: # abre o arquivo em modo de escrita
        for tarefa in tarefas: # percorre cada tarefa na lista
            f.write(tarefa + '\n') # escreve cada tarefa seguida de uma quebra de linha

def adicionar_tarefa(tarefa): #funcao adicionar_tarefa que adiciona as tarefas
    tarefas.append(tarefa) #metodo append chamado na lista tarefas para adicionar uma tarefa na lista
    historico.append(tarefa) #metodo append chamado na lista historico para adicionar uma tarefa na lista
    fila_execucao.append(tarefa)#metodo append chamado na lista fila_execucao para adicionar uma tarefa na lista da fila de execucao
    print(f"Tarefa '{tarefa}' adicionada!\n")#ao adicionar a tarefa nas listas, o print mostra a tarefa que foi adicionada

def desfazer_ultima_tarefa():# funcao desfazer_ultima_tarefa para desfazer a ultima tarefa
    if historico:#estrutura condicional que definira comandos para o caso de que historico ser true, no caso de ele existir
        ultima = historico.pop()#o metodo pop obtem o ultimo item da lista historico e atribui para a variavel ultima
        tarefas.remove(ultima) #o metodo remove, remove o item ultima da lista tarefas.
        fila_execucao.remove(ultima) #o metodo remove, remove o item ultima da lista de fila de execuçao
        print(f"Tarefa '{ultima}' desfeita!\n") # print mostra a ultima tarefa que foi desfeita
    else: #estrutura condicional conjunta ao if para representar o caso contrario
        print("Nenhuma tarefa para desfazer.\n") # print que mostra que nao existe nenhuma tarefa adicionada, e nem para remover

def atender_tarefa(): # funçao atender_tarefa para mudar status de conclusao da tarefa, ou seja, marca-la como "atendida"
    if fila_execucao: # estrutura condiconal que define comandos para o caso da lista fila de execuçao existir
        feita = fila_execucao.pop(0) # o metodo pop busca na posiçao 0, ou a primeira posiçao da fila de execuçao para atribuir na varivel feita
        tarefas.remove(feita) # o metodo remove, remove a variavel feita de dentro da lista tarefas
        print(f"Tarefa '{feita}' atendida!\n") # o print mostra que a tarefa foi atendida
    else: #estrutura condicional conjunta ao if para representar o caso contrario
        print("Nenhuma tarefa para atender.\n") # o print mostra que nao ha nenhuma tarefa pra atender
        
def mostrar_tarefas(): # funçao mostrar_tarefas 
    print("\n Lista de Tarefas:") # exibe o título da lista de tarefas
    for i, t in enumerate(tarefas): # loop que percorre a lista de tarefas com índice (i) e valor (t)
        print(f"{i + 1}. {t}") #  imprime cada tarefa com numeração a partir de 1
    print() # linha em branco para melhorar visualização

while True: # laço infinito para manter o menu em execução até o usuário sair
    print("1. Adicionar Tarefa") # opção de adicionar tarefa
    print("2. Desfazer Última Tarefa") # opção de desfazer última tarefa adicionada
    print("3. Atender Tarefa (modo fila)") # opção de atender tarefa na ordem em que foi adicionada
    print("4. Mostrar Tarefas") # opção de listar todas as tarefas atuais
    print("5. Sair") # opção para sair do programa

    opcao = input("Escolha uma opção: ") # recebe a opção digitada pelo usuário

    if opcao == '1': # verifica se a opção escolhida foi '1'
        tarefa = input("Digite a tarefa: ") # solicita ao usuário o nome da tarefa
        adicionar_tarefa(tarefa) # chama a função para adicionar a tarefa
    elif opcao == '2': # verifica se a opção foi '2'
        desfazer_ultima_tarefa() # chama a função para desfazer a última tarefa
    elif opcao == '3': # verifica se a opção foi '3'
        atender_tarefa() # chama a função para atender a próxima tarefa da fila
    elif opcao == '4': # verifica se a opção foi '4'
        mostrar_tarefas() # chama a função para mostrar as tarefas
    elif opcao == '5': # verifica se a opção foi '5'
        salvar_tarefas() # chama a função para salvar as tarefas no arquivo ao sair
        print("Tarefas salvas no arquivo.") # mensagem informando que as tarefas foram salvas
        print("Saindo do programa...") # mensagem de saída
        break # encerra o laço e finaliza o programa
    else: # caso o usuário digite uma opção inválida
        print("Opção inválida!\n") # informa que a opção não é válida
