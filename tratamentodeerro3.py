# Exemplo simples de tratamento de erro
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)
except ValueError:
    print("Erro: você não digitou um número válido.")
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")

