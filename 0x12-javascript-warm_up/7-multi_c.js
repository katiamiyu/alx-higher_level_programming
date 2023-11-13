#!/usr/bin/node

if (isNaN(process.argv[2]))
{
	console.log('Missing number of occurrences');
}
else
{
	let i;
	const count = parseInt(process.argv[2]);
	for(i=0; i<count; i++)
		console.log('C is fun');
}
