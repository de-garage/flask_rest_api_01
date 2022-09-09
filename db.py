import sqlite3

conn = sqlite3.connect('dbs/database_sqlite.db')
print("DB Opened successfully")

conn.execute(
    'CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pincode TEXT)')
print("Table Students created successfully")

conn.close()
