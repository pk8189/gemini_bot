from os import getenv
import gemini
import requests
import pandas as pd
import pickle

from gemini_bot.utils.client_helpers import CustomGeminiPublicClient

class GeminiPublicClient:
    def __init__(self):
        self.client = gemini.PublicClient()
        self.custom_client = CustomGeminiPublicClient()

    def symbols(self):
        return self.client.symbols()

    def get_ticker(self, symbol):
        return self.client.get_ticker(symbol)

    def get_current_order_book(self, symbol):
        return self.client.get_current_order_book(symbol)

    def get_last_500_trade_history(self, symbol):
        return self.client.get_trade_history(symbol)

    def get_auction_history(self, symbol, since=None):
        return self.client.get_auction_history(symbol, since)


class GeminiPrivateClient:
    def __init__(self):
        self.api_key = getenv("API_KEY", None)
        self.private_key = getenv("API_SECRET", None)
        self.private_client = gemini.PrivateClient(
            self.api_key, self.private_key, sandbox=False
        ) if self.api_key and self.private_key else None
        
    def get_balance(self):
        return self.private_client.get_balance()

    def new_order(self, symbol, amount, price, side):
        order_res = self.private_client.new_order(
            symbol,
            amount,
            price,
            side,
        )
        return order_res

class CryptoDataDownloadClient:
    def __init__(self):
        self.daily_crypto_data_download = "http://www.cryptodatadownload.com/cdd/Gemini"
        self.others_crypto_data_download = "http://www.cryptodatadownload.com/cdd/gemini"

    def get_and_save_data(self, symbol: str, frequency: str) -> str:
        if frequency == "d":
            url = f"{self.daily_crypto_data_download}_{symbol.upper()}_{frequency}.csv"
        else:
            url = f"{self.others_crypto_data_download}_{symbol.upper()}_{frequency}.csv"
        try:
            df = pd.read_csv(url)
        except ValueError as value_err:
            raise value_err
        pickle_name = url.split("/")[-1].split(".")[0] + ".pkl"
        with open(pickle_name, "wb") as pkl:
            pickle.dump(df, pkl)
            return pickle_name
