import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
# CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()
# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Registrar valores nas colunas da tabela
# CUIDADO: sql injection
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(?, ?)'
)
# cursor.execute  #Para um unico valor ou executemany para mais valores
cursor.executemany(sql,
                   [
                       ['Fabio Alves Cordeiro', 102],
                       ['Luciene Almeida da Silva', 97],
                       ['Lucas da Silva Cordeiro', 25],
                       ['Maria de Lourdes Alves Cordeiro', 56],
                       ['Maria de Lourdes Almeida da Silva', 87],
                       ['Leandro', 78],
                       ['Emília', 79],
                       ['Eduardo', 48],
                       ['Chanrley', 75],
                       ['Arlande', 75],
                       ['Mateus', 56],
                       ['Beatriz', 34],
                       ['Cicero', 79],
                       ['Ariane', 39],
                       ['Bianca', 56],
                       ['Carlos', 78],
                       ['Dionizio', 63],
                       ['Davi', 85],
                       ['Elaine', 61],
                       ['Evandro', 45],
                       ['Fabiana', 67],
                       ['Geraldo', 99],
                       ['Guilherme', 86],
                       ['Hugo', 32],
                       ['Henrique', 44],
                       ['Isaias', 142],
                       ['Isaque', 78],
                       ['Ivan', 65],
                       ['Ismael', 77],
                       ['Julia', 23],
                       ['Josué', 91],
                       ['João', 88],
                       ['Janaina', 55],
                       ['Lemos', 67],
                       ['Lilian', 87],
                       ['Lourdes', 62],
                       ['Miriam', 22],
                       ['Mary', 46],
                       ['Marcos', 78],
                       ['Mauro', 22],
                       ['Nivaldo', 11],
                       ['Nicolas', 13],
                       ['Nancy', 22],
                       ['Otávio', 43],
                       ['Osmar', 34],
                       ['Onofre', 65],
                       ['Paula', 67],
                       ['Paulo', 87],
                       ['Pedro', 24],
                       ['Priscila', 43],
                       ['Quenia', 34],
                       ['Kronus', 58],
                       ['Kaike', 33],
                       ['Ricardo', 123],
                       ['Ronaldo', 118],
                       ['Rubens', 132],
                       ['Silvio', 84],
                       ['Simone', 79],
                       ['Sueli', 83],
                       ['Santiago', 89],
                       ['Tiago', 92],
                       ['Tadeu', 96],
                       ['Tatiane', 56],
                       ['Tirso', 12],
                       ['Ubirajara', 93],
                       ['Valdete', 41],
                       ['Valmir', 52],
                       ['Valquiria', 63],
                       ['Vanderlei', 58],
                       ['Xandi', 26],
                       ['Xandira', 45],
                       ['Zuleica', 59],
                       ['Zenaide', 91],
                       ['Yong', 76],
                       ['Yang', 56]
                   ])

connection.commit()
print(sql)

cursor.close()
connection.close()
