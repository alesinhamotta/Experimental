# Função para programas infantis
def programas_infantis():
    print("\n🎬 Programas infantis disponíveis:")
    programas = ["Peppa Pig", "Galinha Pintadinha", "Turma da Mônica", "Patrulha Canina", "Hora da Aventura"]
    for p in programas:
        print("-", p)

# Função para carros e preços
def lista_carros():
    print("\n🚗 Lista de carros e seus preços:")
    carros = {
        "Fiat Uno": "R$ 35.000",
        "Chevrolet Onix": "R$ 75.000",
        "Toyota Corolla": "R$ 140.000",
        "Honda Civic": "R$ 160.000",
        "BMW Série 3": "R$ 320.000"
    }
    for carro, preco in carros.items():
        print(f"- {carro}: {preco}")

# Programa principal
idade = int(input("Digite a sua idade: "))

if idade < 18:
    programas_infantis()
else:
    lista_carros()
