#!/usr/bin/node
// Class rectangle that defines a rectangle//

class Rectangle {
  // constructors for height and width //
  constructor (w, h) {
    if (parseInt(w) > 0 && parseInt(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // method //
  print () {
    let x = '';
    for (let a = 0; a < this.height; a++) {
      for (let b = 0; b < this.width; b++) {
        x += 'X';
      }
      console.log(x);
      x = '';
    }
  }
}

module.exports = Rectangle;
