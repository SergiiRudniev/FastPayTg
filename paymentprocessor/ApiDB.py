import requests

class ApiDB:
    def __init__(self, url = "db"):
        self.url = url
    def Set(self, Key: str, Value: int) -> dict:
        url = f"http://{self.url}/set/{Key}"
        payload = {"value": str(Value)}
        response = requests.post(url, json=payload)
        return response.json()

    def Get(self, Key: str) -> dict | None:
        response = requests.get(f"http://{self.url}/get/{Key}")
        if response.status_code == 404:
            return None
        return response.json()
