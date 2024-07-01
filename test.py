import requests


key = 631097127
value = 10.28

url = f"http://localhost:9090/set/{key}"
payload = {"value": value}
headers = {"Content-Type": "application/json"}
response = requests.post(url, json=payload, headers=headers)