# Operação ternária com Python.
# Ou, simplesmente condicional de uma linha.
# <valor> if <condicao> else <valor>
#
# Exemplo:
digito = 9
novo_digito = digito if digito <= 9 else 0 # Se digito for menor ou igual a 9, o novo_digito será o próprio digito. Caso contrário, o novo_digito será 0.
print(novo_digito) # 9

# Exemplo 2:
digito = 10 
novo_digito = digito if digito <= 9 else 0 # novo_digito recebe o valor digito se digito for menor ou igual a 9, senão recebe 0
print(novo_digito) # 0

# Exemplo 3:
digito = 10
print(digito if digito <= 9 else 0) # Exibe o valor de digito se digito for menor ou igual a 9, senão exibe 0