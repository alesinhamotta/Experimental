#demonstração de acesso a lista 

print ("Vou montar minha marmita com 5 alimentos")
marmita=[ "feijão", "arroz","legumes","salada", "carne"]
print ("Essa é a nossa recomendação:", marmita)

resposta = input (" Quer montar uma marmita diferente (S/N)?")
if resposta == "S":
    for x in range (len(marmita)):
        print(f"Digite o {x+1}o. item do cardápio:")
        marmita[x] = input ()
        print ("A marmita montada foi", marmita)
        print (" Os três primeiros itens foram:", marmita [0:3])
        print (" O ultimo item da marmita foi:", marmita [-1])
    else:
     print ("Ok. Você decide...")       
     print (marmita [:])
     print (marmita [2:3])
     print (marmita[0:4:2])
     print (marmita[-3:-1])