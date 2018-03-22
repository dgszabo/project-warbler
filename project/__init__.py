from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
import os

app = Flask(__name__)

if os.environ.get('ENV') == 'production':
    app.config['DEBUG'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
else:
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/warbler'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or "it's a secret"
toolbar = DebugToolbarExtension(app)

modus = Modus(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from project.users.views import users_blueprint
from project.messages.views import messages_blueprint
from project.users.models import User
from project.messages.models import Message

app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(
    messages_blueprint, url_prefix='/users/<int:id>/messages')


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
def root():
    found_user = User.query.get(session['user_id'])
    ids = [found_user.id] + [user.id for user in found_user.following]
    messages = Message.query.filter(Message.user_id.in_(ids)).order_by('timestamp desc').limit(100)
    return render_template('home.html', messages=messages)

@app.errorhandler(404)
def error(e):
    return render_template('404.html'), 404

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
