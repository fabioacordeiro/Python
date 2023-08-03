# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
from typing import cast

import pymysql
import pymysql.cursors

TABLE_NAME = 'customers'
CURRENT_CURSOR = pymysql.cursors.DictCursor

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Lucas',
    database='base_de_dados',
    charset='utf8mb4',
    cursorclass=CURRENT_CURSOR,

)
connection.commit()

with connection.cursor() as cursor:
    sql = (f'SELECT * FROM {TABLE_NAME} ')

    ver = (cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE id < 5 '))
    print(ver)
    print(60*'-')
    print('For 1:')
    dados = cursor.fetchall()

    for row in dados:
        print(row)

    print(f'linhas afetadas:{len(dados)}')
    print(f'Contando ultima operação cursor:{cursor.rowcount}')
    print()

    cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE id >= 5 ')
    print('For 2: CURSOR NORMAL')
    for row in cursor.fetchall():
        print(row)

    print(f'Contando ultima operação cursor:{cursor.rowcount}')
    cursor.execute(
        f'SELECT id FROM {TABLE_NAME} ORDER BY id DESC LIMIT 1'
    )
    lastIdFromselect = cursor.fetchone()
    print(f'Ultimo Id :{lastIdFromselect}')
    cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE id >= 5 ')
    cursor.scroll(4, 'absolute')

    print(f'Qual a linha que o cursor está ? :{cursor.rownumber}')
# não precisa de commit para somente seleção de dados
# print(sql)
# print(data2)
