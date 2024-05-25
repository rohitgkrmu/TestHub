from flask import Blueprint, request, render_template, redirect, url_for
from models import db, Question, Course
from utils import apply_filters, apply_sorting, apply_pagination

question_bp = Blueprint('questions', __name__)

@question_bp.route('/create', methods=['GET', 'POST'])
def create_question():
    if request.method == 'POST':
        content = request.form['content']
        course_id = request.form['course_id']
        bloom_level = request.form['bloom_level']
        topic = request.form['topic']
        difficulty = request.form['difficulty']
        question_type = request.form['question_type']

        if question_type in ['Single Correct Answer', 'Multiple Correct Answers']:
            options = request.form.getlist('options[]')
            correct_answer = request.form['correct_answer']
            options_str = ','.join(options)  # Storing options as comma-separated string
            question = Question(content=content, course_id=course_id, bloom_level=bloom_level,
                                topic=topic, difficulty=difficulty, question_type=question_type,
                                options=options_str, correct_answer=correct_answer,
                                created_by=current_user.email)
        elif question_type == 'True/False':
            correct_answer = request.form['correct_answer']
            question = Question(content=content, course_id=course_id, bloom_level=bloom_level,
                                topic=topic, difficulty=difficulty, question_type=question_type,
                                correct_answer=correct_answer, created_by=current_user.email)
        elif question_type == 'Matching':
            left_items = request.form.getlist('left[]')
            right_items = request.form.getlist('right[]')
            pairs = ','.join([f"{left}:{right}" for left, right in zip(left_items, right_items)])  # Storing pairs as comma-separated string
            question = Question(content=content, course_id=course_id, bloom_level=bloom_level,
                                topic=topic, difficulty=difficulty, question_type=question_type,
                                pairs=pairs, created_by=current_user.email)
        elif question_type == 'Fill in the Blank':
            correct_answer = request.form['correct_answer']
            question = Question(content=content, course_id=course_id, bloom_level=bloom_level,
                                topic=topic, difficulty=difficulty, question_type=question_type,
                                correct_answer=correct_answer, created_by=current_user.email)
        elif question_type == 'Short Answer':
            correct_answer = request.form['correct_answer']
            question = Question(content=content, course_id=course_id, bloom_level=bloom_level,
                                topic=topic, difficulty=difficulty, question_type=question_type,
                                correct_answer=correct_answer, created_by=current_user.email)
        elif question_type == 'Essay':
            essay_details = request.form['essay_details']
            question = Question(content=content, course_id=course_id, bloom_level=bloom_level,
                                topic=topic, difficulty=difficulty, question_type=question_type,
                                essay_details=essay_details, created_by=current_user.email)

        db.session.add(question)
        db.session.commit()
        return redirect(url_for('questions.list_questions'))
    courses = Course.query.all()
    return render_template('question_form.html', courses=courses)

@question_bp.route('/', methods=['GET', 'POST'], endpoint='list_questions')
def list_questions():
    query = Question.query

    # Apply filters, sorting, and pagination
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

    return render_template('question_list.html', questions=questions, total_questions=total_questions, bloom_levels=bloom_levels, difficulties=difficulties, question_types=question_types, pagination=pagination, per_page=per_page, page=page)

@question_bp.route('/edit/<int:question_id>', methods=['GET', 'POST'])
def edit_question(question_id):
    question = Question.query.get_or_404(question_id)
    if request.method == 'POST':
        question.content = request.form['content']
        question.course_id = request.form['course_id']
        question.bloom_level = request.form['bloom_level']
        question.topic = request.form['topic']
        question.difficulty = request.form['difficulty']
        question.question_type = request.form['question_type']
        question.last_edited_by = current_user.email
        question.last_edited_at = datetime.utcnow()
        db.session.commit()
        return redirect(url_for('questions.list_questions'))
    courses = Course.query.all()
    return render_template('question_form.html', question=question, courses=courses)

@question_bp.route('/delete/<int:question_id>', methods=['POST'])
def delete_question(question_id):
    question = Question.query.get_or_404(question_id)
    db.session.delete(question)
    db.session.commit()
    return redirect(url_for('questions.list_questions'))

@question_bp.route('/view/<int:question_id>', methods=['GET'])
def view_question(question_id):
    question = Question.query.get_or_404(question_id)
    course = Course.query.get(question.course_id)

    prev_question = Question.query.filter(Question.id < question_id).order_by(Question.id.desc()).first()
    next_question = Question.query.filter(Question.id > question_id).order_by(Question.id.asc()).first()

    return render_template('question_view.html', question=question, course=course, prev_question=prev_question, next_question=next_question)