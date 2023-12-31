# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL

# pip install python-dotenv
import os

import dotenv
import pymysql

dotenv.load_dotenv()
connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_ROOT_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)
# print(os.environ['MYSQL_DATABASE'])

with connection:
    with connection.cursor() as cursor:
        # SQL
        print(cursor)
