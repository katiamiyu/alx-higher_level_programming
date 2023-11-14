#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    let chr = '';
    if (c === undefined) {
      chr = 'X';
    } else {
      chr = c;
    }
    for (let i = 0; i < this.size; i++) {
      let lineStr = '';
      for (let j = 0; j < this.size; j++) {
        lineStr += chr;
      }
      console.log(lineStr);
    }
  }
}

module.exports = Square;
