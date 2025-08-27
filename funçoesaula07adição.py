# demonstração do uso de funções 
def adição ( x , y):
    w = x + y
    return w
def subtração ( x , y ):
    return x - y

print (" Digite dois valores inteiro...")
N1 = int( input ("x:"))
N2 = int ( input ("y:"))
OP = input (" Qual operação (+ ou -)?")

if OP == "+":
    z = adição (N1,N2)
    print ("Resultado a soma:",z)
elif OP == "-":
    z = subtração (N1, N2)   
    print (" Resultado da subtração:",z)
else:
    print("Opção digitada inexistente!")