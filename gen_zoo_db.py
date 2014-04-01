import sqlite3

db = sqlite3.connect('animals.db')

# Get a cursor object
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE zoo_animals(id INTEGER PRIMARY KEY, spieces TEXT,
                      age INTEGER, name TEXT, gender TEXT, weight INTEGER)
''')
print("The table is created.")
db.commit()

base2 = [("lion", 3, "Ivo", "male", 25), ("monkey", 2, "Sonia", "female", 6),
		("hippo", "Sava", "male", 8), ("raccoon", "Vera", "female", 4),
		("lion", 5, "Lara", "female", 22), ("kangaroo", 3, "Jerry", "male", 15)]
cursor.executemany(''' INSERT INTO zoo_animals(spieces, age, name, gender, weight) VALUES(?,?,?)''', base2)

print ("All info created in the base.")
db.commit()

db.close()
