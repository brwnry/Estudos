# .format() é um método de string que permite formatar strings.
# Exemplo 1:
#
nome = 'João'                                                             # variável nome recebe 'João'
altura = 1.75                                                             # variável altura recebe 1.75
peso = 80                                                                 # variável peso recebe 80
imc = peso / (altura * altura)                                            # variável imc recebe o resultado da divisão de peso por altura ao quadrado
#
print('{} tem {} de altura e pesa {} kg.'.format(nome, altura, peso))     # João tem 1.75 de altura e pesa 80 kg.
print('O IMC de {} é {:.2f}'.format(nome, imc))                           # O IMC de João é 23.33

# Exemplo 2:
#
nome = 'João'                                                             # variável nome recebe 'João'
altura = 1.75                                                             # variável altura recebe 1.75
peso = 80                                                                 # variável peso recebe 80
imc = peso / (altura * altura)                                            # variável imc recebe o resultado da divisão de peso por altura ao quadrado
#
print('{0} tem {1} de altura e pesa {2} kg.'.format(nome, altura, peso))  # João tem 1.75 de altura e pesa 80 kg
