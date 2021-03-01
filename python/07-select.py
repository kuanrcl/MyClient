from __future__ import print_function

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
DB_NAME = 'employees'
operation = 'SELECT * from employees limit 10'

config = {
	'user': _user,
	'password': _pass,
	'host': _host,
	'port': _port,
	'database': 'employees',
	'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)

cursor = cnx.cursor()

try:
  for result in cursor.execute(operation, multi=True):
     if result.with_rows:
        print("rows producted by statement '{}':".format(result.statement ))
        row = cursor.fetchone()
        while row:
           print(row)
           row = cursor.fetchone()
        print("Number of rows affeted by statement '{}':{}".format(result.statement, result.rowcount))
     else:
        print("Number of rows affeted by statement '{}':{}".format(result.statement, result.rowcount))
except mysql.connector.Error as err:
        print(err.msg)

cursor.close()
cnx.close()


