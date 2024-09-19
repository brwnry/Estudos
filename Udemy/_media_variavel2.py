# Método para se calcular a média de um número variável de valores passando uma lista contendo os valores

def calcula_media(lista):
    acc = 0
    for valor in lista:
        acc += valor
    return acc/len(lista)

valores = int(input(('Informe quantos valores a serem calculados: ')))
lista = []

for valor in range(valores):
    lista.append(int(input('Informe o valor: ')))

print('Média dos valores informados: {:.2f}'.format(calcula_media(lista)))