from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)

# Create and deploy a microservice where a client application will be able to:

# retrieve the current price of Bitcoin (BTC) in both EUR and CZK;

# local file instead of database
DATA_FILE = 'data.txt'
# CoinGecko API URL
API_URL = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur,czk'
# 12 months in seconds
RETENTION_PERIOD = 12 * 30 * 24 * 60 * 60

def get_btc_price():
    response = requests.get(API_URL)
    data = response.json()
    eur_price = data['bitcoin']['eur']
    czk_price = data['bitcoin']['czk']
    return eur_price, czk_price

##test
#print(get_btc_price())

def save_price(eur, czk):
    timestamp = int(time.time())
    entry = {'timestamp': timestamp, 'eur': eur, 'czk': czk}
    with open(DATA_FILE, 'a') as f:
        f.write(json.dumps(entry) + '\n')

# retrieve locally calculated daily and monthly averages for the price mentioned above, obtained from locally stored data.

def monthly_avg():
    for i in DATA_FILE;
    return sum*DATA_FILE/count

# @app.route("/")
# def get_results():
#     return