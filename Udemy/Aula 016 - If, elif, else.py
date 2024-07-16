# Condicionais são usadas para tomar decisões em Python.
# If é usado para testar uma condição.
# Else é usado para executar um bloco de código caso a condição do if não seja atendida.
# Elif é usado para testar uma condição adicional caso a condição do if não seja atendida.
#
# Exemplos:
#
if 10 > 5: # True
     print('10 é maior que 5') # 10 é maior que 5

if 10 < 5: # False
     print('10 é menor que 5') # Não será executado

if 10 > 5: # True
     print('10 é maior que 5') # 10 é maior que 5
  
else: # Não será executado
     print('10 não é maior que 5') # 10 não é maior que 5


entrada = input('Digite entrar ou sair ') # Digite entrar ou sair sair

if entrada == 'entrar': # False
    print('Você entrou no sistema') # Não será executado

elif entrada == 'sair': # True
    print('Você saiu do sistema') # Você saiu do sistema

else: # Não será executado
    print('Você não digitou entrar ou sair') # Você não digitou entrar ou sair