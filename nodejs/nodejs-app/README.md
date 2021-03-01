# This is the nodejs App using "express"

1. Demo Install Instruction 

   install nodejs generator "express" and nodemon
```
sudo npm install -g express-generator
sudo npm install -g nodemon
```

2. Install corresponding module to express including the MySQL Connector
   The MySQL connector is downloaded as mysql-connector-nodejs-8.0.23.tar.gz
   You can refer to the link - https://dev.mysql.com/downloads/connector/nodejs/
```
express demo --view pug
express mychart --view pug
cd demo
npm install pug
npm install http-errors
npm install express
npm install cookie-parser
npm install morgan
npm install debug
npm install ../mysql-connector-nodejs-8.0.23.tar.gz
npm audit fix
```

cp -r ../myapp/demo/* .

```

3. Startup the demo app
```
   cd demo
   nodemon
```
   Use browser to connect to http://<host IP>:3000/demo
   
   It is the demo app to allow Input Firstname and Lastname and List customer records on the Web Screen.


