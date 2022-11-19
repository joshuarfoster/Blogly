"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User, Post, Tag, PostTag
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret"
app.debug=True

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home():
    """Redirects to list of users"""
    return redirect('/users')

@app.route('/users')
def show_users():
    """List links of users"""
    users = User.query.all()
    return render_template('users.html', users = users)

@app.route('/users/new')
def show_form():
    """Shows form to make new user"""
    return render_template('new_user.html')

@app.route('/users/new', methods=['POST'])
def create_user():
    first_name=request.form['first_name']
    last_name=request.form['last_name']
    image_url=request.form['image_url']
    user = User(first_name = first_name, last_name = last_name, image_url = image_url)
    db.session.add(user)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<int:user_id>')
def show_user(user_id):
    """Shows User"""
    user = User.query.get_or_404(user_id)
    posts = Post.query.filter(Post.user_id == user_id )
    return render_template('user.html',user=user,posts=posts)

@app.route('/users/<int:user_id>/edit')
def show_edit_form(user_id):
    """Shows edit form"""
    user = User.query.get_or_404(user_id)
    return render_template('edit.html',user = user)

@app.route('/users/<int:user_id>/edit/', methods=['POST'])
def edit_user(user_id):
    """Edits User"""
    user = User.query.get_or_404(user_id)
    first_name=request.form['first_name']
    last_name=request.form['last_name']
    image_url=request.form['image_url']
    user.first_name=first_name
    user.last_name=last_name
    user.image_url=image_url
    db.session.commit()
    return redirect(f'/users/{user.id}')

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).delete()
    db.session.commit()
    return redirect ('/users')

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    user = User.query.get_or_404(post.user_id)
    tags = post.tags
    return render_template('post.html', user = user, post = post, tags = tags)

@app.route('/users/<int:user_id>/posts/new')
def show_new_post_form(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('new_post.html',user= user)

@app.route('/users/<int:user_id>/posts/new', methods=['POST'])
def add_post(user_id):
    content=request.form['content']
    title=request.form['title']
    post= Post(title = title, content = content, user_id = user_id)
    db.session.add(post)
    db.session.commit()
    return redirect(f'/users/{user_id}')

@app.route('/posts/<int:post_id>/edit')
def show_edit_post_form(post_id):
    post=Post.query.get_or_404(post_id)
    return render_template ('edit_post.html', post=post)

@app.route('/posts/<int:post_id>/edit', methods=['POST'])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    title=request.form['title']
    content=request.form['content']
    post.title = title
    post.content = content
    db.session.commit()
    return redirect(f'/posts/{post.id}')

@app.route('/posts/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    user_id=post.user_id
    post = Post.query.filter_by(id=post_id).delete()
    db.session.commit()
    return redirect(f'/users/{user_id}')

@app.route('/tags')
def show_tags():
    tags =  Tag.query.all()
    return render_template('tags.html', tags = tags)

@app.route('/tags/<int:tag_id>')
def show_tag_with_posts(tag_id):
    tag= Tag.query.get_or_404(tag_id)
    posts = tag.posts
    return render_template('tag.html', tag=tag, posts=posts)

@app.route('/tags/new')
def show_new_tag_form():
    return render_template('create_tag.html')

@app.route('/tags/new', methods = ['POST'])
def create_tag():
    name=request.form['name']
    tag = Tag(name=name)
    db.session.add(tag)
    db.session.commit()
    return redirect('/tags')

@app.route('/tags/<int:tag_id>/delete', methods =['POST'])
def delete_tag(tag_id):
    tag = Tag.query.filter_by(id=tag_id).delete()
    db.commit()
    return redirect('/tags')