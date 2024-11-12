import random

class HOUSE:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return  f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

h1 = HOUSE('ЖК Горский', 18)
h2 = HOUSE('Домик в деревне', 50)
h3 = HOUSE('ЖК Знак', 12)

print(h1)
print(h2)
print(h3)

print(len(h1))
print(len(h2))
print(len(h3))
