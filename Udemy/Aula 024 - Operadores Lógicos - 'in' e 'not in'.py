# Operadores 'in' e 'not in':
#
# 'in' verifica se um valor está presente em uma lista.
# 'not in' verifica se um valor não está presente em uma lista.
#
# Exemplo:

lista = ['maçã', 'banana', 'laranja']        # variável lista recebe [maçã, banana, laranja]

if 'maçã' in lista:                          # Se 'maçã' estiver presente na lista
  print('A maçã está na lista')              # Exibe 'A maçã está na lista'

if 'pera' not in lista:                      # Se 'pera' não estiver presente na lista
  print('A pera não está na lista')          # Exibe 'A pera não está na lista'

# Exemplo:

entrada = input('Digite uma fruta: ')        # Digite uma fruta: maçã

if entrada in lista:                         # Se entrada estiver presente na lista
  print(f'{entrada} está na lista')          # Exibe entrada está na lista
  
else:                                        # Se não
  print(f'{entrada} não está na lista')      # Exibe entrada não está na lista

# Exemplo 2:

nome = 'Bruno'                               # variável nome recebe Bruno

if 'u' in nome:                              # Se 'u' estiver presente na variável nome
  print('A letra u está presente no nome')   # Exibe 'A letra u está presente no nome'