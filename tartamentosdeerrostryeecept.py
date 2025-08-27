#tartamento de erros try e except
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)

except ValueError:
    print("⚠️ Você precisa digitar um número válido!")

except ZeroDivisionError:
    print("⚠️ Não é possível dividir por zero!")

finally:
    print("Fim da execução do programa.")
