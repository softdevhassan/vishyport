# Academic Portfolio - Warisha Faiz

## 1. Planning
**Objective:** To design and develop a clean, academic portfolio to showcase my journey as a 3rd-semester BS Computer Science student at Punjab Group of Colleges.
**Target Audience:** Professors, academic peers, and potential internship recruiters.
**Architecture Design:**
- **Framework:** Python Flask (utilizing MVC-like patterns).
- **Frontend:** HTML5, CSS3 via Tailwind CSS (for a clean, light-mode academic aesthetic).
- **Database:** SQLite (lightweight, file-based database perfect for small-scale applications).
- **Content Strategy:** Focus on educational milestones, foundational programming languages (C, C++, Python, Assembly), and university projects.

## 2. Development
**Tech Stack Used:**
- **Backend:** Python, Flask, SQLAlchemy
- **Frontend:** Jinja2 Templating, Tailwind CSS
- **Tools:** Git, GitHub, VS Code

**Development Phases:**
1. **Environment Preparation:** Initialized the project environment, structured the directory, and installed necessary Python packages.
2. **Database Integration:** Utilized Object-Relational Mapping (ORM) to define tables for academic projects and currently learned skills, ensuring the portfolio can be easily updated.
3. **Template Design:** Developed an elegant, light-themed user interface utilizing Jinja2 template inheritance (`base.html`) to keep code DRY (Don't Repeat Yourself).
4. **Refinement:** Ensured responsive design so the portfolio is accessible on both mobile devices and desktop screens.

## 3. Documentation
- **Modular Structure:** The project uses a structured `app/` directory containing models, routes, and templates to separate concerns.
- **Database Initialization:** Included an automated database seeding script to populate the SQLite database with initial academic data and projects.
- **Readability:** Code is written with clear variable names, and templates are broken down into reusable components (header, footer).

## 4. Deployment
Prepared for cloud deployment:
- **Git & GitHub:** Version control initialized to track development progress.
- **Cloud Hosting (Heroku):** A `Procfile` is included using `gunicorn` as the WSGI HTTP server, making the app production-ready for Heroku deployment.
