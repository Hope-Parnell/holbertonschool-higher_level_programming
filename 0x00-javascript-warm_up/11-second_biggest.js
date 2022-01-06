#!/usr/bin/node
const len = process.argv.length;
let second = 0;
if (len > 3) {
  const n1 = Number(process.argv[2]);
  const n2 = Number(process.argv[3]);
  let largest;
  let n;
  if (n1 > n2) {
    largest = n1;
    second = n2;
  } else {
    largest = n2;
    second = n1;
  }
  for (let i = 4; i < len; i++) {
    n = Number(process.argv[i]);
    if (n > largest) {
      second = largest;
      largest = n;
    } else if (n > second) {
      second = n;
    }
  }
}
console.log(second);
