# Variável constante:
# As boas práticas para nomes de variáveis são:
# - Constantes: nomes de variáveis em MAIÚSCULO.
# - Variáveis: nomes de variáveis em minúsculo.
# 
# Exemplo:
#
PI = 3.14                                          # variável PI recebe 3.14
raio = float(input('Digite o raio do círculo: '))  # Digite o raio do círculo: 2
area = PI * raio ** 2                              # variável area recebe PI vezes raio ao quadrado
print(area)                                        # Exibe 12.56

# As boas práticas para condições são:
# Não usar muitas condições no mesmo 'if'
# Não usar muitas condições no mesmo 'elif'
# Não usar muitas condições no mesmo 'else'
#
# Exemplo:
#
if carro == 'audi':                               # Se carro for igual a audi
   print('Tem certeza que não prefere outro?')    # Exibe 'Tem certeza que não prefere outro?'
 elif carro == 'bmw':                             # Se carro for igual a bmw
   print('Tem certeza que não prefere outro?')    # Exibe 'Tem certeza que não prefere outro?'
 elif carro == 'ferrari':                         # Se carro for igual a ferrari
   print('Tem certeza que não prefere outro?')    # Exibe 'Tem certeza que não prefere outro?'
 else:                                            # Se não
   print('Não sei, tente outro.')                 # Exibe 'Não sei, tente outro.'
