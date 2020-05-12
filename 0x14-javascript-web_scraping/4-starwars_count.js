#!/usr/bin/node
// script returns the amount of filrm the character Wedge Antilles is in//

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) throw error;
  let index = 0;
  for (const film of JSON.parse(body).results) {
    for (const character of film.characters) {
      if (character.includes('18')) {
        index++;
      }
    }
  }
  console.log(index);
});
