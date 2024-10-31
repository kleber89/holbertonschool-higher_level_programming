#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request

users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
         "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def jsonify_function():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>", methods=["GET"])
def user_name(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def new_user():
    user_data = request.get_json()
    user_name = user_data.get("name")
    if not user_name:
        return jsonify({"error": "Username is required"}), 400
    else:
        users[user_name] = user_data
        return jsonify({
        "message": "User added",
        "user": user_data}), 201


if __name__ == "__main__":
    app.run()