import os
from flask import Flask, render_template
from flask_migrate import Migrate
from models import db, Course, CourseOutcome, Question, User
from routes.courses import course_bp
from routes.questions import question_bp
from routes.rubrics import rubric_bp
from routes.auth import auth_bp
from flask_login import LoginManager, login_required, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exam_office.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')  # Use environment variable or a default

db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@app.before_request
def create_tables():
    app.before_request_funcs[None].remove(create_tables)
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def home():
    return render_template('index.html')

app.register_blueprint(course_bp, url_prefix='/courses')
app.register_blueprint(question_bp, url_prefix='/questions')
app.register_blueprint(rubric_bp, url_prefix='/rubrics')
app.register_blueprint(auth_bp)


if __name__ == '__main__':
    app.run(debug=True)
