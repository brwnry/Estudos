# 'split' e 'join' com list e str:

# split - divide uma string
# join - junta uma lista

# Exemplo split:

frase = 'Olha só que, coisa interessante'                                                       # str
lista_palavras = frase.split()                                                                           # separa a string em uma lista
print(lista_palavras)                                                                                       # ['Olha', 'só', 'que,', 'coisa', 'interessante']

frase = 'Olha só que, coisa interessante'                                                       # str
lista_palavras = frase.split(,)                                                                          # separa a string em uma lista usando o separador ','
print(lista_palavras)                                                                                       # ['Olha', 'só', 'que,', 'coisa', 'interessante']

# Exemplo join:

frases_unidas = ''.join(lista_palavras)                                                             # junta a lista em uma string
print(frases_unidas)                                                                                        # Olha só que, coisa interessante

frases_unidas = '-'.join(lista_palavras)
print(frases_unidas)                                                                                        # Olha-só-que-coisa-interessante

