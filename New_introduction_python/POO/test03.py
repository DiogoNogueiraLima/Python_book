# https://pythontutor.com
# a partir do momento que eu importo ele roda o codigo, caso eu queira chamar uma função no codigo, eu preciso importar ela
# From tambem roda o codigo,
#from test01 import func, func2 # ou import *

age = 42
bigstring = 'KSJFAFAKDSJFLDSFJÇDASKFASJFASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS'

class Pai:
    def __init__(self, idade):
        self.idade = idade
        self.maluco = True
        

Edgardson = Pai(42)
print(Edgardson.idade)
print(f'É VERDADE QUE Edgardson é maluco? {Edgardson.maluco}')

x = 1
def outer():
    x = 2

    def inner():
        x = 3

        def double_inner():
            nonlocal x
            x = 4
            print(f'double inner sees x equal to {x}')

        double_inner()
        print(f'inner sees x equal to {x}')
    
    inner()
    print(f'outer sees x equal to {x}')

outer()
print(f'global sees x equal to {x}')