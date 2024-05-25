from flask import Blueprint, request, render_template, redirect, url_for
from models import db, Course, CourseOutcome, Question
from utils import apply_filters, apply_sorting, apply_pagination
from sqlalchemy import func

course_bp = Blueprint('courses', __name__)

SCHOOLS = [
    "SOET", "SOMC", "SOLS", "SMAS", "SOED", "SOHS", "SOAD", "SOAS", "SBAS", "SJMC", "SPRS", "SOHMCT"
]

@course_bp.route('/create', methods=['GET', 'POST'])
def create_course():
    if request.method == 'POST':
        name = request.form['name']
        course_code = request.form['course_code']
        school = request.form['school']
        department = request.form['department']
        
        course = Course(name=name, course_code=course_code, school=school, department=department)
        db.session.add(course)
        db.session.flush()  # Get the course ID without committing

        outcomes = request.form.getlist('outcome')
        for i, outcome in enumerate(outcomes, 1):
            course_outcome = CourseOutcome(number=i, description=outcome, course=course)
            db.session.add(course_outcome)

        db.session.commit()
        return redirect(url_for('courses.list_courses'))
    return render_template('course_form.html', schools=SCHOOLS)

@course_bp.route('/edit/<int:course_id>', methods=['GET', 'POST'])
def edit_course(course_id):
    course = Course.query.get_or_404(course_id)
    if request.method == 'POST':
        course.name = request.form['name']
        course.course_code = request.form['course_code']
        course.school = request.form['school']
        course.department = request.form['department']

        # Remove existing outcomes
        for outcome in course.outcomes:
            db.session.delete(outcome)

        # Add new outcomes
        outcomes = request.form.getlist('outcome')
        for i, outcome in enumerate(outcomes, 1):
            course_outcome = CourseOutcome(number=i, description=outcome, course=course)
            db.session.add(course_outcome)

        db.session.commit()
        return redirect(url_for('courses.list_courses'))
    return render_template('course_form.html', course=course, schools=SCHOOLS, edit=True)

@course_bp.route('/delete/<int:course_id>', methods=['POST'])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    return redirect(url_for('courses.list_courses'))

@course_bp.route('/', methods=['GET', 'POST'])
def list_courses():
    query = Course.query

    search_fields = ['course_code', 'name', 'school', 'department']
    filter_fields = ['school', 'department']
    query = apply_filters(query, Course, search_fields, filter_fields)
    query = apply_sorting(query, Course)
    courses, total_courses, pagination = apply_pagination(query)

    # Retrieve per_page and page from request arguments to pass to the template
    per_page = int(request.args.get('per_page', 50))
    page = int(request.args.get('page', 1))

    schools = db.session.query(Course.school).distinct().all()
    departments = db.session.query(Course.department).distinct().all()

    return render_template('course_list.html', courses=courses, total_courses=total_courses, schools=schools, departments=departments, per_page=per_page, page=page, pagination=pagination)

@course_bp.route('/view/<int:course_id>', methods=['GET'])
def view_course(course_id):
    course = Course.query.get_or_404(course_id)
    query = Question.query.filter_by(course_id=course_id)

    # Apply filters, sorting, and pagination for questions
    search_fields = ['content', 'bloom_level', 'topic', 'difficulty', 'question_type']
    filter_fields = ['bloom_level', 'difficulty', 'question_type']
    query = apply_filters(query, Question, search_fields, filter_fields)
    query = apply_sorting(query, Question)
    questions, total_questions, pagination = apply_pagination(query)

    bloom_levels = db.session.query(Question.bloom_level).distinct().all()
    difficulties = db.session.query(Question.difficulty).distinct().all()
    question_types = db.session.query(Question.question_type).distinct().all()

    # Retrieve per_page and page from request arguments to pass to the template
    per_page = int(request.args.get('per_page', 50))
    page = int(request.args.get('page', 1))

    # Get the previous and next courses
    prev_course = Course.query.filter(Course.id < course_id).order_by(Course.id.desc()).first()
    next_course = Course.query.filter(Course.id > course_id).order_by(Course.id.asc()).first()

    # Summary statistics
    difficulty_counts = db.session.query(Question.difficulty, func.count(Question.id)).filter_by(course_id=course_id).group_by(Question.difficulty).order_by(func.count(Question.id).desc()).all()
    topic_counts = db.session.query(Question.topic, func.count(Question.id)).filter_by(course_id=course_id).group_by(Question.topic).order_by(func.count(Question.id).desc()).all()
    type_counts = db.session.query(Question.question_type, func.count(Question.id)).filter_by(course_id=course_id).group_by(Question.question_type).order_by(func.count(Question.id).desc()).all()

    difficulty_data = {d: c for d, c in difficulty_counts}
    topic_data = {t: c for t, c in topic_counts}
    type_data = {t: c for t, c in type_counts}

    total_questions = sum(difficulty_data.values())

    return render_template(
        'course_view.html',
        course=course, 
        questions=questions,
        total_questions=total_questions,
        bloom_levels=bloom_levels,
        difficulties=difficulties,
        question_types=question_types,
        pagination=pagination,
        per_page=per_page, page=page,
        prev_course=prev_course,
        next_course=next_course,
        difficulty_data=difficulty_data,
        topic_data=topic_data,
        type_data=type_data,
    )
