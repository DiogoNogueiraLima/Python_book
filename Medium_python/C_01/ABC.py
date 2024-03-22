from abc import ABC, abstractmethod
from math import pi

# Definindo uma classe abstrata de base para formas geométricas
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Criando uma classe de círculo que herda da classe abstrata Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

# Criando uma classe de retângulo que herda da classe abstrata Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

# Agora podemos criar instâncias de círculo e retângulo
circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=6)

# Podemos chamar o método 'area()' em ambas as instâncias, pois ambas implementam a classe abstrata Shape
print(f"Área do círculo: {circle.area()}")
print(f"Área do retângulo: {rectangle.area()}")
