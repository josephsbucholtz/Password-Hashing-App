from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import bcrypt
import os

app = Flask(__name__)
CORS(app)

#Sign Up users by storing username and password in json file
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    print('Received data:', data)

    users = []

    # If the file exists and is not empty, load existing users
    if os.path.exists('users.json') and os.path.getsize('users.json') > 0:
        with open('users.json', 'r') as f:
            users = json.load(f)

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        print('Missing username or password')
        return jsonify({'error': 'Missing data'}), 400
    
    if any(u['username'] == username for u in users):
        return jsonify({'error': 'Username already exists'}), 400

    #Bcrypt Hashing Algorithm
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(bytes, salt)

    user_data = {'username': username, 'password': password_hash.decode("utf-8")}

    # If the file exists and is not empty, load existing users
    if os.path.exists('users.json') and os.path.getsize('users.json') > 0:
        with open('users.json', 'r') as f:
            users = json.load(f)

    users.append(user_data)

    #Users to JSON
    try:
        with open('users.json', 'w') as f:
            json.dump(users, f, indent=4)
    except Exception as e:
        print('File write error ❌:', e)
        return jsonify({'error': 'Failed to write file'}), 500

    return jsonify({'message': 'Signup successful'})

#Login Users
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print('Received data:', data)

    username = data.get('username')
    input_password = data.get('password')

    users = []

    # If the file exists and is not empty, load existing users
    if os.path.exists('users.json') and os.path.getsize('users.json') > 0:
        with open('users.json', 'r') as f:
            users = json.load(f)

    # Find the user
    user = next((u for u in users if u['username'] == username), None)

    if not user:
        print('Username not found')
        return jsonify({'error': 'Invalid username or password'}), 400


    input_password = input_password.encode('utf-8')
    filebase_password = user['password'].encode('utf-8')

    result = bcrypt.checkpw(input_password, filebase_password)

    if (result == False):
        print('Input Password does not match User Password Hash')
        return jsonify({'error': 'Invalid Password'}), 400
    else:
        print('Login Successful')
        return jsonify({'message': 'Login successful'})

if __name__ == '__main__':
    app.run(debug=True)
