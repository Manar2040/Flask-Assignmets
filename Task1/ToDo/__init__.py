from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
ToDoApp = Flask(__name__)
ToDoApp.config['SECRET_KEY'] = "hello from my secret key"
ToDoApp.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:anas204@localhost/ToDoListDB'



db = SQLAlchemy(ToDoApp)
bcrypt = Bcrypt(ToDoApp)
loginManager = LoginManager(ToDoApp)
loginManager.login_view = "users.login"
loginManager.login_message_category = "info"

# import users, blogs, main blueprints
from ToDo.main.routes import main
from ToDo.users.routes import users
from ToDo.tasks.routes import tasks

ToDoApp.register_blueprint(main)
ToDoApp.register_blueprint(users)
ToDoApp.register_blueprint(tasks)