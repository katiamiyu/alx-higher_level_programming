#!/usr/bin/node

const arg = process.argv;
let max = 0;
let second = 0;
if (arg.length === 3 || arg.length === 2) {
  console.log(second);
} else {
  for (let ele of arg) {
    ele = parseInt(ele);
    if (ele > max) {
      second = max;
      max = ele;
    } else if (ele > second) {
      second = ele;
    }
  }
  console.log(second);
}
