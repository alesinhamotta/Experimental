# demosntração de operadores lógicos em condicionais 
print (" O que você vai fazer amanhã?")
print (" domrir/ estudar / planejar ")
manha = input()
print ( "O que você vai fazer amnhã de tarde?")
print ("jogar / treinar / trabalhar ")
tarde = input()

if not manha or not tarde:
    print (" Você precisa dizer o que vai fazer!")
else:
    if manha == "dormir" or tarde == "jogar":
        print (" Você esta disperdiçãndo o seu dia!")
    elif  manha == "estudar" or tarde == "treinar":
        print (" Que bom que você irá se aperfeiçoar !")
    elif manha == " planejar" and tarde == " trabalhar":
        print (" Para trabalhar melhor , devo planejar!")
    else:
        print (" Não combinamos essas ações...")
print (" tenha um bom dia!")