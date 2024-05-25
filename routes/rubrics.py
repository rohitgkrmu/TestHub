from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Rubric, Course
import json

rubric_bp = Blueprint('rubrics', __name__)

@rubric_bp.route('/', methods=['GET', 'POST'], endpoint='list_rubrics')
def list_rubrics():
    rubrics = Rubric.query.all()
    return render_template('rubric_list.html', rubrics=rubrics)

@rubric_bp.route('/create', methods=['GET', 'POST'])
def create_rubric():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        question_types = json.dumps(request.form.getlist('question_types[]'))
        sections = json.dumps(request.form.getlist('sections[]'))
        difficulty_levels = json.dumps(request.form.getlist('difficulty_levels[]'))
        coverage = json.dumps(request.form.getlist('coverage[]'))
        time_limit = request.form['time_limit']
        randomization = 'randomization' in request.form
        course_id = request.form['course_id']
        rubric = Rubric(
            name=name, description=description, question_types=question_types, sections=sections,
            difficulty_levels=difficulty_levels, coverage=coverage, time_limit=time_limit,
            randomization=randomization, course_id=course_id
        )
        db.session.add(rubric)
        db.session.commit()
        return redirect(url_for('rubrics.list_rubrics'))
    courses = Course.query.all()
    return render_template('rubric_form.html', courses=courses)

@rubric_bp.route('/edit/<int:rubric_id>', methods=['GET', 'POST'])
def edit_rubric(rubric_id):
    rubric = Rubric.query.get_or_404(rubric_id)
    if request.method == 'POST':
        rubric.name = request.form['name']
        rubric.description = request.form['description']
        rubric.question_types = json.dumps(request.form.getlist('question_types[]'))
        rubric.sections = json.dumps(request.form.getlist('sections[]'))
        rubric.difficulty_levels = json.dumps(request.form.getlist('difficulty_levels[]'))
        rubric.coverage = json.dumps(request.form.getlist('coverage[]'))
        rubric.time_limit = request.form['time_limit']
        rubric.randomization = 'randomization' in request.form
        rubric.course_id = request.form['course_id']
        db.session.commit()
        return redirect(url_for('rubrics.list_rubrics'))
    courses = Course.query.all()
    return render_template('rubric_form.html', rubric=rubric, courses=courses)

@rubric_bp.route('/delete/<int:rubric_id>', methods=['POST'])
def delete_rubric(rubric_id):
    rubric = Rubric.query.get_or_404(rubric_id)
    db.session.delete(rubric)
    db.session.commit()
    return redirect(url_for('rubrics.list_rubrics'))

@rubric_bp.route('/view/<int:rubric_id>', methods=['GET'])
def view_rubric(rubric_id):
    rubric = Rubric.query.get_or_404(rubric_id)
    return render_template('rubric_view.html', rubric=rubric)
