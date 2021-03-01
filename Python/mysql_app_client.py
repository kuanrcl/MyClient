import mysql.connector
from mysql.connector import errorcode
from mysql.connector.constants import ClientFlag
from random  import randint

config = {
  'user': 'demo',
  'password': 'demo',
  'host': '127.0.0.1',
  'database': 'demo',
  'raise_on_warnings': True
}

print("\n".join(
  sorted(ClientFlag.get_full_info())
))

mydb = mysql.connector.MySQLConnection(**config)
mydb.start_transaction(isolation_level = 'READ COMMITTED')
mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE if not exist demo.mytable (f1 int auto_increment not null primary key, f2 varchar(200)) engine=innodb")
sql_insert = "INSERT INTO demo.mytable VALUES (%s, %s)"
record = (0, "John Doe")
print(record)

mycursor.execute(sql_insert, record)
mydb.commit()

sql_select = "SELECT * FROM demo.mytable"
mycursor.execute(sql_select)

for row in mycursor:
  print(row)

count = mycursor.rowcount
print("Number of rows:", count)

sql_delete = "DELETE from demo.mytable where f1 = %(id)s"

id = randint(0, count)
print("Record id to be deleted", id)

mycursor.execute(sql_delete, {"id": id})

print("DELETE statement: ", mycursor.statement)
mydb.rollback()

print("Rollback DELETE statement", mycursor.statement)
mycursor.execute(sql_select)

for row in mycursor:
    print(row)
count = mycursor.rowcount
print("Number of rows:", count)

mycursor.close()
mydb.close()
