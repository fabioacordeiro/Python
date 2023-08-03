'''
https://www.techonthenet.com/sqlite/index.php
https://www.sqlite.org/doclist.html
https://dbeaver.io/download/
'''
import sqlite3
from pathlib import Path
from time import sleep

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
print(DB_FILE)
sleep(0.5)
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# SQL

cursor.close()
connection.close()
