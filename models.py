from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    course_code = db.Column(db.String(20), nullable=False)
    school = db.Column(db.String(10), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    outcomes = db.relationship('CourseOutcome', backref='course', lazy=True, cascade="all, delete-orphan")

class CourseOutcome(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    bloom_level = db.Column(db.String(50))
    topic = db.Column(db.String(100))
    difficulty = db.Column(db.String(50))
    question_type = db.Column(db.String(50))
    options = db.Column(db.Text)  # To store options for MCQs
    correct_answer = db.Column(db.Text)  # To store correct answer(s)
    pairs = db.Column(db.Text)  # To store pairs for matching questions
    essay_details = db.Column(db.Text)  # To store details for essay questions
    created_by = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_edited_by = db.Column(db.String(100), nullable=True)
    last_edited_at = db.Column(db.DateTime, nullable=True)
    course = db.relationship('Course', backref=db.backref('questions', lazy=True))

class Rubric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    blueprint = db.Column(db.JSON)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)