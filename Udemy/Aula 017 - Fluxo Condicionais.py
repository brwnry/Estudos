# Condicionais são usadas para tomar decisões em Python.
# If é usado para testar uma condição.
# Else é usado para executar um bloco de código caso a condição do if não seja atendida.
# Elif é usado para testar uma condição adicional caso a condição do if não seja atendida.

condição1 = False                                # variável condição1 recebe False
condição2 = False                                # variável condição2 recebe False
condição3 = False                                # variável condição3 recebe False
condição4 = False                                # variável condição4 recebe False

if condição1:                                    # Se condição1 for verdadeiro
  print('Código para condição 1')                # Exibe 'Código para condição 1'

elif condição2:                                  # Se condição2 for verdadeiro
  print('Código para condição 2')                # Exibe 'Código para condição 2'

elif condição3:                                  # Se condição3 for verdadeiro
  print('Código para condição 3')                # Exibe 'Código para condição 3'

elif condição4:                                  # Se condição4 for verdadeiro
  print('Código para condição 4')                # Exibe 'Código para condição 4'

else:                                            # Se não
  print('Nenhuma condição foi satisfeita.')      # Exibe 'Nenhuma condição foi satisfeita.'