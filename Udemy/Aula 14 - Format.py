# .format() é um método de string que permite formatar strings.
# Exemplo:
#
nome = 'João' # string
altura = 1.75 # float
peso = 80 # int
imc = peso / (altura * altura) # float
#
print('{} tem {} de altura e pesa {} kg.'.format(nome, altura, peso)) # João tem 1.75 de altura e pesa 80 kg.
print('O IMC de {} é {:.2f}'.format(nome, imc)) # O IMC de João é 23.33
