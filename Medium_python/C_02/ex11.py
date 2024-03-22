# Exemplo de dados geográficos
def soma(a, b):
    return a + b

def fun(a, *rest):
    b = a
    for i in rest:
        b = b + i
    return b


c = fun(1, 2, 3, 4, 5)
dados_geograficos = ['Paris', 48.8566, 2.3522, 2.0]
t = [20, 8]

soma(*t)

# Padrão de correspondência usando expressões de chamada de construtores
match dados_geograficos:
    case [str(nome), *gard, float(altitude)]:
        print(f"Nome: {nome}, {gard}, Altitude: {altitude}")
    case _:
        print("Padrão não correspondido")

