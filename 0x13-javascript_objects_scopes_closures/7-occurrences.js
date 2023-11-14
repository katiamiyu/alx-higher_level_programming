#!/usr/bin/node
function nbOccurences (list, searchElement) {
  let count = 0;
  for (const e of list) {
    if (e === searchElement) {
      count++;
    }
  }
  return count;
}
module.exports = { nbOccurences };
