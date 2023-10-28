#!/bin/python3
"""A Web server (program) that performs
simple crud operations on a database"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)