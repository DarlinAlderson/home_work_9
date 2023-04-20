# 1) Реализовать дескрипторы для любых двух классов

class Car:

    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine

    def __str__(self):
        return '{0} {1} с двигателем {2} л.'.format(self.make, self.model, self.engine)


car_1 = Car('Subaru', 'Forester', 2.5)
print(car_1)


class House:

    def __init__(self, name, kindergarten, school):
        self.name = name
        self.kindergarten = kindergarten
        self.school = school

    def __str__(self):
        return 'ЖК {0} с {1} детским садом и {2} школой на территории - новое решение для молодых семей.'.format \
            (self.name, self.kindergarten, self.school)


house_1 = House('Яблоневый сад', 1, 1)
print(house_1)
