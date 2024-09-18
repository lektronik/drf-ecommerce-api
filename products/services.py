import requests

class PrintifyService:
    BASE_URL = 'https://api.printify.com/v1/'

    def __init__(self, api_key, shop_id):
        self.api_key = api_key
        self.shop_id = shop_id

    def get_products(self):
        url = f'{self.BASE_URL}shops/{self.shop_id}/products.json'
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_orders(self):
        url = f'{self.BASE_URL}shops/{self.shop_id}/orders.json'
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_order(self, order_id):
        url = f'{self.BASE_URL}shops/{self.shop_id}/orders/{order_id}.json'
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def update_order(self, order_id, data):
        url = f'{self.BASE_URL}shops/{self.shop_id}/orders/{order_id}.json'
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        response = requests.put(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
