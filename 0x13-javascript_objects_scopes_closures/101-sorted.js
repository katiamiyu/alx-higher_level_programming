#!/usr/bin/node

const { dict } = require('./101-data.js');
const newDict = {};
for (const d in dict) {
  if (newDict[dict[d]] === undefined) {
    newDict[dict[d]] = [];
  }
  newDict[dict[d]].push(d);
}
console.log(newDict);
