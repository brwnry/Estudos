# Listas em Python

# Tipo list -> mutável, ou seja, podemos Criar, Alterar, Remover e Adicionar elementos (CRUD).

lista = [123, True, 'Python', 1.0,
         []]  # lista de inteiros, booleanos, strings, floats e listas vazias
lista[
    2] = 'Java'  # Alterando o elemento na posição 2 da lista - Deus me livre!
del lista[
    2]  # Removendo o elemento na posição 2 da lista. Não é interessante para listas grandes porque o Python realoca todos os elementos para ocupar a posição que foi deletada causando lentidão de memória.
lista.append('C++')  # Adicionando um elemento no final da lista.
lista.pop()  # Removendo o último elemento da lista.

# Aceita qualquer tipo de dado

lista = [123, True, 'Python', 1.0,
         []]  # lista de inteiros, booleanos, strings, floats e listas vazias

# Índices e fatiamento

print(lista[3]).upper(), type(
    lista[2]
)  # Acessando um elemento na posição 3 da lista usando o método upper() e o tipo da variável referente ao elemento na posição 2 da lista.

# Métodos úteis:

# append() -> Adiciona um elemento no final da lista.

lista = [123, True, 'Python', 1.0,
         []]  # lista de inteiros, booleanos, strings, floats e listas vazias
lista.append(456)  # Adicionando um elemento no final da lista.
print(lista)  # [123, True, 'Python', 1.0, [], 456]

# pop() -> Remove o último elemento da lista.

lista = [123, True, 'Python', 1.0,
         []]  # lista de inteiros, booleanos, strings, floats e listas vazias
lista.pop()  # Remove o último elemento da lista.
print(lista)  # [123, True, 'Python', 1.0]

# insert() -> Adiciona um elemento em uma posição específica da lista.

lista = [123, True, 'Python', 1.0,
         []]  # lista de inteiros, booleanos, strings, floats e listas vazias
lista.insert(2, 'C++')  # Adicionando um elemento na posição 2 da lista.
print(lista)  # Adicionando um elemento na posição 2 da lista.

# remove() -> Remove um elemento específico da lista.

lista = [123, True, 'Python', 1.0,
         []]  # lista de inteiros, booleanos, strings, floats e listas vazias
lista.remove(123)  # remove o elemento 123 da lista
print(lista)  # OBS: Se o elemento não existir na lista, ocorre um erro.

# index() -> Retorna o índice de um elemento específico na lista.

lista = [123, True, 'Python', 1.0,
         []]  # lista de inteiros, booleanos, strings, floats e listas vazias
print(lista.index(123))  # Retorna o índice do elemento 123 na lista. (0)

# count() -> Retorna a quantidade de vezes que um elemento específico aparece na lista

lista = [
    'Egg', 'Bacon', 'Spam', 'Spam', 'Spam', 'Sausage', 'Spam', 'Cheese', 'Ham'
]  # Lista do menu do dia.
print(lista.count(
    'Spam'))  # Contando quantas vezes o elemento Spam aparece na lista.
print('But I dont like SPAM!')

# del(lista[posição]) -> Remove um elemento específico da lista.)

lista_a = [1, 2, 3]  # Criando uma lista com 3 elementos.
del lista_a[1]  # Removendo o elemento na posição 1 da lista.
print(lista_a)  # [1, 3]

# clear() -> Remove todos os elementos da lista.

lista = [123, True, 'Python', 1.0,
         []]  # lista de inteiros, booleanos, strings, floats e listas vazias
lista.clear()  # Removendo todos os elementos da lista.

# extend() -> Adiciona todos os elementos de uma lista a outra lista.

lista_a = [1, 2, 3]  # Lista A
lista_b = [4, 5, 6]  # Lista B
lista_c = lista_a + lista_b  # Concatena as listas A e B, criando uma nova lista C.
lista_a.extend(
    lista_b
)  # Adicionando a lista B a lista A. Tem o mesmo efeito dado pela concatenação da lista_c, mas ALTERA a lista_a.
print(lista_a)  # [1,2,3,4,5,6]

# sort() -> Ordena os elementos da lista.

lista_a = [94, 41, 57, 49, 99, 32, 12, 1, 0, -1, -2, -3, -4, -5, -6]  # Lista A
lista_a.sort()  # Ordenando a lista_a.
print(lista_a
      )  # lista_a = [94, 41, 57, 49, 99, 32, 12, 1, 0, -1, -2, -3, -4, -5, -6]

# reverse() -> Inverte a ordem dos elementos da lista.

lista_a = [1, 2, 3]  # Lista A
lista_a.reverse()  # Invertendo a ordem dos elementos da lista A.

# copy() -> Retorna uma cópia da lista.

lista_a = [1, 2, 3]  # Lista A
lista_b = lista_a.copy()  # Criando uma cópia da lista A.

# Tipo tuple -> imutável
# Tipo set -> não ordenado, não index

# enumarate() -> Retorna um iterável com os índices e os elementos da lista.

lista = ['Maria', 'Helena', 'Luiz']  # Lista de nomes
for indice, nome in enumerate(lista):  # Para cada índice e nome na lista enumerada,
         print(indice, nome) # Imprima o índice seguido do nome
