import sqlite3

conn = sqlite3.connect("placement.db")
cursor = conn.cursor()

with open("placement_database.sql", "r") as f:
    sql_script = f.read()

cursor.executescript(sql_script)

conn.commit()
conn.close()

print("Database created successfully!")