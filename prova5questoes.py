# Gabarito da prova
GABARITO = ["B", "C", "A", "E", "D"]

# Lista para armazenar as respostas do usuário
respostas = []

# Usuário responde cada questão
for i in range(5):
    resposta = input(f"Digite a resposta da questão {i+1}: ").upper()
    respostas.append(resposta)

# Contar acertos
acertos = 0
for i in range(5):
    if respostas[i] == GABARITO[i]:
        acertos += 1

print(f"\nVocê acertou {acertos} de 5 questões.")
