import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')
print('id - ',  '  nome  - ', 'peso')
for row in cursor.fetchall():
    id = row[0]
    name = row[1]
    weight = row[2]
    print(id, name, weight)

cursor.close()
connection.close()
