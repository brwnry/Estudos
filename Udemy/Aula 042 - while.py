# Criar um programa que conte as letras da frase, e mostre a quantidade de letras, \
# ignorando os espaços.
#
frase = 'O Python é uma linguagem de programação de alto nível,' \
'interpretada, de script, imperativa'

# Criar um índice para percorrer a frase
i = 0 # int

# Criar uma variável para armazenar a quantidade de letras
quantidade_de_letras = 0 # int

# Criar um laço de repetição para percorrer a frase
while i < len(frase): # enquanto i for menor que o tamanho da frase, faça:
  
# Criar uma condição para verificar se o caractere é uma letra
# Se for uma letra, incrementar a quantidade de letras
  
  if frase[i].isalpha(): # se frase[i] for uma letra, faça:
    quantidade_de_letras += 1 # quantidade_de_letras recebe quantidade_de_letras + 1

# Incrementar o índice
  i += 1 # i recebe i + 1

# Mostrar a quantidade de letras
print(f'A frase possui {quantidade_de_letras} letras.') # imprima 'A frase possui {quantidade_de_letras} letras.'

'''
______________________________________________________________________________________
'''

texto = 'Python' # string

i = 0 # int

while i < len(texto): # enquanto i for menor que o tamanho da string, faça:
  print(texto[i], i) # imprima texto[i] e i
  i += 1 # i recebe i + 1

