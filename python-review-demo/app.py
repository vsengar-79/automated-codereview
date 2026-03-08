from flask import Flask, request, jsonify
from services.user_service import get_user, create_user

app = Flask(__name__)

@app.route("/users/<email>")
def get_user_api(email):
    user = get_user(email)
    return jsonify(user)

@app.route("/users", methods=["POST"])
def create_user_api():
    data = request.json
    create_user(data["name"], data["email"], data["password"])
    return {"status": "created"}

if __name__ == "__main__":
    app.run(debug=True, port=5000)
