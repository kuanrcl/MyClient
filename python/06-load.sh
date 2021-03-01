if [ -d employees_db ]
then
  rm -rf employees_db
fi
tar -zxvf employees_db.tgz
mysql -u$3 -h$1 -P$2 -p$4 employees < employees_db/load_employees.dump
