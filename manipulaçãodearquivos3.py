# Criar e escrever em um arquivo
with open("teste.txt", "w") as arquivo:
    arquivo.write("Olá, mundo!\n")
    arquivo.write("Aprendendo Python.\n")

# Ler o conteúdo do arquivo
with open("teste.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:\n", conteudo)

# Adicionar mais texto no arquivo (modo append)
with open("teste.txt", "a") as arquivo:
    arquivo.write("Nova linha adicionada.\n")

