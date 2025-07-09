from flask import Flask, request, jsonify
from models import User, Session, init_db

app = Flask(__name__)
init_db()

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    session = Session()
    if session.query(User).filter_by(username=data["username"]).first():
        return jsonify({"message": "User exists"}), 400
    user = User(username=data["username"], password=data["password"])
    session.add(user)
    session.commit()
    return jsonify({"message": "User registered"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    session = Session()
    user = session.query(User).filter_by(username=data["username"], password=data["password"]).first()
    if not user:
        return jsonify({"message": "Invalid credentials"}), 401
    return jsonify({"message": "Login successful"}), 200

if __name__ == "__main__":
    app.run(debug=True)
