'use strict';
const mysqlx = require('@mysql/xdevapi');
const args = require('minimist')(process.argv.slice(2))
const myhost=args['host']
const myport=args['port']
const myuser=args['user']
const mypass=args['password']

console.log("host:" + myhost );
console.log("host:" + myport );
