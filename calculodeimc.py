# calculo de IMC 
# Solicita ao usuário o peso e a altura
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

# Calcula o IMC -> fórmula: peso / (altura * altura)
imc = peso / (altura ** 2)

# Exibe o resultado do IMC com duas casas decimais
print("Seu IMC é:", round(imc, 2))

# Estrutura condicional para verificar a situação
if imc > 25:
    print("Acima do peso ideal.")
elif imc < 18:
    print("Abaixo do peso ideal.")
else:
    print("O seu peso está OK.")
