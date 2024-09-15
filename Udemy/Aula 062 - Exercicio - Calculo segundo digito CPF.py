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
