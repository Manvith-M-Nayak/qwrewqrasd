import sqlite3
import hashlib
import jwt
from flask import Flask, request

app = Flask(_name_)

SECRET_KEY = "my-super-secret-key"

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def authenticate(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{hash_password(password)}'"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = authenticate(data['username'], data['password'])
    
    if user:
        token = jwt.encode({'username': user[0], 'password': user[1]}, SECRET_KEY, algorithm='HS256')
        return {'token': token}
    else:
        return {'error': 'Invalid credentials'}, 401

if _name_ == '_main_':
    app.run(debug=True)
