#!/usr/bin/node
function nbOccurences (list, searchElement) {
  let count = 0;
  for (const e of list) {
    if (e === searchElement) {
      count++;
    }
  }
  console.log(count);
}

module.exports = { nbOccurences };
