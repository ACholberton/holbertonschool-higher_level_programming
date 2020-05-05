#!/usr/bin/node
// script prints the argument passed in the command line//

if (process.argv[2]) {
  console.log(process.argv);
} else {
  console.log('No argument');
}
