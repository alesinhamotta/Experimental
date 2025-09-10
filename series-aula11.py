opcao=999
series= []; serviços=[];temporadas=[]
while opcao !=0:
    print("Escolha a operação:")
    print("1- Cadastar/ 2- Exibir/ 3- Editar/ 4- Excluir")
    opcao = int(input("Digite 0 para sai:"))
    
    if opcao ==1:
        serie= input("Digite o nome da série:")
        servico= input("Digite  nome do serviço:")
        temporada= input("Digite a temporada que já assistu:")
        series.append (serie); serviços.append(servico); temporadas.append(temporada)
        
print(series,serviços,temporadas)
        
