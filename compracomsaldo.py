# Solicita ao usuário o saldo da conta
saldo = float(input("Digite o saldo da sua conta: "))

# Solicita o valor do produto
valor_produto = float(input("Digite o valor do produto que deseja comprar: "))

# Calcula se há saldo suficiente
if saldo >= valor_produto:
    print("Compra realizada com sucesso!")
    saldo = saldo - valor_produto  # atualiza o saldo após a compra
    print("Saldo restante:", saldo)
else:
    print("Saldo insuficiente. Você não pode fazer essa compra.")
