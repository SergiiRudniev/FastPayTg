import requests

class ApiDB:
    def __init__(self, url = "db:80"):
        self.url = url
    def Set(self, Key: str, Value: str) -> dict:
        url = f"http://{self.url}/set/{Key}"
        payload = {"value": Value}
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    def Get(self, Key: str) -> dict | None:
        response = requests.get(f"http://{self.url}/get/{Key}")
        if response.status_code == 404:
            print(response)
            return None
        return response.json()
