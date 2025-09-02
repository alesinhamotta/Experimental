# Gabarito
gabarito = ["B", "C", "A", "E", "D"]

respostas = []
acertos = 0

# Usuário responde
for i in range(5):
    r = input(f"Digite a resposta da questão {i+1}: ").upper()
    respostas.append(r)

# Contagem de acertos
for i in range(5):
    if respostas[i] == gabarito[i]:
        acertos += 1

print(f"\nVocê acertou {acertos} de 5 questões.")

