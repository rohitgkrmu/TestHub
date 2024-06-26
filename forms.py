from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, FieldList, FormField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, Optional, Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class SectionForm(FlaskForm):
    section_name = StringField('Section Name', validators=[DataRequired()])
    single_mcq = IntegerField('Single Answer MCQs', default=0)
    multi_mcq = IntegerField('Multiple Answer MCQs', default=0)
    true_false = IntegerField('True/False', default=0)
    fill_blank = IntegerField('Fill in the Blanks', default=0)
    short_essay = IntegerField('Short Answer Essay', default=0)
    long_essay = IntegerField('Long Answer Essay', default=0)

class RubricBasicForm(FlaskForm):
    name = StringField('Rubric Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])

class NumberOfSectionsForm(FlaskForm):
    number_of_sections = IntegerField('Number of Sections', validators=[DataRequired()])

class RubricSectionsForm(FlaskForm):
    sections = FieldList(FormField(SectionForm), min_entries=1)

class EmptyForm(FlaskForm):
    pass

class TestCreationForm(FlaskForm):
    name = StringField('Test Name', validators=[DataRequired()])
    course = SelectField('Course', coerce=int, validators=[DataRequired()])
    rubric = SelectField('Rubric', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Create Test')

