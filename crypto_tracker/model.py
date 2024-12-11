import requests


class CryptoModel:
    @staticmethod
    def fetch_crypto_prices(cryptos, currency="usd"):
        crypto_ids = ",".join(cryptos)
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_ids}&vs_currencies={currency}"
        response = requests.get(url)
        if response.status_code == 200:
            print(response.json())
            return response.json()
        else:
            return None        
