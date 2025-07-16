#!/usr/bin/node

// Get the number of command-line arguments (excluding 'node' and script path)
const argsCount = process.argv.length - 2;

// Check the number of arguments and print the appropriate message
if (argsCount === 0) {
  console.log('No argument');
} else if (argsCount === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}