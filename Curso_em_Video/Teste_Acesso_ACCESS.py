#import pandas as db
#import win32com.client, sys, os.path, glob
import pandas as pd
#import vision as vision

db_filename = pd.read_excel('C:\MultiOrigem\BD_MultiOrigem.xlsx')

print(db_filename)
'''
for tbl in pd.list_tables(db_filename):
    display(tbl)
    print(tbl)

'''

