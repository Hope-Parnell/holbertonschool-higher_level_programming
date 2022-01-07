#!/usr/bin/node
const sq = require('./5-square');
class Square extends sq {
  charPrint (c) {
    if (!c) { c = 'X'; }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
