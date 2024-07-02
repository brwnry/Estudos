# Next, iter, iterável e iterador

# Iterável -> o que pode ser iterado - str, ramge, list, tuple, dict, set 
# Iterador -> quem sabe entregar um valor por vez
# next() -> retorna o próximo item do iterador
# iter() -> retorna um iterador

texto = 'Python' # string
iterador = iter(texto) # iterador recebe o iterador da string

while true: # enquanto verdadeiro, faça:
  try: # tente:
    letra = next(iterador) # letra recebe o próximo valor do iterador
    print(letra) # imprima letra
  except StopIteration: # se StopIteration for lançado, faça:
    break # pare

# Que é exatamente a mesma coisa que:

for letra in texto: # para cada letra na string texto, faça:
  print(letra) # imprima letra

