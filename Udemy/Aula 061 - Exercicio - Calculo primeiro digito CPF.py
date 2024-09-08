# Exercício
# Verificador de dígito de CPF passo-a-passo:

'''
Exemplo 1:
Usando funções
'''

def calcula (soma):                                      # Função calcula recebe a variável soma
    calculo = (soma * 10) % 11                           # calculo recebe o resto da divisão inteira de soma * 10
    if calculo > 9:                                      # Se calculo for maior que 9
        calculo = 0                                      # calculo recebe 0
    lista_numeros.append(calculo)                        # Incrementando a lista com o primeiro dígito verificador


cpf = input('Digite os nove primeiros números do CPF: ') # Recebendo os nove primeiros números do CPF

# Lógica para o primeiro dígito verificador:

lista_numeros = [int(digito) for digito in str(cpf)]    # Convertendo os itens da lista em int
soma = 0                                                # Inicializando a variável
contador = 10                                           # Inicializando a variável

for numero in lista_numeros:                            # Para cada número na lista criada:
    n1 = numero * contador                              # n1 recebe ele mesmo + o contador regressivo de 10 a 0
    contador -= 1                                       # Contador regressivo é decrementado
    soma += n1                                          # Soma acumula os valores

calcula(soma)                                           # Chamando a função calcula

print(lista_numeros)                                    # Exibindo a lista

# Lógica para o segundo dígito verificador:

contador = 11                                           # contador recebe 11 porque temos mais um item na lista
soma = 0                                                # Zerando a soma para começar de novo

for numero in lista_numeros:                            # Para cada número na lista criada:
    n2 = numero * contador                              # n2 recebe ele mesmo + o contador regressivo de 10 a 0
    contador -= 1                                       # Contador regressivo é decrementado
    soma += n2                                          # Soma acumula os valores

calcula(soma)                                           # Chamando a função calcula    


print('O dígito verificador do CPF é: ', lista_numeros) # Exibindo a lista

''' 
Exemplo 2:
Sem funções
'''

cpf = input('Digite os nove primeiros números do CPF: ')

# Lógica para o primeiro dígito verificador:

lista_numeros = [int(digito) for digito in str(cpf)]    # Convertendo os itens da lista em int
soma = 0                                                # Inicializando a variável
contador = 10                                           # Inicializando a variável

for numero in lista_numeros:                            # Para cada número na lista criada:
    n1 = numero * contador                              # n1 recebe ele mesmo + o contador regressivo de 10 a 0
    contador -= 1                                       # Contador regressivo é decrementado
    soma += n1                                          # Soma acumula os valores


calculo = (soma * 10) % 11                              # calculo recebe o resto da divisão inteira de soma * 10
if calculo > 9:
    calculo = 0

lista_numeros.append(calculo)                           # Incrementando a lista com o primeiro dígito verificador

print(lista_numeros)

# Lógica para o segundo dígito verificador:

contador = 11                                           # contador recebe 11 porque temos mais um item na lista
soma = 0                                                # Zerando a soma para começar de novo

for numero in lista_numeros:
    n2 = numero * contador
    contador -= 1
    soma += n2

calculo2 = (soma * 10) % 11
if calculo2 > 9:
    calculo2 = 0

lista_numeros.append(calculo2)


print('O dígito verificador do CPF é: ', calculo,calculo2)

'''
Exemplo 3:
Professor
'''

cpf = '74682489070'                                                # Recebendo os nove primeiros números do CPF
nove_digitos = cpf[:9]                                             # nove_digitos recebe os 9 primeiros números do CPF
contador_regressivo = 10                                           # contador_regressivo recebe 10

resultado_digito_1 = 0                                             # resultado_digito_1 recebe 0
for digito_1 in nove_digitos:                                      # Para cada número na lista criada:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1    # resultado_digito_1 recebe ele mesmo + o contador regressivo de 10 a 0
    contador_regressivo_1 -= 1                                     # contador_regressivo_1 é decrementado
digito_1 = (resultado_digito_1 * 10) % 11                          # digito_1 recebe o resto da divisão inteira de resultado_digito_
digito_1 = digito_1 if digito_1 <= 9 else 0                        # Se digito_1 for menor ou igual a 9, o digito_1 será o próprio digito_1, senão será 0
print(digito_1)                                                    # Exibindo o digito_1

'''
Exemplo 4:
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