# demonstração de método em lista ...
inss= ["Maria","Manoel","José","Isabela"]
print("Eis, a lista do INSS:",inss)

novo=input("Insira mais uma pessoa:")
inss.append(novo)
print("Conferindo a nova lista:",inss)

print("Vou tirar a ultima pessoa dessa lista...")
especial=inss.pop()

print("agora, vou colocá-la na frente de todos:!")
inss.insert (0, especial)
print ("Conferindo a lista:",inss)

print (" Maria não gostou e reclamou...")
inss.remove ("Maria")
print ("E agora ela saiu `Pê da vida`",inss)

print(" para não ter mais reclamação vamos atender...")
inss.sort()
print("...em ordem alfabética:",inss)

print("Onde esta essa nova chamada", especial,"?")
print("Ela agora ficou na posição",inss.index(especial)+1,"!")