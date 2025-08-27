#Demosntração do uso de funções 
def apresentar():
    print (f"Meu nome é {MyName}.")
    print (f"Minha Altura é de {Myheigh} metros")
    print (f"Minha idade é {MyAge} anos")
    return
def conferir (X):
    if X >=18:
        print("Você é maior de idade!")
    else:
        print ( " Ops , menor de idade não pode!")    
        return
    MyName = str(input("Digite seu nome:"))
    MyHeigh = float(input("Gigite sua altura:"))
    MyAge = int(input("Digite sua idade:"))

apresentar()
conferir (Myheigh)

