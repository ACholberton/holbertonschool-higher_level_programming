#!/usr/bin/node
// script computes and prints a factorial//

const arg = parseInt(process.argv[2]);

if (isNaN(arg)) {
  console.log(1);
} else {
  console.log(factorial(arg));
}

function factorial (arg) {
  if (arg < 0) {
    return -1;
  } else if (arg === 0) {
    return 1;
  } else {
    return (arg * factorial(arg - 1));
  }
}
