from flask_sqlalchemy import SQLAlchemy
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
    posts = db.relationship('Post', backref='user', cascade='all, delete-orphan')

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
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    tags = db.relationship('Tag',
                            secondary='posts_tags',
                            cascade = 'all,delete',
                            backref='posts')


class Tag(db.Model):
    """Tag"""

    __tablename__="tags"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                     nullable=False)

class PostTag(db.Model):
    """PostTag"""

    __tablename__ = "posts_tags"

    post_id = db.Column(db.Integer,
                        db.ForeignKey('posts.id', ondelete='CASCADE'),
                        primary_key=True,)
    tag_id = db.Column(db.Integer,
                        db.ForeignKey('tags.id', ondelete='CASCADE'),
                        primary_key=True)
        


