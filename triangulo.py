# Exercício 3 - Triângulo 
 
a = int(input("Digite o lado A: ")) 
b = int(input("Digite o lado B: ")) 
c = int(input("Digite o lado C: ")) 
 
# Primeiro: verificar se forma triângulo 
if (a + b > c) and (a + c > b) and (b + c > a): 
    if a == b and b == c: 
        print("Triângulo Equilátero (todos os lados iguais)") 
    elif a == b or a == c or b == c: 
        print("Triângulo Isósceles (dois lados iguais)") 
    else: 
        print("Triângulo Escaleno (todos diferentes)") 
else: 
    print("Os valores não formam um triângulo!") 