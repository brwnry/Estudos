# Suponha que o usuário preencha os números do CPF usando os pontos de separação:
# É possível chamar métodos para resolver

cpf = '746.824.890-70' \                                                   
    .replace('.', '')  \                                           
    .replace(' ', '')  \                                           
    .replace('-', '')                                              
    
    # nove_digitos recebe os 9 primeiros números do CPF, e
    # substituir ponto por vazio
    # substituir espaço por vazio
    # substituir traço por vazio

# O método replace substitui os caracteres da string por algo que você especificar, neste caso, vazio.
# Existe uma forma melhor de se fazer isto, importando um módulo chamado re (regular expression)

nove_digitos = cpf[:9]                                             # nove_digitos recebe os 9 primeiros números do CPF
contador_regressivo = 10                                           # contador_regressivo recebe 10

resultado_digito_1 = 0                                             # resultado_digito_1 recebe 0
for digito_1 in nove_digitos:                                      # Para cada número na lista criada:
    resultado_digito_1 += int(digito_1) * contador_regressivo      # resultado_digito_1 recebe ele mesmo + o contador regressivo de 10 a 0
    contador_regressivo -= 1                                       # contador_regressivo_1 é decrementado
digito_1 = (resultado_digito_1 * 10) % 11                          # digito_1 recebe o resto da divisão inteira de resultado_digito_
digito_1 = digito_1 if digito_1 <= 9 else 0                        # Se digito_1 for menor ou igual a 9, o digito_1 será o próprio digito_1, senão será 0
print(digito_1)                                                    # Exibindo o digito_1

cpf = '74682489070'                                                # Recebendo os nove primeiros números do CPF
dez_digitos = nove_digitos + str(digito_1)                         # dez_digitos recebe os 9 primeiros números do CPF e o  digito_1
contador_regressivo = 11                                           # contador_regressivo recebe 11

resultado_digito_2 = 0                                             # resultado_digito_2 recebe 0
for digito_2 in dez_digitos:                                       # Para cada número na lista criada:
    resultado_digito_2 += int(digito_2) * contador_regressivo      # resultado_digito_2 recebe ele mesmo + o contador regressivo de 10 a 0
    contador_regressivo -= 1                                       # contador_regressivo_1 é decrementado
digito_2 = (resultado_digito_2 * 10) % 11                          # digito_2 recebe o resto da divisão inteira de resultado_digito_
digito_2 = digito_2 if digito_2 <= 9 else 0                        # Se digito_2 for menor ou igual a 9, o digito_2 será o próprio digito_2, senão será 0
print(digito_2)                                                    # Exibindo o digito_2
