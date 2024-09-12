# 'split' e 'join' com list e str:

# split - divide uma string
# join - junta uma string

# Exemplo split:

frase = 'Olha só que, coisa interessante'       # Variável frase recebe uma string                                               
lista_palavras = frase.split()                  # Variável lista_palavras recebe o conteúdo da variável frase, dividida por espaços.                   
print(lista_palavras)                           # Mostra a lista de palavras: ['Olha', 'só', 'que', ',', 'coisa', 'interessante']
                                                                  

# Exemplo join:

frases_unidas = ''.join(lista_palavras)         # Variável frases_unidas recebe o conteúdo da lista_palavras                                                        
print(frases_unidas)                            # Mostra a string unida: 'Olha só que, coisa interessante'


frases_unidas = '-'.join(lista_palavras)        # Variável frases_unidas recebe o conteúdo da lista_palavras
print(frases_unidas)                            # Mostra a string unida: 'Olha-só-que,-coisa-interessante'                                                       

