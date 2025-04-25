from flask import Blueprint, redirect, url_for, render_template, flash, request, abort
from flask_login import current_user, login_required
from ToDo.tasks.forms import AddTaskForm, UpdateTaskForm

from ToDo.models import Task
from ToDo import db

tasks = Blueprint("tasks", __name__)

@tasks.route("/task/add", methods=["GET", "POST"])
@login_required
def addTask():
    form = AddTaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data, content=form.content.data, user_id=current_user.id
        )
        db.session.add(task)
        db.session.commit()
        flash(f"Task added successfully", "success")
        return redirect(url_for("tasks.get_tasks"))
    return render_template("add_task.html", title="Add Task", form=form)


@tasks.route("/tasks", methods=["GET"])
@login_required
def get_tasks():
    tasks_res = current_user.tasks

    return render_template("tasks.html", title="Tasks", tasks=tasks_res)
@tasks.route("/task/<int:taskId>/update", methods=["GET", "POST"])
@login_required
def updateTask(taskId):
    form = UpdateTaskForm()
    task = Task.query.get_or_404(taskId)
    if task.author != current_user:
        abort(403)

    if request.method == "GET":
        form.title.data = task.title
        form.content.data = task.content

    if form.validate_on_submit():
        task.title = form.title.data
        task.content = form.content.data
        task.completed=form.complete.data
        db.session.commit()
        flash(f"Task updated successfully", "success")
        return redirect(url_for("tasks.get_tasks"))

    return render_template(
        "update_task.html", title="Update Task", task=task, form=form
    )


@tasks.route("/blog/<int:taskId>/delete", methods=["GET"])
def deleteTask(taskId):
    task = Task.query.get_or_404(taskId)
    if task.author != current_user:
        abort(403)
    db.session.delete(task)
    db.session.commit()
    flash(f"task {task.title} deleted successfully ", "success")
    return redirect(url_for("tasks.get_tasks"))