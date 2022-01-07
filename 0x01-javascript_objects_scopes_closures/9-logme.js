#!/usr/bin/node
let ct = 0;
exports.logMe = function (item) {
  console.log(ct + ':', item);
  ct++;
};
