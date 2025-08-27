# Exercício - Contagem regressiva

import time  # para dar uma pausa entre os números

print("Contagem regressiva:")

for i in range(10, -1, -1):  # começa em 10, vai até 0
    print(i)
    time.sleep(1)  # pausa de 1 segundo (opcional, só para ficar mais real)

print("🎉 Feliz Ano Novo!")
