class Person:

    
    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf

class Client(Person):
    

    def __init__(self, id_client, name, cpf):
        super().__init__(name, cpf)
        self.id_client = id_client

class Seller(Person):

    def __init__(self, id_Seller, name, cpf):
        super().__init__(name, cpf)
        self.id_Seller = id_Seller



   


c1 = Client(2, 'Caio Sampaio', '412323')

print(c1.id_client)
print(c1.name)
print(c1.cpf)

print('------')
v1 = Seller(1, 'Marcos Pedro', '243345')

print(v1.id_Seller)
print(v1.name)
print(v1.cpf)