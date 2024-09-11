# Calculadora com 'while':

numero_1 = float(input('Digite o primeiro número: '))         # Digite o primeiro número: 
numero_2 = float(input('Digite o segundo número: '))          # Digite o segundo número: 
operadores = input('Digite o operador: ( +, -, *, / )')       # Escolha algum dos operadores

try:                                                          # tente:
  while operadores not in ('+', '-', '*', '/'):               # enquanto operadores não estiver em ('+', '-', '*', '/'), faça:
    operadores = input('Digite o operador: ( +, -, *, / )')   # Escolha algum dos operadores

  if operadores == '+':                                       # se operadores for igual a '+', faça:
    print(numero_1 + numero_2)                                # imprima numero_1 + numero_2

  elif operadores == '-':                                     # se operadores for igual a '-', faça:
    print(numero_1 - numero_2)                                # imprima numero_1 - numero_2

  elif operadores == '*':                                     # se operadores for igual a '*', faça:
    print(numero_1 * numero_2)                                # imprima numero_1 * numero_2

  elif operadores == '/':                                     # se operadores for igual a '/', faça:
    print(numero_1 / numero_2)                                # imprima numero_1 / numero_2

  else:                                                       # se não, faça:
    print('Operador inválido')                                # imprima 'Operador inválido'

except ValueError:                                            # se ValueError for lançado, faça:
  print('Favor digitar um valor em números. ')                # Mostra a mensagem de erro 'Favor digitar um valor em números. '