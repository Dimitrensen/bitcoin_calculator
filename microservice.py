from flask import Flask, jsonify, request
import requests
import json
from datetime import datetime

app = Flask(__name__)

# Create and deploy a microservice where a client application will be able to:

# retrieve the current price of Bitcoin (BTC) in both EUR and CZK;

# local file instead of database
DATA_FILE = 'data.txt'
# CoinGecko API URL
API_URL = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur,czk'
# 12 months in seconds
# RETENTION_PERIOD = 12 * 30 * 24 * 60 * 60 -- if monthily/daily average is to be calculated

def get_btc_price():
    response = requests.get(API_URL)
    data = response.json()
    eur_price = data['bitcoin']['eur']
    czk_price = data['bitcoin']['czk']
    return eur_price, czk_price

##test
#print(get_btc_price())

# using ISO 8601 format for better readability
def save_price(eur, czk):
    timestamp = datetime.utcnow().isoformat() + 'Z'
    entry = {
        'timestamp': timestamp,
        'eur': eur,
        'czk': czk
    }
    with open(DATA_FILE, 'a') as f:
        f.write(json.dumps(entry) + '\n')

# Endpoint to retrieve the current price of Bitcoin
@app.route('/current_price')
def current_price():
    eur, czk = get_btc_price()
    save_price(eur, czk)
    response_time = datetime.utcnow().isoformat() + 'Z'
    return jsonify({
        'btc_price_eur': eur,
        'btc_price_czk': czk,
        'client_request_time': datetime.now().isoformat(),
        'server_data_time': response_time
    })

# Endpoint to retrieve the latest saved price entry
@app.route('/latest_price')
def latest_price():
    try:
        with open(DATA_FILE, 'r') as f:
            lines = f.readlines()
            if not lines:
                return jsonify({'error': 'No data available'})
            last_entry = json.loads(lines[-1])
            return jsonify(last_entry)
    except FileNotFoundError:
        return jsonify({'error': 'No data available'})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)