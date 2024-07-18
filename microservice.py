from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)

DATA_FILE = 'data.txt'
# CoinGecko API URL
API_URL = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur,czk'


@app.route("/")
def get_results():
    return