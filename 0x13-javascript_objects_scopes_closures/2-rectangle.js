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
}

module.exports = Rectangle;
