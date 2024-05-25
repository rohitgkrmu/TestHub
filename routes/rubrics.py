from flask import Blueprint, request, render_template, redirect, url_for
from models import db, Rubric, Course

rubric_bp = Blueprint('rubrics', __name__)

@rubric_bp.route('/create', methods=['GET', 'POST'])
def create_rubric():
    if request.method == 'POST':
        name = request.form['name']
        course_id = request.form['course_id']
        blueprint = request.form['blueprint']  # Assuming this is JSON
        rubric = Rubric(name=name, course_id=course_id, blueprint=blueprint)
        db.session.add(rubric)
        db.session.commit()
        return redirect(url_for('rubrics.list_rubrics'))
    courses = Course.query.all()
    return render_template('rubric_form.html', courses=courses)

@rubric_bp.route('/')
def list_rubrics():
    rubrics = Rubric.query.all()
    return render_template('rubric_list.html', rubrics=rubrics)
