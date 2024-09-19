# Argumento Posicional
# Os argumentos posicionais são passados para a função na ordem em que são definidos.

def somar(a, b):
    return a + b

# Chamando a função com argumentos posicionais

resultado = somar(3, 5)
print(resultado)

# Resultado: 8

# Argumento Nomeado
# Os argumentos nomeados são passados para a função especificando o nome do parâmetro, o que permite que sejam passados em qualquer ordem.

def apresentar(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")

# Chamando a função com argumentos nomeados

apresentar(nome="Ana", idade=30)
apresentar(idade=25, nome="Carlos")

# Resultado: 
# Nome: Ana, Idade: 30
# Nome: Carlos, Idade: 25

# Nos exemplos acima, somar(3, 5) usa argumentos posicionais, enquanto apresentar(nome="Ana", idade=30) 
# e apresentar(idade=25, nome="Carlos") usam argumentos nomeados

# Exemplo 2:

def soma(x, y):
    print(x + y)


soma(3, 5)      # Argumentos posicionais
soma(y=5, x=3)  # Argumentos nomeados

# Resultado:
# 8