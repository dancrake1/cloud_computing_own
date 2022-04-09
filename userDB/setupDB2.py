from flask import Flask, render_template, request, jsonify, json, url_for, abort, redirect, session,flash
from flask_sqlalchemy import sqlalchemy, SQLAlchemy




db_name = "auth.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{db}'.format(db=db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#SECRET_KEY required for session, flash and Flask Sqlalchemy to work
app.config['SECRET_KEY'] = '{Your Secret Key}'

db = SQLAlchemy(app)


class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    pass_hash = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '' % self.username


    """ # Execute this first time to create new db in current directory. """
db.create_all()
