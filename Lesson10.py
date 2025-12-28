import sqlite3

connection = sqlite3.connect('DB.sl3')
cursor = connection.cursor()
"""
cursor.execute('''CREATE TABLE IF NOT EXISTS First_Table (name Text);''')
#cursor.execute("INSERT INTO First_Table (name) VALUES ('');")
cursor.execute("SELECT rowid, name FROM First_Table WHERE rowid = 2;")
cursor.execute("UPDATE First_Table SET name = 'Dmitro' WHERE rowid = 6;")
"""
cursor.execute("DROP TABLE First_Table;")

connection.commit()
result = cursor.fetchall()
print(result)

connection.close()
