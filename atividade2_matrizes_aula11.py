#atividade quadrado mágico matrizes em Python
print("Esse o é jogo quadrado mágico...")
contador=[[4,9,2],
         [3,5,7],
         [8,1,6]]

quadrado= int(input("Digite o numero:"))
for x in range(0,3):
    for y in range (0,3):
     contador = contador + quadrado[x][y]
        
print ("digite o numero:", quadrado)
print ("Confira o resultado das operações")
if contador == 15: 
   print(contador)