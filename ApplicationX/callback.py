import requests
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/post_data', methods=['GET'])
def post_data():
    data = {"name": "food", "amount": 100, "callbackurl": "http://localhost:5000/receive_data"}
    return jsonify(data), 200


@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.get_json()
    response_data = data
    print(response_data)
    return jsonify(response_data), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
