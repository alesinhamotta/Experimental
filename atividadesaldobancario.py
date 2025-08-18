# Programa saldo bancário valor do produto 
print("Digite a seu saldo bancário: ")
saldo = float(input())
print("Digite o valor do produto:")
produto = float(input())
valor_disponivel = saldo - produto 
print("Seu saldo é:", valor_disponivel)

if valor_disponivel <-0:
    print( " Você não tem saldo suficiente!")
    print( "Não poderá realizar operações bancárias!")

elif valor_disponivel >=10:
    print("seu saldo esta baixo")
    print("Podemos oferecer suporte técnivo ")

else: 
    print("Você tem saldo suficiente para sua compra .")
    print("Portanto, poderá realizar quando quiser!")
    
    print (" Obrigado por escolher os nossos serviços! ")

