import requests


class Notificator:
    def __init__(self):
        self.url = "notificator:345"

    def SendCode(self, id, code):
        data = {
            "chat_id": id,
            "code": code
        }
        requests.post(f"http://{self.url}/send_code", json=data)
