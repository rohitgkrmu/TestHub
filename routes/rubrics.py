from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from models import db, Rubric
from forms import RubricBasicForm, RubricSectionsForm
from utils import apply_filters, apply_sorting, apply_pagination
import json

rubric_bp = Blueprint('rubrics', __name__)

@rubric_bp.route('/create', methods=['GET', 'POST'])
def create_rubric():
    # Initialize or reset session step
    if 'step' not in session or (request.method == 'GET' and 'reset' in request.args):
        session['step'] = 1
        session['rubric_data'] = {}

    step = session['step']
    rubric_data = session['rubric_data']

    # Handle Step 1
    if step == 1:
        print("####DEBUGGING MODE#######")
        print("####Entering Step 1######")
        form = RubricBasicForm()
        if form.validate_on_submit():
            rubric_data['name'] = form.name.data
            rubric_data['description'] = form.description.data
            session['rubric_data'] = rubric_data
            session['step'] = 2
            return redirect(url_for('rubrics.create_rubric'))
        return render_template('rubrics/create_step_1.html', form=form)

    # Handle Step 2
    elif step == 2:
        print("####DEBUGGING MODE#######")
        print("####Entering Step 2######")
        form = RubricSectionsForm()
        if form.validate_on_submit():
            rubric_data['sections'] = form.sections.data
            session['rubric_data'] = rubric_data
            session['step'] = 3
            return redirect(url_for('rubrics.create_rubric'))
        return render_template('rubrics/create_step_2.html', form=form)

    # Handle Step 3 (Final Step)
    elif step == 3:
        rubric = Rubric(
            name=rubric_data['name'],
            description=rubric_data['description'],
            sections=json.dumps(rubric_data['sections'])
        )
        db.session.add(rubric)
        db.session.commit()
        flash('Rubric created successfully!', 'success')
        session.pop('step', None)
        session.pop('rubric_data', None)
        return redirect(url_for('rubrics.list_rubrics'))

    # Default: should not reach here
    return redirect(url_for('rubrics.create_rubric'))

@rubric_bp.route('/', methods=['GET', 'POST'], endpoint='list_rubrics')
def list_rubrics():
    query = Rubric.query

    # Apply filters, sorting, and pagination
    search_fields = ['name', 'description']
    filter_fields = []
    query = apply_filters(query, Rubric, search_fields, filter_fields)
    query = apply_sorting(query, Rubric)
    rubrics, total_rubrics, pagination = apply_pagination(query)

    # Retrieve per_page and page from request arguments to pass to the template
    per_page = int(request.args.get('per_page', 50))
    page = int(request.args.get('page', 1))

    return render_template('rubric_list.html', rubrics=rubrics, total_rubrics=total_rubrics, pagination=pagination, per_page=per_page, page=page)

@rubric_bp.route('/edit/<int:rubric_id>', methods=['GET', 'POST'])
def edit_rubric(rubric_id):
    rubric = Rubric.query.get_or_404(rubric_id)
    if request.method == 'POST':
        rubric.name = request.form['name']
        rubric.description = request.form['description']
        rubric.sections = json.dumps(request.form['sections'])
        db.session.commit()
        return redirect(url_for('rubrics.list_rubrics'))
    return render_template('rubric_form.html', rubric=rubric)

@rubric_bp.route('/delete/<int:rubric_id>', methods=['POST'])
def delete_rubric(rubric_id):
    rubric = Rubric.query.get_or_404(rubric_id)
    db.session.delete(rubric)
    db.session.commit()
    return redirect(url_for('rubrics.list_rubrics'))

@rubric_bp.route('/view/<int:rubric_id>', methods=['GET'])
def view_rubric(rubric_id):
    rubric = Rubric.query.get_or_404(rubric_id)
    sections = json.loads(rubric.sections)

    prev_rubric = Rubric.query.filter(Rubric.id < rubric_id).order_by(Rubric.id.desc()).first()
    next_rubric = Rubric.query.filter(Rubric.id > rubric_id).order_by(Rubric.id.asc()).first()

    return render_template('rubric_view.html', rubric=rubric, sections=sections, prev_rubric=prev_rubric, next_rubric=next_rubric)
