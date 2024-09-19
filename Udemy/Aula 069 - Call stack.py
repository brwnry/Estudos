# Call Stack - pilha de chamadas

# O python tem um limite de recursão, que é de 1000 chamadas.
# Se passar desse limite, o python vai dar um erro de recursão.
# Para resolver esse problema, podemos aumentar o limite de recursão, mas é melhor evitar isso.

# Exemplo de pilha de chamadas:

def recursao(n):
    print(n)
    if n < 10:
        recursao(n + 1)

recursao(0)

# Explicação:
# A função recursao é chamada com o parâmetro n = 0.
# A função print(n) é chamada e imprime o valor de n.
# A função recursao é chamada novamente com o parâmetro n = 1.
# A função print(n) é chamada e imprime o valor de n.
# A função recursao é chamada novamente com o parâmetro n = 2.
# A função print(n) é chamada e imprime o valor de n.
# E assim por diante, até que n seja maior ou igual a 10.
# Quando n é maior ou igual a 10, a função recursao não é chamada novamente e a pilha de chamadas é liberada.
# O programa termina.


