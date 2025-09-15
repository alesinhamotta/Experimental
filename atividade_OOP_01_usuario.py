#Demonstrção de OOP em python 
class usuário:
    def __init__(self,nome,idade,altura):
        self.nome=nome
        self.idade=idade
        self.altura= altura
    def apresentar(self):
        print("Olá! me chamo:",self.nome)
        print("Minha idade é:",self.idade)
        print("E tenho de altura:",self.altura)
              
            
#instancia 
fulano= usuário ("Alessandra","43 anos", 1.70 )
fulano.apresentar()

#executando o método de intancia criada

def conferir (X):
    if X >=18:
        print("Você é maior de idade!")
    else:
        print ( " Ops , menor de idade não pode!")    
    
        
    
#Acessando os atributos das intancias criadas 
print ("Você tem essa idade:", fulano.idade)
print ("E tem essa altura:", fulano.altura)
