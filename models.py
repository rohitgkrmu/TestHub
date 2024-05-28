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

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'course_id': self.course_id,
            'bloom_level': self.bloom_level,
            'topic': self.topic,
            'difficulty': self.difficulty,
            'question_type': self.question_type,
            'options': self.options,
            'correct_answer': self.correct_answer,
            'pairs': self.pairs,
            'essay_details': self.essay_details,
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat(),
            'last_edited_by': self.last_edited_by,
            'last_edited_at': self.last_edited_at.isoformat() if self.last_edited_at else None
        }

class Rubric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    sections = db.Column(db.Text, nullable=False)  # JSON string to store sections and their details

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    rubric_id = db.Column(db.Integer, db.ForeignKey('rubric.id'), nullable=False)
    questions = db.Column(db.Text, nullable=False)  # JSON string to store questions and their details
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    course = db.relationship('Course', backref=db.backref('tests', lazy=True))
    rubric = db.relationship('Rubric', backref=db.backref('tests', lazy=True))
