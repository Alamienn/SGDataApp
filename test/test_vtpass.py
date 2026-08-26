import requests
import json

# Your regenerated keys - replace with your actual keys
API_KEY = "c484ec1381736ec006c96d039c78b385"
SECRET_KEY = "SK_7490db2022066529cb30832abeec2c1bf96616c1d30"

def test_connection():
    # Test API endpoint to get available services
    url = "https://sandbox.vtpass.com/api/service-variations"
    
    headers = {
        "api-key": API_KEY,
        "secret-key": SECRET_KEY,
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            print("✅ Connection successful!")
            data = response.json()
            
            # Check if we got services
            if 'data' in data and len(data['data']) > 0:
                print(f"✅ Found {len(data['data'])} services available")
                print("\n📋 First 3 services:")
                for service in data['data'][:3]:  # Show first 3 services
                    print(f"  - {service.get('name', 'Unknown')} ({service.get('type', 'N/A')})")
            else:
                print("⚠️ No services found. Check your sandbox whitelist.")
                
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"❌ Connection failed: {str(e)}")

if __name__ == "__main__":
    test_connection()