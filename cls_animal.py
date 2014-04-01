class Animal():
    """docstring for Animal"""
    def __init__(self, species, name, age, gender, weight):
        self.species = species
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    def eat(self, food_per_day):
        return self.weight + food_per_day

    def grow(self):
        return self.age + 1

    def give_birth(self):
        if self.gender == "female" and self.age:
            pass
