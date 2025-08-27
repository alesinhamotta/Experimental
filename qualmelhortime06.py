# Demonstração de estrutura repetitiva 
# Exercício - Melhor Clube de Futebol

# Definindo a resposta correta dentro do programa
melhor_clube = "Flamengo"   # <-- aqui você pode trocar pelo time que quiser

# Pergunta inicial
resposta = input("Qual é o melhor clube de futebol do Brasil? ")

# Enquanto a resposta estiver incorreta, continua perguntando
while resposta.strip().lower() != melhor_clube.lower():
    print("❌ Resposta incorreta! Tente novamente...\n")
    resposta = input("Qual é o melhor clube de futebol do Brasil? ")

# Quando acertar, sai do laço e mostra a mensagem de acerto
print("🎉 Parabéns! Você acertou!")