from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    profession: str

# Creating an instance of the data class
person1 = Person("John", '30', "Engineer")
person4 = Person("John", 30, "Engineer")

# Accessing the fields of the instance
print(person1.name)         # Output: John
print(person1.age)          # Output: 30
print(type(person1.age))
print(person1.profession)   # Output: Engineer
print(person1)
print(person1==person4)

class Person:
    def __init__(self, name, age, profession) -> None:
        pass

# Creating an instance of the data class
person2 = Person("John", 30, "Engineer")
person3 = Person("John", 30, "Engineer")

# Accessing the fields of the instance
print(person2)
print(person2==person3)