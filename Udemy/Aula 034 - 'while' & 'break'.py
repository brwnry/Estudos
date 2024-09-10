# O comando 'while' é usado para repetir um bloco de código enquanto uma condição for verdadeira.
# Exemplo:

i = 1                # variável i recebe 1
while i <= 10:       # enquanto i for menor ou igual a 10, faça:
     print(i)        # imprima i
     i += 1          # some 1 a i

# O comando 'break' é usado para sair de um loop.
# Exemplo:

i = 1                # variável i recebe 1
while i <= 10:       # enquanto i for menor ou igual a 10, faça:
     print(i)        # imprima i
     if i == 5:      # se i for igual a 5, faça:
         break       # pare o loop
     i += 1          # some 1 a i

# O comando 'continue' é usado para pular para a próxima iteração de um loop.
# Exemplo:

i = 1                # variável i recebe 1
while i <= 10:       # enquanto i for menor ou igual a 10, faça:
     if i == 5:      # se i for igual a 5, faça:
         i += 1      # some 1 a i
         continue    # pule para a próxima iteração do loop
     print(i)        # imprima i
     i += 1          # some 1 a i