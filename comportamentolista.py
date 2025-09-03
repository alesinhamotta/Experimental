#Demonstração do comportamento das listas...
print(" Vou almoçar em um restaurante a quilo!")

original=["arroz","feijão","batata","alface","frango"]
print(" Eis, a minha comida:",original)
derivada = original
print (" Meu amigo irá comer também:", derivada)

print(" Vou alterar as opçãoes sem ele ver...")
original.remove("arroz")
original.remove("feijão")
original.remove("alface")
original.append("picanha")
original.append("linguiça")

print(" Amiguinho, me mostre o que você vai comer?")
print(" Claro! Dá uma conferida",derivada)