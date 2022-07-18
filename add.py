import mysql.connector as conn

mydb = conn.connect(host='localhost', user='root', passwd='tikeswari', use_pure=True)
print(mydb.is_connected())

crs = mydb.cursor()
crs.execute('show databases')
print(crs.fetchall())
