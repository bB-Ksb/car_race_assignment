import random

class Car:
    __name: str
    __distance: int = 0

    def __init__(self, name):
        self.name = name
        self.distance = 0

    def move(self):
        random_value = random.randint(0, 9)
        if random_value >= 4:
            self.distance += 1

    def __str__(self):
        return f"{self.name}: {'-' * self.distance}"
