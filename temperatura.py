print("=== Conversor de Temperaturas ===")
print("Escolha a unidade de origem:")
print("1 - Celsius")
print("2 - Kelvin")
print("3 - Fahrenheit")

try:
    opcao = int(input("Digite a opcao (1/2/3): "))
    # aceita virgula como decimal
    valor = float(input("Digite o valor da temperatura: ").replace(",", "."))
except ValueError:
    print("Entrada invalida. Use apenas numeros.")
    raise SystemExit

if opcao == 1:  # Celsius
    kelvin = valor + 273.15
    fahrenheit = (valor * 9/5) + 32
    print(f"{valor} C = {kelvin:.2f} K")
    print(f"{valor} C = {fahrenheit:.2f} F")

elif opcao == 2:  # Kelvin
    celsius = valor - 273.15
    fahrenheit = (valor - 273.15) * 9/5 + 32
    print(f"{valor} K = {celsius:.2f} C")
    print(f"{valor} K = {fahrenheit:.2f} F")

elif opcao == 3:  # Fahrenheit
    celsius = (valor - 32) * 5/9
    kelvin = (valor - 32) * 5/9 + 273.15
    print(f"{valor} F = {celsius:.2f} C")
    print(f"{valor} F = {kelvin:.2f} K")

else:
    print("Opcao invalida! Escolha 1, 2 ou 3.")


