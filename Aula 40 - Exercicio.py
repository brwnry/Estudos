# Calculadora com 'while':

numero_1 = float(input('Digite o primeiro número: '))
numero_2 = float(input('Digite o segundo número: '))
operadores = input('Digite o operador: ( +, -, *, / )')

try:
  while operadores not in ('+', '-', '*', '/'):
    operadores = input('Digite o operador: ( +, -, *, / )')

  if operadores == '+':
    print(numero_1 + numero_2)

  elif operadores == '-':
    print(numero_1 - numero_2)

  elif operadores == '*':
    print(numero_1 * numero_2)

  elif operadores == '/':
    print(numero_1 / numero_2)

  else:
    print('Operador inválido')

except ValueError:
  print('Favor digitar um valor em números. ')
  


  




