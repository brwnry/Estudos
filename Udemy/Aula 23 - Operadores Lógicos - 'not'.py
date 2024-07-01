# Operador Lógico 'not':
#
# Se uma condição for verdadeira, o resultado será falso.
# Se uma condição for falsa, o resultado será verdadeiro.

# É usado para inverter expressões lógicas.
# not True = False
# not False = True
#
# # Exemplo:
#
condição = True
#
if not condição: # False
   print('A condição é verdadeira') # A condição é verdadeira

else: # True
   print('A condição é falsa') # A condição é falsa

# Exemplo:

entrada = input('[E]ntrar [S]air: ') # E ou S
senha = input('Senha:')

if not senha: # False
   print('Você não digitou a senha')

elif entrada == 'E' and senha == '123456': # True
   print('Você entrou no sistema')

else: # False
   print('Você saiu do sistema')

