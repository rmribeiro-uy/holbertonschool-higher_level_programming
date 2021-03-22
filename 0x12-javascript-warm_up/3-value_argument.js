#!/usr/bin/node
/*
  Prints the first argument passed to it
*/

let numArguments = 0;
const argument = [];
process.argv.forEach((val, index) => {
  numArguments += 1;
  argument[index] = val;
});
if (numArguments >= 3) console.log(argument[2]);
else if (numArguments === 2) console.log('No argument');
