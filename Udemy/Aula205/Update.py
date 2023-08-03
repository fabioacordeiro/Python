import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
TABLE_NAME = 'customers'
DB_FILE = ROOT_DIR / DB_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'UPDATE {TABLE_NAME} SET name="Fabiana Centopeia", weight=68.23 WHERE id="21"')
print('id 21 foi atualizado')
print(70*'-')
connection.commit()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')

print('id - ',  '  nome  - ', 'peso')
for row in cursor.fetchall():
    id = row[0]
    name = row[1]
    weight = row[2]
    print(id, name, weight)

cursor.close()
connection.close()
