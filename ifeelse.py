# demonstração do uso de if/ else 
print("Digite a sua idade: ")
idade = int(input())

if idade < 18:
    print( " Você não é maior de idade!")
    print( "Não poderá realizar operações bancárias!")

elif idade >=65:
    print("Você está aposentado")
    print("Podemos oferecer suporte técnivo ")

else: 
    print("Você é maior de idade.")
    print("Portanto, poderá realizar operações bancárias!")
    
    print (" Obrigado por escolher os nossos serviços! ")
