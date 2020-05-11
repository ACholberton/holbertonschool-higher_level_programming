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

  // method print//
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

  // method rotate //
  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }
// method double //
  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

module.exports = Rectangle;
