# Operadores de precedência
#
# Operadores de precedência são os operadores que são executados primeiro.

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -

# Exemplos:
#
print(10 + 5 * 2) # 20
print(10 + 5 * 2 ** 3) # 50
print((10 + 5) * 2 ** 3) # 200
print(10 + 5 * (2 ** 3)) # 100
print(10 + 5 ** 2 * 3) # 100
print(10 + 5 ** (2 * 3)) # 100 
print(10 + 5 ** 2 * 3 ** 2) # 100
print(10 + 5 ** (2 * 3) ** 2) # 100
#


