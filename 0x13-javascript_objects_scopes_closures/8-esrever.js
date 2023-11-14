#!/usr/bin/node
function esrever (list) {
  let count = list.length - 1;
  const newList = [];
  for (count; count >= 0; count--) {
    newList.push(list[count]);
  }
  return newList;
}
module.exports = { esrever };
