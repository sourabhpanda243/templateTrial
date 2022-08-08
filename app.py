import pyodbc
print("Hello from Sourabh")
server = 'sgsin01sql001v.database.windows.net'
database = 'control-tower-test-db'
username = 'sourabh'
password = '{admin@123}'   
#driver= '{FreeTDS}'
driver= '{ODBC Driver 18 for SQL Serverrrrr}'

#conn = pyodbc.connect('DRIVER={FreeTDS};SERVER=sgsin01sql001v.database.windows.net;PORT=1433;DATABASE=control-tower-test-db;UID=sourabh;PWD=admin@123', autocommit=True)

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()