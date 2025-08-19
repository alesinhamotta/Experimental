# Solicita o nome do filme ou série
filme = input("Digite o nome do filme ou série que deseja avaliar: ")

# Solicita a nota
nota = int(input("De 1 a 5, qual a sua nota para esse conteúdo? "))

# Verifica a nota e responde de acordo
if nota == 1:
    print("Avaliação: Péssimo")
    motivo = input("Você poderia dizer por que achou tão ruim? ")
    print("Comentário registrado:", motivo)

elif nota == 2:
    print("Avaliação: Ruim")
    motivo = input("Gostaria de dizer por que não gostou? ")
    print("Comentário registrado:", motivo)

elif nota == 3:
    print("Avaliação: Razoável")

elif nota == 4:
    print("Avaliação: Bom")

elif nota == 5:
    print("Avaliação: Ótimo")

else:
    print("⚠️ Nota inválida! Digite apenas valores entre 1 e 5.")
