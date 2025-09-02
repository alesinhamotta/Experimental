# Lista para armazenar os jogadores
time = []

# Cadastro dos 11 jogadores
for i in range(11):
    nome = input(f"Digite o nome do jogador {i+1}: ")
    numero = input(f"Digite o número da camisa de {nome}: ")
    time.append({"nome": nome, "numero": numero})

print("\nEscalação inicial do time:")
for jogador in time:
    print(f"Camisa {jogador['numero']} - {jogador['nome']}")

# Substituições (máximo 3)
for i in range(3):
    resposta = input("\nDeseja fazer uma substituição? (s/n): ").lower()
    if resposta == "s":
        sair = input("Digite o nome do jogador que vai sair: ")
        entrar = input("Digite o nome do jogador que vai entrar: ")
        numero = input(f"Digite o número da camisa de {entrar}: ")

        # Procurar o jogador que vai sair e substituir
        for j in range(len(time)):
            if time[j]["nome"].lower() == sair.lower():
                time[j] = {"nome": entrar, "numero": numero}
                break

print("\nEscalação atualizada:")
for jogador in time:
    print(f"Camisa {jogador['numero']} - {jogador['nome']}")

