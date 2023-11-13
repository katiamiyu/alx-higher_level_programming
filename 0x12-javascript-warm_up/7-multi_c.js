#!/usr/bin/node

let argv = process.argv;
if ((argv !== null) && !isNaN(argv[2]))
{
	let i;
	const count = parseInt(argv[2]);
	for(i=0; i<count; i++)
		console.log('C is fun');
}
else
	console.log('Missing number of occurrences');
