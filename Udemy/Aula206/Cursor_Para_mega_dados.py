# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
from typing import cast

import pymysql
import pymysql.cursors

TABLE_NAME = 'customers'
CURRENT_CURSOR = pymysql.cursors.SSDictCursor

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

    for row in cursor.fetchall_unbuffered():
        print(row)
    print()
    cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE id >= 5 ')
    print('For 2: CURSOR DE MEGADADOS NÃO VOLTA')
    # cursor.scroll(-2), 'absolute'  # voltando 2 linhas
    for row in cursor.fetchall_unbuffered():
        print(row)


# não precisa de commit para somente seleção de dados
# print(sql)
# print(data2)
