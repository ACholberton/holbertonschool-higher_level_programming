#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file //
const fs = require('fs');
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  fs.writeFile(process.argv[3], body, 'utf8', function (err, data) {
    if (err) {
      return console.log(err);
    }
  });
});
