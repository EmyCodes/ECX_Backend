#!/bin/python3
"""A Web server (program) that performs
simple crud operations on a database"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecx_backend.db'
# Database name = ecx_backend.db
# Database path = sqlite:///ecx_backend.db

db = SQLAlchemy(app)


class Book(db.Model):
    """Book model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(90), nullable=False)
    author = db.Column(db.Text, nullable=False)

# Create the database
@app.route('/books', methods=['GET', 'POST'])
def manage_books():
    """Handles GET and POST requests"""
    if request.method == "GET":
        books = Book.query.all()
        books = [{"id": book.id, "title": book.title, "author": book.author} for book in books]
        return jsonify(books)

    if request.method == "POST":
        book = Book(title=request.json["title"], author=request.json['author'])
        db.session.add(book)
        db.session.commit()
        return jsonify({"message": "Book successfully added!! "})

if __name__ == '__main__':
    app.run(debug=True)
