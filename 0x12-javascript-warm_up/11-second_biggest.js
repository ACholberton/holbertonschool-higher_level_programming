#!/usr/bin/node
// script searches the second biggest integer in the list of arguments//

const list = process.argv.length;
const arr = [];
let i;
let arg;

if (list === 3 || list === 2) {
  console.log(0);
} else {
  for (i = 2; i < list; i++) {
    arg = parseInt(process.argv[i]);
    if (!isNaN(arg)) {
      arr.push(arg);
    }
  }
  arr.sort();
  arr.pop();
  console.log(Math.max.apply(null, arr));
}
