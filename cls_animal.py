# Import
from random import randint
import sqlite3


class Animal():
    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight

        self.alive = True

        self.conn = sqlite3.connect("animals.db")
        self.cursor = self.conn.cursor()

    def get_data(self, query):
        return self.cursor.execute(query, (self.species,)).fetchone()[0]

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def determine_food_type(self):
        query = "SELECT food_type FROM animals WHERE species = ?;"
        return self.fetch_data(query)

    # def get_food_type(self):
    #     return self.food_type

    def __str__(self):
        return "{0}: {1}, {2}, {3}".format(self.name, self.species, self.age, self.weight)

    def grow(self, average_weight, weight_age_ratio):
        if self.weight < average_weight:
            self.weight += weight_age_ratio
        self.age += 1

    def lives(self, life_expectancy):
        life_expectancy_in_months = life_expectancy * 12
        return randint(1, life_expectancy_in_months) > self.age

    def feed(self, food_weight_ratio):
        return food_weight_ratio * self.weight

