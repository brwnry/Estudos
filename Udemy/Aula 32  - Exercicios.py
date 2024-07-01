'''
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. 
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
'''
# Bruno:

try:
  num = int(input('Digite um número inteiro: '))
  if num % 2 == 0: 
    print('O número é par') 
  else: 
    print('O número é ímpar')
except ValueError:
  print('Não é um número inteiro.')

# IA:

try:
  entrada_usuario = int(input('Digite um número inteiro: '))
  if entrada_usuario % 2 == 0:
      resultado = 'par'
  else:
      resultado = 'ímpar'
  print(f'O número é {resultado}')
except ValueError:
  print('Não é um número inteiro.')

'''
Faça um programa que pergunte a hora ao usuário e, basenado-se no horário descrito, exiba a saudação apropriada. 
Ex. Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''
# Bruno:

try:
  hora = int(input('Digite a hora: '))
  if hora >= 0 and hora <= 11:
    saudacao = 'Bom dia!'
  elif hora >= 12 and hora <= 17:
    saudacao = 'Boa tarde!'
  elif hora >= 18 and hora <=23:
    saudacao = 'Boa noite!'
  else:
    saudacao = 'As horas devem estar entre 0 e 23.'
  print(saudacao)
except ValueError:
  print('Favor digitar um valor em números. ')

# IA

hora = int(input("Digite a hora (0-23): "))

if 0 <= hora < 12:
    print("Bom dia!")
elif 12 <= hora < 18:
    print("Boa tarde!")
else:
    print("Boa noite!")
  
'''
Faça um programa que peça o primeiro nome do usuário. 
Se o nome tiver 4 letras ou menos escreva "seu nome é curto"; se tiver entre 5 e 6 letras,
escreva "seu nome é normal"; maior que 6 escreva "seu nome é muito grande".
'''
# Bruno:

try:
  nome = str(input('Digite seu nome: '))
  if len(nome) <=4:
    print('Seu nome é curto')
  elif len(nome) >=5 and len(nome) <=6:
    print('Seu nome é normal')
  else:
    print('Seu nome é grande')
except ValueError:
  print('Você digitou incorretamente')

# IA

nome = input("Digite o seu primeiro nome: ")

if len(nome) <= 4:
    print("Seu nome é curto.")
elif 5 <= len(nome) <= 6:
    print("Seu nome é normal.")
else:
    print("Seu nome é muito grande.")
