from app import create_app, db
from app.models import User, SiteSettings, Project, Service

app = create_app()

@app.cli.command("init-db")
def init_db():
    with app.app_context():
        db.create_all()
        
        # Admin
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin')
            admin.set_password('admin')
            db.session.add(admin)
            
        # Settings
        if not SiteSettings.query.first():
            settings = SiteSettings(
                name="Warisha Faiz",
                role="Computer Science Student",
                location="ILM College",
                about_text="A passionate 3rd-semester Computer Science student learning core programming concepts and exploring software development.",
                email="warisha@placeholder.com",
                github_url="",
                linkedin_url="",
                whatsapp="00000000000"
            )
            db.session.add(settings)
            
        # Seed Projects
        if Project.query.count() == 0:
            projects_data = [
                {"title": "Console Calculator", "desc": "A basic calculator built using Assembly language concepts.", "stack": "Assembly", "url": "", "order": 1},
                {"title": "Library Management System", "desc": "Object-oriented terminal application for managing library books and users.", "stack": "C++", "url": "", "order": 2},
                {"title": "Student Record System", "desc": "A simple record-keeping application utilizing file handling.", "stack": "C, PHP", "url": "", "order": 3},
                {"title": "Basic Web Portfolio", "desc": "My first web portfolio showcasing my academic journey.", "stack": "HTML, CSS, JS", "url": "", "order": 4}
            ]
            for p in projects_data:
                db.session.add(Project(title=p['title'], description=p['desc'], stack=p['stack'], live_url=p['url'], order=p['order']))
                
        # Seed Services / Categories
        if Service.query.count() == 0:
            services_data = ["HTML / CSS", "JavaScript", "PHP", "Python", "C & C++", "Assembly Language"]
            for i, s in enumerate(services_data):
                db.session.add(Service(name=s, order=i+1))
                
        db.session.commit()
        print("Database initialized and fully seeded with projects and services!")

if __name__ == '__main__':
    app.run(debug=True)
