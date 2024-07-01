# Introdução ao try/except:

# try -> tenta executar o código.
# except -> se der erro, executa o código.
# else -> se não der erro, executa o código.
# finally -> sempre executa o código.

# Exemplos:
#
try:
  valor = int(input('Digite o valor do seu produto: '))
  print(valor)

except ValueError:
  print('Favor digitar um valor em números. ')