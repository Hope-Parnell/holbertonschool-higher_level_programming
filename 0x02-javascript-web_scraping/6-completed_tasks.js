#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const tasks = JSON.parse(body);
    const res = {};
    for (const task of tasks) {
      if (task.completed) {
        if (!res[task.userId]) {
          res[task.userId] = 1;
        } else {
          res[task.userId]++;
        }
      }
    }
    console.log(res);
  }
}
);
