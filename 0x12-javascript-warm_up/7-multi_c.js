#!/usr/bin/node
/* print argv number of C is fun */

let i;
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurences');
} else {
  for (i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('C is fun');
  }
}
