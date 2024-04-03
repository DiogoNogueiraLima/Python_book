class PersonA:
    def hello():
        print('hello im A')

class PersonB(PersonA):
    def __init__(self):
        super().__init__()

    def hello():
        print('hello im B')

class PersonC(PersonB):
    def __init__(self):
        super().__init__()

PersonC().hello()