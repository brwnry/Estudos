# Introdução ao try/except:

# try -> tenta executar o código.
# except -> se der erro, executa o código.
# else -> se não der erro, executa o código.
# finally -> sempre executa o código.

# Exemplos:
#
try:                                                     # Tenta executar o código
  valor = int(input('Digite o valor do seu produto: '))  # Digite o valor do seu produto: 100
  print(valor)                                           # Exibe 100

# Mas suponha que o usuário digite uma letra ao invés de um número:

except ValueError:                                       # Se der erro
  print('Favor digitar um valor em números. ')           # Exibe 'Favor digitar um valor em números. '

# Ou se o usuário digitar um número negativo:

except ValueError:                                       # Se der erro
  print('Favor digitar um valor positivo. ')             # Exibe 'Favor digitar um valor positivo. '

# Ou se o usuário digitar um número decimal:

except ValueError:                                       # Se der erro
  print('Favor digitar um valor inteiro. ')              # Exibe 'Favor digitar um valor inteiro. '

# Exemplo 2:

num = input('Vou dobrar o número que vc digitar: ')       # Vou dobrar o número que vc digitar: 10
try:                                                      # Tenta executar o código
  num = int(num)                                          # num recebe o valor inteiro de num
  print(num * 2)                                          # Exibe 20
except ValueError:                                        # Se der erro
  print('Favor digitar um valor em números. ')            # Exibe 'Favor digitar um valor em números. '