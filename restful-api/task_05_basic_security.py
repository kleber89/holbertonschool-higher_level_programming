from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt_claims,
)

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this in your application
jwt = JWTManager(app)

# Example users (in a real application, use a database)
users = {
    "john": {"password": "hashedpassword", "role": "admin"},
    "jane": {"password": "hashedpassword", "role": "user"},
}


# Login route to generate JWT token
@app.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get("username")
    password = request.json.get("password")
    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    if username not in users or not check_password_hash(
        users.get(username).get("password"), password
    ):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(
        identity=username, user_claims={"role": users.get(username).get("role")}
    )
    return jsonify(access_token=access_token), 200


# Protected route using JWT token
@app.route("/protected-jwt")
@jwt_required()
def protected_jwt():
    current_user = get_jwt_identity()
    user_role = get_jwt_claims().get("role")
    return jsonify(logged_in_as=current_user, role=user_role), 200


if __name__ == "__main__":
    app.run(debug=True)
