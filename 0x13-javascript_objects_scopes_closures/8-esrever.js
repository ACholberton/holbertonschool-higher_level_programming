#!/usr/bin/node
// function returns the reversed version of a list//
exports.esrever = function (list) {
  const rev = [];
  for (let a = 0; a < list.length; a++) {
    rev.unshift(list[a]);
  }
  return rev;
}
