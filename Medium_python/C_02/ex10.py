# Usando match
def exemplo_match(valor):
    match valor:
        case 1:
            print("Valor é 1")
        case 1:
            print("Valor é 'dois'")
        case _:
            print("Valor não corresponde a nenhum caso especificado")

# Usando if
def exemplo_if(valor):
    if valor == 7:
        print("Valor é 7")
    elif valor == 7:
        print("Valor é 'dois'")
    else:
        print("Valor não corresponde a nenhum caso especificado")

exemplo_match(1)    # Saída: Valor é 1
exemplo_if(7)       # Saída: Valor é 1

