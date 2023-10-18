import os
import requests
from . import transactions
from flask import jsonify
from ..serializers import *
from dotenv import load_dotenv

load_dotenv()

url = os.environ.get("FETCH_END")


def get_data():
    data = requests.get(url)
    return data.json()


@transactions.route('/createtransaction', methods=['GET'])
def add_transaction():
    data = get_data()
    name = data['name']
    amount = data['amount']
    callbackurl = data['callbackurl']

    # Create a new transaction object
    new_trans = Transcations(name=name, amount=amount)

    db.session.add(new_trans)
    db.session.commit()

    response_data = {"details": "Successfully created transaction"}
    callback_response = requests.post(callbackurl, json=response_data)
    if callback_response.status_code == 200:
        return jsonify({'message': 'Callback sent successfully'}), 200
    else:
        return jsonify({'message': 'Callback failed to send'}), 500
