# Lista para armazenar os clientes
cliente = []

# Cadastro dos 4 clientes
for i in range(4):
    nome = input(f"Digite o nome do cliente {i+1}: ")
    numero = input(f"Digite o número do telefone de {nome}: ")
    cliente.append({"nome": nome, "numero": numero})

print("\nLista de seus clientes:")
for aparelho in cliente:
    print(f"Modelo {aparelho['numero']} - {aparelho['nome']}")

# Substituições (máximo 1)
for i in range(1):
    resposta = input("\nDeseja fazer uma substituição? (s/n): ").lower()
    if resposta == "s":
        sair = input("Digite o nome do cliente que vai sair: ")
        entrar = input("Digite o nome do cliente que vai entrar: ")
        numero = input(f"Digite o número do celular de {entrar}: ")

        # Procurar o cliente  que vai sair e substituir
        for j in range(len(cliente)):
            if cliente[j]["nome"].lower() == sair.lower():
                cliente[j] = {"nome": entrar, "numero": numero}
                break

print("\nLista de clientes atualizada:")
for aparelho in  cliente:
    print(f"Modelo {aparelho['numero']} - {cliente['nome']}")
