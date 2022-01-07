#!/usr/bin/node
exports.converter = function (base) {
  return function (n) {
    return Number(n).toString(base);
  };
};
