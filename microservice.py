from flask import Flask, jsonify, request
import json

# CoinGecko API URL
API_URL = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur,czk'