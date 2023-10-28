#!/usr/bin/python3
'''Database initialization script'''

# Import app and db from server.py
from server import app, db

# Create the Flask app context
app.app_context().push()

# Initialize the database
db.create_all()
