#!/usr/bin/node
// script print C is fun x amount of times//

const arg = parseInt(process.argv[2], 10);
let i;

if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < arg; i++) {
    console.log('C is fun');
  }
}
