from os import environ

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
    def __init__(self, sandbox=True):
        self.api_key = environ.get("API_KEY", None)
        self.private_key = environ.get("API_SECRET", None)
        self.private_client = gemini.PrivateClient(
            self.api_key, self.private_key, sandbox=sandbox
        ) if self.api_key and self.private_key else None
        if not self.private_client:
            raise EnvironmentError(
                "Please add the API_KEY and API_SECRET to your environment"
            )
