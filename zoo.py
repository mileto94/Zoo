# Import
import sqlite3


class Zoo():
    """docstring for Zoo"""
    def __init__(self, name, capacity, budget):
    # def __init__(self, name):
        self.conn = sqlite3.connect("animals.db")
        self.cursor = self.conn.cursor()

        self.name = name
        self.budget = budget
        self.capacity = capacity
        self.max_capacity = capacity


        self.zoo_id = self.get_zoo_id()

    def get_name(self):
        return "Welcome to {}".format(self.name)

    def get_zoo_id(self):

        zoo_id = self.cursor.execute("SELECT zoo_id FROM zoos  where zoo_name = ?", (self.name,)).fetchone()[0]

        self.zoo_id = zoo_id
        return self.zoo_id

    def current_capacity(self):
        number_animals = self.cursor.execute("SELECT COUNT(species) FROM animals_in_zoo WHERE zoo_id = ?", (self.zoo_id,)).fetchone()[0]

        return "Currently, there are {} animals at {}".format(number_animals, self.name)

    def present_animals_in_zoo(self):
        query = "SELECT species, name FROM animals_in_zoo"

        print("At {} you will find the following animals:".format(self.name))
        for row in self.cursor.execute(query):
            print("{} called '{}'".format(row[0], row[1]))

    # def create_new_zoo(self):

    #     zoo_name = input("Enter zoo name>")
    #     zoo_capacity = input("Enter zoo capacity>")
    #     zoo_budget = input("Enter zoo current budget>")

    #     self.cursor.execute("INSERT INTO zoos (zoo_name, capacity, budget) VALUES (?, ?, ?)", (zoo_name, zoo_capacity, zoo_budget))

    #     return "New zoo was created with the following charachteristics: \n Zoo Name >>> {} \n Zoo capacity >>> {} \n Zoo current budget >>> {}".format(zoo_name, zoo_capacity, zoo_budget)

    # def delete_existing_zoo(self):
    #     query = "SELECT zoo_name FROM zoos"

    #     for row in self.cursor.execute(query):
    #         print("{}".format(row[0]))

    #     zoo_name_to_delete = input("Enter zoo name to delete>")

    #     query_delete = "DELETE FROM zoos WHERE zoo_name = ?"
    #     self.cursor.execute(query_delete, (zoo_name_to_delete,))

    # def get_income(self):
    #     return (self.current_capacity() * 60)

    # def get_expenses(self):
        # pass


# def main():
#     sofia_zoo = Zoo("SOFIA ZOO")
#     print(sofia_zoo.get_name())
#     print(sofia_zoo.current_capacity())
#     sofia_zoo.present_animals_in_zoo()


# if __name__ == '__main__':
#     main()
