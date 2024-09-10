# Operador Lógico 'or':

# Se pelo menos uma condição for verdadeira, o resultado será verdadeiro.

# Exemplo:

condição1 = True                                                    # variável condição1 recebe True   
condição2 = False                                                   # variável condição2 recebe False
condição3 = False                                                   # variável condição3 recebe False
condição4 = False                                                   # variável condição4 recebe False

if condição1 or condição2 or condição3 or condição4:                # Se pelo menos uma condição for verdadeira
   print('Pelo menos uma condição é verdadeira')                    # Exibe 'Pelo menos uma condição é verdadeira'

else:                                                               # Se não
   print('Nenhuma condição é verdadeira')                           # Exibe 'Nenhuma condição é verdadeira'

# Exemplo:

entrada = input('[E]ntrar [S]air: ')                                # Digite entrar ou sair sair
senha = input('Senha:')                                             # Digite a senha: 1234

senha_permitida = '123456'                                          # variável senha_permitida recebe 123456
if (entrada == 'E' or entrada == 'e') and senha == senha_permitida: # Se entrada for igual a E ou e e senha for igual a senha_permitida
   print('Você entrou no sistema')                                  # Exibe 'Você entrou no sistema'

else:                                                               # Se não   
   print('Você saiu do sistema')                                    # Exibe 'Você saiu do sistema'