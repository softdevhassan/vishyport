from app import db

class SiteSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), default='Warisha Faiz')
    role = db.Column(db.String(100), default='Computer Science Student')
    location = db.Column(db.String(100), default='Punjab Group of Colleges')
    about_text = db.Column(db.Text, default='A passionate 3rd-semester Computer Science student learning core programming concepts and exploring software development.')
    email = db.Column(db.String(120), default='warisha@placeholder.com')
    github_url = db.Column(db.String(200), default='')
    linkedin_url = db.Column(db.String(200), default='')
    whatsapp = db.Column(db.String(20), default='+923000000000')

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
