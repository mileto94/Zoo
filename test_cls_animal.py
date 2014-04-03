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
        self.animal = cls_animal.Animal("raccoon", 2, "Jerry", "male", 14)

    def test_get_data(self):
        self.assertEqual(self.zoo_an, self.animal.get_data(self.zoo_an))

    def tearDown(self):
        os.remove("test_animals.db")

if __name__ == '__main__':
    unittest.main()
