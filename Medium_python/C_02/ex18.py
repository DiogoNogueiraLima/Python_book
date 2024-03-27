class Diogo:
    def __init__(self) -> None:
        self.number = 3

    def __iadd__(self, other):
        self.number = self.number + other
        return self
    
a = Diogo() 
a += 5
pass