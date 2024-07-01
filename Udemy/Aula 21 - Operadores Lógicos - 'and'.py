# Operador Lógico 'and':

# Todas as condições precisam ser verdadeiras para que o resultado seja verdadeiro.
# Se uma condição for falsa, o resultado será falso.

# Exemplo:

condição1 = True
condição2 = True
condição3 = True
condição4 = True

if condição1 and condição2 and condição3 and condição4: # True
   print('Todas as condições são verdadeiras') # Todas as condições são verdadeiras

else:
   print('Pelo menos uma condição é falsa') # Pelo menos uma condição é falsa


# Exemplo:

entrada = input('[E]ntrar [S]air: ') # E ou S
senha = input('Senha:')

senha_permitida = '123456'
if entrada == 'E' and senha == senha_permitida: # True
   print('Você entrou no sistema') # Você entrou no sistema

else: # False
   print('Você saiu do sistema') # Você saiu do sistema
   