'''
Exemplo:
Bruno
'''

# Primeiro dígito verificador do CPF:

cpf = '74682489070'                         # Números do CPF
lista_num = cpf[:9]                         # Lista dos 9 primeiros números do CPF
contador = 10                               # Contador regressivo
soma = 0                                    # Zera a soma

for num in lista_num:                       # Para cada número na lista:
    num = int(num)                          # Converte o número em int
    resultado = num * contador              # Multiplica o número pelo contador
    soma = resultado + soma                 # Acumula o resultado
    contador -= 1                           # Decrementa o contador

digito1 = (soma * 10) % 11                  # Calcula o primeiro dígito verificador
digito1 = digito1 if digito1 <= 9 else 0    # Se o digito1 for menor ou igual a 9, o digito1 será o próprio digito1, senão será 0

# Segundo dígito verificador do CPF:

contador = 11                               # Contador regressivo
soma = 0                                    # Zera a soma

for num in lista_num:                       # Para cada número na lista:
    num = int(num)                          # Converte o número em int
    resultado = num * contador              # Multiplica o número pelo contador
    soma = resultado + soma                 # Acumula o resultado
    contador -= 1                           # Decrementa o contador

digito2 = (soma * 10) % 11                  # Calcula o segundo dígito verificador
digito2 = digito2 if digito2 <= 9 else 0    # Se o digito2 for menor ou igual a 9, o digito2 será o próprio digito2, senão será 0

print(f'O dígito verificador do CPF é: {digito1}{digito2}')

'''

Exemplo:
Professor
'''

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

# Nota: as variáveis com erros só farão sentido com o código completo, já que referenciam a primeira parte do código