from flask import Flask, render_template, request, redirect, url_for, session
from modelo import db, TaskControl, Users
from datetime import datetime

# Instantiating de Flask class.
app = Flask(__name__)

# Secret key configuration.
app.config["SECRET_KEY"] = "tu_clave_secreta_aqui"

# Database configuration.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Database initialization.
db.init_app(app)

### PATHS ###

# LANDING PAGE.
@app.route("/")
def landing_page():
    
    """
    This path will give the users a general view of the page function.
    """
    
    return render_template("landing.html")

# SIGN-IN.
@app.route("/login", methods=["GET", "POST"])
def login():
    
    """
    This path will be for user sign-in.
    """
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
            
        # Validate user credentials.
        user = Users.query.filter_by(username=username, password=password).first()  # Query the database to find a user with the given username and password.
        if user:
            # Store the username in the session after successful login.
            session["username"] = username
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

# SIGN-UP.    
@app.route("/register", methods=["GET", "POST"])
def register():
    
    """
    This path will be for user sign-up.
    """
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
                
        # Validate the data and add the user to the database.
        user = Users(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        
        # Saving the session's username.
        session['username'] = username
        
        return redirect(url_for("index"))
    return render_template("register.html")

## CRUD PATHS ##

# CRUD - READ.
@app.route("/index")
def index():
    
    """
    This path will read every information that's inside the datebase and update the task state based on current date.
    """
    
    tasks = TaskControl.query.all()
    current_date = datetime.now().date()    # Saving the current date.
    
    for task in tasks:
        if task.date < current_date and task.state != "Done":
            task.state = "Undone"
        elif task.date > current_date and task.state != "Done":
            task.state = "Pending"

    db.session.commit()
    
    username = session.get("username", "Guest")     # Use "Guest" as default if username is not in session

    return render_template("index.html", tasks=tasks, user=username)

@app.route("/done/<id>", methods=["POST"])
def done(id):
    
    """
    This path will mark a task as 'Done'.
    """
    
    task = TaskControl.query.get(id)
    task.state = "Done"
    
    db.session.commit()       
    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))  # Redirect to the login page.

# CRUD - CREATE.
@app.route("/create", methods=["POST"])
def create():
    
    """
    This path will take the data that the user insert and save it into the database.
    """
    
    if request.method == "POST":
        
        # Obtaining the form data.
        date_str = request.form.get("date")
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")  # Convert date string to a Python date object.
        description = request.form.get("description")
        state = "Pending"
        comment = request.form.get("comment")
        
        # Creating the 'task' object.
        task = TaskControl(date=date_obj, description=description, state=state, comment=comment)
        
        # Adding into the database.
        db.session.add(task)
        
        # Saving the changes.
        db.session.commit()
        
        return redirect(url_for("index"))
    
# CRUD - UPDATE
@app.route("/update/<id>", methods = ["GET", "POST"])
def update(id):
    
    """
    This path will make changes in the database information if the user wants to.
    """
    
    # Obtaining the task the user wants to update.
    task = TaskControl.query.get(id)
    if request.method == "POST":
        
        # Obtaining the form data.
        date_str = request.form.get("date")
        task.date = datetime.strptime(date_str, "%Y-%m-%d")     # Convert date string to a Python date object.
        task.state = request.form.get("state")
        task.description = request.form.get("description")
        task.comment = request.form.get("comment")
        
        # Adding the tasks updates into the database.
        db.session.commit()
        return redirect(url_for("index"))
    
    return render_template("update.html", task=task)

# CRUD - DELETE
@app.route("/delete/<id>")
def delete(id):
    
    """
    This path will delete any data the user wants to.
    """
    
    # Obtaining the task the user wants to delete.
    tasks = TaskControl.query.get(id)
    
    # Deleting the selected task.
    db.session.delete(tasks)
    
    # Saving the changes.
    db.session.commit()
    
    return redirect(url_for("index"))





### BREAKPOINT ###
if __name__ == "__main__":
    app.run(debug = True)