from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Session, BehaviorLog
from datetime import datetime

behavior_bp = Blueprint("behavior", __name__)

@behavior_bp.route("/log-action", methods=["POST"])
@jwt_required()
def log_action():
    token = request.headers.get("Authorization").split()[1]
    session = Session.query.filter_by(token=token, is_active=True).first()

    if not session:
        return {"msg": "Session revoked"}, 401

    log = BehaviorLog(
        session_id=session.id,
        action=request.json["action"],
        ip_address=request.remote_addr,
        user_agent=request.headers.get("User-Agent"),
        time_gap=0.5
    )
    db.session.add(log)
    db.session.commit()

    return {"msg": "Action logged"}
