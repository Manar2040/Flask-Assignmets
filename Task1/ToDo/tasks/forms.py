from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField,BooleanField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired

class AddTaskForm(FlaskForm):
    title =StringField('Task', validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    submit = SubmitField('Add Task')
    complete = BooleanField('Completed')

class UpdateTaskForm(AddTaskForm):
    submit = SubmitField("Edit")