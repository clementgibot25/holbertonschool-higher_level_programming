from flask import Flask, jsonify, request

app = Flask(__name__)

# Global users dictionary to store user data
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    user = list(users)
    return jsonify(user)

@app.post("/add_user")
def add():
    data = request.json
    user = {"username": data.get("username"), "name": data.get("name"), "age": data.get("age"), "city": data.get("city")}

    if user["username"] is None:
        return {"error":"Username is required"}, 400
    users[data.get("username")] = user
    return jsonify({'message': 'User added', 'user': user}), 201

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

@app.route("/status")
def status():
    # Simple status endpoint
    return "OK"

if __name__ == "__main__":
    app.run(debug=False)
