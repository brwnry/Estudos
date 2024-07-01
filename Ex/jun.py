# o comando for é uma estrutura de repetição, que permite que você execute um bloco de código várias vezes.
#
for i in range(10): # range(10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  print(i) # imprima i

# Exemplos:
# Pegar um número variável de nomes e exibí-los em seguida:

qt_nomes = int(input('Quantos nomes você quer? ')) # int
for i in range(qt_nomes): # range(qt_nomes) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  nome = input('Digite um nome: ') # str
  print('nome #  {}' .format(i+1), nome)
