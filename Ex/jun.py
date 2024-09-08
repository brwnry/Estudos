# ESCOLHA ENTRE 1, 2 OU 3

numero = int(input('Escolha entre 1, 2 ou 3: '))

nome = 'Bruno' if numero == 1 \
else 'Miguel' if numero == 2 \
else 'João' if numero == 3 \
else 'Não existe'

print(nome)

# Lambda
# Exemplo:
# Sem lambda
#
# def calcula_media(nota1,nota2):
#     return (nota1 + nota2) / 2
#
# nota_1 = float(input('Informe a primeira nota: '))
# nota_2 = float(input('Informe a segunda nota: '))
#
# print(f'A média das notas informadas é {calcula_media(nota_1,nota_2)}')
#
# # Com lambda
#
# calcula_media = lambda nota1,nota2: (nota1 + nota2) / 2
#
# nota_1 = float(input('Informe a primeira nota: '))
# nota_2 = float(input('Informe a segunda nota: '))
#
# print(f'A média das notas informadas é {calcula_media(nota_1,nota_2)}')
