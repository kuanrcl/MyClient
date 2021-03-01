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
    const session = await mysqlx.getSession( {user:myuser, password:mypass, host:myhost, port:myport});
    console.log(session.inspect());
    process.exit();
  } catch (err) {
    console.log(err.message);
    process.exit(1);
  }
})();
