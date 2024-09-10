# Fatiamento de strings & função 'len'.

 012345678
'Olá mundo'
 987654321

# Fatiamento [i:f:p]
# i = início
# f = fim
# p = passo

# Exemplo:
#
nome = 'Olá mundo'     # string
print(nome[0:4])       # Olá
print(nome[4:8])       # mund
print(nome[4:])        # mundo
print(nome[:4])        # Olá
print(nome[:])         # Olá mundo
print(nome[0:8:2])     # Oámn
print(nome[::2])       # Oámno
print(nome[::-1])      # odnum álO
print(nome[::-2])      # onmáO
print(nome[::-3])      # Ouá

# A função 'len' retorna o tamanho de uma string.
#
print(len(nome)) # 8