# File: app.py
import os
from flask import Flask, render_template
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from flask_login import LoginManager, login_required, current_user
from models import db, User
from routes.courses import course_bp
from routes.questions import question_bp
from routes.rubrics import rubric_bp
from routes.tests import test_bp
from routes.auth import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    csrf = CSRFProtect(app)  # Ensure CSRFProtect is initialized

    initialize_extensions(app)
    register_blueprints(app)

    with app.app_context():
        db.create_all()

    return app

def initialize_extensions(app):
    db.init_app(app)
    Migrate(app, db)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

def register_blueprints(app):
    app.register_blueprint(course_bp, url_prefix='/courses')
    app.register_blueprint(question_bp, url_prefix='/questions')
    app.register_blueprint(rubric_bp, url_prefix='/rubrics')
    app.register_blueprint(test_bp, url_prefix='/tests')
    app.register_blueprint(auth_bp)

app = create_app()

@app.route('/')
@login_required
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
