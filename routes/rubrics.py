from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from models import db, Rubric
from forms import RubricBasicForm, RubricSectionsForm
from utils import apply_filters, apply_sorting, apply_pagination
import json

rubric_bp = Blueprint('rubrics', __name__)

@rubric_bp.route('/create', methods=['GET', 'POST'])
def create_rubric():

    if 'step' not in session:
        print("step is now 1")
        session['step'] = 1
        session['rubric_data'] = {}

    step = session['step']
    rubric_data = session['rubric_data']

    if step == 1:
        form = RubricBasicForm()
        print("############################")
        print(form)
        print("############################")
        if form.validate_on_submit():
            rubric_data['name'] = form.name.data
            rubric_data['description'] = form.description.data
            session['step'] = 2
            session['rubric_data'] = rubric_data
            return redirect(url_for('rubrics.create_rubric'))

    elif step == 2:
        form = RubricSectionsForm()
        if form.validate_on_submit():
            sections = []
            for section_form in form.sections:
                section = {
                    'name': section_form.name.data,
                    'single_mcq': section_form.single_mcq.data,
                    'multi_mcq': section_form.multi_mcq.data,
                    'true_false': section_form.true_false.data,
                    'fill_blank': section_form.fill_blank.data,
                    'short_essay': section_form.short_essay.data,
                    'long_essay': section_form.long_essay.data
                }
                sections.append(section)
            rubric_data['sections'] = sections
            session['step'] = 3
            session['rubric_data'] = rubric_data
            return redirect(url_for('rubrics.create_rubric'))

    elif step == 3:
        rubric = Rubric(
            name=rubric_data['name'],
            description=rubric_data['description'],
            sections=json.dumps(rubric_data['sections'])
        )
        db.session.add(rubric)
        db.session.commit()
        session.pop('step')
        session.pop('rubric_data')
        flash('Rubric created successfully!', 'success')
        return redirect(url_for('rubrics.list_rubrics'))

    form = form if 'form' in locals() else None
    return render_template(f'rubrics/create_step_{step}.html', form=form)

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
