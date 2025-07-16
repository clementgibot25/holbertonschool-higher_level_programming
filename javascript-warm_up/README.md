# JavaScript Basics

Welcome to the JavaScript Basics guide! This README covers fundamental JavaScript concepts that every developer should know.

## Table of Contents
1. [Why JavaScript is Amazing](#why-javascript-is-amazing)
2. [Running JavaScript](#running-javascript)
3. [Variables and Constants](#variables-and-constants)
4. [Variable Declarations: var, let, const](#variable-declarations)
5. [Data Types](#data-types)
6. [Conditional Statements](#conditional-statements)
7. [Comments](#comments)
8. [Assigning Values](#assigning-values)
9. [Loops](#loops)
10. [Functions](#functions)
11. [Variable Scope](#variable-scope)
12. [Arithmetic Operators](#arithmetic-operators)
13. [Working with Objects (Dictionaries)](#working-with-objects)
14. [Importing Files](#importing-files)

## Why JavaScript is Amazing

JavaScript is a versatile, high-level programming language that powers the modern web. It's:
- **Everywhere**: Runs in browsers, servers (Node.js), mobile apps, and even IoT devices
- **Versatile**: Supports multiple programming paradigms (OOP, functional, procedural)
- **Dynamic**: No need to declare variable types
- **Asynchronous**: Handles multiple operations simultaneously
- **Huge Ecosystem**: NPM (Node Package Manager) offers over a million packages
- **Constantly Evolving**: Regular updates with new features (ECMAScript)

## Running JavaScript

### In Browser:
1. Create an HTML file:
   ```html
   <!DOCTYPE html>
   <html>
   <body>
     <script src="script.js"></script>
   </body>
   </html>
   ```
2. Create a `script.js` file with your JavaScript code
3. Open the HTML file in a web browser

### Using Node.js:
1. Install Node.js from [nodejs.org](https://nodejs.org/)
2. Create a file (e.g., `script.js`)
3. Run it with: `node script.js`

## Variables and Constants

### Creating Variables:
```javascript
let name = "John";    // Mutable variable
var age = 25;         // Old way (avoid in modern JS)
const PI = 3.14;      // Constant (cannot be reassigned)
```

## Variable Declarations

| Keyword | Scope     | Hoisting | Reassignable | Re-declarable |
|---------|-----------|----------|--------------|----------------|
| `var`   | Function  | Yes      | Yes          | Yes            |
| `let`   | Block     | No       | Yes          | No             |
| `const` | Block     | No       | No           | No             |

## Data Types

JavaScript has dynamic types. The same variable can hold different data types:

1. **Primitive Types**:
   - `String`: "Hello World"
   - `Number`: 42, 3.14
   - `Boolean`: true/false
   - `null`: intentional absence of value
   - `undefined`: variable declared but not assigned
   - `Symbol`: unique identifier (ES6+)
   - `BigInt`: large integers (ES2020+)

2. **Object Types**:
   - `Object`: {name: "John", age: 30}
   - `Array`: [1, 2, 3]
   - `Function`: function() {}
   - `Date`: new Date()

## Conditional Statements

### if statement:
```javascript
if (condition) {
    // code to execute if condition is true
}
```

### if...else:
```javascript
if (condition) {
    // code if true
} else {
    // code if false
}
```

### else if:
```javascript
if (condition1) {
    // code if condition1 is true
} else if (condition2) {
    // code if condition2 is true
} else {
    // code if all conditions are false
}
```

## Comments

```javascript
// Single-line comment

/* 
   Multi-line
   comment 
*/

/**
 * Documentation comment
 * @param {number} num - A number parameter
 * @returns {number} The square of the number
 */
function square(num) {
    return num * num;
}
```

## Assigning Values

```javascript
let x = 10;         // Number
let name = "Alice"; // String
let isTrue = true;  // Boolean
let person = {      // Object
    name: "John",
    age: 30
};
let colors = ["red", "green", "blue"]; // Array

// Multiple assignments
let a = 1, b = 2, c = 3;

// Destructuring assignment
const [first, second] = [1, 2];  // first = 1, second = 2
const {name, age} = person;      // name = "John", age = 30
```

## Loops

### while loop:
```javascript
let i = 0;
while (i < 5) {
    console.log(i);
    i++;
}
```

### do...while loop:
```javascript
let i = 0;
do {
    console.log(i);
    i++;
} while (i < 5);
```

### for loop:
```javascript
for (let i = 0; i < 5; i++) {
    console.log(i);
}
```

### for...of loop (for arrays, strings, etc.):
```javascript
const colors = ["red", "green", "blue"];
for (const color of colors) {
    console.log(color);
}
```

### for...in loop (for object properties):
```javascript
const person = {name: "John", age: 30};
for (const key in person) {
    console.log(`${key}: ${person[key]}`);
}
```

### break and continue:
```javascript
// break exits the loop
for (let i = 0; i < 10; i++) {
    if (i === 5) break;
    console.log(i); // 0, 1, 2, 3, 4
}

// continue skips the current iteration
for (let i = 0; i < 5; i++) {
    if (i === 2) continue;
    console.log(i); // 0, 1, 3, 4
}
```

## Functions

### Function Declaration:
```javascript
function greet(name) {
    return `Hello, ${name}!`;
}
```

### Function Expression:
```javascript
const greet = function(name) {
    return `Hello, ${name}!`;
};
```

### Arrow Function (ES6+):
```javascript
const greet = (name) => `Hello, ${name}!`;
```

### Default Parameters:
```javascript
function greet(name = "Guest") {
    return `Hello, ${name}!`;
}
```

### Functions without return:
A function without a return statement returns `undefined`.

```javascript
function noReturn() {
    // no return statement
}
console.log(noReturn()); // undefined
```

## Variable Scope

- **Global Scope**: Variables declared outside any function
- **Function Scope**: Variables declared with `var` inside a function
- **Block Scope**: Variables declared with `let` or `const` inside a block `{}`

```javascript
let globalVar = "I'm global";

function example() {
    var functionVar = "I'm function scoped";
    
    if (true) {
        let blockVar = "I'm block scoped";
        console.log(blockVar); // Works
    }
    
    console.log(globalVar);    // Works
    console.log(functionVar);  // Works
    console.log(blockVar);     // ReferenceError
}
```

## Arithmetic Operators

| Operator | Description          | Example |
|----------|----------------------|---------|
| `+`      | Addition             | 2 + 3 = 5 |
| `-`      | Subtraction          | 5 - 2 = 3 |
| `*`      | Multiplication       | 2 * 3 = 6 |
| `/`      | Division             | 6 / 2 = 3 |
| `%`      | Modulus (Remainder)  | 5 % 2 = 1 |
| `**`     | Exponentiation (ES6) | 2 ** 3 = 8 |
| `++`     | Increment            | let x = 5; x++; // x = 6 |
| `--`     | Decrement            | let x = 5; x--; // x = 4 |

### Assignment Operators:
```javascript
let x = 10;
x += 5;  // x = x + 5
x -= 3;  // x = x - 3
x *= 2;  // x = x * 2
x /= 4;  // x = x / 4
x %= 3;  // x = x % 3
x **= 2; // x = x ** 2
```

## Working with Objects (Dictionaries)

Objects in JavaScript are collections of key-value pairs:

```javascript
// Creating an object
const person = {
    name: "John",
    age: 30,
    isStudent: false,
    address: {
        city: "New York",
        country: "USA"
    },
    hobbies: ["reading", "coding", "gaming"],
    // Method (function in an object)
    greet: function() {
        return `Hello, my name is ${this.name}`;
    }
};

// Accessing properties
console.log(person.name);        // Dot notation
console.log(person["age"]);      // Bracket notation

// Adding properties
person.email = "john@example.com";
person["phone"] = "123-456-7890";

// Deleting properties
delete person.isStudent;

// Checking if property exists
console.log("name" in person);  // true
console.log(person.hasOwnProperty("age"));  // true

// Iterating over properties
for (const key in person) {
    console.log(`${key}: ${person[key]}`);
}

// Object methods
const keys = Object.keys(person);     // Array of keys
const values = Object.values(person); // Array of values
const entries = Object.entries(person); // Array of [key, value] pairs

// Object destructuring
const { name, age, ...rest } = person;
```

## Importing Files

### CommonJS (Node.js):
```javascript
// Exporting (file: math.js)
const add = (a, b) => a + b;
const PI = 3.14159;
module.exports = { add, PI };

// Importing (file: app.js)
const math = require('./math');
console.log(math.add(2, 3));  // 5
console.log(math.PI);         // 3.14159

// Or with destructuring
const { add, PI } = require('./math');
```

### ES Modules (Modern JavaScript):
```javascript
// Exporting (file: math.js)
export const add = (a, b) => a + b;
export const PI = 3.14159;

// Or export default
// export default { add, PI };

// Importing (file: app.js)
import { add, PI } from './math.js';
// Or for default export: import math from './math.js';

console.log(add(2, 3));  // 5
console.log(PI);         // 3.14159
```

### In HTML with ES Modules:
```html
<script type="module">
    import { add } from './math.js';
    console.log(add(2, 3));
</script>
```

## Conclusion

This guide covers the fundamental concepts of JavaScript programming. JavaScript is a powerful and flexible language that continues to evolve. Practice these concepts to build a strong foundation in JavaScript development.

Happy coding! 🚀
