# Função que recebe nome e cidade como argumentos
def boas_vindas(nome, cidade):
    if cidade.strip().lower() == "rio de janeiro":
        print(f"\nOlá {nome}, seja bem-vindo à Cidade Maravilhosa! 🏖️")
    else:
        print(f"\nOlá {nome}, você está em {cidade}.")

# Programa principal
nome = input("Digite seu nome: ")
cidade = input("Digite a cidade de onde está digitando: ")

boas_vindas(nome, cidade)
