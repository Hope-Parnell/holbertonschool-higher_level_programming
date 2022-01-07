#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    w = Number(w);
    h = Number(h);
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
