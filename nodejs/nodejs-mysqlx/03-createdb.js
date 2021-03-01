
'use strict';
const mysqlx = require('@mysql/xdevapi');
const args = require('minimist')(process.argv.slice(2))
const myhost=args['host']
const myport=args['port']
const myuser=args['user']
const mypass=args['password']

console.log("host:" + myhost );
console.log("host:" + myport );
(async function() {
  try {
	const session =await mysqlx.getSession({
	  user: myuser,
	  password: mypass,
	  host: myhost,
	  port: myport
	});

	var myschema = await session.getSchema('products');
	if ( myschema == null) {
	  myschema = await session.createSchema('products');
	  console.log("created new");
	}
	const schema = myschema;
	console.log("Schema Created : " + schema.getName()); // { name: 'products' }
	const schemas = await session.getSchemas();

	console.log(schemas);

	session.dropSchema('products');
	session.close();
	process.exit();
		

  } catch (err) {
	console.log(err.message);
	process.exit(1);
  }

})();
