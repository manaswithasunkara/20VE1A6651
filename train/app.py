from flask import Flask, jsonify, redirect, url_for, request
from flask_cors import CORS
import requests

# Flask setup
app = Flask(_name_)
CORS(app)


# Global Variables
BASE_URL = "http://20.244.56.144"
# It can also be setup in Environment Variables
API_CREDENTIALS = {
    "companyName": "Train Central",
    "clientID": "b557ce16-dab4-4746-b20f-c33cdd82b2d9",
    "clientSecret": "ciKJHOUJDsXdyknT",
    "ownerName": "Rahul",
    "ownerEmail": "rahul@abc.edu",
    "rollNo": "1"
}
AUTH_TOKEN_DATA = {}


# REST API's
@app.route("/")
def index():
    return jsonify({"hello":"hello"})


@app.route("/get-auth-token")
def get_auth():
    global AUTH_TOKEN_DATA
    response = requests.post(f'{BASE_URL}/train/auth', json=API_CREDENTIALS)
    AUTH_TOKEN_DATA = response.json()
    return AUTH_TOKEN_DATA

@app.route("/getAllTrains")
def get_alltrains():
    try:
        headers = {
            'Authorization': f'Bearer {AUTH_TOKEN_DATA["access_token"]}'
        }
        response = requests.get(f'{BASE_URL}/train/trains', headers=headers)
        return response.json()
    except Exception as e:
        get_auth()
        return redirect(url_for('get_alltrains'))
