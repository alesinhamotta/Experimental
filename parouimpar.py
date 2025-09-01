# Função para verificar vencedor
def par_ou_impar(numero_computador, numero_usuario):
    soma = numero_computador + numero_usuario
    print(f"\nComputador jogou: {numero_computador}")
    print(f"Usuário jogou: {numero_usuario}")
    print(f"Soma = {soma}")

    if soma % 2 == 0:  # se for par
        print("Resultado: PAR → Usuário venceu! 🎉")
    else:
        print("Resultado: ÍMPAR → Computador venceu! 🤖")

# Programa principal
print("=== Jogo de Par ou Ímpar ===")
numero_computador = int(input("Digite o número do computador: "))
numero_usuario = int(input("Digite o seu número: "))

par_ou_impar(numero_computador, numero_usuario)
