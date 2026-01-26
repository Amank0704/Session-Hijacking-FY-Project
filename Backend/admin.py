from flask import Blueprint
from models import Session

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/sessions", methods=["GET"])
def all_sessions():
    sessions = Session.query.all()
    return [{
        "user_id": s.user_id,
        "ip": s.ip_address,
        "active": s.is_active,
        "suspicious": s.is_suspicious
    } for s in sessions]
