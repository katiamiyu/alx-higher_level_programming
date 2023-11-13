#!/usr/bin/node

const argvL = process.argv.length;
let msg;
if (argvL <= 2) {
	msg = 'No argument';
} else if (argvL === 3) {
	msg = 'Argument found';
} else {
	msg = 'Arguments found';
}
console.log(msg);
