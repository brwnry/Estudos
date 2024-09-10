# Condicionais são usadas para tomar decisões em Python.
# If é usado para testar uma condição.
# Else é usado para executar um bloco de código caso a condição do if não seja atendida.
# Elif é usado para testar uma condição adicional caso a condição do if não seja atendida.
#
# Exemplos:
#
if 10 > 5:                                         # Se 10 for maior que 5
     print('10 é maior que 5')                     # Exibe '10 é maior que 5'

if 10 < 5:                                         # Se 10 for menor que 5
     print('10 é menor que 5')                     # Exibe '10 é menor que 5'

if 10 > 5:                                         # Se 10 for maior que 5
     print('10 é maior que 5')                     # Exibe '10 é maior que 5'
  
else:                                              # Se não
     print('10 não é maior que 5')                 # Exibe '10 não é maior que 5'


entrada = input('Digite entrar ou sair ')          # Digite entrar ou sair sair

if entrada == 'entrar':                            # Se entrada for igual a entrar
    print('Você entrou no sistema')                # Exibe 'Você entrou no sistema'

elif entrada == 'sair':                            # Se entrada for igual a sair
    print('Você saiu do sistema')                  # Exibe 'Você saiu do sistema'

else:                                              # Se não     
    print('Você não digitou entrar ou sair')       # Exibe 'Você não digitou entrar ou sair'