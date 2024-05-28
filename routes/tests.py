from flask import Blueprint, request, render_template, redirect, url_for, flash
from models import db, Test, Course, Rubric, Question
from forms import TestCreationForm
from utils import apply_filters, apply_sorting, apply_pagination
import json

test_bp = Blueprint('tests', __name__)

@test_bp.route('/create', methods=['GET', 'POST'])
def create_test():
    form = TestCreationForm()
    form.course.choices = [(course.id, course.name) for course in Course.query.all()]
    form.rubric.choices = [(rubric.id, rubric.name) for rubric in Rubric.query.all()]
    
    if form.validate_on_submit():
        course_id = form.course.data
        rubric_id = form.rubric.data
        name = form.name.data
        
        course = Course.query.get(course_id)
        rubric = Rubric.query.get(rubric_id)
        questions = Question.query.filter_by(course_id=course_id).all()
        
        rubric_requirements = json.loads(rubric.sections)
        selected_questions = []

        question_pool = {
            "single_mcq": [],
            "multi_mcq": [],
            "true_false": [],
            "fill_blank": [],
            "short_essay": [],
            "long_essay": []
        }

        for question in questions:
            if question.question_type in question_pool:
                question_pool[question.question_type].append(question)

        sufficient_questions = True
        missing_questions = []

        for section in rubric_requirements:
            section_questions = []
            for q_type, required_count in section.items():
                if q_type == 'csrf_token':  # skip CSRF token
                    continue
                available_questions = question_pool.get(q_type, [])
                if len(available_questions) < required_count:
                    sufficient_questions = False
                    missing_questions.append(f"{required_count - len(available_questions)} more {q_type.replace('_', ' ')} questions")
                else:
                    section_questions.extend(available_questions[:required_count])
                    question_pool[q_type] = available_questions[required_count:]
            selected_questions.extend(section_questions)

        if not sufficient_questions:
            flash(f"Not enough questions to create the test. Please add more questions: {', '.join(missing_questions)}", 'danger')
            return redirect(url_for('tests.create_test'))

        test = Test(name=name, course_id=course_id, rubric_id=rubric_id, questions=json.dumps([q.to_dict() for q in selected_questions]))
        db.session.add(test)
        db.session.commit()
        
        flash('Test created successfully!', 'success')
        return redirect(url_for('tests.view_test', test_id=test.id))
    
    return render_template('test_form.html', form=form)

@test_bp.route('/view/<int:test_id>', methods=['GET'])
def view_test(test_id):
    test = Test.query.get_or_404(test_id)
    questions = json.loads(test.questions)
    return render_template('test_view.html', test=test, questions=questions)

@test_bp.route('/', methods=['GET', 'POST'], endpoint='list_tests')
def list_tests():
    query = Test.query

    # Apply filters, sorting, and pagination
    search_fields = ['name']
    filter_fields = []
    query = apply_filters(query, Test, search_fields, filter_fields)
    query = apply_sorting(query, Test)
    tests, total_tests, pagination = apply_pagination(query)

    # Retrieve per_page and page from request arguments to pass to the template
    per_page = int(request.args.get('per_page', 50))
    page = int(request.args.get('page', 1))

    return render_template('test_list.html', tests=tests, total_tests=total_tests, pagination=pagination, per_page=per_page, page=page)

