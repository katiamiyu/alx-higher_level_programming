#!/usr/bin/node
/* print argv as a square */

const numA = parseInt(process.argv[2]);

function factorial (a) {
  let result = 1;
  if (a === 0 || isNaN(a)) {
    return 1;
  } else {
    result = a * factorial(a - 1);
  }
  return result;
}

console.log(factorial(numA));
