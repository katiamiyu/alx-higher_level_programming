#!/usr/bin/node
/* makes use of args v */

let msg;
const argvL = process.argv.length;
if (argvL < 3){
	msg = 'No argument';
} else if (argvL === 3)
{
	msg = 'Argument found';
} else {
	msg = 'Arguments found';
}
console.log(msg);
