class Diogo:
    def soma(self, a: str, b: str):
        return a + b


    def soma(self, a: int, b: int):
        return a + b
    
print(Diogo().soma(1, 2))
print(Diogo().soma('1', '2'))