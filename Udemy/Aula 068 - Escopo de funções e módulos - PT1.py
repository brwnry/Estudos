# Escopo de funções em Python

# Escopo significa o local onde uma variável pode ser acessada.
# Por exemplo, se uma variável é declarada dentro de uma função, ela só pode ser acessada dentro dessa função.
# Se uma variável é declarada fora de uma função, ela pode ser acessada em qualquer lugar do código.


# Escopo Local
# Variáveis declaradas dentro de uma função são chamadas de variáveis locais e só podem ser acessadas dentro dessa função.

x = 5

def minha_funcao(): # type: ignore
    x = 10
    print(x)

minha_funcao()
# Resultado: 10


# Escopo Global
# Variáveis declaradas fora de uma função são chamadas de variáveis globais e podem ser acessadas em qualquer lugar do código.

x = 5

def minha_funcao():
    print(x)

minha_funcao()
print(x)

# Resultado: 5

# Exemplo do professor:

x = 1                       # Variavel x recebe 1 - Variavel global

def escopo():               # Função escopo
    x = 10                  # Variavel x recebe 10 - Variavel local

    def outra_funcao():     # Função outra_funcao
        x = 20              # Variavel x recebe 20 - Variavel local
        y = 30              # Variavel y recebe 30 - Variavel local
        print(x, y)         # Mostra o valor de x e y

    outra_funcao()          # Chama a função outra_funcao
    print(x)                # Mostra o valor de x

print(x)                    # Mostra o valor de x
escopo()                    # Chama a função escopo

# Resultado: 1
#           20 30
#           10
#           1
#           10