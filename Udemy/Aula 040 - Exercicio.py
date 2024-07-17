# Calculadora com 'while':

numero_1 = float(input('Digite o primeiro número: '))  # float
numero_2 = float(input('Digite o segundo número: '))  # float
operadores = input('Digite o operador: ( +, -, *, / )')  # str

try:  # try -> tenta executar o código.
  while operadores not in (
      '+', '-', '*',
      '/'):  # enquanto operadores não estiver em ('+', '-', '*', '/'), faça:
    operadores = input('Digite o operador: ( +, -, *, / )')  # str

  if operadores == '+':  # se operadores for igual a '+', faça:
    print(numero_1 + numero_2)  # imprima numero_1 + numero_2

  elif operadores == '-':  # se operadores for igual a '-', faça:
    print(numero_1 - numero_2)  # imprima numero_1 - numero_2

  elif operadores == '*':  # se operadores for igual a '*', faça:
    print(numero_1 * numero_2)  # imprima numero_1 * numero_2

  elif operadores == '/':  # se operadores for igual a '/', faça:
    print(numero_1 / numero_2)  # imprima numero_1 / numero_2

  else:  # se não, faça:
    print('Operador inválido')  # imprima 'Operador inválido'

except ValueError:  # except -> se der erro, executa o código.
  print('Favor digitar um valor em números. '
        )  # imprima 'Favor digitar um valor em números. '
