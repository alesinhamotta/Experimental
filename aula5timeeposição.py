# Exercício 1 - Classificação Campeonato Brasileiro 
 
time = input("Digite o nome do time: ") 
posicao = int(input("Digite a posição do time na tabela (1 a 20): ")) 
 
if posicao == 1: 
    print(time, "-> Campeão!") 
elif posicao >= 2 and posicao <= 6: 
    print(time, "-> Libertadores!") 
elif posicao >= 7 and posicao <= 12: 
    print(time, "-> Sul-Americana!") 
elif posicao >= 17 and posicao <= 20: 
    print(time, "-> Rebaixado!") 
elif posicao >= 13 and posicao <= 16: 
    print(time, "-> Escapou do rebaixamento!") 
else: 
    print("Posição inválida!") 