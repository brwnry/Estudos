#Formatação básica de strings:

# s - string
# d - int
# f - float
# .<número de dígitos>f - float com n dígitos
# x ou X - hexadecimal
# o - octal
# e ou E - exponencial
# % - porcentagem
# > - alinhamento à direita
# < - alinhamento à esquerda
# ^ - alinhamento ao centro	
# = - preenchimento com caracteres
# + - preenchimento com caracteres
# - - não preenche espaços em branco
# !r - exibe a string em modo de representação de código
# !s - exibe a string em modo de representação de string
# !a - exibe a string em modo de representação de string com caracteres de controle

variavel = 'ABCD'                               # variável variavel recebe ABCD

print(f'{variavel}')                            # Exibe 'ABCD'
print(f'{variavel: >10}')                       # Exibe 'ABCD    '
print(f'{variavel: <10}')                       # Exibe '    ABCD'
print(f'{variavel: ^10}')                       # Exibe '  ABCD  '
print(f'{variavel: =^10}')                      # Exibe '==ABCD==='
print(f'{1000.4873648123746: >10.2f}')          # Exibe '1000.49'
print(f'O hexadecimal de 1500 é {1500:08X}')    # Exibe '0x0E0'
print(f'O octal de 1500 é {1500:08o}')          # Exibe '0o1776'
print(f'O binário de 1500 é {1500:08b}')        # Exibe '0b10011100'