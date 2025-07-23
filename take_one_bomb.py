import sqlite3
import hashlib
import jwt
from flask import Flask, request

app = Flask(_name_)

SECRET_KEY = "my-super-secret-key"

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
