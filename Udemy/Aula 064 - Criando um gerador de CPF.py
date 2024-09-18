import random                                           # Importa a biblioteca random para gerar números aleatórios

nove_digitos = ''                                       # Variável que vai receber os 9 primeiros números do CPF

for i in range(9):                                      # Cria um loop de 9 repetições    
    nove_digitos += str(random.randint(0, 9))           # Gera 9 números aleatórios


lista_num = nove_digitos[:9]                            # Lista dos 9 primeiros números do CPF
contador = 10                                           # Contador regressivo
soma = 0                                                # Zera a soma

for num in lista_num:                                   # Para cada número na lista:
    num = int(num)                                      # Converte o número em int
    resultado = num * contador                          # Multiplica o número pelo contador
    soma = resultado + soma                             # Acumula o resultado
    contador -= 1                                       # Decrementa o contador

digito1 = (soma * 10) % 11                              # Calcula o primeiro dígito verificador
digito1 = digito1 if digito1 <= 9 else 0                # Se o digito1 for menor ou igual a 9, o digito1 será o próprio digito1, senão será 0

contador = 11                                           # Contador regressivo
soma = 0                                                # Zera a soma

for num in lista_num:                                   # Para cada número na lista:
    num = int(num)                                      # Converte o número em int
    resultado = num * contador                          # Multiplica o número pelo contador
    soma = resultado + soma                             # Acumula o resultado
    contador -= 1                                       # Decrementa o contador

digito2 = (soma * 10) % 11                              # Calcula o segundo dígito verificador
digito2 = digito2 if digito2 <= 9 else 0                # Se o digito2 for menor ou igual a 9, o digito2 será o próprio digito2, senão será 0

cpf = str(nove_digitos) + str(digito1) + str(digito2)   # Concatena os 9 primeiros dígitos com os dois dígitos verificadores
print(f'O número de CPF é: {cpf}')                      # Imprime o número de CPF
