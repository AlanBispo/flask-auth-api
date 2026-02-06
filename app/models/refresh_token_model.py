from app.extensions import db
from datetime import datetime, timezone

class RefreshTokenModel(db.Model):
    __tablename__ = 'refresh_tokens'

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(500), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    expires_at = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))