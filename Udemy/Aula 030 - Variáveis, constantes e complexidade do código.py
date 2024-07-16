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
if carro == 'audi': # Se carro for igual a 'audi', faça:
   print('Tem certeza que não prefere outro?') # Tem certeza que não prefere outro?
 elif carro == 'bmw': # Se carro for igual a 'bmw', faça:
   print('Tem certeza que não prefere outro?') # Tem certeza que não prefere outro?
 elif carro == 'ferrari': # Se carro for igual a 'ferrari', faça:
   print('Tem certeza que não prefere outro?') # Tem certeza que não prefere outro?
 else: # Se não for nenhum dos anteriores, faça:
   print('Não sei, tente outro.') # Não sei, tente outro.
