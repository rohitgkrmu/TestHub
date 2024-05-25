from flask import Blueprint, request, render_template, redirect, url_for
from models import db, Course, CourseOutcome, Question
from utils import apply_filters, apply_sorting, apply_pagination

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

    # Search functionality
    #search = request.args.get('search')
    #if search:
    #    query = query.filter(or_(Course.course_code.ilike(f'%{search}%'),
    #                             Course.name.ilike(f'%{search}%'),
    #                             Course.school.ilike(f'%{search}%'),
    #                             Course.department.ilike(f'%{search}%')))

    search_fields = ['course_code', 'name', 'school', 'department']
    filter_fields = ['school', 'department']
    query = apply_filters(query, Course, search_fields, filter_fields)
    query = apply_sorting(query, Course)
    courses, total_courses, pagination = apply_pagination(query)

    """# Filter functionality
    school_filter = request.args.get('school_filter')
    department_filter = request.args.get('department_filter')
    if school_filter:
        query = query.filter(Course.school == school_filter)
    if department_filter:
        query = query.filter(Course.department == department_filter)

    # Sort functionality
    sort_by = request.args.get('sort_by', 'id')
    sort_order = request.args.get('sort_order', 'asc')
    if sort_order == 'asc':
        query = query.order_by(getattr(Course, sort_by).asc())
    else:
        query = query.order_by(getattr(Course, sort_by).desc())

    # Pagination
    per_page = int(request.args.get('per_page', 50))
    page = int(request.args.get('page', 1))
    total_courses = query.count()
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    courses = pagination.items"""

    # Retrieve per_page and page from request arguments to pass to the template
    per_page = int(request.args.get('per_page', 50))
    page = int(request.args.get('page', 1))

    schools = db.session.query(Course.school).distinct().all()
    departments = db.session.query(Course.department).distinct().all()

    return render_template('course_list.html', courses=courses, total_courses=total_courses, schools=schools, departments=departments, per_page=per_page, page=page, pagination=pagination)

@course_bp.route('/view/<int:course_id>', methods=['GET'])
def view_course(course_id):
    course = Course.query.get_or_404(course_id)
    questions = Question.query.filter_by(course_id=course_id).all()
    return render_template('course_view.html', course=course, questions=questions)
