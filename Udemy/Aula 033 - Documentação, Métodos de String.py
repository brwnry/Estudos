'''
Documentação do Python:
https://docs.python.org/pt-br/3/contents.html
'''

# Métodos de String são funções que podem ser aplicadas a strings.
# Exemplo:

nome = 'João'
print(nome.upper()) # João
print(nome.lower()) # joão
print(nome.capitalize()) # João
print(nome.title()) # João
print(nome.count('o')) # 2
print(nome.find('o')) # 1
print(nome.replace('o', 'a')) # Jaaã
print(nome.strip()) # João
print(nome.split()) # ['João']
print(nome.split('o')) # ['J', 'ã', 'ã']
print(nome.split('a')) # ['J', 'o', 'ã', 'ã']
print(nome.split('a', 1)) # ['J', 'oão']
print(nome.split('a', 2)) # ['J', 'o', 'ão']
print(nome.split('a', 3)) # ['J', 'o', 'ão']
print(nome.split('a', 4)) # ['J', 'o', 'ão']