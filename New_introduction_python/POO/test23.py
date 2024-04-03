from functools import cached_property

class Calculator:
    def __init__(self, numbers):
        self.__numbers = numbers

    @property
    def numbers(self):
        return self.__numbers
    
    @numbers.setter
    def numbers(self, numbers):
        if self.__numbers != numbers:
            del self.sum
        self.__numbers = numbers 

    @cached_property
    def sum(self):
        print("Calculating sum...")
        return sum(self.__numbers)

calc = Calculator([1, 2, 3, 4, 5])
print(calc.sum)  # Output: Calculating sum... 15
calc.numbers.append(6)
del calc.sum
print(calc.sum)  # Output: 15 (cached value, no recalculation)
