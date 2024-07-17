nome = 'Tyler Durden'
indice = 0 # Geralmente, o índice é chamado de i
novo_nome = ''

while indice < len(nome): # Enquanto o índice for menor que o tamanho do nome
  letra = nome[indice] # Pega a letra na posição do índice
  novo_nome += f'*{letra}' # Adiciona um asterisco na nova string
  indice += 1 # Incrementa o índice

novo_nome += '*' # Adiciona um asterisco no final da nova string
print(novo_nome) # Imprime a nova string