# --- Etapa 1: Coleta de Dados do Usuário ---
# Usamos a função input() para exibir uma mensagem na tela e capturar
# o que o usuário digitar. O texto digitado é guardado em uma variável.

print("--- Preencha as informações para gerar a carta de demissão ---")

nome_empresa = input("Digite o nome da empresa: ")
nome_gestor = input("Digite o nome do gestor ou responsável do RH: ")
seu_cargo = input("Digite o seu cargo atual: ")
data_inicio_aviso = input("Digite a data de início do aviso prévio (ex: 01/08/2025): ")
data_termino_aviso = input("Digite a data de término do aviso prévio (ex: 30/08/2025): ")
local_e_data_atual = input("Digite o local e a data atual (ex: São Paulo, 12 de Agosto de 2025): ")
seu_nome_completo = input("Digite seu nome completo: ")


# --- Etapa 2: Montagem e Exibição da Carta ---
# Agora, vamos usar as variáveis que coletamos para montar a carta.
# A dica do exercício é usar "f-print", que na verdade se refere a "f-strings".
# Uma f-string permite colocar variáveis diretamente dentro de um texto.

# Usamos três aspas (""") para criar um texto de múltiplas linhas.
# Dentro do texto, colocamos as variáveis entre chaves {}.
# O Python substituirá automaticamente {nome_empresa} pelo conteúdo da variável nome_empresa, e assim por diante.

print("\n\n--- Sua Carta de Demissão Gerada ---") # \n cria uma linha em branco para separar
print("----------------------------------------")

carta_formatada = f"""
À {nome_empresa}

Prezado(a) {nome_gestor},

Venho por meio desta carta comunicar formalmente meu pedido de demissão do cargo de {seu_cargo}.

Estarei à disposição da empresa durante o aviso prévio, no período de {data_inicio_aviso} a {data_termino_aviso}.

Atenciosamente,


{local_e_data_atual}

_________________________
(Sua assinatura)

{seu_nome_completo}
"""

# --- Etapa 3: Imprimir o resultado final ---
# A variável 'carta_formatada' agora contém o texto completo.
# Só precisamos imprimi-la na tela para o usuário ver.

print(carta_formatada)
print("----------------------------------------")
print("Cópia gerada com sucesso! Use como referência para escrever a carta de próprio punho.")
