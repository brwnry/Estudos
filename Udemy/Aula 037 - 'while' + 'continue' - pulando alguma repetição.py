# 'while' + 'continue' - pulando alguma repetição.

i = 1             # variável i recebe 1
while i <= 10:    # enquanto i for menor ou igual a 10, faça:
  if i == 5:      # se i for igual a 5, faça:
    i += 1        # some 1 a i
    continue      # pule para a próxima iteração do loop
  print(i)        # imprima i
  i += 1          # some 1 a i

# Exemplo:

contador = 0                        # variável contador recebe 0

while contador <= 100:              # enquanto contador for menor ou igual a 100, faça:
  contador += 1                     # some 1 a contador
  if contador == 6:                 # se contador for igual a 6, faça:
    print('não vou mostrar o 6.')   # imprima 'não vou mostrar o 6.'
    continue                        # pule para a próxima iteração do loop

  print(contador)                   # imprima contador

if contador == 40:                  # se contador for igual a 40, faça:
  print('O contador chegou a 40.')  # imprima 'O contador chegou a 40.'
  break                             # pare o loop