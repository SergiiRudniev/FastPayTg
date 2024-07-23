import requests


key = 631097127
value = 10.28

url = f"http://localhost:8080/api/send/6033910454"
payload = {"PayerId": "881637263", "Amount": 100}
headers = {"Content-Type": "application/json"}
response = requests.post(url, json=payload, headers=headers)
print(response)