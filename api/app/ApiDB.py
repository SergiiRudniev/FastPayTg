import requests

class ApiDB:
    def Set(self, Key: str, Value: int) -> dict:
        url = f"http://db/set/{Key}"
        payload = {"value": Value}
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    def Get(self, Key: str) -> dict | None:
        response = requests.get(f"http://db/get/{Key}")
        if response.status_code == 404:
            return None
        return response.json()
