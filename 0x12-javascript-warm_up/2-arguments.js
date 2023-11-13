#!/usr/bin/node
/* makes use of args v */

if (process.argv[2] === undefined)
{
	console.log('No argument');
}
else if (process.argv[3] === undefined)
{
	console.log('Argument found');
}
else
{
	console.log('Arguments found');
}
