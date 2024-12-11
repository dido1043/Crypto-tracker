from flask import render_template

class CryptoView:
    @staticmethod
    def render_price(prices):
        return render_template("crypto_prices.html", prices=prices)