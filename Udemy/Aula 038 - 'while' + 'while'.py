# while + while (laços internos):

i = 1 # int
while i <= 10: # enquanto i for menor ou igual a 10, faça:
   j = 1 # int
   while j <= 10: # enquanto j for menor ou igual a 10, faça:
      print(i, j) # imprima i e j
      j += 1 # some 1 a j

   i += 1 # some 1 a i

# Exemplo:

qtd_linhas = 5 # int
qtd_colunas = 5 # int

linha = 1 # int
while linha <= qtd_linhas: # enquanto linha for menor ou igual a qtd_linhas, faça:
  coluna = 1 # int
  while coluna <= qtd_colunas: # enquanto coluna for menor ou igual a qtd_colunas, faça:
    print(f'{linha=} {coluna=}') # imprima linha e coluna
    coluna += 1 # some 1 a coluna
  linha += 1 # some 1 a linha

