from flask import Flask , render_template,flash,redirect,url_for
from forms import *

from flask_sqlalchemy import SQLAlchemy
from models import Tasks
from extensions import db
ToDoApp = Flask(__name__)
ToDoApp.config['SECRET_KEY'] = "hello from my secret key"
ToDoApp.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:anas204@localhost/toDoListDB'
db.init_app(ToDoApp)


with ToDoApp.app_context():
    db.create_all()
@ToDoApp.route('/')
def index():
    return render_template('base.html',title='Home')
@ToDoApp.route('/tasks')
def tasks():
   tasks=Tasks.query.all()
   return  render_template('tasks.html',title='Tasks',tasks=tasks)

@ToDoApp.route('/addTask',methods=['GET','POST'])
def addTask():
    task_to_add = None
    form = AddTaskForm()
    if form.validate_on_submit():
        task=Tasks(title=form.task_to_add.data,completed=form.complete.data)
        db.session.add(task)
        db.session.commit()
        form.task_to_add.data = ''
        return redirect(url_for('tasks'))

    return  render_template('add_task.html',title='Add Task',task_to_add=task_to_add,form=form)

if __name__=='__main__':
    ToDoApp.run(debug=True,port=9000)