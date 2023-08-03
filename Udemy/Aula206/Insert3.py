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
'''
# O COMANDO TRUNCATE ABAIXO APAGA OS DADOS DA TABELA
CUIDADO
cursor.execute(
            f'TRUNCATE TABLE {TABLE_NAME} '
            )
connection.commit()
'''
with connection:
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data = ('Carlos', 25)
        result = cursor.execute(sql, data)  # type: ignore
        print(sql, data)
        print(result)
    connection.commit()
