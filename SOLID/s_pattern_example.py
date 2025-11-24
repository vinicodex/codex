"""
The first princple of SOLID means SRP "Single Responsability Principle"
Which states every function, class or module should have only one reason to change
In other words, each piece of code should have a clear responsability.
"""

import sqlite3
from urllib import request
from fastapi import FastAPI

app = FastAPI()


@app.route("/users", methods=["POST"])
def create_user():
    # 1. Validação
    data = request.json
    if "email" not in data:
        return {"error": "Email is required"}, 400

    # 2. Inserção no banco
    conn = sqlite3.connect("db.sqlite")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (email) VALUES (?)", (data["email"],))
    conn.commit()
    conn.close()

    # 3. Notificação (simulada)
    send_welcome_email(data["email"])

    return {"message": "User created successfully"}, 201