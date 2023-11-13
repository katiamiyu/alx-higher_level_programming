#!/usr/bin/node
/* print argv as a square */

const argv = process.argv;
const numA = parseInt(argv[2]);
const numB = parseInt(argv[3]);

function add(a, b) {
  const result = (a + b);
  console.log(result);
}

add(numA, numB);
