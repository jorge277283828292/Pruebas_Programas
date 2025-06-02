import mysql.connector
conexion = mysql.connector.connect(user='root', 
                                   password='Root1234',
                                   host='localhost', 
                                   database='db_python',
                                   port='3306'
                                   )
print(conexion)