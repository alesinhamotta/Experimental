contador = 0; time=""
while time!= "Flamengo":
    print (" Qual é o melhor clube de futebol do Brasil?")
    time=input()
    if time =="Flamengo":
        print ("Time correto")
        
    else:
        print ("time errado...")
    contador += 1
    if contador == 3:
        print ( "3 tentativas excedidas!")
    break
       