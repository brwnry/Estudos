# Criar um programa que conte as letras da frase, e mostre a quantidade de letras, \
# ignorando os espaços.
#
frase = 'O Python é uma linguagem de programação de alto nível,' \
'interpretada, de script, imperativa'

# Criar um índice para percorrer a frase
i = 0                                                          # variável i recebe 0

# Criar uma variável para armazenar a quantidade de letras
quantidade_de_letras = 0                                       # variável quantidade_de_letras recebe 0

# Criar um laço de repetição para percorrer a frase
while i < len(frase):                                          # enquanto i for menor que o tamanho de frase, faça: 

  # Criar uma condição para verificar se o caractere é uma letra
  # Se for uma letra, incrementar a quantidade de letras

  if frase[i].isalpha():                                       # se frase na posição i for uma letra, faça:
    quantidade_de_letras += 1                                  # some 1 a quantidade_de_letras

# Incrementar o índice
  i += 1                                                       # some 1 a i

# Mostrar a quantidade de letras
print(f'A frase possui {quantidade_de_letras} letras.')        # imprima 'A frase possui {quantidade_de_letras} letras.'

# Resultado:
# A frase possui 52 letras.


'''
______________________________________________________________________________________
'''

texto = 'Python'          # variável texto recebe 'Python'

i = 0                     # variável i recebe 0

while i < len(texto):     # enquanto i for menor que o tamanho de texto, faça:
  print(texto[i], i)      # imprima texto na posição i e i
  i += 1                  # some 1 a i

# Resultado:
# P 0
# y 1
# t 2
# h 3
# o 4
# n 5