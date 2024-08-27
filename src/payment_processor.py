import requests


class PaymentProcessor:
    def __init__(self, gateway_url):
        self.gateway_url = gateway_url

    def process_payment(self, amount):
        response = requests.post(f"{self.gateway_url}/pay", json={"amount": amount})
        return response.json().get("status") == "success"
