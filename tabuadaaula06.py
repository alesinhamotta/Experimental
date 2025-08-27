# aula 06 atividade multiplicar 
# Exercício - Tabuada

# O usuário digita um número
numero = int(input("Digite um número para ver a tabuada: "))

print(f"\nTabuada do {numero}")
print("-" * 20)

# Laço para gerar a tabuada de 1 até 10
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i:2} = {resultado}")

print("-" * 20)
