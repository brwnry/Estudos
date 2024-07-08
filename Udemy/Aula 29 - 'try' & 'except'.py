# Introdução ao try/except:

# try -> tenta executar o código.
# except -> se der erro, executa o código.
# else -> se não der erro, executa o código.
# finally -> sempre executa o código.

# Exemplos:
#
try: # tente:
  valor = int(input('Digite o valor do seu produto: ')) # Digite o valor do seu produto: 10
  print(valor) # 10

except ValueError: # se ValueError for lançado, faça:
  print('Favor digitar um valor em números. ') # Favor digitar um valor em números.