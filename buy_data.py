import requests

API_KEY = "your_api_key"
SECRET_KEY = "your_secret_key"

def buy_data():
    url = "https://sandbox.vtpass.com/api/pay"
    
    headers = {
        "api-key": API_KEY,
        "secret-key": SECRET_KEY,
        "Content-Type": "application/json"
    }
    
    payload = {
        "serviceID": "mtn-data",
        "phone": "08012345678",
        "variation_code": "mtn-10mb-100",  # From your list
        "amount": "100"
    }
    
    response = requests.post(url, headers=headers, json=payload)
    print(f"Status: {response.status_code}")
    print(response.json())

if __name__ == "__main__":
    buy_data()