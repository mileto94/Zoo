import sqlite3


def create_animals_table(cursor):
    create_query = '''CREATE TABLE IF NOT EXISTS
                animals(species TEXT PRIMARY KEY,
                life_expectancy INT,
                food_type TEXT,
                gestation INT,
                newborn_weight REAL,
                average_weight INT,
                weight_age_ratio REAL,
                food_weight_ratio REAL)'''

    cursor.execute(create_query)


def create_zoo_table(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS zoos(zoo_id INTEGER PRIMARY KEY, zoo_name TEXT, capacity INT, budget REAL)""")


def create_animals_in_zoo_table(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS animals_in_zoo(zoo_id INT, species TEXT,
                      age INT, name TEXT, gender TEXT, weight INT, FOREIGN KEY (species) REFERENCES animals(species), FOREIGN KEY (zoo_id) REFERENCES zoos(zoo_id))""")


def insert_animals_in_zoo(cursor, zoo_id, species, age, name, gender, weight):
    insert_query = "INSERT INTO animals_in_zoo VALUES(?, ?, ?, ?, ?, ?)"
    cursor.execute(insert_query, (zoo_id, species, age, name, gender, weight))


def data_entry_create_zoos(cursor):
    cursor.execute("INSERT INTO zoos (zoo_name, capacity, budget) VALUES (?, ?, ?)", ('SOFIA ZOO', 50, 1000))
    cursor.execute("INSERT INTO zoos (zoo_name, capacity, budget) VALUES (?, ?, ?)", ('PAZARDJIK ZOO', 25, 500))
    cursor.execute("INSERT INTO zoos (zoo_name, capacity, budget) VALUES (?, ?, ?)", ('PLEVEN ZOO', 35, 750))


def insert_species_into_table(cursor, species, life_expectancy,
        food_type, gestation, newborn_weight, average_weight,
        weight_age_ratio, food_weight_ratio):
    insert_query = "INSERT OR REPLACE INTO animals(species, life_expectancy, food_type, gestation, newborn_weight, average_weight, weight_age_ratio, food_weight_ratio) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(insert_query,
        (species, life_expectancy, food_type,
        gestation, newborn_weight, average_weight,
        weight_age_ratio, food_weight_ratio))


def create_database(filename):
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()

    create_animals_table(cursor)
    create_animals_in_zoo_table(cursor)
    create_zoo_table(cursor)


    animals = [("lion", 15, "carnivore", 3, 2, 200, 7.5, 0.035),
                ("tiger", 20, "carnivore", 4, 1, 250, 12, 0.06),
                ("red panda", 9, "herbivore", 4, 0.15, 5, 0.25, 1),
                ("kangaroo", 12, "herbivore", 9, 8, 50, 1.75, 0.1),
                ("koala", 15, "herbivore", 7, 1, 12, 0.5, 0.05),
                ("raccoon", 3, "herbivore", 2, 0.5, 7, 0.3, 0.35),
                ("baboon", 45, "herbivore", 6, 1, 41, 1, 0.074),
                ("impala", 15, "herbivore", 6, 1, 60, 0.33, 0.1),
                ("hippo", 45, "herbivore", 8, 30, 1500, 2.72, 25),
                ("cougar", 13, "carnivore", 3, 14, 80, 0.42, 0.075),
                ("goat", 18, "herbivore", 5, 5, 52, 0.217, 0.38)]

    for animal in animals:
        insert_species_into_table(cursor, *animal)

    zoo_animals = [(1, "tiger", 2, "Murdok", "male", 200),
                    (2, "lion", 4, "David", "male", 220),
                    (1, "tiger", 3, "Joe", "male", 230),
                    (3, "tiger", 3, "Lola", "female", 210),
                    (1, "koala", 1, "Jenny", "female", 12),
                    (3, "red panda", 2, "Emma", "female", 34),
                    (1, "raccoon", 2, "Jerry", "male", 14),
                    (2, "raccoon", 3, "Jimmy", "male", 12)]

    for zoo_animal in zoo_animals:
        insert_animals_in_zoo(cursor, *zoo_animal)

    data_entry_create_zoos(cursor)

    conn.commit()
    conn.close()


def main():
    create_database("animals.db")

if __name__ == '__main__':
    main()
