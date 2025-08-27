# demonstração do uso de funções 
def multiplicação ( x , y):
    w = x * y
    return w
def divisão ( x , y ):
    return x / y

print (" Digite dois valores inteiro...")
N1 = int( input ("x:"))
N2 = int ( input ("y:"))
OP = input (" Qual operação (* ou /)?")

if OP == "*":
    z = multiplicação (N1,N2)
    print ("Resultado da multiplicação:",z)
elif OP == "/":
    z = divisão (N1, N2)   
    print (" Resultado da divisão:",z)
else:
    print("Opção digitada inexistente!")