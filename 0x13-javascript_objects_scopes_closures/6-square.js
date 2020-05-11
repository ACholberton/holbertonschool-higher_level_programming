#!/usr/bin/node
// Class Square that inherits from Rectangle//
const BetaSquare = require('./5-square');

class Square extends BetaSquare {
  // method print c //
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    let letter = '';
    for (let a = 0; a < this.width; a++) {
      for (let b = 0; b < this.width; b++) {
        letter += 'c';
      }
      console.log(letter);
      letter = '';
    }
  }
}
module.exports = Square;
