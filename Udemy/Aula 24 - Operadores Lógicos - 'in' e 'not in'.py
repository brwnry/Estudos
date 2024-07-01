# Operadores 'in' e 'not in':
#
# 'in' verifica se um valor está presente em uma lista.
# 'not in' verifica se um valor não está presente em uma lista.
#
# Exemplo:

lista = ['maçã', 'banana', 'laranja'] # ['maçã', 'banana', 'laranja']

if 'maçã' in lista: # True
  print('A maçã está na lista') # A maçã está na lista

if 'pera' not in lista: # True
  print('A pera não está na lista') # A pera não está na lista

# Exemplo:

entrada = input('Digite uma fruta: ') # maçã

if entrada in lista: # True
  print(f'{entrada} está na lista') # {entrada} está na lista
  
else: # False
  print(f'{entrada} não está na lista') # {entrada} não está na lista
  
# Exemplo:

entrada = input('Digite uma fruta: ') # banana

if entrada in lista: # True
  print(f'{entrada} está na lista') # {entrada} está na lista

else: # False
  print(f'{entrada} não está na lista') # {entrada} não está na lista
  
  