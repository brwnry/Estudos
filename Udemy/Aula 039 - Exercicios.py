nome = 'Tyler Durden'        # variável nome recebe 'Tyler Durden'
indice = 0                   # variável indice recebe 0
novo_nome = ''               # variável novo_nome recebe ''

# A variável indice é meramente um contador, que vai de 0 até o tamanho da string nome.
# A variável novo_nome é uma string vazia, que vai receber as letras da string nome.

while indice < len(nome):    # enquanto indice for menor que o tamanho de nome, faça:
  letra = nome[indice]       # variável letra recebe o caractere da string nome na posição indice
  novo_nome += f'*{letra}'   # variável novo_nome recebe '*' + letra 
  indice += 1                # some 1 a indice

novo_nome += '*'              # variável novo_nome recebe mais um '*'
print(novo_nome)              # imprima novo_nome

# Resultado:
# *T*y*l*e*r* *D*u*r*d*e*n