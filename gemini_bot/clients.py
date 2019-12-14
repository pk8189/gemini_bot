from os import getenv
from sys import exit

import gemini

class PublicClient:
    def __init__(self):
        self.client = gemini.PublicClient()

    def symbols(self):
        return self.client.symbols()

    def get_ticker(self, symbol):
        return self.client.get_ticker(symbol)

    def get_current_order_book(self, symbol):
        return self.client.get_current_order_book(symbol)

    def get_trade_history(self, symbol, since=None):
        if since:
            return self.client.get_trade_history(symbol, since)
        # if since is not supplied, the last 500 trades are returned.
        return self.client.get_trade_history(symbol)

    def get_auction_history(self, symbol, since=None):
        if since:
            return self.client.get_auction_history(symbol, since)
        # if since is not supplied, the last 500 trades are returned.
        return self.client.get_auction_history(symbol)

class PrivateClient:
    def __init__(self):
        self.api_key = getenv("API_KEY", None)
        self.private_key = getenv("API_SECRET", None)
        self.sandbox = False if getenv("PRODUCTION_MODE", False) == "True" else True
        self.private_client = gemini.PrivateClient(
            self.api_key, self.private_key, sandbox=self.sandbox
        ) if self.api_key and self.private_key else None
        
    def get_balance(self):
        if not self.sandbox:
            return self.private_client.get_balance()
        return "You must be in production mode to see your current balance."