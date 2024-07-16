# Interpolação de Strings:

# Interpolação de Strings é uma técnica de interpolar variáveis em strings.

# Exemplo:

nome = 'Marcos'
sobrenome = 'Silva'
profissão = 'Programador'

texto = 'O ' + nome + ' ' + sobrenome + ' é um excelente ' + '[' + profissão + ']' # O Marcos Silva é um excelente [Programador]

texto2 = f'O {nome} {sobrenome} é um excelente [{profissão}]' # O Marcos Silva é um excelente [Programador]

print(texto) # O Marcos Silva é um excelente [Programador]
print(texto2) # O Marcos Silva é um excelente [Programador]

# Exemlo:

mensagem = 'Eu adoro comida caseira'
print(mensagem.lower()) # eu adoro comida caseira

# s - string
# d e i - int
# f - float
# .2f - float com 2 casas decimais
# x ou X - hexadecimal
# o - octal
# e ou E - exponencial
# % - porcentagem
 

nome = 'Luis' # string
preço = 100.95897643 # float
variavel = '%s, o preço é R$ %.2f' % (nome, preço)'
print(variavel) # Luis, o preço é R$ 100.96



