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

    username = data.get('username')
    password = data.get('password')

    #Bcrypt Hashing Algorithm
    bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()

    password_hash = bcrypt.hashpw(bytes, salt)

    if not username or not password:
        print('Missing username or password')
        return jsonify({'error': 'Missing data'}), 400

    user_data = {'username': username, 'password': password_hash.decode("utf-8")}

    try:
        with open('users.json', 'a') as f:
            f.write(json.dumps(user_data) + '\n')
    except Exception as e:
        print('File write error ❌:', e)
        return jsonify({'error': 'Failed to write file'}), 500

    return jsonify({'message': 'Signup successful'})

if __name__ == '__main__':
    app.run(debug=True)
