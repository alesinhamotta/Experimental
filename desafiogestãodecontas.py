# DESAFIO - Gestão de contas

saldo = 0.0
meta = float(input("Digite o valor da meta a ser alcançada: R$ "))

# Variáveis de controle
qtd_depositos = 0
qtd_saques = 0
valores_movimentados = []

while saldo < meta:
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("Escolha uma operação:")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":  # depósito
        valor = float(input("Digite o valor do depósito: R$ "))
        saldo += valor
        qtd_depositos += 1
        valores_movimentados.append(valor)

    elif opcao == "2":  # saque
        valor = float(input("Digite o valor do saque: R$ "))
        if valor <= saldo:
            saldo -= valor
            qtd_saques += 1
            valores_movimentados.append(valor)
        else:
            print("⚠️ Saldo insuficiente! Não é possível realizar este saque.")

    elif opcao == "3":  # sair manualmente
        print("Saindo do sistema...")
        break
    else:
        print("❌ Opção inválida! Tente novamente.")

# Relatório final
if valores_movimentados:  # evita divisão por zero
    media = sum(valores_movimentados) / len(valores_movimentados)
else:
    media = 0

print("\n===== RELATÓRIO FINAL =====")
print(f"Saldo final: R$ {saldo:.2f}")
print(f"Quantidade de depósitos: {qtd_depositos}")
print(f"Quantidade de saques: {qtd_saques}")
print(f"Total de operações: {len(valores_movimentados)}")
print(f"Média dos valores movimentados: R$ {media:.2f}")
print("============================")
