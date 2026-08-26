import requests

API_KEY = "your_key"
SECRET_KEY = "your_secret"

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