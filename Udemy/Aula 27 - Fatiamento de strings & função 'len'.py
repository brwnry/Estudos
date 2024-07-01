# Fatiamento de strings & função 'len'.

 012345678
'Olá mundo'
 987654321

# Fatiamento [i:f:p]
# i = início
# f = fim
# p = passo

# Exemplo:
#
nome = 'Olá mundo' # string
print(nome[0:4]) # Olá
print(nome[4:8]) # mundo
print(nome[4:]) # mundo
print(nome[:4]) # Olá
print(nome[:]) # Olá mundo
print(nome[0:8:2]) # O l m d
print(nome[::2]) # O l m d
print(nome[::-1]) # odnum aló
print(nome[::-2]) # odnu ol
print(nome[::-3]) # odno

# A função 'len' retorna o tamanho de uma string.
#
print(len(nome)) # 8

# Exercício
# Peça ao usuário para digitar seu nome
# Peça ao usuário para digitar sua idade
# Se nome e idade forem digitados:
#     Exiba:
#         Seu nome é {nome}
#         Seu nome invertido é {nome invertido}
#         Seu nome contém (ou não) espaços
#         Seu nome tem {n} letras
#         A primeira letra do seu nome é {letra}
#         A última letra do seu nome é {letra}
# Se nada for digitado em nome ou idade:
#     exiba "Desculpe, você deixou campos vazios."

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome contém espaços? {"Sim" if " " in nome else "Não"}')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')

else:
    print('Desculpe, você deixou campos vazios.')
  