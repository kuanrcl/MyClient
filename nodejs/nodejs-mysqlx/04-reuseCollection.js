
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
	const session = await mysqlx.getSession({
	  user: myuser,
	  password: mypass,
	  host: myhost,
	  port: myport
	});

	var myschema = session.getSchema('products');
	if (! await myschema.existsInDatabase())
	  myschema = await session.createSchema('products');
	const schema = myschema;
	console.log("Schema Created : " + schema.getName()); // { name: 'products' }

	// const collection = await schema.createCollection('servers', { reuseExisting:true});
	const collection = await schema.createCollection('servers', { reuseExisting:false});
	console.log("Collection created : " + collection.getName());

	const collections = await schema.getCollections();
	console.log(collections);

	await session.dropSchema('products');
	await session.close();
	process.exit();
		

  } catch (err) {
	console.log(err);
	console.log(err.message);
	process.exit(1);
  }

})();
