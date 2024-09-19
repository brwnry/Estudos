# Um método bem simples de calcular a média de um número variável de valores, a ser informado pelo usuário

def calcula_media(valores):
    acc = 0
    for valor in range(valores):
        numero = int(input(('{}° número: '.format(valor+1))))
        acc += numero
    return(acc/valores)

valores = int(input(('Informe quantos valores a serem calculados: ')))

print('Média dos valores informados: {:.2f}'.format(calcula_media(valores)))