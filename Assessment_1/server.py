#!/bin/python3
"""A Web server (program) that performs
simple crud operations on a database"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class Book(db.Model):
    """Book model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.Text, nullable=False)


if __name__ == '__main__':
    app.run(debug=True)
