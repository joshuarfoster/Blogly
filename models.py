from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(50),
                     nullable=False)
    last_name = db.Column(db.String(50),
                     nullable=False)
    image_url = db.Column(db.String(1000), nullable=True)
    posts = db.relationship('Post', backref='users', cascade='all, delete-orphan')

class Post(db.Model):
    """Post"""

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String(50),
                     nullable=False)
    content = db.Column(db.String(1000),
                     nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now,nullable=False)
    user_id = db.column(db.Integer,db.ForeignKey('users.id'))