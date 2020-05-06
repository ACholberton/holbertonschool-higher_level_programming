#!/usr/bin/node
// js script prints a square//

const squareSize = parseInt(process.argv[2], 10);
let i;
let x = '';

if (isNaN(squareSize)) {
  console.log('Missing size');
} else {
  for (i = 0; i < squareSize; i++) {
    x += 'X';
  }
  for (i = 0; i < squareSize; i++) {
    console.log(x);
  }
}
