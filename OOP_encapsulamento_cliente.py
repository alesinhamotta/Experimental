#Demonstracão de OOP em python
from abc import ABC,abstractmethod
class cliente:
    @abstractmethod
    def __init__(self, titular, conta, saldo):
        self.titular= titular
        self.__conta =conta
        self.__saldo = saldo
class cliente_fisico (cliente):
    def apresentar(self):
        print ("Olá Eu sou", self.titular)
        print ("Minha conta é",self.__conta)
        print ("Eu quero saber meu saldo")
        return
    
      #para criar uma instancia baseada na classe cliente 
    fulano= cliente ("João","423.050205-21",25000.00)
    #executando o método de intancia criada
    fulano.apresentar()
    
    #Acessando os atributos das intancias criadas 
    print ("De fato , você realmete é ", fulano.titular)
    print ("No momento, a sua conta possui R$", fulano.__saldo)