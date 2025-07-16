#!/usr/bin/node

// Get the two arguments
const firstArg = process.argv[2] || '';
const secondArg = process.argv[3] || '';

// Print the arguments in the specified format
console.log(`${firstArg} is ${secondArg}`);