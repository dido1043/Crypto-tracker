import requests
from flask import Flask
from model import CryptoModel 
from view import CryptoView

app = Flask(__name__)

@app.route('/')
def home():
    return "Crypto tracker"

@app.route('/cryptos/<cryptos>')
def get_crypto_prices(cryptos):
    crypto_list = cryptos.split(",")
    prices = CryptoModel.fetch_crypto_prices(crypto_list)
    if prices:
        return CryptoView.render_price(prices)
    else:
        return "Error fetching data"

if __name__ == '__main__':
    app.run(debug=True)