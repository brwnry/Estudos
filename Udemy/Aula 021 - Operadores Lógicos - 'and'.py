# Operador Lógico 'and':

# Todas as condições precisam ser verdadeiras para que o resultado seja verdadeiro.
# Se uma condição for falsa, o resultado será falso.

# Exemplo:

condição1 = True                                        # variável condição1 recebe True
condição2 = True                                        # variável condição2 recebe True
condição3 = True                                        # variável condição3 recebe True
condição4 = True                                        # variável condição4 recebe True

if condição1 and condição2 and condição3 and condição4: # Se todas as condições forem verdadeiras
   print('Todas as condições são verdadeiras')          # Exibe 'Todas as condições são verdadeiras'

else:                                                   # Se não
   print('Pelo menos uma condição é falsa')             # Exibe 'Pelo menos uma condição é falsa'


# Exemplo:

entrada = input('[E]ntrar [S]air: ')                    # Digite entrar ou sair sair
senha = input('Senha:')                                 # Digite a senha: 1234

senha_permitida = '123456'                              # variável senha_permitida recebe 123456
if entrada == 'E' and senha == senha_permitida:         # Se entrada for igual a E e senha for igual a senha_permitida
   print('Você entrou no sistema')                      # Exibe 'Você entrou no sistema'

else:                                                   # Se não
   print('Você saiu do sistema')                        # Exibe 'Você saiu do sistema'
   