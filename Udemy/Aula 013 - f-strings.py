# F-strings são strings formatadas.
#
# Exemplos:
#  
nome = 'João' # string
altura = 1.75 # float
peso = 80 # int
imc = peso / (altura * altura) # float
#
print(f'{nome} tem {altura} de altura e pesa {peso} kg.') # João tem 1.75 de altura e pesa 80 kg.
print(f'O IMC de {nome} é {imc:.2f}') # O IMC de João é 23.33

# modo alternativo:

nome = 'João' # string
altura = 1.75 # float
peso = 80 # int
imc = peso / (altura * altura) # float

lin1 = f'{nome} tem {altura} de altura e pesa {peso} kg.' # João tem 1.75 de altura e pesa 80 kg.
lin2 = f'O IMC de {nome} é {imc:.2f}' # O IMC de João é 23.33
print(lin1) # João tem 1.75 de altura e pesa 80 kg.
print(lin2) # O IMC de João é 23.33

# A formatação :.2f é para mostrar apenas 2 casas decimais.

