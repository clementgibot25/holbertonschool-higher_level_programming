#!/usr/bin/python3
"""
Simple HTTP server implementation using http.server module
"""

import http.server
import socketserver
import json

PORT = 8000


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    A simple HTTP request handler that responds to GET requests
    with a text message.
    """

    def do_GET(self):
        """
        Handle GET requests based on the path requested.
        """
        if self.path == "/status":
            # Handle /status endpoint
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            # Send text response
            self.wfile.write("OK".encode('utf-8'))
            return

        elif self.path == "/info":
            # Handle /info endpoint
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            # Sample JSON data
            datas = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            # Send JSON response
            self.wfile.write(json.dumps(datas).encode('utf-8'))
            return

        elif self.path == "/data":
            # Handle /data endpoint
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            # Sample JSON data as specified
            data = {"name": "John", "age": 30, "city": "New York"}

            # Send JSON response
            self.wfile.write(json.dumps(data).encode('utf-8'))
            return

        elif self.path == "/":
            # Handle root path
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            # Default message
            message = {"message": "Hello, this is a simple API!"}
            self.wfile.write(json.dumps(message).encode('utf-8'))
            return

        else:
            # Handle undefined endpoints with 404 error
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            # Error message
            self.wfile.write("status: 404 Not Found", "message: Endpoint not found".encode('utf-8'))
            return


def run_server():
    """
    Function to start the server
    """
    # Create a server, binding to localhost on port 8000
    with socketserver.TCPServer(("", PORT), SimpleAPIHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        # Serve until process is killed
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")


if __name__ == "__main__":
    run_server()
