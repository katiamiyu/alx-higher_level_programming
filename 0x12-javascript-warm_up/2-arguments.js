#!/usr/bin/node
/* makes use of args v */

if (process.argv[2] === undefined)
{
	console.log('No argument');
}
else if (process.argv[3] === undefined)
{
	// console.log(process.argv[2]);
	console.log('Argument found');
}
else
{
	/* let myVar = process.argv[2];
	process.argv.forEach((value, index) => {
		if (index >= 3)
		{
			myVar += ` ${value}`;
		}
	});
	console.log(myVar); */
	console.log('Arguments found');
}
