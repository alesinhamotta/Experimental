print("=== Meu Clube do Coração ===")

# Passo 1: perguntar a naturalidade
regiao = input("Você é carioca, paulista ou mineiro? ").strip().lower()

# Passo 2: sugerir times com base na região
if regiao == "carioca":
    clubes = ["Flamengo", "Fluminense", "Vasco", "Botafogo"]
elif regiao == "paulista":
    clubes = ["Corinthians", "Palmeiras", "São Paulo", "Santos"]
elif regiao == "mineiro":
    clubes = ["Atlético-MG", "Cruzeiro", "América-MG"]
else:
    clubes = []
    print("Ops! Não reconheci essa região...")

# Passo 3: mostrar opções e perguntar a escolha
if clubes:
    print("Esses são alguns clubes da sua região:")
    for i, clube in enumerate(clubes, start=1):
        print(f"{i} - {clube}")

    escolha = int(input("Digite o número do seu clube do coração: "))

    if 1 <= escolha <= len(clubes):
        clube_escolhido = clubes[escolha - 1]
        print(f"Você escolheu o {clube_escolhido}! 🏆 Que orgulho ser torcedor!")
    else:
        print("Número inválido!")
