# 'while' & 'else'

string = 'Valor qualquer'     # variável string recebe 'Valor qualquer'

i = 0                        # variável i recebe 0
while i < len(string):       # enquanto i for menor que o tamanho de string, faça:
  letra = string[i]          # variável letra recebe o caractere da string string na posição i
  
  if letra == ' ':           # se letra for igual a ' ', faça:
    break                    # pare o loop
  
  print(letra )              # imprima letra
  i += 1                     # some 1 a i
else:                        # se não, faça:
  print('Fim da string')     # imprima 'Fim da string'

# Resultado:
# V
# a
# l
# o
# r
