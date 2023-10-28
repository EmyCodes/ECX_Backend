#!/usr/bin/python3
'''Database initialization script'''

from server import app, db  # Import app and db from server.py

# Create the Flask app context
app.app_context().push()

# Initialize the database
db.create_all()
