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
