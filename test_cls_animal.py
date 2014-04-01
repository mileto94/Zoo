import cls_animal
import unittest
import sqlite3
import create_animals_database
import os


class TestAnimal(unittest.TestCase):
    """docstring for TestAnimal"""
    def setUp(self):
        create_animals_database.create_database("test_animals.db")
        self.connection = sqlite3.connect("test_animals.db")
        self.pointer = self.connection.cursor()
        self.zoo_an = self.pointer.execute("SELECT * FROM animals_in_zoo").fetchall()

    def test_make_new_animal(self):
        animal = cls_animal.Animal("tiger", 24, "Mandy", "male", 200)
        self.zoo_an.append(animal)
        expected = self.pointer.execute("SELECT name, spieces FROM animals_in_zoo ").fetchall()
        self.assertIn(expected, self.zoo_animals)

    def tearDown(self):
        os.remove("test_animals.db")

if __name__ == '__main__':
    unittest.main()
