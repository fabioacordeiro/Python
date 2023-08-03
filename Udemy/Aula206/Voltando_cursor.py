# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import pymysql
import pymysql.cursors

TABLE_NAME = 'customers'

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Lucas',
    database='base_de_dados',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,

)
connection.commit()

with connection.cursor() as cursor:
    sql = (f'SELECT * FROM {TABLE_NAME} ')

    print(cursor.execute(f'SELECT * FROM {TABLE_NAME} '))
    print(60*'-')
    print('For 1:')
    for row in cursor.fetchall():
        print(row)

    print()
    print('For 2: voltando o cursor 2 linhas')
    cursor.scroll(-2), 'absolute'  # voltando 2 linhas
    for row in cursor.fetchall():
        print(row)


# não precisa de commit para somente seleção de dados
# print(sql)
# print(data2)
