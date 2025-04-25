from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import random
import string
import os

app = Flask(__name__)
CORS(app)

def gen_salt(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, length))

def hashingFunction():
    return

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    print('Received data:', data)

    username = data.get('username')
    password = data.get('password')

    salt = gen_salt(32)

    hashed_value = hashingFunction(password)

    if not username or not password:
        print('Missing username or password')
        return jsonify({'error': 'Missing data'}), 400

    user_data = {'username': username, 'password': hashed_value}

    try:
        with open('users.json', 'a') as f:
            f.write(json.dumps(user_data) + '\n')
    except Exception as e:
        print('File write error ❌:', e)
        return jsonify({'error': 'Failed to write file'}), 500

    return jsonify({'message': 'Signup successful'})

if __name__ == '__main__':
    app.run(debug=True)
