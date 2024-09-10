'''
Documentação do Python:
https://docs.python.org/pt-br/3/contents.html
'''

# Métodos de String são funções que podem ser aplicadas a strings.
# Exemplo:

nome = 'João'                    # variável nome recebe João
print(nome.upper())              # Exibe a string em maiúsculas: JOÃO
print(nome.lower())              # Exibe a string em minúsculo
print(nome.capitalize())         # Exibe a variável nome com a primeira letra maiúscula
print(nome.title())              # Exibe a variável nome com a primeira letra de cada palavra em maiúsculo
print(nome.count('o'))           # Exibe o índice da letra 'o'
print(nome.find('o'))            # Encontra o índice da letra 'o'
print(nome.replace('o', 'a'))    # Exibe a variável nome com a letra 'o' substituída por 'a'
print(nome.strip())              # Exibe a variável nome sem os espaços em branco do início e do fim
print(nome.split())              # Exibe a variável nome como uma lista
print(nome.split('o'))           # Exibe a variável nome como uma lista, separando a string em 'o'
print(nome.split('a'))           # Exibe a variável nome como uma lista, separando a string em 'a'
print(nome.split('a', 1))        # Exibe a variável nome como uma lista, separando a string em 'a' e limitando a 1 vez
print(nome.split('a', 2))        # Exibe a variável nome como uma lista, separando a string em 'a' e limitando a 2 vezes
print(nome.split('a', 3))        # Exibe a variável nome como uma lista, separando a string em 'a' e limitando a 3 vezes
print(nome.split('a', 4))        # Exibe a variável nome como uma lista, separando a string em 'a' e limitando a 4 vezes