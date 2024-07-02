# 'while' & 'else'

string = 'Valor qualquer' # str

i = 0 # int
while i < len(string): # enquanto i for menor que o tamanho da string, faça:
  letra = string[i] # letra recebe string[i]
  print(letra ) # imprima letra
  i += 1 # i recebe i + 1
else: # se não, faça:
  print('Fim da string') # imprima 'Fim da string'
  
  