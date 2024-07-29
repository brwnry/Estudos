# Imprecisão de pontos flutuantes
# Double-precision floating-point format IEEE 754

# O uso de floats pode acarretar um resultados imprecisos.
# Por exemplo, a divisão de 1/3 resulta em 0.3333333333333333

# Há fomas de se contornar este problema:
# 1. Usando a função round()
# 2. Usando a função format()
# 3. Usando a função str()
# 4. Usando a função f-string
# 5. Importando a biblioteca decimal

# Exemplo:

import decimal # Importando a biblioteca decimal quando se precisar de precisão maior

numero_1 = decimal.Decimal(0.1)
numero_2 = decimal.Decimal(0.7)
numero_3 = numero_1 + numero_2
print(numero_3) # 0.8999999999999999

# Exemplo:

numero_1 = (0.1)
numero_2 = (0.7)
numero_3 = numero_1 + numero_2
print(f'{numero_3:.2f}') # 0.8

# Exemplo:

numero_1 = (0.1)
numero_2 = (0.7)
numero_3 = numero_1 + numero_2
print(round(numero_3, 3)) # 0.8
