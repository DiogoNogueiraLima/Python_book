class A:
    def __init__(self):
        print("Inicializando classe A")

class B(A):
    def __init__(self):
        print("Inicializando classe B start")
#        A.__init__(self)
        super()
        print("Inicializando classe B END")

class C(A):
    def __init__(self):
        print("Inicializando classe C start")
#        A.__init__(self)
        super()
        print("Inicializando classe C end")

class D(B, C):
    def __init__(self):
        print("Inicializando classe D start")
#        B.__init__(self)
        print("Inicializando classe D mid")
#        C.__init__(self)
        print("Inicializando classe D end")

Diogo = D()
print(D.__mro__)