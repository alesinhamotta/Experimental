# Exercício - Sequência de Fibonacci até 2000

a, b = 0, 1

print("Sequência de Fibonacci até 2000:")
while a <= 2000:
    print(a, end=" ")
    a, b = b, a + b  # atualiza os valores