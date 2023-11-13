#!/usr/bin/node
/* print argv as a square */

let i, j;
let linePrint;
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (i = 0; i < parseInt(process.argv[2]); i++) {
    linePrint = '';
    for (j = 0; j < parseInt(process.argv[2]); j++) {
      linePrint += 'X';
    }
    console.log(linePrint);
  }
}
