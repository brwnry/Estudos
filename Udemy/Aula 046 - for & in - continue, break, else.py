# Comando 'for' utilizando continue, break e else:

for i in range(10):                        # para cada número na sequência de 0 a 10, faça:
  
  if i == 2:                                 # se i for igual a 2, faça:
    print('i é 2, pulando...')               # imprima 'i é 2, pulando...'
    continue                                 # pule para a próxima iteração do loop

  if i == 8:                                 # se i for igual a 8, faça:
    print('i é 8, seu else não executará')   # imprima 'i é 8, seu else não executará'
    break                                    # pare o loop

for j in range(1, 3):                      # para cada número de 1 a 3, faça:
  print(i, j)                              # imprima i e j

else:                                      # se não, faça:
  print('For completo com sucesso!')       # imprima 'For completo com sucesso!'

# Resultado:

# i é 2, pulando...
# i é 8, seu else não executará
# 8 1
# 8 2
# For completo com sucesso!