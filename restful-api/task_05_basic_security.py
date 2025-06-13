#!/usr/bin/env python3
"""
Task 05: Basic Security with JWT for login
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity, verify_jwt_in_request, get_jwt

app = Flask(__name__)
auth = HTTPBasicAuth()

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "i_need_to_change_the_secret_key"
jwt = JWTManager(app)


# In-memory database for users
users = {
    "user1": {"username": "user1", "password_hash": generate_password_hash("password123"), "role": "user"},
    "admin1": {"username": "admin1", "password_hash": generate_password_hash("adminpass"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    """Verify password for basic auth"""
    user = users.get(username)
    if user and check_password_hash(user.get('password_hash'), password):
        return user
    return None

@app.route('/')
def home():
    """Home route"""
    return "Welcome!"

@app.route('/login', methods=['POST'])
def login():
    """Logs a user in and returns a JWT token with their role."""
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing username or password"}), 400

    username = data.get('username')
    password = data.get('password')

    user = users.get(username)

    if user and check_password_hash(user.get('password_hash'), password):
        # Include the user's role in the JWT's claims
        additional_claims = {"role": user.get("role")}
        access_token = create_access_token(identity=username, additional_claims=additional_claims)
        return jsonify(access_token=access_token)

    return jsonify({"error": "Invalid username or password"}), 401

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """A route protected by HTTP Basic Auth."""
    return jsonify(message="Basic Auth: Access Granted")

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """A route protected by JWT."""
    return jsonify(message="JWT Auth: Access Granted")


def admin_required(fn):
    """Decorator to protect routes that require admin privileges."""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims.get("role") != "admin":
            return jsonify({"error": "Admin access required"}), 403
        else:
            return fn(*args, **kwargs)
    return wrapper

@app.route('/admin-only')
@admin_required
def admin_only():
    """An admin-only route protected by JWT with role check."""
    return jsonify(message="Admin Access: Granted")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
