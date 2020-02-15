import requests

class CustomGeminiPublicClient:
    """
    Client class for making requests out of the scope of the 
    "gemini" package imported above ^^
    """
    def __init__(self):
        self.public_base_url = "https://api.gemini.com/v1"

    def get_trade_history_since(self, symbol, since):
        history_res = requests.get(
            f"{self.public_base_url}/trades/{symbol}?since={since}"
        )
        return history_res.json()
