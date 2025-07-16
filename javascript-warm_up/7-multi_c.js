#!/usr/bin/node

// Get the first argument and convert it to a number
const x = parseInt(process.argv[2]);

// Check if the conversion was successful and x is a positive number
if (isNaN(x) || x <= 0) {
  console.log('Missing number of occurrences');
} else {
  // Print 'C is fun' x times using a loop
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}