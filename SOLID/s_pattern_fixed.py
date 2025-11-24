"""
Now, the main route has a single responsibility and uses other methods to help achieve its goal.
We break the main logic in different methods, this way improves the readbility and maintainability
Since we can use those methods in different parts of our code.
"""

import sqlite3
from urllib import request

def validate_user_data(data):
    if "email" not in data:
        raise ValueError("Email is required")

def save_user_to_db(email):
    conn = sqlite3.connect("db.sqlite")
    with conn:
        conn.execute("INSERT INTO users (email) VALUES (?)", (email,))
    return True

def send_notification(email):
    return email

@app.route("/users", methods=["POST"])
def create_user():
    try:
        data = request.json
        validate_user_data(data)
        save_user_to_db(data["email"])
        send_notification(data["email"])
        return {"message": "User created successfully"}, 201
    except ValueError as e:
        return {"error": str(e)}, 400