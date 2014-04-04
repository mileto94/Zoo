# Import
from random import randint
import sqlite3


class Animal():
    def __init__(self, species, age, name, gender, weight):
        self.conn = sqlite3.connect("animals.db")
        self.cursor = self.conn.cursor()

        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight

        self.life_expectancy = self.determine_life_expectancy()
        self.food_type = self.determine_food_type()
        self.gestation = self.determine_gestion()
        self.newborn_weight = self.determine_newborn_kg()
        self.average_weight = self.determine_average_weight()
        self.weight_age_ratio = self.determine_weight_age_ratio()
        self.food_weight_ratio = self.determine_food_weight_ratio()

        self.alive = True

    def __str__(self):
        return "{0}: {1}, {2}, {3}".format(self.name, self.species, self.age, self.weight)

    # def get_data(self, query):
    #     return self.cursor.execute(query, (self.species,)).fetchone()[0]

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def determine_life_expectancy(self):
        query = self.cursor.execute("SELECT life_expectancy FROM animals WHERE species = ?", (self.species,)).fetchone()[0]

        return query

    def lives(self):
        life_expectancy_in_months = self.determine_life_expectancy() * 12
        return randint(1, life_expectancy_in_months) > self.age

    def determine_food_type(self):
        query = self.cursor.execute("SELECT food_type FROM animals WHERE species = ?", (self.species,)).fetchone()[0]

        return query

    def determine_gestion(self):
        query = self.cursor.execute("SELECT gestation FROM animals WHERE species = ?", (self.species,)).fetchone()[0]

        return query

    def determine_newborn_kg(self):
        query = self.cursor.execute("SELECT newborn_weight FROM animals WHERE species = ?", (self.species,)).fetchone()[0]

        return query

    def determine_average_weight(self):
        query = self.cursor.execute("SELECT average_weight FROM animals WHERE species = ?", (self.species,)).fetchone()[0]

        return query

    def determine_weight_age_ratio(self):
        query = self.cursor.execute("SELECT weight_age_ratio FROM animals WHERE species = ?", (self.species,)).fetchone()[0]

        return query

    def determine_food_weight_ratio(self):
        query = self.cursor.execute("SELECT food_weight_ratio FROM animals WHERE species = ?", (self.species,)).fetchone()[0]

        return query

    # def grow(self, average_weight, weight_age_ratio):
    #     if self.weight < average_weight:
    #         self.weight += weight_age_ratio
    #     self.age += 1

    # def feed(self, food_weight_ratio):
    #     return food_weight_ratio * self.weight


def main():
    lion = Animal("tiger", 2, "Murdok", "male", 200)
    # print(lion.get_name())
    # print("")
    # print(lion.determine_food_type())
    # print("")
    # print(lion.determine_life_expectancy())
    # print("")
    # print(lion.determine_newborn_kg())
    # print("")
    # print(lion.determine_average_weight())
    # print("")
    # print(lion.determine_weight_age_ratio())
    # print("")
    # print(lion.determine_food_weight_ratio())

    print(lion.food_type)
    print("")
    print(lion.gestation)
    print("")
    print(lion.newborn_weight)
    print("")
    print(lion.average_weight)
    print("")
    print(lion.weight_age_ratio)
    print("")
    print(lion.food_weight_ratio)


if __name__ == '__main__':
    main()
