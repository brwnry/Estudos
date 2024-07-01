# Variável constante:
# As boas práticas para nomes de variáveis são:
# - Constantes: nomes de variáveis em MAIÚSCULO.
# - Variáveis: nomes de variáveis em minúsculo.
# 
# Exemplo:
#
PI = 3.14
raio = float(input('Digite o raio do círculo: '))
area = PI * raio ** 2
print(area)

# As boas práticas para condições são:
# Não usar muitas condições no mesmo 'if'
# Não usar muitas condições no mesmo 'elif'
# Não usar muitas condições no mesmo 'else'
#
# Exemplo:
#
if carro == 'audi':
   print('Tem certeza que não prefere outro?')
 elif carro == 'bmw':
   print('Tem certeza que não prefere outro?')
 elif carro == 'ferrari':
   print('Tem certeza que não prefere outro?')
 else:
   print('Não sei, tente outro.')
