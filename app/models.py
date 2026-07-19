from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class SiteSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), default='Warisha Faiz')
    role = db.Column(db.String(100), default='Computer Science Student')
    location = db.Column(db.String(100), default='Punjab Group of Colleges')
    about_text = db.Column(db.Text, default='A passionate 3rd-semester Computer Science student learning core programming concepts and exploring software development.')
    email = db.Column(db.String(120), default='warisha@placeholder.com')
    github_url = db.Column(db.String(200), default='')
    linkedin_url = db.Column(db.String(200), default='')
    whatsapp = db.Column(db.String(20), default='923277133082')

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    stack = db.Column(db.String(200), nullable=False) # Comma separated
    live_url = db.Column(db.String(200), nullable=True)
    order = db.Column(db.Integer, default=0)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    order = db.Column(db.Integer, default=0)
