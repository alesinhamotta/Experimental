# Exercício 2 - Ordem dos números 
 
x = int(input("Digite o número X: ")) 
y = int(input("Digite o número Y: ")) 
z = int(input("Digite o número Z: ")) 
 
if x < y and y < z: 
    print("Os números estão em ordem crescente!") 
elif x > y and y > z: 
    print("Os números estão em ordem decrescente!") 
else: 
    print("Eles estão misturados!")