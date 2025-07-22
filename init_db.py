import sqlite3

conn = sqlite3.connect('restaurant.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT NOT NULL,
        qty INTEGER NOT NULL,
        price REAL NOT NULL
    )
''')

conn.commit()
conn.close()
print(" restaurant.db created with 'orders' table")
