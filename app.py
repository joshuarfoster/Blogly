"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User
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
    return render_template('user.html',user=user)

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

