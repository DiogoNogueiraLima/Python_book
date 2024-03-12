# brincar com add e radd

# codigo que nao funciona... porque irá buscar o __bool__ apenas e diretamente vai verificar se o que tem lá é um True,
# dentro de instacia
class A:
    d = 5

    def __len__(self):
        return 0
    

instancia = A()
if instancia is False:
    print("A is True")
else:
    print("A is False")


# Já nesse o codigo que funciona... porque o if verifica se a instancia possui um __bool__ definido ou __len__ definido,
# caso nao tenha, ele é avaliada como verdadeira; Ele nao procura por True ou False, ele procura pelo __bool__ definido
class B:
    d = 5

    def __len__(self):
        return 0

instancia = B()
if instancia:
    print("B is True")
else:
    print("B is False")



# codigo que ja funciona, retornando false por que ele verifica o __len__
class C:
    d = 5
x = 5 == 6

instancia = None
if x is True:
    print("C is True")
else:
    print("C is False")