# Retorno de valores nas funções (return)

# O return é o que faz a função retornar um valor

def soma(a, b):                 # Função que soma dois valores
    return a + b                # retorna a soma dos dois valores


def saudacao(nome):             # Função que retorna uma saudação
    return f'Olá, {nome}!'      # retorna uma string com a saudação


def area_circulo(raio):        # Função que retorna a área de um círculo
    return 3.14 * raio ** 2    # retorna o valor da área do círculo


print(soma(2, 3))              # Chamando a função soma e imprimindo o resultado
print(saudacao('João'))        # Chamando a função saudacao e imprimindo o resultado
print(area_circulo(5))         # Chamando a função area_circulo e imprimindo o resultado

# Resultado:

# 5
# Olá, João!
# 78.5