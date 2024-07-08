# Funções são blocos de código dedicados a realizar uma tarefa. Podem receber parâmetros ou não,
# retornar dados ou não.

# Sintaxe:
# def <nome da função> (argumentos recebidos):

def calcula_media(nota1,nota2):
    return (nota1 + nota2) / 2


nota_1 = float(input('Informe a primeira nota: '))
nota_2 = float(input('Informe a segunda nota: '))

print(f'A média das notas informadas é {calcula_media(nota_1,nota_2)}') # Chamamos a função calcula_media, passando como parâmetros nota_1 e nota_2
print('A média das notas informadas é ',calcula_media(nota_1,nota_2))   # Mesma coisa, de um jeito diferente.
print('A média das notas informadas é {}'.format(calcula_media(nota_1,nota_2))) # Meeeeeeesma coisa. Você escolhe como vai apresentar.