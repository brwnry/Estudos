# Valores padrão para parâmetros
# Um valor padrão para um parâmetro é um valor que será utilizado pelo parâmetro se nada for passado para ele.
# Ao definir uma função, os parâmetros podem ter valores padrão. Caso o valor não seja passado, o parâmetro usará o valor padrão.

# Exemplo:

def soma(x, y):
    print(x + y)

soma(2, 3)
soma(3, 5)
soma(5, 7)
soma() # type: ignore

# Resultado: 
# 5
# 8
# 12
# 0

# Neste exemplo, a função soma() tem dois parâmetros, x e y. Se não for passado nenhum valor para x e y, o valor padrão será 0.