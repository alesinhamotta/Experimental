#Atividade 1 de matrizes em Python
soma=[]
for x in range (1,10):
    linhas=[]
    for y in range (1,10):
        linhas.append(x*y)
    soma.append(linhas)
    
for tabela in soma:
    print(tabela)