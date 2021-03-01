# Python app

A simple python app using MySQL python connector to execute SQL transactions

1. Install Python virtual environment and mysql connector

```
python3 -m pip install --user virtualenv
python3 -m venv mysql-env
cd mysql-env
chmod +x bin/activate
bin/activate
sudo python3 -m pip install mysql.connector-python
```

2. Run the sample app

```
python3 mysql_client_app.py
```
