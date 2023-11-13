#!/usr/bin/node

const argv = process.argv;
if (isNaN(argv[2]))
{
	console.log('Missing number of occurrences');
}
else
{
	let i;
	const count = parseInt(argv[2]);
	for(i=0; i<count; i++)
		console.log('C is fun');
}
