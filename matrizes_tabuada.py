#Demonstração de matrizes em Python
tabuada=[]
for x in range (1,10):
    linhas=[]
    for y in range (1,10):
        linhas.append(x*y)
    tabuada.append(linhas)
    
for tabela in tabuada:
    print(tabela)