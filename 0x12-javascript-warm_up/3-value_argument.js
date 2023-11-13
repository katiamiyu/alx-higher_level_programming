#!/usr/bin/node

const argvL = process.argv.length;
let msg;
if (argvL < 3) {
	msg = 'No argument';
} else {
	msg = process.argv[2];
}
console.log(msg);
