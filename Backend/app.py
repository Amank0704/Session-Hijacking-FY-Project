from flask import Flask
from flask_jwt_extended import JWTManager
from config import *
from models import db
from auth import auth_bp
from behavior import behavior_bp
from admin import admin_bp

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(behavior_bp, url_prefix="/api")
app.register_blueprint(admin_bp, url_prefix="/api/admin")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
