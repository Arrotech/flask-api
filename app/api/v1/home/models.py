from sqlalchemy import inspect
from app.extensions import db

# write your models here


class User(db.Model):
    """User model."""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username=None, email=None):
        """User constructor."""
        super().__init__()
        self.username = username
        self.email = email

    def as_dict(self):
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}

    def __repr__(self):
        """Print the user object."""
        return "<User '{}'>".format(self.firstname)
