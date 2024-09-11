# while + while (laços internos):

i = 1                               # variável i recebe 1
while i <= 10:                      # enquanto i for menor ou igual a 10, faça:
   j = 1                            # variável j recebe 1
   while j <= 10:                   # enquanto j for menor ou igual a 10, faça:
      print(i, j)                   # imprima i e j
      j += 1                        # some 1 a j

   i += 1                           # some 1 a i

# Resultado:
# 1 1
# 1 2
# 1 3
# 1 4
# 1 5
# 1 6
# 1 7
# 1 8
# 1 9
# 1 10
# 2 1
# 2 2
# 2 3
# etc.

# Exemplo:

qtd_linhas = 5                      # variável qtd_linhas recebe 5
qtd_colunas = 5                     # variável qtd_colunas recebe 5

linha = 1                           # variável linha recebe 1
while linha <= qtd_linhas:          # enquanto linha for menor ou igual a qtd_linhas, faça:
  coluna = 1                        # variável coluna recebe 1
  while coluna <= qtd_colunas:      # enquanto coluna for menor ou igual a qtd_colunas, faça:
    print(f'{linha=} {coluna=}')    # imprima linha e coluna
    coluna += 1                     # some 1 a coluna
  linha += 1                        # some 1 a linha

# Resultado:
# linha=1 coluna=1
# linha=1 coluna=2
# linha=1 coluna=3
# linha=1 coluna=4
# linha=1 coluna=5
# linha=2 coluna=1
# linha=2 coluna=2
# linha=2 coluna=3
# linha=2 coluna=4
# linha=2 coluna=5
# linha=3 coluna=1
# linha=3 coluna=2
# linha=3 coluna=3
# linha=3 coluna=4
# linha=3 coluna=5
# linha=4 coluna=1
# linha=4 coluna=2
# linha=4 coluna=3
# linha=4 coluna=4
# linha=4 coluna=5
# linha=5 coluna=1
# linha=5 coluna=2
# linha=5 coluna=3
# linha=5 coluna=4
# linha=5 coluna=5