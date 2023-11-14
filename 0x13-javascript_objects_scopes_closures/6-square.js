#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let lineStr = '';
      for (let j = 0; j < this.width; j++) {
        lineStr += c;
      }
      console.log(lineStr);
    }
  }
}

module.exports = Square;
