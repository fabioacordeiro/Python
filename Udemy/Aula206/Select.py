# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import pymysql

TABLE_NAME = 'customers'

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Lucas',
    database='base_de_dados',
    charset='utf8mb4',
)
connection.commit()

with connection.cursor() as cursor:
    sql = (
        f'SELECT * FROM {TABLE_NAME} '
    )

    cursor.execute(sql)  # type: ignore
    data2 = cursor.fetchall()

    for row in data2:
        print(row)

# não precisa de commit para somente seleção de dados
    print(sql)
    print(data2)
