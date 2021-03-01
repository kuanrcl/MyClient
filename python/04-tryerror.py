import mysql.connector
from mysql.connector import errorcode
import sys

if len(sys.argv) != 4 :
	_host = sys.argv[1]	
	_port = sys.argv[2]	
	_user = sys.argv[3]
	_pass = sys.argv[4]
else :
	_host = '127.0.0.1'
	_port = '3306'
	_user = 'demo'
	_pass = 'demo'

_db='demo'

try:
  cnx = mysql.connector.connect(user=_user, password=_pass, host=_host, port=_port, database=_db)

  print("connect success")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  print ("Finally - close connection")
  cnx.close()
