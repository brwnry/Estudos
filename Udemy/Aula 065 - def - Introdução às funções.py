'''
Introdução às funções (def) em Python.

Funções são trechos de códigos que podem ser reaproveitados em outros lugares do programa.
Elas podem receber parâmetros (argumentos) e retornar um valor.
Por padrão, as funções retornam None, caso não seja especificado o valor de retorno.
'''

# Exemplo 1:
def greeting():                 # função saudação sem parâmetros
    print('Olá, mundo!')        # imprime uma mensagem na tela

greeting()                      # chama a função saudacao

# Resultado: Olá, mundo!

# Exemplo 2:
def saudacao(nome):             # função saudação com parâmetro
    print(f'Olá, {nome}!')      # imprime uma mensagem na tela com o nome passado como parâmetro

saudacao('João')                # chama a função saudacao passando o nome 'João' como parâmetro

# Resultado: Olá, João!

# Exemplo 3:
def sum(a, b):                 # função soma com dois parâmetros
    return a + b                # retorna a soma dos dois parâmetros

print(sum(2, 3))               # chama a função soma passando os parâmetros 2 e 3 e imprime o resultado na tela

# Resultado: 5

# Exemplo 4:
def soma(a, b):                 # função soma com dois parâmetros
    return a + b                # retorna a soma dos dois parâmetros

print(soma(2, 3))               # chama a função soma passando os parâmetros 2 e 3 e imprime o resultado na tela
print(soma(5, 5))               # chama a função soma passando os parâmetros 5 e 5 e imprime o resultado na tela
print(soma(10, 10))             # chama a função soma passando os parâmetros 10 e 10 e imprime o resultado na tela
print(soma(20, 20))             # chama a função soma passando os parâmetros 20 e 20 e imprime o resultado na tela

# Resultado:
# 5
# 10
# 20
# 40
