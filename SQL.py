import pyodbc

SERVER = "sql10"
DATABASE = "dm_ciap"
USERNAME = "bi.admin"
PASSWORD = "SSB1-Adm1n"
DRIVER = 'ODBC Driver 17 for SQL Server'
SQL_QUERY = 'SELECT * from PBI_Profile'

dados_conexao = (
    f'DRIVER={DRIVER};'
    f'SERVER={SERVER};'
    f'DATABASE={DATABASE};'
    f'UID={USERNAME};'
    f'PWD={PASSWORD};'
     'ENCRYPT=NO;'
     'TRUSTED_CONNECTION=NO'
    )

conn = pyodbc.connect(dados_conexao)
cursor = conn.cursor()

query = cursor.execute(SQL_QUERY)

records = cursor.fetchall()
for r in records:
    print(r)