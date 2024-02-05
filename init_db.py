from flask import Flask
from modelo import db, TaskControl

"""
Here you're going to initialize the database according to the model in 'Modelo'.
Once the database is created, it will enter two tasks in order to demonstrate the
'Read' function of the CRUD.
"""

# Instantiating the Flask class.
app = Flask(__name__)

# Database configuration.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Database initialization.
db.init_app(app)

# try:
#     # Creating the database tables. (Once the tables have been created, this part should stay commented)
#     with app.app_context():
#         db.create_all()
#         print("Database tables created successfully! Don't forget to comment this snipped.")
# except Exception as e:
#     print(f"Error creating database tables {e}")     