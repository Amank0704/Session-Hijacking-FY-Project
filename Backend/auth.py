from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from models import db, User, Session
from datetime import datetime

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    user = User(
        username=data["username"],
        email=data["email"],
        password_hash=generate_password_hash(data["password"])
    )
    db.session.add(user)
    db.session.commit()
    return {"msg": "User registered"}

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()

    if not user or not check_password_hash(user.password_hash, data["password"]):
        return {"msg": "Invalid credentials"}, 401

    token = create_access_token(identity=user.id)

    session = Session(
        user_id=user.id,
        token=token,
        ip_address=request.remote_addr,
        user_agent=request.headers.get("User-Agent"),
        created_at=datetime.utcnow()
    )
    db.session.add(session)
    db.session.commit()

    return {"token": token}
