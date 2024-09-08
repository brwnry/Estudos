'''
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. 
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
'''
# Bruno:

try:                                                                    # tente:
  num = int(input('Digite um número inteiro: '))                        # Digite um número inteiro: 10
  if num % 2 == 0:                                                      # Se o resto da divisão de num por 2 for igual a 0, faça:
    print('O número é par')                                             # O número é par
  else:                                                                 # Se não, faça:
    print('O número é ímpar')                                           # O número é ímpar
except ValueError:                                                      # se ValueError for lançado, faça:
  print('Não é um número inteiro.')                                     # Não é um número inteiro.

# IA:

try:                                                                    # tente:
  entrada_usuario = int(input('Digite um número inteiro: '))            # Digite um número inteiro: 10
  if entrada_usuario % 2 == 0:                                          # Se o resto da divisão de num por 2 for igual a 0, faça:
    resultado = 'par'                                                   # resultado recebe 'par'
  else:                                                                 # Se não, faça:
    resultado = 'ímpar'                                                 # resultado recebe 'ímpar'
  print(f'O número é {resultado}')                                      # O número é par
except ValueError:                                                      # se ValueError for lançado, faça:
  print('Não é um número inteiro.')                                     # Não é um número inteiro.
'''
Faça um programa que pergunte a hora ao usuário e, basenado-se no horário descrito, exiba a saudação apropriada. 
Ex. Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''
# Bruno:

try:                                                                    # tente:
  hora = int(input('Digite a hora: '))                                  # Digite a hora: 10
  if hora >= 0 and hora <= 11:                                          # Se hora for maior ou igual a 0 e menor ou igual a 11, faça:
    saudacao = 'Bom dia!'                                               # saudacao recebe 'Bom dia!'
  elif hora >= 12 and hora <= 17:                                       # Se hora for maior ou igual a 12 e menor ou igual a 17, faça:
    saudacao = 'Boa tarde!'                                             # saudacao recebe 'Boa tarde!'
  elif hora >= 18 and hora <= 23:                                       # Se hora for maior ou igual a 18 e menor ou igual a 23, faça:
    saudacao = 'Boa noite!'                                             # saudacao recebe 'Boa noite!'
  else:                                                                 # Se não, faça:
    saudacao = 'As horas devem estar entre 0 e 23.'                     # saudacao recebe 'As horas devem estar entre 0 e 23.'
  print(saudacao)                                                       # imprima saudacao
except ValueError:                                                      # se ValueError for lançado, faça:
  print('Favor digitar um valor em números. ')                          # Favor digitar um valor em números.

# IA

hora = int(input("Digite a hora (0-23): "))                             # Digite a hora (0-23): 10

if 0 <= hora < 12:                                                      # Se hora for maior ou igual a 0 e menor que 12, faça:
  print("Bom dia!")                                                     # imprima 'Bom dia!'
elif 12 <= hora < 18:                                                   # Se hora for maior ou igual a 12 e menor que 18, faça:
  print("Boa tarde!")                                                   # imprima 'Boa tarde!'
else:                                                                   # Se não, faça:
  print("Boa noite!")                                                   # imprima 'Boa noite!'
'''
Faça um programa que peça o primeiro nome do usuário. 
Se o nome tiver 4 letras ou menos escreva "seu nome é curto"; se tiver entre 5 e 6 letras,
escreva "seu nome é normal"; maior que 6 escreva "seu nome é muito grande".
'''
# Bruno:

try:                                                                    # tente:
  nome = str(input('Digite seu nome: '))                                # Digite seu nome: Marcos
  if len(nome) <= 4:                                                    # Se o tamanho do nome for menor ou igual a 4, faça:
    print('Seu nome é curto')                                           # imprima 'Seu nome é curto'
  elif len(nome) >= 5 and len(nome) <= 6:                               # Se o tamanho do nome for maior ou igual a 5 e menor ou igual a 6,
    print('Seu nome é normal')                                          # imprima 'Seu nome é normal'
  else:                                                                 # Se não, faça:
    print('Seu nome é grande')                                          # imprima 'Seu nome é grande'
except ValueError:                                                      # se ValueError for lançado, faça:
  print('Você digitou incorretamente')                                  # Você digitou incorretamente

# IA

nome = input("Digite o seu primeiro nome: ")                            # Digite o seu primeiro nome: Marcos

if len(nome) <= 4:                                                      # Se o tamanho do nome for menor ou igual a 4, faça:
  print("Seu nome é curto.")                                            # imprima 'Seu nome é curto'
elif 5 <= len(nome) <= 6:                                               # Se o tamanho do nome for maior ou igual a 5 e menor ou igual a 6,
  print("Seu nome é normal.")                                           # imprima 'Seu nome é normal'
else:                                                                   # Se não, faça:
  print("Seu nome é muito grande.")                                     # imprima 'Seu nome é grande'
