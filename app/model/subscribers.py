from datetime import datetime, timezone
from ..extensions import db
    
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    date_registered = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))


    def __repr__(self):
        return f"Post('{self.emain}', '{self.date_registered}')"
    
