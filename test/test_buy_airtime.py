import requests
import json

# === UPDATE THESE WITH YOUR EXACT KEYS ===
API_KEY = "c484ec1381736ec006c96d039c78b385"
SECRET_KEY = "SK_7490db2022066529cb30832abeec2c1bf96616c1d30"
# ==========================================

def buy_airtime():
    # Sandbox endpoint
    url = "https://sandbox.vtpass.com/api/pay"
    
    # Your keys as they appear in the dashboard
    headers = {
        "api-key": API_KEY,
        "secret-key": SECRET_KEY,
        "Content-Type": "application/json"
    }
    
    # Test payload (sandbox uses fake money)
    payload = {
        "serviceID": "mtn-airtime",
        "phone": "08012345678", 
        "amount": "100"
    }
    
    print("🔑 Testing API Keys...")
    print(f"API Key: {API_KEY[:10]}... (first 10 chars)")
    print(f"Secret Key: {SECRET_KEY[:10]}... (first 10 chars)")
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        print(f"\n📊 Status Code: {response.status_code}")
        
        data = response.json()
        print("\n📋 Response:")
        print(json.dumps(data, indent=2))
        
        if response.status_code == 200:
            print("\n✅ Connection successful!")
        else:
            print(f"\n❌ Error: Check your keys or sandbox activation")
            
    except Exception as e:
        print(f"❌ Connection error: {str(e)}")

if __name__ == "__main__":
    buy_airtime()