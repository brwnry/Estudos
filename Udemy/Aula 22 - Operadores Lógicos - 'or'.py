# Operador Lógico 'or':

# Se pelo menos uma condição for verdadeira, o resultado será verdadeiro.

# Exemplo:

condição1 = True
condição2 = False
condição3 = False
condição4 = False

if condição1 or condição2 or condição3 or condição4: # True
   print('Pelo menos uma condição é verdadeira') # Pelo menos uma condição é verdadeira

else: # False
   print('Nenhuma condição é verdadeira') # Nenhuma condição é verdadeira

# Exemplo:

entrada = input('[E]ntrar [S]air: ') # E ou S
senha = input('Senha:')

senha_permitida = '123456'
if (entrada == 'E' or entrada == 'e') and senha == senha_permitida: # True
   print('Você entrou no sistema') # Você entrou no sistema

else: # False
   print('Você saiu do sistema') # Você saiu do sistema