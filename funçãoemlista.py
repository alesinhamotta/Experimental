#demosntração de funções e, listas...
print (" Eis, os meus maiores sonhos ...")
sonhos= ["1. Me divertir na dysney",
         "2. Me banhar na praia de sepetiba", 
         "3. Tiras férias em Paris",
         "4. Fazer compras no west shopping",
         "5. Ver as piramides do Egito"]
for x in sonhos:
    print (x)
    
    print (" Ops, não quero sepetiba!")
    del(sonhos [0])
    print(" E nem West Shopping...")
    del(sonhos[2])
    
    print (" Conferindo os sonhos...")
    for x in sonhos:
        print (x)