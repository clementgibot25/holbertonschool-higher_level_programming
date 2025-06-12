# RESTful API Project

This project covers the fundamental concepts of building and interacting with RESTful APIs, from basic principles to advanced development and security practices.

## Core Concepts

### 1. HTTP/HTTPS Basics
**HTTP (HyperText Transfer Protocol)** is the foundation of data communication for the World Wide Web. It's a client-server protocol where a client (like a web browser) sends a request to a server, which then returns a response.

- **Methods**: Common actions performed on resources, such as:
  - `GET`: Retrieve a resource.
  - `POST`: Create a new resource.
  - `PUT`: Update an existing resource.
  - `DELETE`: Remove a resource.
- **Status Codes**: Indicate the result of the request (e.g., `200 OK`, `404 Not Found`, `500 Internal Server Error`).
- **HTTPS (HTTP Secure)**: The secure version of HTTP. It encrypts the data exchanged between the client and server using TLS/SSL, protecting it from eavesdropping and tampering.

### 2. API Consumption with Command Line
Interacting with APIs directly from the command line is a fundamental skill. The most common tool for this is `curl`.

**Example (using `curl` to fetch data):**
```bash
# Make a GET request to an API endpoint
curl https://jsonplaceholder.typicode.com/posts/1

# Send data with a POST request
curl -X POST -H "Content-Type: application/json" -d '{"title": "foo", "body": "bar", "userId": 1}' https://jsonplaceholder.typicode.com/posts
```

### 3. API Consumption with Python
The `requests` library is the de-facto standard for making HTTP requests in Python, simplifying the process of consuming APIs.

**Example (using `requests`):**
```python
import requests
import json

# GET request
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
if response.status_code == 200:
    print('Success!')
    print(response.json()) # Automatically decodes JSON

# POST request
new_post = {
    'title': 'New Title',
    'body': 'Some content',
    'userId': 1
}
post_response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)
print(post_response.status_code)
print(post_response.json())
```

### 4. API Development with `http.server`
Python's built-in `http.server` module allows you to create a simple web server and a basic API without any external libraries. It's great for learning but is single-threaded and not suitable for production.

**Example (a simple API):**
```python
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response_data = {'message': 'Hello, API!'}
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

httpd = HTTPServer(('localhost', 8000), SimpleAPI)
httpd.serve_forever()
```

### 5. API Development with Flask
**Flask** is a lightweight and flexible Python web framework ideal for building robust and scalable APIs. It provides tools for routing, request handling, and more.

**Example (a simple Flask API):**
```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify({'items': ['item1', 'item2']})

@app.route('/api/items', methods=['POST'])
def add_item():
    new_item = request.json.get('item')
    # Logic to add the item...
    return jsonify({'message': f'Item "{new_item}" added'}), 201

if __name__ == '__main__':
    app.run(debug=True)
```

### 6. API Security & Authentication
Protecting your API is crucial. Common strategies include:

- **API Keys**: A simple token sent with each request to identify the client.
- **Token-Based Authentication (e.g., JWT)**: The client authenticates once to get a token (like a JSON Web Token), which is then sent with subsequent requests to prove identity.
- **OAuth**: A standard for delegated access, allowing users to grant third-party applications access to their resources without sharing credentials.
- **Always use HTTPS** to encrypt all communication.

### 7. API Standards & Documentation with OpenAPI
Good documentation makes an API usable. The **OpenAPI Specification** (formerly Swagger) is a standard for describing REST APIs.

- **Benefits**: It creates a contract that is both human-readable and machine-readable, enabling:
  - **Automatic documentation generation**.
  - **Client SDK generation** in various languages.
  - **Automated testing**.

**Example (OpenAPI snippet in YAML):**
```yaml
openapi: 3.0.0
info:
  title: Simple Items API
  version: 1.0.0
paths:
  /items:
    get:
      summary: Returns a list of items.
      responses:
        '200':
          description: A JSON array of items.
          content:
            application/json:
              schema:
                type: array
                items:
                  type: string
