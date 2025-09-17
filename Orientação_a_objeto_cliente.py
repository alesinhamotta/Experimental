# Demonstração de OOP em python
class Cliente:
    def __init__(self, titular, conta, saldo):
        self.titular = titular
        self.conta = conta
        self.saldo = saldo

    def apresentar(self):
        print("Olá! Eu sou", self.titular)
        print("Minha conta é:", self.conta)
        print("E quero saber o meu saldo.")

# Para criar uma instância baseada na classe Cliente
fulano = Cliente("João", "423.050205-21", 25000.00)

# Executando o método da instância criada
fulano.apresentar()

# Acessando os atributos da instância criada
print("De fato, você realmente é", fulano.titular)
