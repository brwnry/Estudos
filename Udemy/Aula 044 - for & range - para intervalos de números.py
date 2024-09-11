# Usando 'for' e 'range' para percorrer um intervalo de números

# range serve para criar um intervalo de números 

# Criar um laço de repetição para percorrer um intervalo de números
# range -> range(star, stop, step)

numeros = range(1, 11, 2)   # variável numeros recebe um intervalo de 1 a 11, com passo de 2

for numero in numeros:      # para cada número na variável numeros, faça:
  print(numero)             # imprima número

# Resultado:
# 1
# 3
# 5
# 7
# 9