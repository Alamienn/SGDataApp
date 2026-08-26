import requests

API_KEY = "your_keyc484ec1381736ec006c96d039c78b385"
SECRET_KEY = "your_secretSK_7490db2022066529cb30832abeec2c1bf96616c1d30"

def test_connection():
    url = "https://sandbox.vtpass.com/api/service-variations"
    
    headers = {
        "api-key": API_KEY,
        "secret-key": SECRET_KEY
    }
    
    response = requests.get(url, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(response.text[:500])  # Show first 500 chars

if __name__ == "__main__":
    test_connection()