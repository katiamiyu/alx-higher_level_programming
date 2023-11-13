#!/usr/bin/node
/* print argv as a square */

const argv = process.argv;
function add(a, b) {
  return (a + b);
}

console.log(`${add(parseInt(argv[2]), parseInt(argv[3]))}`);
