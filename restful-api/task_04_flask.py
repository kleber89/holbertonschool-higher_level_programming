from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


# Root endpoint
@app.route("/")
def home():
    return "Welcome to the Flask API!"


# Data endpoint
@app.route("/data")
def get_data():
    usernames = list(users.keys())
    return jsonify(usernames)


# Status endpoint
@app.route("/status")
def status():
    return "OK"


# Get user details by username
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


# Add a new user
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")
    if username and username not in users:
        users[username] = {
            "name": data.get("name"),
            "age": data.get("age"),
            "city": data.get("city"),
        }
        return (
            jsonify({"message": "User added successfully", "user": users[username]}),
            201,
        )
    else:
        return jsonify({"error": "User already exists or invalid data"}), 400


if __name__ == "__main__":
    app.run(debug=True)
