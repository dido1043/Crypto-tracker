import requests
from flask import Flask

app = Flask(__name__)



def fetch_crypto_price(crypto, currency='usd'):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[crypto][currency]
    else:
        print("Error fetching data")
        return 


crypto_name = "bitcoin"
price = fetch_crypto_price(crypto_name)
if price:
    print(f"The current price of {crypto_name.capitalize()} is ${price:.2f}.")

@app.route('/')
def home():
    return "Crypto tracker"

@app.route('/crypto/<crypto_name>')
def main(crypto_name):
    
    price = fetch_crypto_price(crypto_name)
    if price :
        return f"{crypto_name} ->{price}"
    else:
        return "Error!!!"


if __name__ == '__main__':
    app.run(debug=True)