import requests

API_KEY = "your_actual_api_key"
SECRET_KEY = "your_actual_secret_key"

def get_mtn_data_plans():
    url = "https://sandbox.vtpass.com/api/service-variations"
    
    headers = {
        "api-key": API_KEY,
        "secret-key": SECRET_KEY
    }
    
    # Add the required serviceID parameter
    params = {
        "serviceID": "mtn-data"  # This requests MTN data plans
    }
    
    response = requests.get(url, headers=headers, params=params)
    print(f"Status Code: {response.status_code}")
    print("Response:")
    print(response.text[:1000])  # Show first 1000 chars

if __name__ == "__main__":
    get_mtn_data_plans()