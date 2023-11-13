#!/usr/bin/node

let argv = process.argv
if (argv[2] == null)
{
	console.log('No argument');
}
else
{
	console.log(argv[2]);
}
