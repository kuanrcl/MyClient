	var myschema = await session.getSchema('products');
	if ( myschema == null)
	  myschema = await session.createSchema('products');
	const schema = myschema;
