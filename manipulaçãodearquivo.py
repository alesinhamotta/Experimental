# Criando e escrevendo em um arquivo
with open("dados.txt", "w") as arquivo:
    arquivo.write("Linha 1: Olá mundo!\n")
    arquivo.write("Linha 2: Aprendendo Python.\n")

# Lendo o conteúdo do arquivo
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("\nConteúdo do arquivo:")
    print(conteudo)
