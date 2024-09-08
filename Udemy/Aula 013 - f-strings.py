# F-strings são strings formatadas.
#
# Exemplos:
#  
nome = 'João'                                             # variável nome recebe 'João'
altura = 1.75                                             # variável altura recebe 1.75
peso = 80                                                 # variável peso recebe 80
imc = peso / (altura * altura)                            # variável imc recebe o resultado da divisão de peso por altura ao quad
#
print(f'{nome} tem {altura} de altura e pesa {peso} kg.') # João tem 1.75 de altura e pesa 80 kg.
print(f'O IMC de {nome} é {imc:.2f}')                     # O IMC de João é 23.33

# modo alternativo:

nome = 'João'                                             # variável nome recebe 'João'
altura = 1.75                                             # variável altura recebe 1.75
peso = 80                                                 # variável peso recebe 80
imc = peso / (altura * altura)                            # variável imc recebe o resultado da divisão de peso por altura ao quad

lin1 = f'{nome} tem {altura} de altura e pesa {peso} kg.' # variável lin1 recebe a string formatada
lin2 = f'O IMC de {nome} é {imc:.2f}'                     # variável lin2 recebe a string formatada
print(lin1)                                               # imprime a variável lin1
print(lin2)                                               # imprime a variável lin2

# A formatação :.2f é para mostrar apenas 2 casas decimais.

