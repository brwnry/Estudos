nota_1 = float(input('Digite a nota do primeiro aluno: '))
nota_2 = float(input('Digite a nota do segundo aluno: '))
nota_3 = float(input('Digite a nota do terceiro aluno: '))

media = (nota_1 + nota_2 + nota_3) / 3
nota_alta = max(nota_1, nota_2, nota_3)

print (f'A média da turma é {media}')
print(f'A maior nota da turma é {nota_alta}') 