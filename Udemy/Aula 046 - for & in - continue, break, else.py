# Comando 'for' utilizando continue, break e else:

if i == 2: # se i for igual a 2, faça:
  print('i é 2, pulando...') # imprima 'i é 2, pulando...'
  continue # pule para a próxima repetição

if i == 8: # se i for igual a 8, faça:
  print('i é 8, seu else não executará') # imprima 'i é 8, seu else não executará'
  break # pare o loop

for j in range(1, 3): # para cada j no intervalo de 1 a 2, faça:
  print(i, j) # imprima i e j

else: # se não, faça:
  print('For completo com sucesso!') # imprima 'For completo com sucesso!'


