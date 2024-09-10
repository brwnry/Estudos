# Interpolação de Strings:

# Interpolação de Strings é uma técnica de interpolar variáveis em strings.

# Exemplo:

nome = 'Marcos'                     # variável nome recebe Marcos
sobrenome = 'Silva'                 # variável sobrenome recebe Silva
profissão = 'Programador'           # variável profissão recebe Programador

texto = 'O ' + nome + ' ' + sobrenome + ' é um excelente ' + '[' + profissão + ']' # texto recebe 'O Marcos Silva é um excelente [Programador]'
texto2 = f'O {nome} {sobrenome} é um excelente [{profissão}]'                      # texto2 recebe 'O Marcos Silva é um excelente [Programador]'

print(texto)                        # Exibe 'O Marcos Silva é um excelente [Programador]'
print(texto2)                       # Exibe 'O Marcos Silva é um excelente [Programador]'

# Exemplo:

mensagem = 'Eu adoro comida caseira'    # variável mensagem recebe 'Eu adoro comida caseira'
print(mensagem.lower())                 # Exibe 'eu adoro comida caseira'

# s - string
# d e i - int
# f - float
# .2f - float com 2 casas decimais
# x ou X - hexadecimal
# o - octal
# e ou E - exponencial
# % - porcentagem
 

nome = 'Luis'                                         # variável nome recebe Luis
preço = 100.95897643                                  # variável preço recebe 100.95897643
variavel = '%s, o preço é R$ %.2f' % (nome, preço)'   # variável variavel recebe 'Luis, o preço é R$ 100.96'
print(variavel) # Luis, o preço é R$ 100.96           # Exibe 'Luis, o preço é R$ 100.96'



