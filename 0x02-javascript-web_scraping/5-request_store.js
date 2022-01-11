#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const fileName = process.argv[3];
    fs.writeFile(fileName, body, 'utf-8', (err) => { if (err) console.log(err); });
  }
});
