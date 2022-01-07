#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let ct = 0;
  for (const item of list) {
    if (item === searchElement) { ct++; }
  }
  return ct;
};
