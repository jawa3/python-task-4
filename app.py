from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    1: {"name": "Jawahar", "email": "jawahar@example.com"},
    2: {"name": "John", "email": "john@example.com"}
}


# GET - Get all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)


# GET - Get one user
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[user_id])


# POST - Create user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json

    new_id = max(users.keys(), default=0) + 1

    users[new_id] = {
        "name": data["name"],
        "email": data["email"]
    }

    return jsonify({
        "id": new_id,
        "message": "User created successfully",
        "user": users[new_id]
    }), 201


# PUT - Update user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.json

    users[user_id]["name"] = data.get(
        "name",
        users[user_id]["name"]
    )

    users[user_id]["email"] = data.get(
        "email",
        users[user_id]["email"]
    )

    return jsonify({
        "message": "User updated successfully",
        "user": users[user_id]
    })


# DELETE - Delete user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    deleted_user = users.pop(user_id)

    return jsonify({
        "message": "User deleted successfully",
        "user": deleted_user
    })


if __name__ == "__main__":
    app.run(debug=True)
