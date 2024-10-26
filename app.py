from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)

SECRET_KEY = os.getenv("SECRET_MESSAGE")

secret = [
    {
        "message" : SECRET_KEY
    }
]

@app.route("/secret", methods=['GET'])
def get_secret_message():
    return jsonify(secret)

if __name__ == '__main__':
    app.run(debug=True)


