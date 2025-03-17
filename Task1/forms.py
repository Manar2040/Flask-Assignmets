from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField,BooleanField
from wtforms.validators import DataRequired

class AddTaskForm(FlaskForm):
    task_to_add =StringField('Task', validators=[DataRequired()])
    submit = SubmitField('Add Task')
    complete = BooleanField('Completed')