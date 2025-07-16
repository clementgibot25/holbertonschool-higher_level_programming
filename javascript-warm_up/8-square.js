#!/usr/bin/node

// Get the size argument and convert it to a number
const size = parseInt(process.argv[2]);

// Check if the conversion was successful and size is a positive number
if (isNaN(size) || size <= 0) {
  console.log('Missing size');
} else {
  // Print the square
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}