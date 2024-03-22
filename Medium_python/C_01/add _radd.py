# errado    

class Nene:
    def __init__(self, number):
        self.number = number

class Diogo:
    def __init__(self, numero):
        self.number = numero

    def __add__(self, other):
            return self.__radd__(other)

    def __radd__(self, other):
        print("Chamou o método __radd__")
        return NotImplemented
        if isinstance(other, int):
            return self.number + other
        elif isinstance(other, Diogo):
            result = self.number + other.number
            return result
        else:
            return NotImplemented

a = Diogo(2)
b = Diogo(3)
c = a + b
pass

