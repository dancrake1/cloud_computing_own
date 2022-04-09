from flask import Flask, jsonify, render_template, request
import requests
from flask_sqlalchemy import sqlalchemy, SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from userDB.setupDB import user


app = Flask(__name__)
# Connect to the database
engine = create_engine("sqlite:///userDB//user_database.db")

@app.route('/')
def hello():
	return render_template("login.html")


@app.route("/signup/", methods=["GET", "POST"])
def signup():
    """
    Implements signup functionality. Allows username and password for new user.
    Hashes password with salt using werkzeug.security.
    Stores username and hashed password inside database.
    Username should to be unique else raises sqlalchemy.exc.IntegrityError.
    """
	Session = sessionmaker(bind=engine)
	session = Session()
	if request.method == "POST":
		username = request.form['username']
		password = request.form['password']

		if not (username and password):
            flash("Username or Password cannot be empty")
            return redirect(url_for('signup'))
        else:
            username = username.strip()
            password = password.strip()

        # Returns salted pwd hash in format : method$salt$hashedvalue
        hashed_pwd = generate_password_hash(password, 'sha256')

        new_user = user(username=username, pass_hash=hashed_pwd)

        Session = sessionmaker(bind=engine)
	session = Session()
	session.add(new_user)

        try:
            session.commit()
        except sqlalchemy.exc.IntegrityError:
            flash("Username {u} is not available.".format(u=username))
            return redirect(url_for('signup'))

        flash("User account has been created.")
        return redirect(url_for("login"))

    return render_template("signup.html")

@app.route("/", methods=["GET", "POST"])
@app.route("/login/", methods=["GET", "POST"])
def login():
    """
    Provides login functionality by rendering login form on get request.
    On post checks password hash from db for given input username and password.
    If hash matches redirects authorized user to home page else redirect to
    login page with error message.
    """

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if not (username and password):
            flash("Username or Password cannot be empty.")
            return redirect(url_for('login'))
        else:
            username = username.strip()
            password = password.strip()

        user = user.query.filter_by(username=username).first()

        if user and check_password_hash(user.pass_hash, password):
            session[username] = True
            return redirect(url_for("user_home", username=username))
        else:
            flash("Invalid username or password.")

    return render_template("login_form.html")


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
