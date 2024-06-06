import sqlite3

conn = sqlite3.connect('safaritech.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        date_of_birth TEXT NOT NULL,
        address TEXT NOT NULL
    )
''')
conn.commit()
conn.close()
