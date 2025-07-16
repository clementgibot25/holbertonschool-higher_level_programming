#!/usr/bin/node

// Function to add two integers
function add (a, b) {
  return a + b;
}

// Get the two integer arguments
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

// Check if both arguments are valid numbers
if (isNaN(num1) || isNaN(num2)) {
  console.log('Please provide two valid integers as arguments');
} else {
  // Print the result of the addition
  console.log(add(num1, num2));
}