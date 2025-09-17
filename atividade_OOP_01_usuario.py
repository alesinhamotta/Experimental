# Demonstração de OOP em Python
class Usuario:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def apresentar(self):
        print("Olá! Meu nome é", self.nome)
        print("Minha idade é:", self.idade)
        print("Minha altura é:", self.altura)

    def verificar_maioridade(self):
        if self.idade >= 18:
            print("✅ Você é maior de idade!")
        else:
            print("⚠️ Ops, você é menor de idade e não pode acessar o sistema!")

# Criando uma instância do usuário
fulano = Usuario("Alessandra", 17, 1.70)

# Chamando os métodos
fulano.apresentar()
fulano.verificar_maioridade()

# Acessando atributos diretamente
print("Confirmando -> Nome:", fulano.nome)
print("Confirmando -> Idade:", fulano.idade)
print("Confirmando -> Altura:", fulano.altura)

