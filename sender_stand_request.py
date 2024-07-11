import requests
from configuration import BASE_URL

def create_order(order_data):
    create_order_url = f"{BASE_URL}/api/v1/orders"
    response = requests.post(create_order_url, json=order_data)
    response.raise_for_status()
    return response.json()

def get_order(order_id):
    get_order_url = f"{BASE_URL}/api/v1/orders/track?t={order_id}"
    response = requests.get(get_order_url)
    response.raise_for_status()
    return response.json()