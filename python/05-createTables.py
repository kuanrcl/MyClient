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

TABLES = {}
TABLES['employees'] = (
    "CREATE TABLE if not exists `employees` ("
    "  `emp_no` int NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ") ENGINE=InnoDB")

TABLES['departments'] = (
    "CREATE TABLE if not exists `departments` ("
    "  `dept_no` char(4) NOT NULL,"
    "  `dept_name` varchar(40) NOT NULL,"
    "  PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)"
    ") ENGINE=InnoDB")

TABLES['salaries'] = (
    "CREATE TABLE if not exists `salaries` ("
    "  `emp_no` int NOT NULL,"
    "  `salary` int NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`,`from_date`), KEY `emp_no` (`emp_no`),"
    "  CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_no`) "
    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['dept_emp'] = (
    "CREATE TABLE if not exists `dept_emp` ("
    "  `emp_no` int NOT NULL,"
    "  `dept_no` char(4) NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`,`dept_no`), KEY `emp_no` (`emp_no`),"
    "  KEY `dept_no` (`dept_no`),"
    "  CONSTRAINT `dept_emp_ibfk_1` FOREIGN KEY (`emp_no`) "
    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
    "  CONSTRAINT `dept_emp_ibfk_2` FOREIGN KEY (`dept_no`) "
    "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['dept_manager'] = (
    "  CREATE TABLE if not exists `dept_manager` ("
    "  `dept_no` char(4) NOT NULL,"
    "  `emp_no` int NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`,`dept_no`),"
    "  KEY `emp_no` (`emp_no`),"
    "  KEY `dept_no` (`dept_no`),"
    "  CONSTRAINT `dept_manager_ibfk_1` FOREIGN KEY (`emp_no`) "
    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
    "  CONSTRAINT `dept_manager_ibfk_2` FOREIGN KEY (`dept_no`) "
    "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['titles'] = (
    "CREATE TABLE if not exists `titles` ("
    "  `emp_no` int NOT NULL,"
    "  `title` varchar(50) NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date DEFAULT NULL,"
    "  PRIMARY KEY (`emp_no`,`title`,`from_date`), KEY `emp_no` (`emp_no`),"
    "  CONSTRAINT `titles_ibfk_1` FOREIGN KEY (`emp_no`)"
    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")


config = {
	'user': _user,
	'password': _pass,
	'host': _host,
	'port': _port,
	'database': 'mysql',
	'raise_on_warnings': True,
}
cnx = mysql.connector.connect(**config)

cursor = cnx.cursor()
def create_database(cursor):
	try:
		cursor.execute(
			"CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8mb4'".format(DB_NAME))
	except mysql.connector.Error as err:
		print("Failed creating database: {}".format(err))
		exit()

try:
	cnx.database = DB_NAME
except mysql.connector.Error as err:
	create_database(cursor)
cnx.database = DB_NAME

for name, ddl in TABLES.items():
	try:
		print("Creating table if not exists {}:".format(name), end='')
		cursor.execute(ddl)
	except mysql.connector.Error as err:
		print(err)
		if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
			print("{} already exists.".format(name))
		else:
			print(err.msg)
	else:
		print("OK")

cursor.close()
cnx.close()


