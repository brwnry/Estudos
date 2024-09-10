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
condição = True                             # variável condição recebe True
#
if not condição:                            # Se condição for falsa
   print('A condição é verdadeira')         # Exibe 'A condição é verdadeira'

else:                                       # Se não
   print('A condição é falsa')              # Exibe 'A condição é falsa'

# Exemplo:

entrada = input('[E]ntrar [S]air: ')        # Digite entrar ou sair sair
senha = input('Senha:')                     # Digite a senha: 1234

if not senha:                               # Se senha não for digitada
   print('Você não digitou a senha')        # Exibe 'Você não digitou a senha'

elif entrada == 'E' and senha == '123456':  # Se entrada for igual a E e senha for igual a 123456
   print('Você entrou no sistema')          # Exibe 'Você entrou no sistema'

else:                                       # Se não
   print('Você saiu do sistema')            # Exibe 'Você saiu do sistema'

