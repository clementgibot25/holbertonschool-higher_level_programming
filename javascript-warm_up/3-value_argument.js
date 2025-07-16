#!/usr/bin/node

// Get the first argument (index 2 in process.argv)
const arg = process.argv[2];

// Check if argument exists and print the appropriate message
console.log(arg === undefined ? 'No argument' : arg);