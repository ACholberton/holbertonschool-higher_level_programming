#!/usr/bin/node
// function returns the amount of ocurrences in a list//

exports.nbOccurences = function (list, searchElement) {
  let a = 0;
  for (const item of list) {
    if (item === searchElement) {
      a++;
    }
  }
  return a;
};
