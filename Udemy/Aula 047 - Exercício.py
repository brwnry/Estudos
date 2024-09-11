'''
Faça um jogo para o usuário adivinhar qual a palavra secreta.

 - Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.

- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.

    - Se a letra digitada estiver na palavra secreta, exiba a letra.
    - Se a letra digitada não estiver na palavra secreta, exiba '*'.

- Faça a contagem de tentativas do usuário.
'''

'''
Primeiramente, definimos as variáveis de armazenamento das informações.
1. A palavra secreta.
2. As letras que o usuário já digitou.
3. O número de tentativas.
'''

palavra_secreta = 'python'                       # variável palavra_secreta recebe 'python'
letras_acertadas = ''                            # variável letras_acertadas recebe valor vazio
tentativas = 0                                   # variável tentativas recebe 0

'''
Agora, vamos criar um loop que irá repetir enquanto o usuário não acertar a palavra secreta.
Dentro do loop, solicitaremos que o usuário digite uma letra qualquer e armazenaremos essa letra em uma variável.
Em seguida, adicionamos +1 ao número de tentativas.
'''

while True:                                     # enquanto True, faça:
  letra = input('Digite uma letra: ').lower()   # variável letra recebe a letra digitada pelo usuário transfomada em minúscula
  tentativas += 1                               # some 1 a tentativas

  '''
  Se o usuário digitar mais que uma letra por vez, exiba uma mensagem de erro, e repita o loop.
  '''

  if len(letra) > 1:                            # se o tamanho da letra for maior que 1, faça:
    print('Digite apenas uma letra!')           # imprima 'Digite apenas uma letra!'
    continue                                    # pule para a próxima iteração do loop

  '''
  Se o a letra digitada estiver na palavra secreta, a variável 'letras_acertadas' receberá a letra digitada.
  '''

  if letra in palavra_secreta:                  # se a letra estiver na palavra secreta, faça:
    letras_acertadas += letra                   # some a letra digitada a variável letras_acertadas

  '''
  Cria-se uma variável 'palavra_formada' que receberá a letra digitada caso ela esteja na palavra secreta.
  Em seguida, cria um loop para percorrer a palavra secreta e verificar se a letra digitada está na palavra secreta.
  Em caso positivo, a letra digitada é adicionada à variável 'palavra_formada'.
  Em caso negativo, a letra digitada é adicionada a '*' à variável 'palavra_formada'.
  '''

  palavra_formada = ''                          # variável palavra_formada recebe valor vazio
  for letra in palavra_secreta:                 # para cada letra na palavra secreta, faça:
    if letra in letras_acertadas:               # se a letra estiver na variável letras_acertadas, faça:
      palavra_formada += letra                  # some a letra digitada a variável palavra_formada
    else:                                       # se não, faça:
      palavra_formada += '*'                    # some '*' a variável palavra_formada

  '''
  Mostre na tela a palavra formada.
  '''

  print(palavra_formada)                                            # imprima a variável palavra_formada

  if palavra_formada == palavra_secreta:                            # se a palavra formada for igual a palavra secreta, faça:
    print(f'Você acertou! A palavra secreta era {palavra_secreta}') # imprima 'Você acertou! A palavra secreta era {palavra_secreta}'
    print(f'Você precisou de {tentativas} tentativas')              # imprima 'Você precisou de {tentativas} tentativas'
    break                                                           # pare o loop