# calculo de média de nota do aluno 
# Solicita ao usuário as quatro notas trimestrais
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Calcula a média das notas
media = (nota1 + nota2 + nota3 + nota4) / 4

# Verifica se o aluno foi aprovado ou reprovado
if media >= 6:
    print("Aluno aprovado! Média:", media)
else:
    print("Aluno reprovado! Média:", media)
