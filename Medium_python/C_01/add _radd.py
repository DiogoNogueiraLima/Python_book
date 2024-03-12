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
        if isinstance(other, int):
            return Diogo(self.number + other)
        elif isinstance(other, Diogo):
            result = self.number + other.number
            return Diogo(result)
        else:
            return NotImplemented

a = Diogo(18)
b = Diogo(20)
c = a + b
t = a.number + b.number
d = 5 + a # nao entendi por que aqui ele chama o metodo radd se o 5 por padrao python ja possui o metodo add
pass

# outra tentativa
class MinhaClasse:
    def __init__(self, valor):
        self.valor = valor

    def __radd__(self, outro):
        # Método chamado quando outra instância tenta adicionar à sua instância
        print('radd chamado')

# Criando uma instância da classe
minha_instancia = MinhaClasse(5)
instacia_2 = MinhaClasse(3)

# Usando o operador de adição, onde a instância da classe é o operando direito
resultado = 10 + minha_instancia
# resultado = minha_instancia + 10
resultado = 10 + 5 + minha_instancia
# resultado = 10 + minha_instancia + 7
# resultado = instacia_2 + minha_instancia

# Imprimindo o resultado
print(resultado)
