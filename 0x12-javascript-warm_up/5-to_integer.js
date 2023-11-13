#!/usr/bin/node

let argv = process.argv;
if (argv[2] == null)
  console.log('Not a number');
else
{
  if (isNaN(argv[2]))
    console.log('Not a number');
  else
    console.log(`My number: ${parseInt(argv[2])}`);
}
