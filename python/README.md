# This is MySQL Connectivity for Python tutorial
## MySQL Python Connector installation
```
sudo python3 -m pip install mysql-connector-python
```


## Using mysql.connector in Python
1. Connection Setup
2. Try-error for MySQL Exception
3. Create Table and Select Data thru mysql.connector

## examples
```
$ python3 ./01-connect.py [host] [port] [user] [password]

$ python3 ./02-connect.py [host] [port] [user] [password]

$ python3 ./03-connectUsingConfig.py [host] [port] [user] [password]

$ python3 ./04-tryerror.py [host] [port] [user] [password]
connect success
Finally - close connection

$ python3  ./05-createTables.py 10.0.1.3 3306 myroot Welcome1!
mysql
Creating table if not exists employees:OK
Creating table if not exists departments:OK
Creating table if not exists salaries:OK
Creating table if not exists dept_emp:OK
Creating table if not exists dept_manager:OK
Creating table if not exists titles:OK
```
   If database "employees" and tables exist, the following messages come up.   It can happen when the 05-createTables.py is executed more than once.

```
$ python3 ./05-createTables.py [host] [port] [user] [password]
Creating table if not exists employees:1050: Table 'employees' already exists
employees already exists.
Creating table if not exists departments:1050: Table 'departments' already exists
departments already exists.
Creating table if not exists salaries:1050: Table 'salaries' already exists
salaries already exists.
Creating table if not exists dept_emp:1050: Table 'dept_emp' already exists
dept_emp already exists.
Creating table if not exists dept_manager:1050: Table 'dept_manager' already exists
dept_manager already exists.
Creating table if not exists titles:1050: Table 'titles' already exists
titles already exists.

$ ./06-load.sh [host] [port] [user] [password]
employees_db/
employees_db/load_departments.dump
employees_db/load_employees.dump
employees_db/load_titles.dump
employees_db/load_dept_manager.dump
employees_db/load_salaries.dump
employees_db/load_dept_emp.dump
mysql: [Warning] Using a password on the command line interface can be insecure.

$ python3 ./07-select.py [host] [port] [user] [password]
(10001, datetime.date(1953, 9, 2), 'Georgi', 'Facello', 'M', datetime.date(1986, 6, 26))
(10002, datetime.date(1964, 6, 2), 'Bezalel', 'Simmel', 'F', datetime.date(1985, 11, 21))
(10003, datetime.date(1959, 12, 3), 'Parto', 'Bamford', 'M', datetime.date(1986, 8, 28))
(10004, datetime.date(1954, 5, 1), 'Chirstian', 'Koblick', 'M', datetime.date(1986, 12, 1))
(10005, datetime.date(1955, 1, 21), 'Kyoichi', 'Maliniak', 'M', datetime.date(1989, 9, 12))
(10006, datetime.date(1953, 4, 20), 'Anneke', 'Preusig', 'F', datetime.date(1989, 6, 2))
(10007, datetime.date(1957, 5, 23), 'Tzvetan', 'Zielinski', 'F', datetime.date(1989, 2, 10))
(10008, datetime.date(1958, 2, 19), 'Saniya', 'Kalloufi', 'M', datetime.date(1994, 9, 15))
(10009, datetime.date(1952, 4, 19), 'Sumant', 'Peac', 'F', datetime.date(1985, 2, 18))
(10010, datetime.date(1963, 6, 1), 'Duangkaew', 'Piveteau', 'F', datetime.date(1989, 8, 24))
Number of rows affeted by statement 'SELECT * from employees limit 10':10


```

