import sqlite3
import hashlib
import jwt
import os
import subprocess
from flask import Flask, request, make_response

app = Flask(_name_)

# 1️⃣ Hardcoded secret key (Insecure Secret Management)
SECRET_KEY = "my$ecretKey123"

# 2️⃣ Insecure password hashing (Weak Cryptography)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # Use bcrypt or Argon2 instead

# 3️⃣ SQL Injection vulnerability
def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    return user

# 4️⃣ Command injection
@app.route('/ping', methods=['POST'])
def ping():
    ip = request.json.get("ip")
    result = subprocess.getoutput(f"ping -c 1 {ip}")
    return result

# 5️⃣ Hardcoded API key
API_KEY = "sk_test_51M8vZSHARD_CODED_KEY"

# 6️⃣ Information exposure in error messages
@app.route('/debug', methods=['GET'])
def debug():
    try:
        1 / 0
    except Exception as e:
        return f"Error: {e}"  # Should hide internals in prod

# 7️⃣ Using eval on user input (Remote Code Execution)
@app.route('/calc', methods=['POST'])
def calc():
    expr = request.json.get("expression")
    return str(eval(expr))  # Never eval user input

# 8️⃣ Exposing sensitive info in JWT
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = get_user(data['username'])
    if user:
        token = jwt.encode({'username': data['username'], 'password': data['password']}, SECRET_KEY, algorithm='HS256')
        return {'token': token}
    return {'error': 'Login failed'}

# 9️⃣ No rate limiting (Brute Force)
@app.route('/auth', methods=['POST'])
def auth():
    username = request.json.get("username")
    password = request.json.get("password")
    if get_user(username) and password == "123456":
        return {"msg": "Authenticated"}
    return {"msg": "Invalid"}

# 🔟 Insecure file handling (Arbitrary File Access)
@app.route('/readfile', methods=['GET'])
def readfile():
    filename = request.args.get("file")
    with open(filename, 'r') as f:
        return f.read()

if _name_ == '_main_':
    app.run(debug=True)
