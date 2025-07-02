from app import db
from datetime import datetime, timezone

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password=db.Column(db.String(255), nullable=False)
    is_verified=db.Column(db.Boolean, default=False)
    is_ops_user=db.Column(db.Boolean, default=False)# True if ops else false for client
    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
