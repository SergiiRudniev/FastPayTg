import requests

class CodeApi:
    def __init__(self, url: str = "codeservice:90"):
        self.url = url

    def CreateCode(self, id):
        print("Create Code!")
        requests.get(f"http://{self.url}/create_code/{id}")

    def CheckCode(self, id, InputCode):
        data = {
            "input_code": str(InputCode)
        }
        return requests.post(f"http://{self.url}/check_code/{id}", json=data)