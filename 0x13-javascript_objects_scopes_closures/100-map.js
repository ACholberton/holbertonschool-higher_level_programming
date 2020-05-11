#!/usr/bin/node
// script that imports an array and computes a new array //
const list = require('./100-data').list;
console.log(list);
const map = list.map((a, i) => a * i);
console.log(map);
