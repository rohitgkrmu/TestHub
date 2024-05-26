from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, FieldList, FormField, SubmitField
from wtforms.validators import DataRequired, Optional

class SectionForm(FlaskForm):
    name = StringField('Section Name', validators=[DataRequired()])
    single_mcq = IntegerField('Single Answer MCQs', default=0)
    multi_mcq = IntegerField('Multiple Answer MCQs', default=0)
    true_false = IntegerField('True/False', default=0)
    fill_blank = IntegerField('Fill in the Blanks', default=0)
    short_essay = IntegerField('Short Answer Essay', default=0)
    long_essay = IntegerField('Long Answer Essay', default=0)

class RubricBasicForm(FlaskForm):
    name = StringField('Rubric Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])

class RubricSectionsForm(FlaskForm):
    sections = FieldList(FormField(SectionForm), min_entries=1, max_entries=10)

class RubricWizardForm(FlaskForm):
    basic_info = FormField(RubricBasicForm)
    sections_info = FormField(RubricSectionsForm)
    submit = SubmitField('Create Rubric')
