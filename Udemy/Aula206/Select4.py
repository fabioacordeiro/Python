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
    id_recebido = input('Digite o id inicial:')
    id_recebido2 = input('Digite o id final:')
    # coluna = 'id'
    sql = (
        f'SELECT * FROM {TABLE_NAME} '
        f'WHERE id >= %s and id <= %s '
    )

    cursor.execute(sql, (id_recebido, id_recebido2))  # type: ignore
    # Para ver o conteudo do SQL
    print(cursor.mogrify(sql, (id_recebido, id_recebido2,)))
    data2 = cursor.fetchall()

    for row in data2:
        print(row)

# não precisa de commit para somente seleção de dados
# print(sql)
# print(data2)
