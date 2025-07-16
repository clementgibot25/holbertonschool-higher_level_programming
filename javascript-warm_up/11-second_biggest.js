#!/usr/bin/node

// Get all arguments except the first two (node and script path)
const args = process.argv.slice(2);

// Handle edge cases
if (args.length <= 1) {
  console.log(0);
} else {
  // Convert all arguments to numbers and sort in descending order
  const numbers = args.map(Number).sort((a, b) => b - a);
  
  // Find the second biggest number (first unique number after the first one)
  let secondBiggest = numbers[1];
  
  // If all numbers are the same, second biggest is 0
  if (numbers.every(num => num === numbers[0])) {
    secondBiggest = 0;
  } else {
    // Find the first number that's different from the first one
    for (let i = 1; i < numbers.length; i++) {
      if (numbers[i] < numbers[0]) {
        secondBiggest = numbers[i];
        break;
      }
    }
  }
  
  console.log(secondBiggest);
}