#!/usr/bin/node
/* makes use of args v */
const { argv } = require('node:process');

if (argv[2] === null)
{
	console.log('No argument');
}
else if (argv[3] === null)
{
	console.log(argv[2]);
	console.log('Argument found');
}
else
{
	console.log(`${argv[2]} ${argv[3]}`);
	console.log('Arguments found');
}
