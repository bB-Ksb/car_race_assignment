import random

class Car:
    name: str
    distance: int

    def __init__(self, name):
        self.__name = name
        self.distance = 0

    @property
    def name(self):
        return self.__name

    def move(self):
        random_value = random.randint(0, 9)
        if random_value >= 4:
            self.distance += 1

    def __str__(self):
        return f"{self.__name}: {'-' * self.distance}"
