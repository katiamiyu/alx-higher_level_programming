#!/usr/bin/node
/* makes use of args v */
const { argv } = require('node:process');

if (argv[2] === null)
{
	console.log('No argument');
}
else if (argv[3] === null)
{
	console.log('Argument found');
}
else
{
	console.log('Arguments found');
}
