# Ensure you have requests installed (pip install requests)
import requests

response = requests.get("https://api.github.com")
print("Status Code:", response.status_code)
