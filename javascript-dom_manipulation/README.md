# JavaScript DOM Manipulation

This guide covers essential concepts of DOM manipulation in JavaScript.

## Table of Contents
1. [What is the DOM?](#what-is-the-dom)
2. [Selecting HTML Elements](#selecting-html-elements)
3. [ID vs Class vs Tag Name Selectors](#id-vs-class-vs-tag-name-selectors)
4. [Modifying Element Styles](#modifying-element-styles)
5. [Getting and Updating Element Content](#getting-and-updating-element-content)
6. [Modifying the DOM](#modifying-the-dom)
7. [Making Requests with XMLHttpRequest](#making-requests-with-xmlhttprequest)
8. [Making Requests with Fetch API](#making-requests-with-fetch-api)
9. [Listening to DOM Events](#listening-to-dom-events)
10. [Listening to User Events](#listening-to-user-events)

## What is the DOM?

The Document Object Model (DOM) is a programming interface for HTML and XML documents. It represents the page so that programs can change the document structure, style, and content. The DOM represents the document as nodes and objects, allowing programming languages to interact with the page.

## Selecting HTML Elements

JavaScript provides several methods to select HTML elements:

```javascript
// By ID (returns a single element)
const elementById = document.getElementById('myId');

// By class name (returns HTMLCollection)
const elementsByClass = document.getElementsByClassName('myClass');

// By tag name (returns HTMLCollection)
const elementsByTag = document.getElementsByTagName('div');

// Query Selector (returns the first matching element)
const element = document.querySelector('.myClass');

// Query Selector All (returns NodeList)
const elements = document.querySelectorAll('div.myClass');
```

## ID vs Class vs Tag Name Selectors

| Selector | Syntax | Returns | Uniqueness | Performance |
|----------|--------|---------|------------|-------------|
| ID | `#id` | Single element | Must be unique | Fastest |
| Class | `.class` | Collection | Can be used multiple times | Fast |
| Tag | `tag` | Collection | Can be used multiple times | Fastest |

## Modifying Element Styles

You can modify element styles using the `style` property:

```javascript
const element = document.getElementById('myElement');

// Set single style property
element.style.color = 'blue';

// Set multiple styles
Object.assign(element.style, {
    backgroundColor: '#f0f0f0',
    padding: '10px',
    border: '1px solid #ccc'
});

// Add/remove CSS classes
element.classList.add('active');
element.classList.remove('inactive');
element.classList.toggle('highlight');
```

## Getting and Updating Element Content

```javascript
const element = document.getElementById('myElement');

// Get content
const content = element.textContent; // Text only
const htmlContent = element.innerHTML; // HTML content

// Set content
element.textContent = 'New text content'; // Text only (escapes HTML)
element.innerHTML = '<strong>New</strong> content'; // Parses HTML

// Get/set form element values
const input = document.querySelector('input');
const value = input.value; // Get value
input.value = 'New value'; // Set value
```

## Modifying the DOM

### Creating Elements
```javascript
// Create new element
const newDiv = document.createElement('div');
newDiv.textContent = 'New element';

// Add to DOM
document.body.appendChild(newDiv);
```

### Modifying Elements
```javascript
const element = document.getElementById('myElement');

// Add/remove attributes
element.setAttribute('data-info', 'value');
const value = element.getAttribute('data-info');
element.removeAttribute('data-info');

// Add/remove classes
element.classList.add('new-class');
element.classList.remove('old-class');
element.classList.toggle('active');
```

### Removing Elements
```javascript
const element = document.getElementById('myElement');
element.remove(); // Removes the element

// Alternative
element.parentNode.removeChild(element);
```

## Making Requests with XMLHttpRequest

```javascript
const xhr = new XMLHttpRequest();
xhr.open('GET', 'https://api.example.com/data', true);

xhr.onload = function() {
    if (xhr.status >= 200 && xhr.status < 300) {
        const data = JSON.parse(xhr.responseText);
        console.log('Success:', data);
    } else {
        console.error('Error:', xhr.statusText);
    }
};

xhr.onerror = function() {
    console.error('Request failed');
};

xhr.send();

// For POST requests
const xhrPost = new XMLHttpRequest();
xhrPost.open('POST', 'https://api.example.com/data', true);
xhrPost.setRequestHeader('Content-Type', 'application/json');
xhrPost.send(JSON.stringify({ key: 'value' }));
```

## Making Requests with Fetch API

```javascript
// GET request
fetch('https://api.example.com/data')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => console.log('Success:', data))
    .catch(error => console.error('Error:', error));

// POST request
fetch('https://api.example.com/data', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ key: 'value' })
})
.then(response => response.json())
.then(data => console.log('Success:', data))
.catch(error => console.error('Error:', error));

// Async/Await version
async function fetchData() {
    try {
        const response = await fetch('https://api.example.com/data');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        console.log('Success:', data);
    } catch (error) {
        console.error('Error:', error);
    }
}
```

## Listening to DOM Events

### Basic Event Listener
```javascript
const button = document.getElementById('myButton');

// Add event listener
button.addEventListener('click', function(event) {
    console.log('Button clicked!', event);
});

// Remove event listener
const clickHandler = function() {
    console.log('Button clicked!');    
};
button.addEventListener('click', clickHandler);
button.removeEventListener('click', clickHandler);
```

### Event Delegation
```javascript
document.addEventListener('click', function(event) {
    if (event.target.matches('button.action')) {
        console.log('Action button clicked:', event.target);
    }
});
```

## Listening to User Events

### Common User Events
```javascript
const input = document.querySelector('input');
const form = document.querySelector('form');

// Input events
input.addEventListener('input', (e) => {
    console.log('Input value:', e.target.value);
});

// Form submission
form.addEventListener('submit', (e) => {
    e.preventDefault();
    console.log('Form submitted');
});

// Keyboard events
document.addEventListener('keydown', (e) => {
    console.log('Key pressed:', e.key);
    
    // Check for specific key
    if (e.key === 'Escape') {
        console.log('Escape key pressed');
    }
});

// Mouse events
const box = document.getElementById('box');
box.addEventListener('mouseenter', () => console.log('Mouse entered'));
box.addEventListener('mouseleave', () => console.log('Mouse left'));
box.addEventListener('mousemove', (e) => {
    console.log(`Mouse at: ${e.clientX}, ${e.clientY}`);
});

// Scroll events
window.addEventListener('scroll', () => {
    console.log('Scrolling...', window.scrollY);
});

// Resize events
window.addEventListener('resize', () => {
    console.log('Window resized:', window.innerWidth, 'x', window.innerHeight);
});
```

### Touch Events (for mobile)
```javascript
const touchElement = document.getElementById('touchable');

touchElement.addEventListener('touchstart', (e) => {
    console.log('Touch started', e.touches[0].clientX, e.touches[0].clientY);
});

touchElement.addEventListener('touchmove', (e) => {
    e.preventDefault();
    console.log('Touch moved', e.touches[0].clientX, e.touches[0].clientY);
});

touchElement.addEventListener('touchend', () => {
    console.log('Touch ended');
});
```

This guide covers the fundamental concepts of DOM manipulation in JavaScript. Practice these concepts to become proficient in creating dynamic and interactive web applications.
