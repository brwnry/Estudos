# Exercício:
# Crie um código que calcula o IMC:

# Exemplo 1

nome = 'João'                                                 # variável nome recebe 'João'
altura = 1.75                                                 # variável altura recebe 1.75
peso = 80                                                     # variável peso recebe 80
imc = peso / (altura * altura)                                # variável imc recebe o resultado da divisão entre peso e altura ao quadrado

print(nome, 'tem', altura, 'de altura e pesa', peso, 'kg.')   # João tem 1.75 de altura e pesa 80 kg.
print('O IMC de', nome, 'é', imc)                             # O IMC de João é 23.333333333333332 

# Exemplo 2:

nome = 'João'                                                 # variável nome recebe 'João'
altura = 1.75                                                 # variável altura recebe 1.75
peso = 80                                                     # variável peso recebe 80
imc = peso / (altura ** 2)                                    # variável imc recebe o resultado da divisão entre peso e altura ao quadrado

print(nome, 'tem', altura, 'de altura e pesa', peso, 'kg.')   # João tem 1.75 de altura e pesa 80 kg.
print('O IMC de', nome, 'é', imc)                             # O IMC de João é 23.333333333333332 