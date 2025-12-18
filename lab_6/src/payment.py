import requests

class PaymentProcessor:
    def __init__(self, api_url: str):
        self.api_url = api_url

    def convert_price(self, amount: float, currency: str):
        """Метод делает внешний запрос (будем мокать)."""
        response = requests.get(f"{self.api_url}/convert?to={currency}")
        if response.status_code != 200:
            raise Exception("API Error")
        
        data = response.json()
        rate = data.get("rate", 1.0)
        return round(amount * rate, 2)
