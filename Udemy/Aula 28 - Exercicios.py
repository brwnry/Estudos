"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ') # Digite seu nome: Marcos
idade = input('Digite sua idade: ') # Digite sua idade: 25

if nome and idade: # True
    print(f'Seu nome é {nome}.') # Seu nome é Marcos.
    print(f'Seu nome invertido é {nome[::-1]}.') # 
    if " " in nome: # Se houver espaço em branco, faça:
        print('Seu nome tem espaços.') # Seu nome tem espaços.
    else: # Se não houver espaço em branco, faça:
        print('Seu nome não tem espaços.') # Seu nome não tem espaços.

    print(f'Seu nome tem {len(nome)} letras.') # Seu nome tem 8 letras.
    print(f'A primeira letra do seu nome é {nome[0]}.') # A primeira letra do seu nome é M.
    print(f'A última letra do teu nome é {nome[-1]}.') # A última letra do teu nome é s.

else: # Se não houver nome ou idade, faça:
    print('Desculpe, você deixou campos vazios') # Desculpe, você deixou campos vazios.