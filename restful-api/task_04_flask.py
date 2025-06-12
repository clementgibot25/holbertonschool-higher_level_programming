from flask import Flask, jsonify, request

app = Flask(__name__)

# Global users dictionary to store user data
users = {}

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

@app.route("/data")
def data():
    # Returns a list of all usernames
    return jsonify({"usernames": list(users.keys())})

@app.route("/status")
def status():
    # Simple status endpoint
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    # Dynamic route to get user details by username
    if username in users:
        # Create a response that includes the username and all user details
        response = {"username": username}
        response.update(users[username])  # Add all user details to the response
        return jsonify(response)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    # Add a new user to the dictionary
    username = request.json.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    # Extract user details from the request
    user_data = {
        "name": request.json.get("name"),
        "age": request.json.get("age"),
        "city": request.json.get("city")
    }
    
    # Check if user already exists
    if username in users:
        return jsonify({"error": "User already exists"}), 400
        
    # Add the new user to the dictionary
    users[username] = user_data
    
    # Return confirmation with the added user's data
    return jsonify({"message": "User added successfully"}), 201

if __name__ == "__main__":
    app.run(debug=False)