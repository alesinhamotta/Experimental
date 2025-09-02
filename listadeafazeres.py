# Lista de tarefas
tarefas = []

# Cadastrar 5 tarefas
for i in range(5):
    tarefa = input(f"Digite a {i+1}ª tarefa: ")
    tarefas.append(tarefa)

print("\nSuas tarefas atuais:")
for i, tarefa in enumerate(tarefas, 1):
    print(f"{i}. {tarefa}")

# Perguntar se a primeira foi feita
resposta = input("\nA primeira tarefa já foi executada? (s/n): ").lower()

if resposta == "s":
    tarefas.pop(0)  # Remove a primeira tarefa
    nova = input("Digite uma nova tarefa para adicionar: ")
    tarefas.append(nova)

print("\nLista atualizada de tarefas:")
for i, tarefa in enumerate(tarefas, 1):
    print(f"{i}. {tarefa}")

