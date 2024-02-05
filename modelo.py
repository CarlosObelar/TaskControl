from flask_sqlalchemy import SQLAlchemy

# Instantiating SQLAlchemy.
db = SQLAlchemy()

### MODELS ###

class TaskControl(db.Model):
    """
    Model for task control.

    Attributes:
        id (int): Unique identifier for the task.
        date (str): Date of the task in DD/MM/YY format.
        task (str): Description of the task.
        state (str): Current state of the task ('Pending', 'Done', 'Undone').
        comment (str): Additional comment about the task (optional).
    """
    
    id = db.Column(db.Integer, primary_key = True)          
    date = db.Column(db.Date, nullable=False)         # Remember that the date format should be DD/MM/YY.
    description = db.Column(db.String(100), nullable=False)        
    state = db.Column(db.String(20))        
    comment = db.Column(db.String(100))                     # Additional comment if desired.
    
    
class Users(db.Model):
    """
    Model for users log-in information.
    
    Attributes:
        id (int): Unique identifier for the user.
        username (str): User's user name for registration.
        password (str): User's password for registration.
        email (str): User's email for registration.
    """
    
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), nullable=False)       
    password = db.Column(db.String(100), nullable=False)       
    email = db.Column(db.String(30), nullable=False)       